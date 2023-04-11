import os
import cv2
import numpy as np
from tensorflow import keras
import tensorflow as tf

def spell2(video_path):
    # Load the images from the specified directory
    image_dir = "app/services/explanation_ai/primary_model/spell_images"
    image_files = [os.path.join(image_dir, f) for f in os.listdir(image_dir) if f.endswith(".jpg")]
    images = [cv2.imread(f, cv2.IMREAD_GRAYSCALE) for f in image_files]

    # Load the video
    video = cv2.VideoCapture(video_path)

    # Create an empty list to store the results
    results = []

    # Loop over all frames in the video
    frame_count = 0
    while True:
        # Read the next frame
        success, frame = video.read()
        if not success:
            break  # End of video

        # Extract the region of interest from the frame
        region = frame[610:638, 167:197]
        region_gray = cv2.cvtColor(region, cv2.COLOR_BGR2GRAY)
        # Loop over the images and search for each one in the region
        match_found = False
        for image in images:
            # Search for the image in the region using template matching
            result = cv2.matchTemplate(region_gray, image, cv2.TM_CCOEFF_NORMED)

            # Check if a match was found
            threshold = 0.44
            if cv2.minMaxLoc(result)[1] > threshold:
                match_found = True
                # Append 1 to the results list
                results.append(1)
                break

        if not match_found:
            # Append 0 to the results list
            results.append(0)

        frame_count += 1

    # Release the video object
    video.release()

    # Print the results

    # Load the AI model
    model_path = "app/model/spell2_use_epoch25.h5"
    model = tf.keras.models.load_model(model_path, compile=False)

    # Pad the input results to 940
    padded_results = results + [3] * (940 - len(results))
    padded_results = np.array(padded_results)

    # Make predictions using the AI model
    predictions = model.predict(np.array([padded_results]))
    predicted_class = np.argmax(predictions)
    print(predictions)
    # Print the predicted class
    if predicted_class == 0:
        print("don't use")
        return "don't use"
    elif predicted_class == 1:
        print("use")
        return "use"
    elif predicted_class == 2:
        print("don't have")
        return "don't have"