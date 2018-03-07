# title: VisualizationWindow
# author: Avan Patel, Kohler Smallwood, Azlin Reed, Jordan Stremming, Steven Huynh, Zach Butterbaugh, Thea Furby
# purpose: Backbone of visualization window; displays graphical representation of algorithm
from PyQt5.QtWidgets import QMainWindow


# inherits QMainWindow (a basic window)
from gvanim import Animation


class VisualizationWindow(QMainWindow):

    def __init__(self, main_app):
        # run the init of QMainWindow
        super().__init__()

        # save a reference to the main_app
        self.main_application = main_app
