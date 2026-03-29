from PyQt5.QtWidgets import QMainWindow, QApplication #type:ignore
from PyQt5 import uic #type:ignore
import sys
import resourcesConverted

class MainUI(QMainWindow):
    def __init__(self):
        super(MainUI, self).__init__()
        self.ui = uic.loadUi("KioskProject.ui")

        self.ui.pages.setCurrentWidget(self.ui.page1)
    
    def show(self):
        self.ui.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    burger = MainUI()
    burger.show()
    app.exec_()