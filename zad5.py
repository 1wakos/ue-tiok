import cv2

image1 = cv2.imread("images/cat1.jpg")
image2 = cv2.imread("images/cat2.jpg")

if image1 is not None and image2 is not None:
    cv2.imshow("SCARED CAT", image1)
    cv2.imshow("DETECTIVE CAT", image2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print('something was wrong with your cat pictures!')
