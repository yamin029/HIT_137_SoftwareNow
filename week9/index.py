import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread("yamin.jpg")
# cv2.imshow("Yamin", image)
# cv2.waitKey(0)

img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# plt.imshow(image)
# plt.show()
print(img.shape)
h,w  = img.shape[:2]
print("Height: ", h)
print("Width", w)
B,G,R = image[250,250]
b,g,r = img[250,250]
print(f"Blue: {B} Green: {G}, Red: {R}")

# Extract logo of interest
extract_image = img[100:1505, 400:600]
# cv2.imshow("Extracted Image, ", extract_image)
# cv2.waitKey(0)

# Edge detection
edges =cv2.Canny(img, 100, 200)
cv2.imshow("Edge Detection", edges)
cv2.waitKey(0)