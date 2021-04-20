import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.Qt import QPixmap, QIcon, QSize
from PyQt5 import QtGui, QtCore
 
#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("omok01.ui")[0]
 
#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        
        for i in range(10) :
            for j in range(10) :
                button = QPushButton("", self)
                button.setGeometry(j*40, i*40, 40, 40)
                button.setIconSize(QSize(40, 40))
                button.setIcon(QIcon('0.png'))
                button.clicked.connect(self.pb_click)
            
   
    def pb_click(self) :
        print("pb_click")
                
if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 
 
    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 
 
    #프로그램 화면을 보여주는 코드
    myWindow.show()
 
    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()