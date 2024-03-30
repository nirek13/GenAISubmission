import cv2

# Load the pre-trained Haar Cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Create a VideoCapture object to access the webcam
cap = cv2.VideoCapture(0)  # Use 0 for the default webcam, or change it to the appropriate index for your webcam

# Check if the camera was opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

# Set a default window size
window_width = 1000
window_height = 600

# Read frames from the webcam and detect faces
busy = False
while True:  
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Check if the frame was read successfully
    if not ret:
        print("Error: Could not read frame.")
        break

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=7, minSize=(30, 30))
    print(len(faces))
    if len(faces) > 0:
        print(f"Detected {len(faces)} face(s).")
        cv2.imwrite('image1.jpg', frame)
        busy = True



    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Resize the frame to the desired window size
    frame = cv2.resize(frame, (window_width, window_height))

    # Display the resized frame with detected faces
    cv2.imshow('Face Tracking', frame)

    # Exit the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture object and close all windows
cap.release()
cv2.destroyAllWindows()