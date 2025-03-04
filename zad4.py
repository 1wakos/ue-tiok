import cv2

image_gray = cv2.imread("images/cat2.jpg", cv2.IMREAD_GRAYSCALE)
filename = "images/savedImage.jpg"

if image_gray is not None:
    cv2.imwrite(filename, image_gray)
    print("your cat picture has been saved!")