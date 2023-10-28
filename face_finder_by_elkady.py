import cv2
import dlib
import os
import tkinter as tk
from tkinter import filedialog
import numpy as np
from datetime import datetime

# Create a tkinter window for the file dialog
root = tk.Tk()
root.withdraw()  # Hide the main window

# Directory where the script and settings are
script_directory = os.path.dirname(os.path.abspath(__file__))
output_directory = os.path.join(script_directory, "output")

# Create the output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Path to the file for detecting facial landmarks
landmark_model_path = os.path.join(script_directory, "shape_predictor_68_face_landmarks.dat")

# Use the Dlib model for faces and landmarks
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(landmark_model_path)

# Function to open a file dialog for choosing images
def open_file_dialog():
    file_paths = filedialog.askopenfilenames(
        title="Choose images",
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")]
    )
    return file_paths

# Function to detect and draw futuristic-style landmarks
def detect_and_draw_futuristic_landmarks(image_path, output_directory):
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Unable to load image {image_path}")
        return

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    # Initialize face counter for each image
    face_counter = 0

    for i, face in enumerate(faces):
        landmarks = predictor(gray, face)
        landmarks_np = np.array([(p.x, p.y) for p in landmarks.parts()], dtype=int)

        # Draw lines between the facial landmarks in turquoise color
        for start, end in [(0, 17), (17, 22), (22, 27), (27, 36), (36, 42), (42, 48), (48, 60), (60, 68)]:
            cv2.polylines(image, [landmarks_np[start:end]], False, (0, 255, 255), thickness=2)

        # Draw a number under every face
        face_counter += 1
        x_min = min(landmarks_np[:, 0])
        x_max = max(landmarks_np[:, 0])
        y_max = max(landmarks_np[:, 1])

        # Draw face counter
        cv2.putText(image, str(face_counter), (x_min + (x_max - x_min) // 2, y_max + 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)

    # Draw the number of faces in the top right corner
    num_faces = len(faces)
    cv2.putText(image, f"Faces: {num_faces}", (image.shape[1] - 120, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)

    # Draw "by elkady" in the top left corner with white color
    cv2.putText(image, "by elkady", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    # Get the current date and time
    now = datetime.now()
    date = now.strftime("%d/%m/%Y")
    time = now.strftime("%H:%M:%S:%f")  # Add milliseconds

    # Draw the date and time under "by elkady" text
    cv2.putText(image, date, (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    cv2.putText(image, time, (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    # Find the next available result number
    result_number = 1
    while True:
        result_filename = f"result{result_number}.jpg"
        output_path = os.path.join(output_directory, result_filename)
        if not os.path.exists(output_path):
            break
        result_number += 1

    # Save the image with the next available result number
    cv2.imwrite(output_path, image)
    print(f"Processed image saved as {result_filename}")

# Main function
def main():
    input_image_paths = open_file_dialog()
    if not input_image_paths:
        return

    for input_image_path in input_image_paths:
        detect_and_draw_futuristic_landmarks(input_image_path, output_directory)

if __name__ == "__main__":
    main()
