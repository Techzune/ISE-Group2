# title: CodeHighlightWindow
# author: Avan Patel, Kohler Smallwood, Azlin Reed, Jordan Stremming, Steven Huynh, Zach Butterbaugh
# purpose: Backbone of code highlighting window; displays code with algorithm steps highlighted
from PyQt5.QtWidgets import QMainWindow


# inherits QMainWindow (a basic window)
class CodeHighlightWindow(QMainWindow):

    def __init__(self, main_app):
        # run the init of QMainWindow
        super().__init__()

        # save a reference to the main_app
        self.main_application = main_app
