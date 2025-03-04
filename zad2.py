import cv2

image_color = cv2.imread("images/cat1.jpg", cv2.IMREAD_COLOR)
if image_color is not None:
    channels = image_color.shape[2]
    print(f"channels: {channels}")