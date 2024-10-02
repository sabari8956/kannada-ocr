import cv2

def preprocess_image(image_path: str, save_path: str) -> None:
    """
    Preprocesses an image by converting it to grayscale and applying binary thresholding.

    This function reads an image from the specified path, converts it to grayscale, applies binary thresholding, and saves the processed image to the specified save path.

    Parameters:
    - image_path (str): The path to the image file to be processed.
    - save_path (str): The path where the processed image will be saved.
    """
    # Read the image in grayscale
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Apply binary thresholding to the image
    _, thresholded = cv2.threshold(image, 150, 255, cv2.THRESH_BINARY)
    cv2.imwrite(save_path, thresholded)


# def preprocess_image(image_path, save_path):
#     image = cv2.imread(image_path)

#     # Convert to grayscale
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#     # Apply Gaussian blur
#     blurred = cv2.GaussianBlur(gray, (5, 5), 0)

#     # Apply adaptive thresholding
#     thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

#     # Optionally apply morphology operations to clean noise
#     kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
#     morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

#     cv2.imwrite(save_path, morph)
#     return morph
