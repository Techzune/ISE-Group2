# title: CodeHighlightWindow
# author: Avan Patel, Kohler Smallwood, Azlin Reed, Jordan Stremming, Steven Huynh, Zach Butterbaugh, Thea Furby
# purpose: Backbone of code highlighting window; displays code with algorithm steps highlighted
from PyQt5.QtCore import Qt, pyqtSlot, pyqtSignal
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QLabel
from PyQt5.uic import loadUi


# inherits QMainWindow (a basic window)
class CodeHighlightWindow(QMainWindow):

    # set up signal for "Go to next step..."
    # this must be defined outside init
    signal_step = pyqtSignal()

    def __init__(self, main_app):
        """
        Initialization of the CodeHighlightWindow

        :param main_app: a reference to main.py (MainApplication)
        """

        # run the init of QMainWindow
        super().__init__()

        # create list for label elements
        self.list_labels = []

        # save a reference to the main_app
        self.main_application = main_app

        # load .ui file for window
        loadUi('GUI/CodeHighlightWindow.ui', self)

        # set the title
        self.setWindowTitle("SWEG2 - Code Highlight Window")

        # define the font used throughout the application
        self.master_font = QFont()
        self.master_font.setFamily(self.algorithm_name.font().family())
        self.master_font.setPointSize(12)

        # add event listener to next button click
        self.pushButton.clicked.connect(self.on_next_clicked)

        # set spacing for the line list to none
        self.line_list.setContentsMargins(0, 0, 0, 0)
        self.line_list.setSpacing(0)
        self.line_list.update()

    @pyqtSlot()
    def on_next_clicked(self):
        """
        Event handler for NextStep button
        * emits a pyqtSignal: signal_step
        """
        self.signal_step.emit()

    def set_alg_name(self, name: str):
        """
        Sets the algorithm's name in the GUI
        """
        self.algorithm_name.setText(name)

    def add_line(self, text: str):
        """
        Adds a line of code to the list layout
        :param text: the text of the line
        :return: the line number
        """

        # create a new label
        new_line = QLabel()
        new_line.setText(text)
        new_line.setFont(self.master_font)

        new_line.setContentsMargins(0, 5, 0, 5)
        new_line.setFixedHeight(28)
        new_line.adjustSize()

        # add the label to the layout and set alignment
        self.line_list.addWidget(new_line)
        self.line_list.setAlignment(Qt.AlignTop)

        # add the label to the list
        self.list_labels.append(new_line)

    def add_lines_from_file(self, file_path: str):
        """
        Imports multiple lines from a file
        :param file_path: the file to import from
        """

        # open the path as "file" -- this automatically closes the file
        with open(file_path) as file:
            # for each line in the file
            for line in file:
                # add the line
                self.add_line(line)

    def highlight_line(self, line: int):
        """
        Enables the background for a particular line, but disables backgrounds for all other lines
        :param line: the line number (starts at 0)
        """

        # iterate through the stored labels
        for i in range(len(self.list_labels)):
            # select the label
            cur_label = self.list_labels[i]

            # check if we are at the line we are looking for
            cur_label.setStyleSheet("QLabel { background-color: transparent; font-weight: normal; }")

        # highlight the correct one
        self.list_labels[line].setStyleSheet("QLabel { background-color: #FFB6C1; font-weight: bold; }")

    def clear_lines(self):
        """
        Deletes all lines in the line_list layout
        """

        # iterate through the stored labels
        for cur_label in self.list_labels:
            # make sure label exists
            if cur_label is not None:
                # delete the label
                cur_label.deleteLater()

        # clear the list
        self.list_labels.clear()
