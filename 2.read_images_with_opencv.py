import cv2

img = cv2.imread("inputs/cat.jpg")
(h, w, c) = img.shape
if len(img.shape) < 3:
    type_ = 'gray scale'
elif len(img.shape) == 3:
    type_ = 'Color'

print(f'the image width is {w} and the image heigth is {h} and it is a {type_}')
res = cv2.resize(img, (w // 3, h // 3))
# print(img)
cv2.imshow("img", img)
cv2.imshow("resized", res)
cv2.waitKey(0)
