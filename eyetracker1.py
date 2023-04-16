import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 2


eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')


cap = cv2.VideoCapture(0)


left_eye_pos = None
right_eye_pos = None

while True:
   
    ret, frame = cap.read()
   
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

   
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

   
    for (x, y, w, h) in faces:
       
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

       
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

       
        eyes = eye_cascade.detectMultiScale(roi_gray)

       
        for (ex, ey, ew, eh) in eyes:
           
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

           
            eye_center = (x + ex + ew//2, y + ey + eh//2)

            if eye_center[0] < x + w//2:
                left_eye_pos = eye_center

           
            else:
                right_eye_pos = eye_center

   
    if left_eye_pos is not None and right_eye_pos is not None:
        eye_distance = abs(left_eye_pos[0] - right_eye_pos[0])
       
        if eye_distance > 100:
            cv2.putText(frame, "Looking off screen", (50,50), font, font_scale, (0, 0, 255))

       
        else:
           
            cv2.putText(frame, "Looking at screen", (50,50), font, font_scale, (0, 0, 255))

   
    cv2.imshow('img', frame)

    # Exit the loop if the user presses the 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the window
cap.release()
cv2.destroyAllWindows()

#detecting faces
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 2

# Load the cascade for detecting eyes
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# Start the camera
cap = cv2.VideoCapture(0)

# Initialize variables for eye position
left_eye_pos = None
right_eye_pos = None

while True:
    # Read the frame
    ret, frame = cap.read()

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # Loop through each face
    for (x, y, w, h) in faces:
        # Draw a rectangle around the face
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # Crop the region of interest (ROI) for the eyes
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        # Detect eyes
        eyes = eye_cascade.detectMultiScale(roi_gray)

        # Loop through each eye
        for (ex, ey, ew, eh) in eyes:
            # Draw a rectangle around the eye
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

            # Calculate the center of the eye
            eye_center = (x + ex + ew//2, y + ey + eh//2)

            # If the eye is on the left half of the face, update left_eye_pos
            if eye_center[0] < x + w//2:
                left_eye_pos = eye_center

            # If the eye is on the right half of the face, update right_eye_pos
            else:
                right_eye_pos = eye_center

 
    if left_eye_pos is not None and right_eye_pos is not None:
        eye_distance = abs(left_eye_pos[0] - right_eye_pos[0])
       
        if eye_distance < 50:
            cv2.putText(frame, "Looking at screen", (50,50), font, font_scale, (0, 0, 255))

        # Otherwise, the eyes are looking straight ahead
        else:
           
            cv2.putText(frame, "Looking off screen", (50,50), font, font_scale, (0, 0, 255))
    
    # Display the image with the detected faces and eyes
    cv2.imshow('img', frame)

    # Exit the loop if the user presses the 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the window
cap.release()
cv2.destroyAllWindows()
