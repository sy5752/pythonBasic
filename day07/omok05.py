import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtGui
from PyQt5.QtGui import * 
from PyQt5.QtCore import *
from Cython.Compiler.Naming import self_cname
 
#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("omok05.ui")[0]
 
#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.flag_wb = True
        self.flag_playing = True
        self.icon0 = QIcon('0.png')
        self.icon1 = QIcon('1.png')
        self.icon2 = QIcon('2.png')
        self.icon3 = QIcon('3.png')
        self.arr2dpb = []
        self.arr2d = [
                        [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                        [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                        [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                        [0,0,0,3,0, 0,0,0,0,3, 0,0,0,0,0, 3,0,0,0],
                        [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],

                        [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                        [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                        [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                        [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                        [0,0,0,3,0, 0,0,0,0,3, 0,0,0,0,0, 3,0,0,0],

                        [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                        [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                        [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                        [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                        [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],

                        [0,0,0,3,0, 0,0,0,0,3, 0,0,0,0,0, 3,0,0,0],
                        [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                        [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                        [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0]
                    ]
        
        for i in range(19):
            line = []
            for j in range(19):
                button = QPushButton("", self)
                button.setGeometry(j*40, i*40, 40, 40)
        #         button.setGeometry(x, y, width, height)
                button.setIconSize(QSize(40, 40))
                button.setIcon(self.icon0)
                button.setToolTip("" + str(i) + "," + str(j) + "")
                button.clicked.connect(self.pb_click)
                line.append(button)
            self.arr2dpb.append(line)
        self.myrender()
        
        self.pb_reset.clicked.connect(self.pb_click_reset)
    
        
    def myrender(self):
        for i in range(19):
            for j in range(19):
                if self.arr2d[i][j] == 0:
                    self.arr2dpb[i][j].setIcon(self.icon0)
                elif self.arr2d[i][j] == 1:
                    self.arr2dpb[i][j].setIcon(self.icon1)
                elif self.arr2d[i][j] == 2:
                    self.arr2dpb[i][j].setIcon(self.icon2)
                elif self.arr2d[i][j] == 3:
                    self.arr2dpb[i][j].setIcon(self.icon3)
                
    def pb_click_reset(self):
        for i in range(19):
            for j in range(19):
                if i==3 and j==3 or i==3 and j==9 or i==3 and j==15:
                    self.arr2d[i][j] = 3
                elif i==9 and j==3 or i==9 and j==9 or i==9 and j==15:
                    self.arr2d[i][j] = 3
                elif i==15 and j==3 or i==15 and j==9 or i==15 and j==15:
                    self.arr2d[i][j] = 3
                else :
                    self.arr2d[i][j] = 0
        self.myrender()
        self.flag_playing = True
        self.flag_wb = True
        
    def pb_click(self) :
        if not self.flag_playing :
            return 
        
        str_ij = self.sender().toolTip()
        arr_ij = str_ij.split(",")
        i = int(arr_ij[0])
        j = int(arr_ij[1])
        
        if self.arr2d[i][j] == 1 or self.arr2d[i][j] == 2:
#         if self.arr2d[i][j] >0:
            return 
        
        stone_info = 0
        
        if self.flag_wb == True:
            self.arr2d[i][j] = 1
            stone_info = 1
        elif self.flag_wb == False:
            self.arr2d[i][j] = 2
            stone_info = 2
        
        up = self.getUp(i, j, stone_info)
        dw = self.getDw(i, j, stone_info)
        le = self.getLe(i, j, stone_info)
        ri = self.getRi(i, j, stone_info)
        
        ur = self.getUR(i, j, stone_info)
        ul = self.getUL(i, j, stone_info)
        
        dr = self.getDR(i, j, stone_info)
        dl = self.getDL(i, j, stone_info)
        
        self.myrender()
        
        if (up+dw)+1 == 5 or (le+ri)+1 == 5 or (ur+dl)+1 == 5 or (dr+ul)+1 == 5:
            if self.flag_wb == True:
                QMessageBox.about(self, "결과", "백돌이 이겼습니다.")
            else:
                QMessageBox.about(self, "결과", "흑돌이 이겼습니다.")
            
            self.flag_playing = False
                
        self.flag_wb = not self.flag_wb
    
    def getUp(self, i, j, stone_info):
        cnt = 0
        while True :
            i -= 1
            if i < 0:
                return cnt
            if j < 0:
                return cnt
            try:
                if self.arr2d[i][j] == stone_info:
                    cnt += 1
                else:
                    return cnt
            except:
                return cnt
 
    def getDw(self, i, j, stone_info):
        cnt = 0
        while True :
            i += 1
            if i < 0:
                return cnt
            if j < 0:
                return cnt
            try:
                if self.arr2d[i][j] == stone_info:
                    cnt += 1
                else:
                    return cnt
            except:
                return cnt
            
    def getLe(self, i, j, stone_info):
        cnt = 0
        while True :
            j -= 1
            if i < 0:
                return cnt
            if j < 0:
                return cnt
            try:
                if self.arr2d[i][j] == stone_info:
                    cnt += 1
                else:
                    return cnt
            except:
                return cnt
            
    def getRi(self, i, j, stone_info):
        cnt = 0
        while True :
            j += 1
            if i < 0:
                return cnt
            if j < 0:
                return cnt
            try:
                if self.arr2d[i][j] == stone_info:
                    cnt += 1
                else:
                    return cnt
            except:
                return cnt
            
    def getUR(self, i, j, stone_info):
        cnt = 0
        while True :
            i -= 1
            j += 1
            if i < 0:
                return cnt
            if j < 0:
                return cnt
            try:
                if self.arr2d[i][j] == stone_info:
                    cnt += 1
                else:
                    return cnt
            except:
                return cnt
            
    def getUL(self, i, j, stone_info):
        cnt = 0
        while True :
            i -= 1
            j -= 1
            if i < 0:
                return cnt
            if j < 0:
                return cnt
            try:
                if self.arr2d[i][j] == stone_info:
                    cnt += 1
                else:
                    return cnt
            except:
                return cnt
            
    def getDR(self, i, j, stone_info):
        cnt = 0
        while True :
            i += 1
            j += 1
            if i < 0:
                return cnt
            if j < 0:
                return cnt
            try:
                if self.arr2d[i][j] == stone_info:
                    cnt += 1
                else:
                    return cnt
            except:
                return cnt
            
    def getDL(self, i, j, stone_info):
        cnt = 0
        while True :
            i += 1
            j -= 1
            if i < 0:
                return cnt
            if j < 0:
                return cnt
            try:
                if self.arr2d[i][j] == stone_info:
                    cnt += 1
                else:
                    return cnt
            except:
                return cnt
            
            
if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 
 
    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 
 
    #프로그램 화면을 보여주는 코드
    myWindow.show()
 
    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()