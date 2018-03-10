# title: CodeHighlightWindow
# author: Avan Patel, Kohler Smallwood, Azlin Reed, Jordan Stremming, Steven Huynh, Zach Butterbaugh, Thea Furby
# purpose: Backbone of code highlighting window; displays code with algorithm steps highlighted
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QColor
from PyQt5.QtWidgets import QMainWindow, QLabel
from PyQt5.uic import loadUi


# inherits QMainWindow (a basic window)
class CodeHighlightWindow(QMainWindow):

    def __init__(self, main_app):
        """
        Initialization of the CodeHighlightWindow

        :param main_app: a reference to main.py (MainApplication)
        """

        # run the init of QMainWindow
        super().__init__()

        # save a reference to the main_app
        self.main_application = main_app

        # load .ui file for window
        loadUi('GUI/CodeHighlightWindow.ui', self)

        # set the title
        self.setWindowTitle("SWEG2 - Code Highlight Window")

        self.master_font = QFont()
        self.master_font.setFamily(self.algorithm_name.font().family())
        self.master_font.setPointSize(12)

    def add_line(self, text):
        """
        Adds a line of code to the list layout
        :param text: the text of the line
        :return: the line number
        """

        # create a new label
        new_line = QLabel()
        new_line.setText(text)
        new_line.setFont(self.master_font)
        new_line.setFixedHeight(25)

        # set the highlight color
        palette = new_line.palette()
        palette.setColor(new_line.backgroundRole(), QColor(70, 130, 180, 100))
        new_line.setPalette(palette)

        self.line_list.addWidget(new_line)
        self.line_list.setAlignment(Qt.AlignTop)

    def highlight_line(self, line):
        """
        Enables the background for a particular line, but disables backgrounds for all other lines
        :param line: the line number (starts at 0)
        """

        # iterate through the items in the layout
        for i in range(self.line_list.count()):
            # select the item
            cur_item = self.line_list.takeAt(i).widget()

            # check if we are at the line we are looking for
            if i == line:
                # if so, enable the background color
                cur_item.setAutoFillBackground(True)
            else:
                # otherwise, clear it
                cur_item.setAutoFillBackground(False)

    def clear_lines(self):
        """
        Deletes all lines in the line_list layout
        """

        # iterate through the items in the layout
        for i in reversed(range(self.line_list.count())):
            # select the item
            cur_item = self.line_list.takeAt(i).widget()

            # make sure item exists
            if cur_item is not None:
                cur_item.deleteLater()
