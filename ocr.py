import easyocr
import pytesseract
from PIL import Image


def extractText_easyOCR(image_path):
    # Initialize the reader with Kannada and English language
    reader = easyocr.Reader(['kn'])

    # Perform OCR on the image
    result = reader.readtext(image_path, detail=0)

    # Join the result list into a single string with newline separators
    result = "\n".join(result)
    
    return result


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
def extractText_tesseract(image_path):
    
    # Configure Tesseract OCR
    custom_config = r'--oem 3 --psm 1 -l kan+eng'
    # OEM 3: Default OCR Engine mode
    # PSM 1: Automatic page segmentation with OSD (Orientation and Script Detection)
    # -l kan+eng: Use Kannada and English language models
    
    # Additional options to improve accuracy
    # custom_config += r' --dpi 300'  # Assume 300 DPI for better accuracy
    # custom_config += r' --tessdata-dir "C:\Program Files\Tesseract-OCR\tessdata"'  # Specify tessdata directory if needed
    
    result = pytesseract.image_to_string(Image.open(image_path), config=custom_config)
    
    
    return result

def write_to_file(text, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)


if __name__ == "__main__":
    image_path = r'images\processed\page_1.png'
    write_to_file(extractText_easyOCR(image_path), 'easyocr_output.txt')
    # write_to_file(extractText_tesseract(image_path), 'tesseract_output.txt')