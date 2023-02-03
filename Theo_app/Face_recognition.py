import numpy as np 
import pandas as pd
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow import keras
from tensorflow.keras import layers
import matplotlib.pyplot as plt
import cv2
import joblib

data = 'Test_of_unknown'

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
outputs = keras.layers.Dense(7, activation = 'softmax')(x)
# Combine inputs and outputs to create model
model = keras.Model(inputs=inputs, outputs=outputs)

base_model.trainable = False

# Compile the model with a low learning rate
model.compile(optimizer=keras.optimizers.RMSprop(learning_rate = 0.0001),
              loss = 'categorical_crossentropy' , metrics = ['accuracy'])

history = model.fit(train_it,steps_per_epoch=610,epochs=10)

#save model
filename = 'model_7_class.sav'
joblib.dump(model, filename)

#load saved model
filename = 'model_7_class.sav'
model = joblib.load(filename)

import cv2
import sys
import numpy as np
import os
from tensorflow.keras.utils import load_img, img_to_array
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import time
# %matplotlib inline

cascPath = sys.argv[1]
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

video_capture = cv2.VideoCapture(0)
image = video_capture.read()
count = 0

students = pd.read_excel("Student_Data.xlsx")
# time.sleep(3)
while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    #saves frame as jpg file
    cv2.imwrite("C:\Tempo_file\%d.jpg" % count, frame)
    
    
#     predicting images
    path = 'C:\Tempo_file\%d.jpg' % count
    img = load_img(path, target_size=(224,224))
#     imgplot = plt.imshow(img)
    x = img_to_array(img)
    x = np.expand_dims(x, axis=0)

    images = np.vstack([x])
    classes = model.predict(images, batch_size=10)
    
    
    
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    
    if 1 in classes[0]:
        mask = students['id'].isin([list(classes[0]).index(1)])


        df_filter = students.loc[mask]
        
        print(df_filter['Student_name'].iloc[0])
    else:
        print('none')

    
#     os.remove("C:\Tempo_file\%d.jpg" % count)
#     count += 1
    
    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
#     cv2.putText(path, "Theodore", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        

cv2.destroyAllWindows()