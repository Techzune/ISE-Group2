# title: SWEG2Application
# author: Avan Patel, Kohler Smallwood, Azlin Reed, Jordan Stremming, Steven Huynh, Zach Butterbaugh
# purpose: Primary application file; hub of application
import PyQt5
import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication
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

    def start_algorithm(self, **kwargs):
        """
        Starts the algorithm.
        Acts as a callback from InitWindow.

        :param kwargs: dictionary-arguments for the algorithm to run
        """

        # show visualization_window if requested
        if "show_viz" in kwargs and kwargs["show_viz"] is True:
            self.viz_window.show()

        pass


# PROGRAM START #

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

    # create the main application (python does not use "new")
    main = MainApplication()
