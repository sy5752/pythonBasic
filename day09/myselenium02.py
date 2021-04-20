from selenium import webdriver
import time
from PyQt5 import uic
from PyQt5.Qt import QMainWindow
from anaconda_navigator.utils.qthelpers import qapplication
import sys
 
browser = webdriver.Chrome()

# browser.get("http://localhost:8081/HELLOWEB2/mylogin")
# time.sleep(1)
browser.get("http://localhost:8081/HELLOWEB2/mycrawl")
# time.sleep(1)
 

form_class = uic.loadUiType("myselenium02.ui")[0]
#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.pb_click)
        
    def pb_click(self):
        menus = browser.find_elements_by_css_selector('td')
        for i in menus:
            print(i.text)
        
if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = qapplication(sys.argv) 
 
    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 
 
    #프로그램 화면을 보여주는 코드
    myWindow.show()
 
    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()      