# title: SWEG2Application
# author: Avan Patel, Kohler Smallwood, Azlin Reed, Jordan Stremming, Steven Huynh, Zach Butterbaugh, Thea Furby
# purpose: Primary application file; hub of application
import threading

import PyQt5
import sys
import time

from PyQt5.QtCore import QThread, pyqtSignal, QObject, pyqtSlot

import Utils
from Algorithm.Algorithm import Algorithm
from Algorithm.BubbleSort import BubbleSort
from Algorithm.CountingSort import CountingSort
from Algorithm.ExampleAlgorithm import ExampleAlgorithm
from Algorithm.InsertionSort import InsertionSort
from Algorithm.MergeSort import MergeSort
from Algorithm.QuickSort import QuickSort
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication
from GUI.InitWindow import InitWindow
from GUI.CodeHighlightWindow import CodeHighlightWindow
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

    def start_algorithm(self, options: dict):
        """
        Starts the algorithm.
        Acts as a callback from InitWindow.

        :param options: dictionary-arguments for the algorithm to run
        """

        # create a blank algorithm
        alg = None

        # ensure that algorithm is specified
        if "algorithm" not in options:
            raise Exception("algorithm is not defined")

        # set the algorithm properly
        if options["algorithm"] == "BubbleSort":
            alg = BubbleSort(self.viz_window, self.code_window)
        elif options["algorithm"] == "CountingSort":
            alg = CountingSort(self.viz_window, self.code_window)
        elif options["algorithm"] == "InsertionSort":
            alg = InsertionSort(self.viz_window, self.code_window)
        elif options["algorithm"] == "MergeSort":
            alg = MergeSort(self.viz_window, self.code_window)
        elif options["algorithm"] == "QuickSort":
            alg = QuickSort(self.viz_window, self.code_window)
        elif options["algorithm"] == "ExampleAlgorithm":
            alg = ExampleAlgorithm(self.viz_window, self.code_window)

        # create an empty int list
        num_list = []

        # determine source of number input
        if "file" in options:
            num_list = Utils.file_to_nums(options["file"])
        elif "random" in options:
            # make sure size N is an integer
            if not Utils.isInt(options["random"]):
                raise Exception("size N is not an integer!")

            # generate random list
            num_list = Utils.generate_ints(int(options["random"]))
        elif "manual" in options:
            num_list = Utils.commas_to_nums(options["manual"])
        else:
            # nothing was specified
            raise Exception("source was not specified!")

        # check if show_viz was specified
        if "show_viz" in options:
            alg.enable_visualization(bool(options["show_viz"]))

        # check if show_highlight was specified
        if "show_highlight" in options:
            alg.enable_highlight(bool(options["show_highlight"]))

        # check if step-by-step was specified
        if "use_steps" in options:
            alg.enable_steps(bool(options["use_steps"]))

        # check if delay was specified
        if "delay" in options:
            # make sure delay is an integer
            if Utils.isInt(options["delay"]):
                # pass data to algorithm
                delay_int = int(options["delay"])
                alg.set_delay(delay_int)

        # output algorithm running
        # output the original list
        print("RUNNING", options["algorithm"])
        print("\tOrig List:", str(num_list))

        # start the algorithm thread
        self.alg_worker = AlgorithmWorker(alg, num_list)
        self.alg_worker.callback = self.algorithm_callback
        self.alg_worker.start()

    def algorithm_callback(self, result_list: list, time_elapsed: int):
        # output the sorted list
        print("\tSort List:", str(result_list))

        # output the time to sort
        print("\tTime (ms):", time_elapsed)


# Worker class to run algorithms in separate threads
class AlgorithmWorker(QThread):
    def __init__(self, alg: Algorithm, num_list: list):
        super().__init__()
        self.alg = alg
        self.num_list = num_list

    def run(self):
        """
        Runs the algorithm
        """

        # time the algorithm and get result
        time_start = time.time()
        result_list = self.alg.sort(self.num_list)
        time_end = time.time()

        # run the callback function
        self.callback(result_list, time_end - time_start)


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
          "|                     Thea Furby                   |",
          "====================================================",
          "",
          sep="\n")

    # define the exception handler
    sys.excepthook = exception_hook

    # create the main application (python does not use "new")
    main = MainApplication()
