import cv2
filepath = 'peakpx.jpg'
image = cv2.imread(filepath, 1)
cv2.imshow("TEN",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
