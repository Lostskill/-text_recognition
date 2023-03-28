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
        return pytesseract.image_to_string(img, config = self.config, lang = "rus")


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_3.clicked.connect(self.showDi)
        self.ui.pushButton_4.clicked.connect(self.recognition)

    def showDi(self):
        
        self.fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', './', '(*.jpg)')[0]
        return self.fname
        print(self.fname)
 

    def recognition(self):
        work = Text()
        path = work.open_file(self.fname)
        text = work.text(path)
        print(text)
        self.ui.textEdit.setText(text)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
