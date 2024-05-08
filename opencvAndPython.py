import cv2
import pytesseract

# Read the image using OpenCV
image = cv2.imread('img2.png')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Use Tesseract to do OCR on the grayscale image
text = pytesseract.image_to_string(gray_image)

# Print the extracted text
print(text)