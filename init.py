import sys

from PyQt5 import QtWidgets

from processor import Processor
from ui import Ui_MainWindow

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    processor = Processor(ui)
    MainWindow.show()
    sys.exit(app.exec_())
