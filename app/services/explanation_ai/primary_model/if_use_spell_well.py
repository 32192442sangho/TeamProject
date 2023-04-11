import cv2
import tensorflow as tf
import numpy as np

# Load model
# Define function to extract frames from video
def extract_frames(video_path):
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


def if_use_spell_well(video_path):
    # Load video and extract frames
    frames = extract_frames(video_path)
    model = tf.keras.models.load_model('app/model/if_use_spell_well.h5', compile=False)
    # Reshape frames to match input shape of model
    frames = np.reshape(frames, (1, frames.shape[0], 224, 224, 3))

    # Make predictions on frames
    predictions = model.predict(frames)
    print(predictions)
    # Check if the first value is bigger than the second value
    if predictions[0][0] > predictions[0][1]:
        print("Even if the player character used the spell well, he died.")
        return "스펠을 옳바르게 사용했어도 죽었다"
    else:
        print("Survived if player character used the spell well")
        return "스펠을 옳바르게 사용했으면 살았다"

