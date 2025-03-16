# Motion Detection using OpenCV

## Project Overview
This Python script uses computer vision techniques to detect motion in real-time using a webcam. The code captures video frames, compares consecutive frames, and highlights areas where significant changes occur (motion). The motion is indicated by drawing bounding boxes around the detected moving objects.

## Requirements

The project relies on the following Python libraries:

1. **OpenCV** (`cv2`): For video capture, image processing, and motion detection.
2. **NumPy** (`np`): For handling arrays and other numerical operations.

To install these libraries, you can run the following commands:

```bash
pip install opencv-python numpy
```

Or you can also install the libraries listed in the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

## Code Description

1. **Video Capture**: The script opens the webcam using OpenCV's `cv2.VideoCapture(0)`. It will continuously capture frames from the webcam until the user presses the 'q' key to stop.
   
2. **Gray-Scale Conversion and Gaussian Blur**: Each frame is converted to grayscale, followed by a Gaussian blur to reduce noise, which helps to improve the accuracy of motion detection.

3. **Frame Difference**: The script calculates the difference between the current frame and the previous frame to detect any movement.

4. **Thresholding**: A binary threshold is applied to the difference frame to isolate significant changes in pixel values, effectively highlighting moving objects.

5. **Contour Detection**: Contours are found in the thresholded frame, and the largest contour is selected, which represents the largest moving object in the scene.

6. **Bounding Box**: If the largest contour area exceeds a predefined threshold (defined as `contourAreaThreshold`), a bounding box is drawn around the detected moving object in the frame.


## Key Parameters

- **contourAreaThreshold**: The minimum area of the detected object required to draw the bounding box. Objects smaller than this threshold are ignored. You can modify this value to adjust the sensitivity of the motion detection.


## Notes

- This script relies on a basic motion detection algorithm by comparing consecutive frames. More sophisticated methods can be employed for robust motion detection (e.g., using background subtraction techniques).
- The webcam feed is displayed in real-time, so ensure you have access to a functional webcam.
