import pytesseract 
from PIL import Image
class Text:
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe" 
    
    def __init__(self): 
        self.config = r'--oem 3 --psm 6'

    def open_file(self,path): 
        self.img = Image.open(path)
        return self.img

    def text(self,img):
        print(pytesseract.image_to_string(img, config = self.config, lang = "rus"))


a = Text()

res = a.open_file(r'C:\Users\User\Documents\im.png')
a.text(res)