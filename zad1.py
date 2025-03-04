import cv2

image = cv2.imread("images/cat1.jpg")
if image is None:
    print("no cat will be shown to you, sorry!")
else:
    cv2.imshow("cat picture!", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()