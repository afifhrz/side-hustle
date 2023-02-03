import numpy as np 
import pandas as pd
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow import keras
from tensorflow.keras import layers
import joblib
from sqlalchemy import create_engine

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
model = keras.Model(inputs=inputs, outputs=outputs)

base_model.trainable = False

# Compile the model with a low learning rate
model.compile(optimizer=keras.optimizers.RMSprop(learning_rate = 0.0001),
              loss = 'categorical_crossentropy' , metrics = ['accuracy'])

history = model.fit(train_it,steps_per_epoch=100,epochs=classLength)

#save model
filename = 'model_trained.sav'
joblib.dump(model, filename)