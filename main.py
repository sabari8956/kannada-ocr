from typing import Dict
from utils import write_to_file
import fitz  
from pre_processing import preprocess_image
from ocr import extractText_easyOCR, extractText_tesseract
from llm_openai import process_image_and_text
import os
import sys

def main():
    """
    Main function to extract images from a PDF, preprocess them, extract text using OCR, 
    and then process the extracted text along with the original image using OpenAI's GPT-4O model.
    """
    
    # Define the file name of the PDF to process
    FILE_NAME = sys.argv[1]
    # Base directory for storing images
    BASE_DIR = "images"
    # Construct output directory based on the PDF file name
    OUTPUT_DIR = f"{BASE_DIR}/{FILE_NAME.split('/')[-1].split('.')[0]}"
    # Directory for storing processed images
    PROCESSED_DIR = f"{OUTPUT_DIR}/processed"
    # Directory for storing final text results
    TEXT_DIR = f"{OUTPUT_DIR}/results"
    
    # Ensure the directories exist
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    os.makedirs(PROCESSED_DIR, exist_ok=True)
    os.makedirs(TEXT_DIR, exist_ok=True)
    
    print("Extracting images from PDF...")
    # Open the PDF file
    doc = fitz.open(FILE_NAME)
    print("Loading ", end="")
    for page_number in range(len(doc)):

        page = doc.load_page(page_number)
        pix = page.get_pixmap()
        output_image_path = f"{OUTPUT_DIR}/page_{page_number}.png"
        pix.save(output_image_path)
        
        processed_image_path = f"{PROCESSED_DIR}/page_{page_number}.png"
        # Preprocess the raw image
        preprocess_image(output_image_path, processed_image_path)
        
        # Extract text from the processed image using Tesseract OCR
        result = extractText_tesseract(processed_image_path)
        # Process the extracted text along with the original image using OpenAI's GPT-4O model
        final_result: Dict = process_image_and_text(result, output_image_path)
        # Write the final processed text to a file
        write_to_file(final_result["choices"][0]["message"]["content"], f"{TEXT_DIR}/page_{page_number}_final.txt")
        
        print(".", end="")
    
if __name__ == "__main__":
    main()