# title: InitWindow
# author: Avan Patel, Kohler Smallwood, Azlin Reed, Jordan Stremming, Steven Huynh, Zach Butterbaugh
# purpose: Backbone of init window; a configuration window to define parameters for software
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5.uic import loadUi
import Utils


# noinspection PyArgumentList
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

        # add event listener to browse button click
        self.btn_browse.clicked.connect(self.on_browse_clicked)

    @pyqtSlot()
    def on_run_clicked(self):
        """
        EVENT: click for "Run Algorithm" button
        """

        # verify that the source is specified
        if len(self.input_source.text()) == 0:
            # show an error message if it is blank
            Utils.error_message("Source box cannot be blank!")
            return

        # exception handling for visual purposes
        # (shows exceptions in a message box)
        try:
            # creates an empty dictionary
            # noinspection PyDictCreation
            options = {}

            # specify the algorithm to run
            options["algorithm"] = self.cbox_algorithm.currentText()

            # get the selected index
            index = self.cbox_source_select.currentIndex()

            if index == 0:
                # "File with numbers" is selected
                options["file"] = self.input_source.text()
            elif index == 1:
                # "Random list of size N" is selected
                options["random"] = self.input_source.text()
            elif index == 2:
                # "Manual number input" is selected
                options["manual"] = self.input_source.text()

            # specify if visualizations should show
            options["show_viz"] = self.check_show_visualization.isChecked()

            # specify if code highlighting should occur
            options["show_highlight"] = self.check_show_highlighting.isChecked()

            # specify if step-by-step should run
            options["use_steps"] = self.check_use_steps.isChecked()

            # specify delay time if enabled
            if self.check_use_delay.isChecked():
                options["delay"] = self.input_delay_seconds.value()

            # run the algorithm
            self.main_application.start_algorithm(options)

            # close the init window
            self.close()

        except Exception as e:
            # if an exception occurs, show the error
            Utils.error_message(str(e))

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

        # clear the input_source textbox
        self.input_source.setText("")

    @pyqtSlot()
    def on_browse_clicked(self):
        """
        EVENT: click for "..." (browse) button
        """

        # make sure QFileDialog doesn't use the native dialog-- for Linux/Windows safety
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog

        # open the dialog for .txt file
        fileName, _ = QFileDialog.getOpenFileName(None, "Select input file", "", "Text Files (*.txt)", options=options)

        # put result in input_source box
        self.input_source.setText(fileName)
