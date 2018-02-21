# title: SWEG2Application
# author: Avan Patel, Kohler Smallwood, Azlin Reed, Jordan Stremming, Steven Huynh, Zach Butterbaugh
# purpose: Primary application file; hub of application
import sys
from PyQt5.QtWidgets import QApplication, QWidget

from GUI.InitWindow import InitWindow
from GUI.CodeHightlightWindow import CodeHighlightWindow
from GUI.VisualizationWindow import VisualizationWindow


# MainApplication class
class MainApplication:

    # runs on MainApplication creation
    def __init__(self):
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

    # starts the algorithm
    # acts as a callback from InitWindow or from command line
    def start_algorithm(self, **kwargs):
        pass


# PROGRAM START #
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
