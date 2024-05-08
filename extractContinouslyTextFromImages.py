import cv2
import pytesseract

#####################################################################################################

# for windows sys:

# Set the path to the Tesseract executable (replace 'path/to/tesseract' with the actual path) 
#pytesseract.pytesseract.tesseract_cmd = r'path/to/tesseract'
#####################################################################################################

# I am on linux sys so i skip this step

# Open a video capture object (0 corresponds to the default camera, you can change it if needed)
cap = cv2.VideoCapture(0)

cap.set(3,1780)
cap.set(4,480)


while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Use Tesseract to do OCR on the grayscale frame
    text = pytesseract.image_to_string(gray_frame)

    # Display the frame with the extracted text
    cv2.putText(frame, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow('Frame', frame)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
