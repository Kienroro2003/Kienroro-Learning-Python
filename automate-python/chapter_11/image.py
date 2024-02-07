import pytesseract, os
from PIL import Image

# print(os.getcwd())

image_path = 'text-image.jpg'

text = pytesseract.image_to_string(Image.open(image_path))

# In ra tất cả các ký tự trong hình ảnh
print(text)