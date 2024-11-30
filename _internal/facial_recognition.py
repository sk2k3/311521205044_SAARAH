import cv2
import numpy as np
import face_recognition
import os
import pandas as pd
import json
from datetime import datetime

# Paths to images and student dataset file
images_path = 'IT IMAGES'
dataset_path = 'IT_STUDENT_DATASET.csv'
encodings_path = 'encodings.json'  # Path to save/load encodings

# Get today's date to create attendance file for today
today = datetime.now().strftime('%d_%m_%Y')
attendance_path = f'attendance_{today}.csv'  # File name format: attendance_DD_MM_YYYY.csv

# Load student data from CSV
student_data = pd.read_csv(dataset_path)
register_numbers = student_data['REGISTER NUMBER'].astype(str).tolist()  # Convert to string
student_names = student_data['STUDENT NAME'].tolist()

# Load images and their encodings
def load_encodings():
    if os.path.isfile(encodings_path):
        with open(encodings_path, 'r') as f:
            encodings = json.load(f)
            return {key: np.array(val) for key, val in encodings.items()}  # Ensure NumPy arrays are restored
    return {}

# Save encodings to a file
def save_encodings(encodings):
    with open(encodings_path, 'w') as f:
        json.dump({key: val.tolist() for key, val in encodings.items()}, f)  # Convert arrays to lists

# Load student images and encode if not already saved
images = []
classNames = []
encodeListKnown = load_encodings()

# Only encode images if encodings are not present
if not encodeListKnown:
    for cl in os.listdir(images_path):
        currentImage = cv2.imread(f'{images_path}/{cl}')
        if currentImage is not None:  # Check if the image was loaded successfully
            images.append(currentImage)
            register_number = os.path.splitext(cl)[0]  # Assuming filenames are register numbers
            classNames.append(register_number)
            img_rgb = cv2.cvtColor(currentImage, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img_rgb)
            if encode:  # Check if encoding is found
                encodeListKnown[register_number] = encode[0]  # Store NumPy arrays directly

    # Save encodings after processing
    save_encodings(encodeListKnown)

# Convert the dictionary to a list for comparison later
classNames = list(encodeListKnown.keys())  # Ensure classNames matches the encodings' keys
encodeListKnown = list(encodeListKnown.values())

# Function to mark attendance
def markAttendance(register_number, student_name):
    # Check if today's attendance file already exists
    if os.path.isfile(attendance_path):
        with open(attendance_path, 'r') as f:
            myDataList = f.readlines()
            for line in myDataList:
                entry = line.split(',')
                if entry[0] == register_number:  # Check if the register number is already recorded
                    return  # If present, exit the function without adding

    # Get the current time
    now = datetime.now()
    timestamp = now.strftime('%H:%M:%S')

    # Determine the status (Present or Late) based on time
    current_time = now.strftime('%H:%M')
    if "08:00" <= current_time <= "08:30":
        status = "Present"
    elif "08:31" <= current_time <= "09:00":
        status = "Late"
    else:
        status = "Absent"  # Automatically mark absent after 9:00 AM

    # Append attendance record to CSV
    with open(attendance_path, 'a') as f:
        f.write(f'{register_number},{student_name},{timestamp},{status}\n')  # Ensure this ends with a newline

# Create today's attendance file if it doesn't exist, with STATUS column
if not os.path.isfile(attendance_path):
    with open(attendance_path, 'w') as f:
        f.write('Register Number,Student Name,Time Stamp,STATUS\n')

# Automatically mark students who haven't been marked by 9:00 AM as 'Absent'
def markAbsentStudents():
    # Check if any students have not been marked
    with open(attendance_path, 'r') as f:
        marked_students = [line.split(',')[0] for line in f.readlines()[1:]]  # Get already marked students

    with open(attendance_path, 'a') as f:
        for register_number, student_name in zip(register_numbers, student_names):
            if register_number not in marked_students:
                now = datetime.now()
                timestamp = now.strftime('%H:%M:%S')
                f.write(f'{register_number},{student_name},{timestamp},Absent\n')

# Enable the webcam
cap = cv2.VideoCapture(0)

# Set a distance threshold for recognition accuracy
distance_threshold = 0.5  # Adjust as needed

# Flag to ensure absent marking is done only once
absent_marked = False

while True:
    success, img = cap.read()
    if not success:  # Check if the frame is read correctly
        print("Ignoring empty camera frame.")
        continue

    imgSmall = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgSmall = cv2.cvtColor(imgSmall, cv2.COLOR_BGR2RGB)

    facesInCurrentFrame = face_recognition.face_locations(imgSmall)
    encodingsOfCurrentFrame = face_recognition.face_encodings(imgSmall, facesInCurrentFrame)

    for encodeFace, faceLoc in zip(encodingsOfCurrentFrame, facesInCurrentFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDistance = face_recognition.face_distance(encodeListKnown, encodeFace)

        if any(matches):  # Only proceed if there is at least one match
            matchIndex = np.argmin(faceDistance)

            # Check if matchIndex is within the valid range for classNames
            if matchIndex < len(classNames) and matches[matchIndex] and faceDistance[matchIndex] < distance_threshold:
                register_number = classNames[matchIndex].upper()
                student_name = student_names[register_numbers.index(register_number)]
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 1)
                cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, student_name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 2)
                markAttendance(register_number, student_name)  # Mark attendance if not already marked

    cv2.imshow('Webcam', img)

    # Automatically mark students absent after 9:00 AM if not already done
    current_time = datetime.now().strftime('%H:%M')
    if current_time >= "09:00" and not absent_marked:
        markAbsentStudents()
        absent_marked = True  # Set the flag to prevent marking absent multiple times

    # Break the loop and close the window on pressing 'x'
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

# Release the webcam and close the window
cap.release()
cv2.destroyAllWindows()
