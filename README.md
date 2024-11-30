Title: Automated Attendance Management System Using Facial Recognition Technology

Overview:

This project implements a cutting-edge facial recognition-based attendance system designed to streamline the process of recording attendance in educational institutions. By leveraging OpenCV, Python, and Flask, the system ensures seamless and efficient attendance management for multiple student groups (1st to 4th-year students).

The system uses facial recognition to identify students in real-time via webcam, dynamically updates the attendance records, and allows downloading the attendance CSV files specific to each year.

Key Features: 

-Facial Recognition Technology: Identifies students' faces and marks attendance automatically.
-Year-Specific Access: Secure login system with unique credentials for each year (1st to 4th year).
-Dynamic Attendance Updates: Real-time attendance table rendering on the web interface.
-Attendance Records: Generates and saves attendance as attendance_{year}_XX_XX_XXXX.csv in the attendance_records directory.
-Camera Control: "Turn On" and "Turn Off" buttons to control the webcam feed.
-Logout Functionality: Redirects to the login page upon clicking the logout button.


How to Run the Application:

Prerequisites
- A webcam connected to the system.

Setup Instructions:
1. Within the "311521205044_SAARAH_AKTHAR" Folder, you will find a zip file called, "311521205044-Project". 

2. Before unzipping the file, right click on it, and click on "Properties". 

3. Under the "General" tab, you will find a section labelled as "Security". 

4. Tick/Mark the "Unblock" option available and click "OK". 

5. Now, you may unzip the file. 

6. After unzipping, you will lead to a file called app, inside of which you will find an executable file called "MSEC_IT_AAMS". 

7. Double click the application to run it. 

8. You will first be redirected to a login page. Log in using the credentials below:
   - Admin Login:  
     - Username: it_admin  
     - Password: itadmin
   - 1st Year Login:  
     - Username: it_1styear  
     - Password: it1styear
   - 2nd Year Login:  
     - Username: it_2ndyear  
     - Password: it2ndyear
   - 3rd Year Login:  
     - Username: it_3rdyear  
     - Password: it3rdyear
   - 4th Year Login:  
     - Username: it_4thyear  
     - Password: it4thyear

9. Upon logging in using admin credentials, you can can upload respective datasets for each year. 
	- Year specific dataset is available in the directory "IT YEARS DATASET". 

	- "IT YEARS' CSV FILES" FOLDER: Contains csv files of year-specific student details, that includes student names and their 			register numbers. 

	- "IT YEARS' IMAGES" FOLDER: Contains "ZIPPED IT IMAGES" folder, which holds year-specific zipped images of students. 

10. Upon logging in using faculty credentials, you can:
   - Control the webcam feed using "Turn On" and "Turn Off" buttons.
   - View real-time attendance updates.
   - Download the attendance file for the day from the interface.


