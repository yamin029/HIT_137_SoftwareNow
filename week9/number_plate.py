import cv2
import matplotlib.pyplot as plt
import imutils
import pytesseract
import numpy as np

# Read the image
image = cv2.imread("car2.jpeg")
# cv2.imshow("Car with Number Plate", image)
# cv2.waitKey(q0)

# converting the image to grayscale form BGR
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.imshow("Gray Color image", gray)
# cv2.waitKey(0)

# Displaying the gray scaled image in a plot
# plt.imshow(gray)
# plt.show()

# applying filters to remove unwanted noise from our image
filter = cv2.bilateralFilter(gray, 11, 17, 17)
# plt.imshow(filter)
# plt.show()

# edge detection of the image
edge = cv2.Canny(filter, 20, 300)
plt.imshow(edge)
# plt.show()

# Finding rectangle in the image
key_points = cv2.findContours(
    edge.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(key_points)
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

location = None
for contour in contours:
    approx = cv2.approxPolyDP(contour, 10, True)
    if (len(approx) == 4):
        location=approx
        break

mask  = np.zeros(gray.shape, np.uint8)
number_plate = cv2.drawContours(mask, [location], 0, 255, -1)
number_plate = cv2.bitwise_and(image, image, mask=mask)

plt.imshow(number_plate)
plt.show()

# masking and cropping the image
(x, y) = np.where(mask==255)
(x1, y1) = (np.min(x), np.min(y))
(x2, y2) = (np.max(x), np.max(y))

cropped_image = gray[x1:x2+1, y1:y2+1]
plt.imshow(cropped_image)
plt.show()

plate = pytesseract.image_to_string(cropped_image, lang='eng')
print("Number Plate: ", plate)

cv2.waitKey(0)
cv2.destroyAllWindows()