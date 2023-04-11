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


def what_to_what(video_path):
    # Load video and extract frames
    frames = extract_frames(video_path)
    model = tf.keras.models.load_model('app/model/what_to_what.h5', compile=False)
    # Reshape frames to match input shape of model
    frames = np.reshape(frames, (1, frames.shape[0], 224, 224, 3))

    # Make predictions on frames
    predictions = model.predict(frames)
    print(predictions)
    # Check which prediction is highest and print result accordingly
    if predictions[0][1] > np.max(np.concatenate([predictions[0][:1] , predictions[0][2:]])):
        print("1vs2")
        return"1vs2"
    elif predictions[0][2] > np.max(np.concatenate([predictions[0][:2] , predictions[0][3:]])):
        print("1vs3")
        return"1vs3"
    elif predictions[0][3] > np.max(np.concatenate([predictions[0][:3] , predictions[0][4:]])):
        print("1vs4")
        return"1vs4"
    elif predictions[0][4] > np.max(np.concatenate([predictions[0][:4] , predictions[0][5:]])):
        print("1vs5")
        return"1vs5"
    elif predictions[0][5] > np.max(np.concatenate([predictions[0][:5] , predictions[0][6:]])):
        print("2vs1")
        return"2vs1"
    elif predictions[0][6] > np.max(np.concatenate([predictions[0][:6] , predictions[0][7:]])):
        print("2vs2")
        return"2vs2"
    elif predictions[0][7] > np.max(np.concatenate([predictions[0][:7] , predictions[0][8:]])):
        print("2vs3")
        return"2vs3"
    elif predictions[0][8] > np.max(np.concatenate([predictions[0][:8] , predictions[0][9:]])):
        print("2vs4")
        return"2vs4"
    elif predictions[0][9] > np.max(np.concatenate([predictions[0][:9] , predictions[0][10:]])):
        print("2vs5")
        return"2vs5"
    elif predictions[0][10] > np.max(np.concatenate([predictions[0][:9] , predictions[0][11:]])):
        print("3vs1")
        return"3vs1"
    elif predictions[0][11] > np.max(np.concatenate([predictions[0][:11] , predictions[0][12:]])):
        print("3vs2")
        return"3vs2"
    elif predictions[0][12] > np.max(np.concatenate([predictions[0][:12] , predictions[0][13:]])):
        print("3vs3")
        return"3vs3"
    elif predictions[0][13] > np.max(np.concatenate([predictions[0][:13] , predictions[0][14:]])):
        print("3vs4")
        return"3vs4"
    elif predictions[0][14] > np.max(np.concatenate([predictions[0][:14] , predictions[0][15:]])):
        print("3vs5")
        return"3vs5"
    elif predictions[0][15] > np.max(np.concatenate([predictions[0][:15] , predictions[0][16:]])):
        print("4vs1")
        return"4vs1"
    elif predictions[0][16] > np.max(np.concatenate([predictions[0][:16] , predictions[0][17:]])):
        print("4vs2")
        return"4vs2"
    elif predictions[0][17] > np.max(np.concatenate([predictions[0][:17] , predictions[0][18:]])):
        print("4vs3")
        return"4vs3"
    elif predictions[0][18] > np.max(np.concatenate([predictions[0][:18] , predictions[0][19:]])):
        print("4vs4")
        return"4vs4"
    elif predictions[0][19] > np.max(np.concatenate([predictions[0][:19] , predictions[0][20:]])):
        print()
        return"4vs5"
    elif predictions[0][20] > np.max(np.concatenate([predictions[0][:20] , predictions[0][21:]])):
        print("5vs1")
        return"5vs1"
    elif predictions[0][21] > np.max(np.concatenate([predictions[0][:21] , predictions[0][22:]])):
        print("5vs2")
        return"5vs2"
    elif predictions[0][22] > np.max(np.concatenate([predictions[0][:22] , predictions[0][23:]])):
        print("5vs3")
        return"5vs3"
    elif predictions[0][23] > np.max(np.concatenate([predictions[0][:23] , predictions[0][24:]])):
        print("5vs4")
        return"5vs4"
    elif predictions[0][24] > np.max(np.concatenate([predictions[0][:24] , predictions[0][25:]])):
        print("5vs5")
        return"5vs5"
