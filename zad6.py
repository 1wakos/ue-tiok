import cv2

image = cv2.imread("images/cat1.jpg")

if image is not None:
    cv2.namedWindow("silly cat!", cv2.WINDOW_NORMAL) 
    cv2.imshow('silly cat!', image) 
    cv2.waitKey(0) 
    cv2.destroyAllWindows()
else:
    print("something is wrong with your cat picture...")