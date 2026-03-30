from PyQt5.QtWidgets import QMainWindow, QApplication #type:ignore
from PyQt5 import uic #type:ignore
import sys
import resourcesConverted

class MainUI(QMainWindow):
    def __init__(self):
        super(MainUI, self).__init__()
        self.ui = uic.loadUi("KioskProject.ui")

        self.ui.pages.setCurrentWidget(self.ui.page1)
        self.ui.gawaKaDitoNgButtonOrAnyClickingObject.clicked.connect(self.showPage1)
    
    def show(self):
        self.ui.show()

    def showPage1(self):
        self.ui.pages.setCurrentWidget(self.ui.objectNameTohTeh)

    def showPage2():
        pass

    def showPage3():
        pass

    def showPage4():
        pass

        #so, sa ngayon, ayusin mo muna yung design.
 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    burger = MainUI()
    burger.show()
    app.exec_()