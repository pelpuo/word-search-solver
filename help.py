from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

print(pytesseract.image_to_string(Image.open('screenshots/puzzle_1.png')))