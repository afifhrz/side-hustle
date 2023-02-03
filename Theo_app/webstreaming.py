# import the necessary packages
from pyimagesearch.motion_detection.singlemotiondetector import SingleMotionDetector
from imutils.video import VideoStream
from flask import Response
from flask import Flask, jsonify, request, redirect
from flask import render_template

from tensorflow.keras.utils import load_img, img_to_array
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow import keras

import numpy as np
import joblib
import threading
import argparse
import datetime
import imutils
import time
import cv2
import os
from sqlalchemy import create_engine

import pandas as pd

# initialize the output frame and a lock used to ensure thread-safe
# exchanges of the output frames (useful when multiple browsers/tabs
# are viewing the stream)
outputFrame = None
lock = threading.Lock()
# initialize a flask object
app = Flask(__name__, static_folder="static")
# initialize the video stream and allow the camera sensor to
# warmup
vs = VideoStream(src=0).start()
time.sleep(2.0)
engine = create_engine("sqlite:///testdb.db")

@app.route("/")
def index():
	# return the rendered template
	return render_template("index.html")

@app.get("/registration")
def register_face():
    return render_template("face_registration.html")

@app.get("/checkin")
def checkin():
    return render_template("face_recognition.html")

filename = 'model_trained.sav'
model = joblib.load(filename)

@app.get("/recordcheckin")
def recordCheckIn():       
        # grab global references to the video stream, output frame, and
        # lock variables
        global vs, outputFrame, lock
        db = engine.connect()
        # read the next frame from the video stream, resize it,
        # convert the frame to grayscale, and blur it
        frame = vs.read()
        frame = imutils.resize(frame, width=400)
        
        cv2.imwrite('temp.jpg', frame)
        
        # recognition code
        # load saved model
        img = load_img("temp.jpg", target_size=(224,224))
        x = img_to_array(img)
        x = np.expand_dims(x, axis=0)

        images = np.vstack([x])
        classes = model.predict(images, batch_size=10)
        # classes = [[0,0,0,0,0,0,0,1]]
        classes_loop = [round(num, 1) for num in classes[0]]
        # print(classes_loop)
        
        if 1 in classes_loop:
            class_id = classes_loop.index(1)
            StudentName = db.execute(f"""SELECT STUDENT_NAME FROM master_student WHERE CLASS_ID = {class_id}""")    
            return jsonify({
                "StudentName":list(StudentName)[0][0]
            })
        else:
            return jsonify({
                "StudentName":"Database Not Found"
                })

@app.get("/train")
def trainView():       
    # return the rendered template
	return render_template("trainView.html")

@app.post("/trainmodel")
def trainStart():
    engine = create_engine("sqlite:///testdb.db")
    db = engine.connect()

    classLength = db.execute("""SELECT COUNT(CLASS_ID) FROM master_student""")

    classLength = list(classLength)[0][0]

    data = "image_databases"

    datagen = ImageDataGenerator(samplewise_center=False,
                                samplewise_std_normalization=False,
                                horizontal_flip = True,
                                vertical_flip = False,
                                height_shift_range = 0.15,
                                width_shift_range = 0.15,
                                rotation_range = 5,
                                shear_range = 0.01,
                                fill_mode = 'nearest',
                                zoom_range=0.10)

    train_it = datagen.flow_from_directory(data,
                                        target_size=(224,224),
                                        batch_size=1,
                                        color_mode='rgb',
                                        class_mode='categorical')

    base_model = keras.applications.ResNet50( weights='imagenet', input_shape=(224,224, 3), include_top=False)
    inputs = keras.Input(shape=(224,224, 3))

    x = base_model(inputs, training=False)

    # Add pooling layer or flatten layer
    x = keras.layers.Flatten()(x)
    # Add final dense layer
    outputs = keras.layers.Dense(classLength, activation = 'softmax')(x)
    # Combine inputs and outputs to create model
    model_trained = keras.Model(inputs=inputs, outputs=outputs)

    base_model.trainable = False

    # Compile the model with a low learning rate
    model_trained.compile(optimizer=keras.optimizers.RMSprop(learning_rate = 0.0001),
                loss = 'categorical_crossentropy' , metrics = ['accuracy'])

    history = model_trained.fit(train_it,steps_per_epoch=100,epochs=classLength)

    #save model
    filename = 'model_trained.sav'
    joblib.dump(model_trained, filename)
    
    global model
    model = joblib.load(filename)
    
    # return the rendered template
    return jsonify({
        "data":True
    })

