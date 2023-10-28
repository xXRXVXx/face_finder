# Face Finder

This Python script allows you to detect and draw facial landmarks on images. It uses the dlib library for face detection and facial landmark prediction based on the "shape_predictor_68_face_landmarks.dat" file.

## Features

- Detect faces in images.
- Draw facial landmarks on detected faces.
- Count the number of faces and display it in the top right corner.
- Display the current date and time, formatted as "dd/mm/yyyy" and "hh:mm:ss:ms," respectively.
- Author information is displayed in the top left corner.

## Usage

1. Clone this repository to your local machine.
2. Install the required libraries by running `pip install -r requirements.txt`.
3. Run the script using `python face_finder.py`.
4. Use the file dialog to choose the images you want to process.

## Tested on Windows 10

The script has been tested on Windows 10 and is confirmed to work on this operating system.

## Requirements

make sure Download the "shape_predictor_68_face_landmarks.dat" file from [this link](https://github.com/italojs/facial-landmarks-recognition/raw/master/shape_predictor_68_face_landmarks.dat) and place it in the same directory as the script.
Make sure you have the following libraries installed:

- opencv-python-headless==4.5.3.56
- dlib==19.22.0
- Pillow==8.3.1

You can install them using the `pip install -r requirements.txt` command.

## Author

Elkady & Chat GPT

## License

This project is open-source and available under the [MIT License](LICENSE).
