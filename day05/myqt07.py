import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import random
from qtconsole.mainwindow import background
 
#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("myqt07.ui")[0]
 
#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.pb1.clicked.connect(self.pb_click)
        self.pb2.clicked.connect(self.pb_click)
        self.pb3.clicked.connect(self.pb_click)
        
    def pb_click(self) :
        rnd = random.randrange(1,4)
        if rnd == 1:
            com = "가위"
        elif rnd == 2:
            com = "바위"
        elif rnd == 3:
            com = "보"
            
        user = self.sender().text()
        
        if user == com:
            result = "비겼습니다"
        elif user=="가위" and com=="보" or user=="바위" and com=="가위" or user=="보" and com=="바위":
            result = "이겼습니다"
        else:
            result = "졌습니다."
            
        self.le1.setText(user)
        self.le2.setText(com)
        self.le3.setText(result)
        
            
  

if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 
 
    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 
 
    #프로그램 화면을 보여주는 코드
    myWindow.show()
 
    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()