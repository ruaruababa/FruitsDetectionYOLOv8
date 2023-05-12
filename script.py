import os
import sys

from PyQt5 import QtCore, QtGui, QtWidgets


def retranslateUi(self, MainWindow):
    _translate = QtCore.QCoreApplication.translate
    MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
    self.photo.setText(_translate("MainWindow", "INPUT"))
    self.browseFile.setText(_translate("MainWindow", "Browse file"))
    self.predict.setText(_translate("MainWindow", "PREDICT"))
    self.photo2.setText(_translate("MainWindow", "OUTPUT"))


def browse_file(self):
    directory = QtWidgets.QFileDialog.getOpenFileName(
        None, "Browse File", "", "PNG (*.PNG *.png);;JPEG (*.JPEG *.jpeg *.JPG *.jpg)"
    )[0]
    print(directory)
    pixmap = QtGui.QPixmap(directory)
    self.photo.setPixmap(pixmap.scaled(self.photo.size()))
    self.lineEdit.setText("{}".format(directory))


def _set_text(self, text):
    return text


def show_predict(self):
    self.photo2.setPixmap(QtGui.QPixmap(os.path.realpath("image/predictions.png")))

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1600, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(10, 20, 761, 651))

        font = QtGui.QFont()
        font.setPointSize(40)
        self.photo.setFont(font)
        self.photo.setFrameShape(QtWidgets.QFrame.Panel)
        self.photo.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.photo.setLineWidth(5)
        self.photo.setMidLineWidth(0)
        self.photo.setScaledContents(True)
        self.photo.setObjectName("photo")

        self.browseFile = QtWidgets.QPushButton(self.centralwidget)
        self.browseFile.setGeometry(QtCore.QRect(350, 700, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.browseFile.setFont(font)
        self.browseFile.setObjectName("browse_File")
        self.browseFile.clicked.connect(browse_file)

        self.predict = QtWidgets.QPushButton(self.centralwidget)
        self.predict.setGeometry(QtCore.QRect(670, 750, 231, 61))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(False)
        font.setWeight(50)
        self.predict.setFont(font)
        self.predict.setObjectName("show_predict")
        self.predict.clicked.connect(show_predict)

        self.photo2 = QtWidgets.QLabel(self.centralwidget)
        self.photo2.setGeometry(QtCore.QRect(790, 20, 791, 651))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.photo2.setFont(font)
        self.photo2.setFrameShape(QtWidgets.QFrame.Panel)
        self.photo2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.photo2.setLineWidth(5)
        self.photo2.setScaledContents(True)
        self.photo2.setObjectName("photo2")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(520, 700, 521, 31))
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1600, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
