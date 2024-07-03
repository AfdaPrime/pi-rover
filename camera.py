import cv2

def main():
    # Open the camera
    cap = cv2.VideoCapture(0)
    
    # Check if the camera opened successfully
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return
    
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        
        # If the frame was not captured successfully, break the loop
        if not ret:
            break
        
        # Display the resulting frame
        cv2.imshow('Camera', frame)
        
        # Press 'q' on the keyboard to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
