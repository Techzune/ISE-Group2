# title: SWEG2Application
# author: Avan Patel, Kohler Smallwood, Azlin Reed, Jordan Stremming, Steven Huynh, Zach Butterbaugh, Thea Furby
# purpose: Primary application file; hub of application

import sys
import time

import PyQt5
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMessageBox

import Utils
from Algorithm.BubbleSort import BubbleSort
from Algorithm.CountingSort import CountingSort
from Algorithm.ExampleAlgorithm import ExampleAlgorithm
from Algorithm.InsertionSort import InsertionSort
from Algorithm.MergeSort import MergeSort
from Algorithm.QuickSort import QuickSort
from GUI.CodeHighlightWindow import CodeHighlightWindow
from GUI.InitWindow import InitWindow
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

        if len(num_list) > 10000:
            # SAFETY - does not accept list of more than 10,000 elements

            print("SORT CANCELLED: List cannot be more than 10,000 elements")

            if alg.viz_enabled:
                # create a message box
                m_box = QMessageBox()

                # set the title and text
                m_box.setWindowTitle("Nope!")
                m_box.setText("List cannot be larger than 10,000 elements")

                # start the message box
                m_box.exec()
            return
        elif len(num_list) > 500 and alg.viz_enabled:
            # SAFETY - does not show visualization with more than 500 nodes

            print("SORT CANCELLED: Cannot show visualization with more than 500 nodes")
            # create a message box
            m_box = QMessageBox()

            # set the title and text
            m_box.setWindowTitle("Nope!")
            m_box.setText("Cannot safely show visualization with more than 500 nodes")

            # start the message box
            m_box.exec()
            return

        # open the GUIs
        self.code_window.show()
        if alg.viz_enabled:
            self.viz_window.show()
            self.moveGUIs()

        # close the init window
        self.init_window.close()

        # store the string of numlist
        str_numlist = str(num_list)

        # output algorithm running
        # output the original list
        print("RUNNING", options["algorithm"])
        print("\tOrig List:", str_numlist)

        # time the algorithm and get result
        time_start = time.time()
        result_list = alg.sort(num_list)
        time_end = time.time()

        # output the sorted list
        print("\tSort List:", str(result_list))

        # output the time to sort
        print("\tTime (ms):", time_end - time_start)

        # create a message box
        m_box = QMessageBox()

        # set the title and text
        m_box.setWindowTitle("All done!")
        if len(num_list) > 1000:
            m_box.setText("Here are the results:\n\nLISTS TOO BIG TO DISPLAY: {}\nTime (ms): {}".format(len(num_list), time_end-time_start))
        else:
            m_box.setText("Here are the results:\n\nOrig List: {}\nSort List: {}\nTime (ms): {}".format(str_numlist, str(result_list), str(time_end-time_start)))

        # start the message box
        m_box.exec()

    def moveGUIs(self):
        """
        Aligns the visualization window and code highlight window
        """

        # get the frames from the windows
        viz_frame = self.viz_window.frameGeometry()
        cod_frame = self.code_window.frameGeometry()

        # create a frame combining the two
        main_frame = PyQt5.QtCore.QRect(0, 0, viz_frame.width() + cod_frame.width(), viz_frame.height() + cod_frame.height())

        # get the screen's center
        screen = PyQt5.QtWidgets.QApplication.desktop().screenNumber(PyQt5.QtWidgets.QApplication.desktop().cursor().pos())
        centerPoint = PyQt5.QtWidgets.QApplication.desktop().screenGeometry(screen).center()

        # align the frames
        main_frame.moveCenter(centerPoint)
        viz_frame.moveRight(main_frame.right())
        cod_frame.moveLeft(main_frame.left())

        # move the windows
        self.viz_window.move(viz_frame.topLeft())
        self.code_window.move(cod_frame.topLeft())


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
