import pytesseract 
from PIL import Image
from interface import Ui_MainWindow

from PyQt5 import  QtWidgets

class Text:
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe" 
    
    def __init__(self): 
        self.config = r'--oem 3 --psm 6'

    def open_file(self,path): 
        self.img = Image.open(path)
        return self.img

    def text(self,img):
        print(pytesseract.image_to_string(img, config = self.config, lang = "rus"))
        return pytesseract.image_to_string(img, config = self.config, lang = "rus")


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_3.clicked.connect(self.showDi)
        

    def showDi(self):
        
        fname = QtWidgets.QFileDialog.getOpenFileName(None, 'Open file', './', '(*.jpg)')[0]
        print(fname)
        work = Text()
        path = work.open_file(fname)
        text = work.text(path)
        self.textEdit.setText(text)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())