@app.post("/appregistration")
def registerApp():
        data = request.get_json()
        studentName = data['NameStudent']
        
        # grab global references to the video stream, output frame, and
        # lock variables
        global vs, outputFrame, lock
        # initialize the motion detector and the total number of frames
        # read thus far
        num_sample = 160
        # students = pd.read_excel("Student_Data.xlsx")
        # Max_id = students['id'].max()
        db = engine.connect()
        
        maxIdStudent = db.execute(
            """SELECT MAX(CLASS_ID) AS ID FROM master_student"""
        )
        maxIdStudent = list(maxIdStudent)[0][0]
        if maxIdStudent == None:
            maxIdStudent = 0
        
        count=0
        parent_dir = "image_databases"
        directory = str(maxIdStudent + 1)
        path = os.path.join(parent_dir, directory)
        os.makedirs(path)
        
        # loop over frames from the video stream
        while True:
            # read the next frame from the video stream, resize it,
            # convert the frame to grayscale, and blur it
            frame = vs.read()
            frame = imutils.resize(frame, width=400)
            
            cv2.imwrite(path + '\%d.jpg' % count, frame)
            count += 1
            if count>num_sample:
                break
            
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            gray = cv2.GaussianBlur(gray, (7, 7), 0)
            # grab the current timestamp and draw it on the frame
            timestamp = datetime.datetime.now()
            cv2.putText(frame, timestamp.strftime(
                "%A %d %B %Y %I:%M:%S%p"), (10, frame.shape[0] - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)
        
        db.execute(
            f"""INSERT INTO master_student (STUDENT_NAME, CLASS_ID) VALUES ('{studentName}',{maxIdStudent+1}) """
            )

def detect_motion(frameCount):
        # grab global references to the video stream, output frame, and
        # lock variables
        global vs, outputFrame, lock
        # initialize the motion detector and the total number of frames
        # read thus far
        md = SingleMotionDetector(accumWeight=0.1)
        total = 0
        # loop over frames from the video stream
        while True:
            # read the next frame from the video stream, resize it,
            # convert the frame to grayscale, and blur it
            frame = vs.read()
            frame = imutils.resize(frame, width=400)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            gray = cv2.GaussianBlur(gray, (7, 7), 0)
            # grab the current timestamp and draw it on the frame
            timestamp = datetime.datetime.now()
            cv2.putText(frame, timestamp.strftime(
                "%A %d %B %Y %I:%M:%S%p"), (10, frame.shape[0] - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)
            # if the total number of frames has reached a sufficient
            # number to construct a reasonable background model, then
            # continue to process the frame
            if total > frameCount:
                # detect motion in the image
                motion = md.detect(gray)
                # check to see if motion was found in the frame
                if motion is not None:
                    # unpack the tuple and draw the box surrounding the
                    # "motion area" on the output frame
                    # (thresh, (minX, minY, maxX, maxY)) = motion
                    # cv2.rectangle(frame, (minX, minY), (maxX, maxY),
                    #     (0, 0, 255), 2)
                    pass
            
            # update the background model and increment the total number
            # of frames read thus far
            md.update(gray)
            total += 1
            # acquire the lock, set the output frame, and release the
            # lock
            with lock:
                outputFrame = frame.copy()
                            
def generate():
	# grab global references to the output frame and lock variables
	global outputFrame, lock
	# loop over frames from the output stream
	while True:
		# wait until the lock is acquired
		with lock:
			# check if the output frame is available, otherwise skip
			# the iteration of the loop
			if outputFrame is None:
				continue
			# encode the frame in JPEG format
			(flag, encodedImage) = cv2.imencode(".jpg", outputFrame)
			# ensure the frame was successfully encoded
			if not flag:
				continue
		# yield the output frame in the byte format
		yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + 
			bytearray(encodedImage) + b'\r\n')

@app.route("/video_feed")
def video_feed():
    # return the response generated along with the specific media
    # type (mime type)
    return Response(generate(),
        mimetype = "multipart/x-mixed-replace; boundary=frame")
    
# check to see if this is the main thread of execution
if __name__ == '__main__':
	# construct the argument parser and parse command line arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--ip", type=str, required=True,
        help="ip address of the device")
    ap.add_argument("-o", "--port", type=int, required=True,
        help="ephemeral port number of the server (1024 to 65535)")
    ap.add_argument("-f", "--frame-count", type=int, default=32,
        help="# of frames used to construct the background model")
    ap.add_argument("-d", "--debug", type=str, default="run",
        help="# debug type")
    args = vars(ap.parse_args())
	# start a thread that will perform motion detection
    t = threading.Thread(target=detect_motion, args=(
        args["frame_count"],))
    t.daemon = True
    t.start()
    # start the flask app
    app.run(host=args["ip"], port=args["port"], debug=True,
		threaded=True, use_reloader=False)
# release the video stream pointer
vs.stop()