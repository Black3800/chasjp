import cv2

img = cv2.imread("cropped/lighthouse/lighthouse_crop14.png", 0)
size = img.shape[0]
sigma = int(size * 0.028)
imgnew = cv2.bilateralFilter(img, 10, sigma, sigma)
imgnew = cv2.bilateralFilter(imgnew, 20, sigma, sigma)
cv2.imwrite("10d2lx.png", imgnew)