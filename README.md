# Face Recognition Webcam Program

This program performs real-time face recognition using a webcam. It compares the faces detected in the webcam feed with preloaded known faces stored in a directory of images. If a match is found, it displays the name of the recognized person on the screen.

## Features
- Real-time face recognition using the webcam.
- Preloads images from a directory and encodes the faces for comparison.
- Displays the name of the recognized person on the webcam feed.
- Draws bounding boxes around detected faces.

## Requirements
Make sure you have Python 3.x installed, then install the required libraries:

- `opencv-python` for video capturing and image manipulation.
- `face_recognition` for encoding and recognizing faces.

You can install these dependencies using `pip`:

```bash
pip install opencv-python face_recognition

project-directory/
│
├── images/                # Folder containing images of known people
│   ├── person1.jpg
│   ├── person2.jpg
│   └── ...                # Additional images
│
├── main.py                # The main Python program
└── README.md              # This README file
