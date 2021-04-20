# -*- coding: utf-8 -*-
 
# Form implementation generated from reading ui file 'C:/Users/PC-05/Desktop/Hello.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
 
# from PyQt5 import QtCore, QtGui, QtWidgets
#  
# class Ui_MainWindow(object):
#     def setupUi(self, MainWindow):
#         MainWindow.setObjectName("MainWindow")
#         MainWindow.resize(651, 474)
#         self.centralwidget = QtWidgets.QWidget(MainWindow)
#         self.centralwidget.setObjectName("centralwidget")
#         self.lbl = QtWidgets.QLabel(self.centralwidget)
#         self.lbl.setGeometry(QtCore.QRect(160, 190, 111, 16))
#         self.lbl.setObjectName("lbl")
#         self.pb = QtWidgets.QPushButton(self.centralwidget)
#         self.pb.setGeometry(QtCore.QRect(380, 190, 75, 23))
#         self.pb.setObjectName("pb")
#         MainWindow.setCentralWidget(self.centralwidget)
#         self.menubar = QtWidgets.QMenuBar(MainWindow)
#         self.menubar.setGeometry(QtCore.QRect(0, 0, 651, 21))
#         self.menubar.setObjectName("menubar")
#         MainWindow.setMenuBar(self.menubar)
#         self.statusbar = QtWidgets.QStatusBar(MainWindow)
#         self.statusbar.setObjectName("statusbar")
#         MainWindow.setStatusBar(self.statusbar)
#  
#         self.retranslateUi(MainWindow)
#         QtCore.QMetaObject.connectSlotsByName(MainWindow)
#  
#     def retranslateUi(self, MainWindow):
#         _translate = QtCore.QCoreApplication.translate
#         MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
#         self.lbl.setText(_translate("MainWindow", "Good Morning"))
#         self.pb.setText(_translate("MainWindow", "click"))
#  
#     if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())


# import sys
#   
# #import PyQt5
# #from PyQt5.QtGui import *
# #from PyQt5.QtCore import *
# from PyQt5.QtWidgets import *
# from PyQt5 import uic
#   
#   
# main_ui = uic.loadUiType('_uiFiles/main.ui')[0]
#   
#   
# class MainDialog(QMainWindow, main_ui):
#     def __init__(self):
#         super().__init__()
#         self.setupUi(self)
#   
#   
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     main_dialog = MainDialog()
#     main_dialog.show()
#     app.exec_()


import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
 
#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("Hello.ui")[0]
 
#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.pb_click)
    def pb_click(self) :
        print("pb_Click")
        self.lbl.setText("good Evening");
 
if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 
 
    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 
 
    #프로그램 화면을 보여주는 코드
    myWindow.show()
 
    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
     
    # Ex 5-1. QPushButton.

