import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open the camera.")
else:
    while True:
        ret, frame = cap.read()

        if not ret:
            print("Error: Could not read a frame from the camera.")
            break

        cv2.imshow("Live Camera Feed", frame)

        # Exit the loop and close the window when the 'q' key is pressed
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break

    # Release the camera
    cap.release()

# Close the OpenCV window
cv2.destroyAllWindows()
