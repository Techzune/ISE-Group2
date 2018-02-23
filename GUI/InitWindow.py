# title: InitWindow
# author: Avan Patel, Kohler Smallwood, Azlin Reed, Jordan Stremming, Steven Huynh, Zach Butterbaugh
# purpose: Backbone of init window; a configuration window to define parameters for software
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi


class InitWindow(QMainWindow):
    """
    Initialization Window, inherits from QMainWindow (a basic window)
    """

    def __init__(self, main_app):
        """
        Initialization of the InitWindow

        :param main_app: a reference to main.py (MainApplication)
        """

        # run the init of QMainWindow
        super().__init__()

        # save a reference to the main_app
        self.main_application = main_app

        # load .ui file for window
        loadUi('GUI/InitWindow.ui', self)

        # set the title
        self.setWindowTitle("Initialization Window")

        # define the algorithms in the comboBox
        self.cbox_algorithm.addItems(["BubbleSort", "CountingSort", "InsertionSort", "MergeSort", "QuickSort"])

        # define the sources for numbers
        self.cbox_source_select.addItems(["File with numbers", "Random list of size N", "Manual number input"])

        # add event listener to button click
        self.btn_run.clicked.connect(self.on_run_clicked)

        # add event listener to combobox
        self.cbox_source_select.currentIndexChanged.connect(self.on_source_select_changed)

    @pyqtSlot()
    def on_run_clicked(self):
        """
        EVENT: click for "Run Algorithm" button
        """

        self.main_application.start_algorithm(show_viz=True)

        # TODO: implement return of data to MainApplication
        print("let's play ball!")

    @pyqtSlot()
    def on_source_select_changed(self):
        """
        EVENT: selection change for "Source Select" comboBox
        """

        # get the selected index
        index = self.cbox_source_select.currentIndex()

        if index == 0:
            # "File with numbers" is selected
            self.lbl_source.setText("Path to numbers file (*.txt):")
            self.btn_browse.setEnabled(True)
        elif index == 1:
            # "Random list of size N" is selected
            self.lbl_source.setText("Size of N (int):")
            self.btn_browse.setEnabled(False)
        elif index == 2:
            # "Manual number input" is selected
            self.lbl_source.setText("List of numbers (separated by commas):")
            self.btn_browse.setEnabled(False)
