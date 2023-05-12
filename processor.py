import logging
import os
import os.path
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from ultralytics import YOLO

from ui import Ui_MainWindow


class Processor:
    ui: Ui_MainWindow

    def __init__(self, ui: Ui_MainWindow):
        self.ui = ui
        ui.browseFile.clicked.connect(self.browse_file)
        ui.predict.clicked.connect(self.show_predict)

    def browse_file(self):
        self.directory = QtWidgets.QFileDialog.getOpenFileName(
            None,
            "Browse File",
            "",
            "Image Files (*.png *.jpeg *.jpg *.bmp *.gif *.tiff *.ico);;All Files (*)",
        )[0]
        self.fileName = QtCore.QFileInfo(self.directory).fileName()
        print(" self.fileName", self.fileName)
        pixmap = QtGui.QPixmap(self.directory)
        self.ui.photo.setPixmap(pixmap.scaled(self.ui.photo.size()))
        self.ui.lineEdit.setText("{}".format(self.directory))

    def _set_text(self, text):
        return text

    def show_predict(self):
        src_ = r"C:\Users\admin\Pictures\fruits\tao.jepg"

        model = YOLO(
            r"C:\Users\admin\FruitsDetectionYOLOv8\models\combine_train\train28\best.pt"
        )
        save_dir = r"C:\Users\admin\FruitsDetectionYOLOv8\results"
        model.overrides = {
            "project": save_dir,
            "exist_ok": True,
        }
        model.predict(
            source=f"{self.directory}",
            save=True,
            conf=0.4,
        )
        self.ui.photo2.setPixmap(
            QtGui.QPixmap(os.path.realpath(f"results/predict/{self.fileName}"))
        )
