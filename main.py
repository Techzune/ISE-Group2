# title: SWEG2Application
# author: Avan Patel, Kohler Smallwood, Azlin Reed, Jordan Stremming, Steven Huynh, Zach Butterbaugh
# purpose: Primary application file; hub of application
import PyQt5
import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication

import Utils
from Algorithm.BubbleSort import BubbleSort
from Algorithm.CountingSort import CountingSort
from Algorithm.InsertionSort import InsertionSort
from Algorithm.MergeSort import MergeSort
from Algorithm.QuickSort import QuickSort
from GUI.InitWindow import InitWindow
from GUI.CodeHightlightWindow import CodeHighlightWindow
from GUI.VisualizationWindow import VisualizationWindow


# MainApplication class
class MainApplication:

    # runs on MainApplication creation
    def __init__(self):
        """
        Initialization of the MainApplication.
        """

        # create the application
        app = QApplication([])

        # create the windows
        self.init_window = InitWindow(self)
        self.code_window = CodeHighlightWindow(self)
        self.viz_window = VisualizationWindow(self)

        # check if the user provided arguments
        if len(sys.argv) > 1:
            # if so, skip showing the init window
            # TODO: run start_algorithm with proper arguments
            # TODO: write the handler for arguments
            print("arguments detected!", sys.argv)
        else:
            # if not, show the init window
            self.init_window.show()

        # start the application loop (this prevents the program from exiting instantly)
        sys.exit(app.exec_())

    def start_algorithm(self, options):
        """
        Starts the algorithm.
        Acts as a callback from InitWindow.

        :param kwargs: dictionary-arguments for the algorithm to run
        """

        # create a blank algorithm
        algorithm = None

        # ensure that algorithm is specified
        if "algorithm" not in options:
            raise Exception("algorithm is not defined")

        # set the algorithm properly
        if options["algorithm"] == "BubbleSort":
            algorithm = BubbleSort(self.code_window, self.viz_window)
        elif options["algorithm"] == "CountingSort":
            algorithm = CountingSort(self.code_window, self.viz_window)
        elif options["algorithm"] == "InsertionSort":
            algorithm = InsertionSort(self.code_window, self.viz_window)
        elif options["algorithm"] == "MergeSort":
            algorithm = MergeSort(self.code_window, self.viz_window)
        elif options["algorithm"] == "QuickSort":
            algorithm = QuickSort(self.code_window, self.viz_window)

        # create an empty int list
        num_list = []

        # determine source of number input
        if "file" in options:
            num_list = Utils.file_to_nums(options["file"])
        elif "random" in options:
            pass
        elif "manual" in options:
            num_list = Utils.commas_to_nums(options["manual"])
        else:
            # nothing was specified
            raise Exception("source was not specified!")

        # check if show_viz was specified
        if "show_viz" in options:
            algorithm.enable_visualization(bool(options["show_viz"]))

        # check if show_highlight was specified
        if "show_highlight" in options:
            algorithm.enable_highlight(bool(options["show_highlight"]))

        # check if step-by-step was specified
        if "use_steps" in options:
            algorithm.enable_steps(bool(options["use_steps"]))

        # check if delay was specified
        if "delay" in options:
            # make sure delay is an integer
            if Utils.isInt(options["delay"]):
                # pass data to algorithm
                delay_int = int(options["delay"])
                algorithm.set_delay(delay_int)

        # run the algorithm
        print(algorithm.sort(num_list))


# PROGRAM START #

def exception_hook(type, value, tback):
    """
    Override PyQt5 crash handling (prevents the program from instantly closing)
    """
    sys.__excepthook__(type, value, tback)


# enable high DPI for application
PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

# check if this is the main file (if the user opened this file first)
if __name__ == "__main__":
    # print a header
    print("====================================================",
          "| SWEG2 (SOFTWARE ENGINEERING GROUP 2) LAB PROJECT |",
          "====================================================",
          "|                   <<[THE TEAM]>>                 |",
          "|              Avan Patel    Kohler Smallwood      |",
          "|              Azlin Reed    Jordan Stremming      |",
          "|            Steven Huynh    Zach Butterbaugh      |",
          "====================================================",
          "",
          sep="\n")

    # define the exception handler
    sys.excepthook = exception_hook

    # create the main application (python does not use "new")
    main = MainApplication()
