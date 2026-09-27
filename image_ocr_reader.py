import cv2
import pytesseract

def test_image_readability(image_path):
    # 1. Loads the visual challenge image
    image = cv2.imread(image_path)
    
    # 2. Pre-processing: Converts to grayscale
    # This helps the AI/OCR algorithm focus only on shapes, ignoring background colors
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # 3. Applies a threshold to make the text purely black and the background purely white
    _, processed_image = cv2.threshold(grayscale, 127, 255, cv2.THRESH_BINARY_INV)
    
    # 4. Runs the OCR to extract characters from the image
    # Tesseract attempts to decode visual patterns into a text string
    extracted_text = pytesseract.image_to_string(processed_image, config='--psm 6')
    
    return extracted_text.strip()

# Usage example (Requires Tesseract installed on the operating system):
# result = test_image_readability("your_captcha_test.png")
# print(f"Security test result: {result}")
