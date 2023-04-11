import cv2
import tensorflow as tf
import numpy as np

# Load model
# Define function to extract frames from video
def extract_frames(video_path):
    print(video_path)
    frames = []
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    num_frames = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            if num_frames % int(fps/3) == 0:
                frame = cv2.resize(frame, (224, 224))
                frame = tf.keras.preprocessing.image.img_to_array(frame)
                frames.append(frame)
            num_frames += 1
        else:
            break
    cap.release()
    # Pad or truncate frames to ensure length 45
    if len(frames) < 45:
        pad_width = ((0, 45 - len(frames)), (0, 0), (0, 0), (0, 0))
        frames = np.pad(frames, pad_width, 'constant')
    else:
        frames = frames[:45]
    return np.array(frames)


def favor(video_path):
    # Load video and extract frames
    frames = extract_frames(video_path)
    model = tf.keras.models.load_model('app/model/favor_unfavor.h5', compile=False)
    # Reshape frames to match input shape of model
    frames = np.reshape(frames, (1, frames.shape[0], 224, 224, 3))

    # Make predictions on frames
    predictions = model.predict(frames)
    print(predictions)
    # Check which prediction is highest and print result accordingly
    if predictions[0][0] > predictions[0][1] and predictions[0][0] > predictions[0][2]:
        print("weaker")
        return "적팀보다 더 약하다"
    elif predictions[0][1] > predictions[0][0] and predictions[0][1] > predictions[0][2]:
        print("stronger")
        return "적팀보다 더 강하다"
    else:
        print("Neck and Neck")
        return "적팀과 비슷하다"
