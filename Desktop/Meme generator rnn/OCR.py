from PIL import Image 
import pytesseract
import sys

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
print sys.stdout.encoding
print pytesseract.image_to_string(Image.open('elm.jpg')).encode(errors='replace') 
##print pytesseract.image_to_string(Image.open('test-european.jpg'), lang='fra')
