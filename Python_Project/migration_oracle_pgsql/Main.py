import sys
from MergeInto import MergeInto
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QLabel, QPushButton, QWidget, QApplication, QTextEdit, QDesktopWidget

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Main Window'
        self.left = 300
        self.top = 300
        self.width = 640
        self.height = 480
        self.initUI()
    
    def button_event(self):
        text = self.text_edit.toPlainText() # text_edit text 값 가져오기
        
        
        str1 = "WITH upsert as"
        str2 = "UPDATE"
        str3 = "SET"
        str4 = "WHERE"
        str5 = "RETURING *"
        str6 = "INSERT INTO"
        str7 = ""
        
        
        self.Update_text_edit.setText(text) # label에 text 설정하기

    
    def windowsCenter(self):
        wfd = self.frameGeometry() #Windows Frame Data 가져옴
        cmc = QDesktopWidget().availableGeometry().center() #ComputerMonitorCenter 위치 파악
        wfd.moveCenter(cmc)
        self.move(wfd.topLeft())
    
    def initUI(self):
            self.setWindowTitle('Hello mig Tool') #타이틀바
            self.resize(1100,700)
            self.windowsCenter()
            
            self.text_edit = QTextEdit(self)
            self.text_edit.setGeometry(50,50,400,400)

            self.Update_text_edit = QTextEdit(self)
            self.Update_text_edit.setGeometry(650,50,400,400)
            self.Update_text_edit.setText('default text')
            self.Update_text_edit.setReadOnly(True)  
            
            self.button = QPushButton(self)
            self.button.move(500, 15)
            self.button.setText('Get Text')
            self.button.clicked.connect(self.button_event)

            self.show()# 출력 
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.aboutToQuit.connect(app.deleteLater)
    ex = App()
    MergeInto.show()
    sys.exit(app.exec_())
    