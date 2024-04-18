import cv2



stream_url = 'http://192.168.0.115:8080/?action=stream'

# Open the camera
cap = cv2.VideoCapture(stream_url)  # 0 for /dev/video0

# Check if camera opened successfully
if not cap.isOpened():
    print("Error: Couldn't open the camera")
    exit()

# Set desired resolution (640x480 in this case)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Loop to capture and display frames
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Check if frame is captured successfully
    if not ret:
        print("Error: Couldn't capture frame")
        break

    # Display the frame
    cv2.imshow('Camera Feed', frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close all windows
cap.release()
cv2.destroyAllWindows()
