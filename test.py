import cv2

# Create a VideoCapture object to capture images from the default camera
cap = cv2.VideoCapture(0)

# Create a window to show real-time video capture
cv2.namedWindow('Webcam')

# Create a variable to keep track of whether the user wants to record an image or not
record_image = False

# Loop through frames from the video capture
while True:
    # Read a frame from the video capture
    ret, frame = cap.read()

    # If the frame was read successfully
    if ret:
        # Show the frame in the window
        cv2.imshow('Webcam', frame)

        # If the user presses the 'q' key, break out of the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        #   กด r เพื่อถ่าย กด q เพื่อออก
        # If the user presses the 'r' key, set the record_image variable to True
        elif cv2.waitKey(1) & 0xFF == ord('r'):
            record_image = True

        # If the record_image variable is True, save the current frame to a file
        if record_image:
            cv2.imwrite('captured_image.jpg', frame)
            print('Image saved successfully!')
            record_image = False

# Release the VideoCapture object and destroy all windows
cap.release()
cv2.destroyAllWindows()
