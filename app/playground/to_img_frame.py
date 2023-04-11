import cv2
import os

# set the path to the input video file
input_file = "./data/13-1_KR-6331999909_01.webm"

# set the path to the output directory where the extracted frames will be saved
output_dir = "../services/testdata"

# create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# open the video file using OpenCV
cap = cv2.VideoCapture(input_file)

# initialize a counter to keep track of the frame number
frame_num = 0

# loop through the video frames
while cap.isOpened():

    # read the next frame from the video
    ret, frame = cap.read()

    # if the frame was successfully read
    if ret:

        # construct the output file path for the current frame
        output_file = os.path.join(output_dir, f"frame{frame_num:04d}.jpg")

        # write the current frame to disk as a JPEG image file
        cv2.imwrite(output_file, frame)

        # increment the frame counter
        frame_num += 1

    # if there are no more frames to read, exit the loop
    else:
        break

# release the video file
cap.release()