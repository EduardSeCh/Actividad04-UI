from PySide2.QtWidgets import QMainWindow
from ui_mainWindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self): 
        super(MainWindow, self).__init__() #Contructor de QMainWindow
        ui = Ui_MainWindow()
        #mandar los datos de ui a la ventana
        ui.setupUi(self)