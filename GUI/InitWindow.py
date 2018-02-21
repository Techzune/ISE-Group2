# title: InitWindow
# author: Avan Patel, Kohler Smallwood, Azlin Reed, Jordan Stremming, Steven Huynh, Zach Butterbaugh
# purpose: Backbone of init window; a configuration window to define parameters for software
from PyQt5 import QtCore
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QMainWindow, QGridLayout, QWidget, QLabel


# inherits QMainWindow (a basic window)
class InitWindow(QMainWindow):

    def __init__(self, main_app):
        # run the init of QMainWindow
        super().__init__()

        # save a reference to the main_app
        self.main_application = main_app

        # set a fixed size, prevents resizing
        self.setFixedSize(640, 480)

        # set the title
        self.setWindowTitle("Initialization Window")

        # set the main widget of the window
        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)

        # create a grid layout for the central widgget
        gridLayout = QGridLayout(self)
        centralWidget.setLayout(gridLayout)

        # create a label centered with "Hello World"
        title = QLabel("Hello World", self)
        title.setAlignment(QtCore.Qt.AlignCenter)
        gridLayout.addWidget(title)
