import cv2
import os

while True:
	imageName = input("File name [include '.jpg' at the end of the name: ")

	if os.path.exists(imageName):
		image= cv2.imread(imageName, 1)
		cv2.imshow(imageName, image)
		cv2.waitKey(0)
		cv2.destroyAllWindows()
		break

	else:
		print("File name doesn't exist...")