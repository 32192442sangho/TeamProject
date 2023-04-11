import tensorflow as tf
from keras import layers, models
import numpy as np
import cv2

# Define the input shape for the frames
input_shape = (720, 1392, 3)

# Define the number of classes
num_classes = 25

# Load the video frames and their labels
video_path = r"D:\PycharmProjects\TeamProject\app\models\data\fullframe_videos_but_348"
truth_file = '/app/models/label/spell_1_truth.txt'
with open(truth_file, 'r') as f:
    labels = f.read().splitlines()
num_samples = len(labels)
frames = np.zeros((num_samples, 7, 720, 1392, 3), dtype=np.uint8)
for i, label in enumerate(labels):
    label = label.split(',')
    video_id = label[0]
    frame_indices = list(range(43, 50))
    for j, idx in enumerate(frame_indices):
        frame_path = f"{video_path}/{video_id}_{idx}.webm"
        cap = cv2.VideoCapture(frame_path)
        ret, frame = cap.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frames[i, j] = frame
        cap.release()
    label_index = int(label[1]) - 1
    labels[i] = label_index
labels = np.array(labels)

# Split the data into training and validation sets
train_ratio = 0.8
num_train_samples = int(num_samples * train_ratio)
train_frames = frames[:num_train_samples]
train_labels = labels[:num_train_samples]
val_frames = frames[num_train_samples:]
val_labels = labels[num_train_samples:]

# Create the CNN model
model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=input_shape))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(128, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(128, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Flatten())
model.add(layers.Dense(512, activation='relu'))
model.add(layers.Dense(num_classes, activation='softmax'))

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.fit(train_frames, train_labels, epochs=10, batch_size=32, validation_data=(val_frames, val_labels))

model.save('test2.h5')