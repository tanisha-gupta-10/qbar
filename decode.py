import cv2
img = cv2.imread("form.png")
data = cv2.QRCodeDetector().detectAndDecode(img)
print('decoded data is: ', data[0])