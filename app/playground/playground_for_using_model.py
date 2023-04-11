import tensorflow as tf
import numpy as np
import os
from keras import layers, models

# Define the number of classes
input_shape = (1392, 720, 3)
num_classes = 25

# Define the input shape of the video frames


# Define the location of the data and ground truth files
data_dir = r"D:\PycharmProjects\TeamProject\app\models\data\fullframe_videos_but_348"
truth_file = '/app/models/label/spell_1_truth.txt'

# Define the model architecture
model = models.Sequential([
    # 3D Convolutional Layers
    layers.Conv3D(64, kernel_size=(3, 3, 3), activation='relu', input_shape=(None,) + input_shape),
    layers.MaxPooling3D(pool_size=(2, 2, 2)),
    layers.Conv3D(128, kernel_size=(3, 3, 3), activation='relu'),
    layers.MaxPooling3D(pool_size=(2, 2, 2)),
    layers.Conv3D(256, kernel_size=(3, 3, 3), activation='relu'),
    layers.MaxPooling3D(pool_size=(2, 2, 2)),
    layers.Conv3D(512, kernel_size=(3, 3, 3), activation='relu'),
    layers.MaxPooling3D(pool_size=(2, 2, 2)),
    layers.Flatten(),
    # Dense Layers
    layers.Dense(256, activation='relu'),
    layers.Dropout(0.5),
    layers.Dense(num_classes, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

train_data = ...  # Load the training video data here
train_labels = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25  # Load the training labels here

# Train the model
model.fit(train_data, train_labels, batch_size=16, epochs=10, validation_split=0.2)
