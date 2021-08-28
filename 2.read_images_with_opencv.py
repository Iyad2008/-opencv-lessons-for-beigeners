import cv2

img = cv2.imread("inputs/cat.jpg")
(h, w, c) = img.shape
print(w, h)
res = cv2.resize(img, (w//4, h//4))
# print(img)
cv2.imshow("image", res)
cv2.waitKey(0)