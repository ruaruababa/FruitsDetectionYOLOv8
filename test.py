import os
import sys

import cv2
from PySide6.QtCore import QDir, QFile, QThread, Signal
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QFileDialog, QWidget
from predict import detectFruits

def convertCVImage2QtImage(cv_img):
    cv_img = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
    height, width, channel = cv_img.shape
    bytesPerLine = 3 * width
    qimg = QImage(cv_img.data, width, height, bytesPerLine, QImage.Format_RGB888)
    return QPixmap.fromImage(qimg)


class ProcessImage(QThread):
    signal_show_frame = Signal(object)

    def __init__(self, fileName):
        QThread.__init__(self)
        self.fileName = fileName

        from predict import detectFruits

        self.detector = detectFruits()

    def run(self):
        self.video = cv2.VideoCapture(self.fileName)
        while True:
            valid, self.frame = self.video.read()
            if valid is not True:
                break
            self.frame = self.detector.detect(self.frame)
            self.signal_show_frame.emit(self.frame)
            cv2.waitKey(30)
        self.video.release()

    def stop(self):
        try:
            self.video.release()
        except:
            pass


class show(QThread):
    signal_show_image = Signal(object)

    def __init__(self, fileName):
        QThread.__init__(self)
        self.fileName = fileName
        self.video = cv2.VideoCapture(self.fileName)

    def run(self):
        while True:
            valid, self.frame = self.video.read()
            if valid is not True:
                break
            self.signal_show_image.emit(self.frame)
            cv2.waitKey(30)
        self.video.release()

    def stop(self):
        try:
            self.video.release()
        except:
            pass


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        loader = QUiLoader()
        self.ui = loader.load("ui/form.ui")

        self.ui.btn_browse.clicked.connect(self.getFile)
        self.ui.btn_start.clicked.connect(self.predict)

        self.ui.show()

    def getFile(self):
        self.fileName = QFileDialog.getOpenFileName(
            self, "Single File", "C:'", "*.jpg *.mp4 *.jpeg *.png *.avi"
        )[0]
        print(self.fileName)
        self.ui.txt_address.setText(str(self.fileName))
        self.show = show(self.fileName)
        self.show.signal_show_image.connect(self.show_input)
        self.show.start()

    def predict(self):
        detectFruits(self.fileName)
        # self.process_image = ProcessImage(self.fileName)
        # self.process_image.signal_show_frame.connect(self.show_output)
        # self.process_image.start()

    def show_input(self, image):
        pixmap = convertCVImage2QtImage(image)
        self.ui.lbl_input.setPixmap(pixmap)

    def show_output(self, image):
        pixmap = convertCVImage2QtImage(image)
        self.ui.lbl_output.setPixmap(pixmap)
        print("show output:", image.shape)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    sys.exit(app.exec())
