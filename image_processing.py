import cv2

def grayscale(image_path):
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('grayscale_image.jpg', gray_image)

def adjust_contrast(image_path, alpha, beta):
    image = cv2.imread(image_path)
    adjusted_image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
    cv2.imwrite('adjusted_contrast_image.jpg', adjusted_image)

def negative(image_path):
    image = cv2.imread(image_path)
    negative_image = cv2.bitwise_not(image)
    cv2.imwrite('negative_image.jpg', negative_image)

if __name__ == "__main__":
    image_path = 'your_image.jpg'
    grayscale(image_path)
    adjust_contrast(image_path, 2.0, 50)
    negative(image_path)
