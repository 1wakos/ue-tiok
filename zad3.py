import cv2

image_gray = cv2.imread("images/cat2.jpg", cv2.IMREAD_GRAYSCALE)
if image_gray is not None:
    print(f"channels: {len(image_gray.shape)}")
