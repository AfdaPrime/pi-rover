import time
import picamera

# Initialize camera
camera = picamera.PiCamera()

try:
    # Start preview
    camera.start_preview()

    # Wait for 10 seconds
    time.sleep(10)

    # Stop preview
    camera.stop_preview()

finally:
    # Close camera
    camera.close()
