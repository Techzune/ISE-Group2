# title: SWEG2Application
# author: Avan Patel, Kohler Smallwood, Azlin Reed, Jordan Stremming, Steven Huynh, Zach Butterbaugh
# purpose: Primary application file; hub of application
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from GUI.InitWindow import InitWindow


# MainAppliction class
class MainApplication:

    # runs on MainApplication creation
    def __init__(self):
        # create the application
        app = QApplication([])

        # start the application loop (this prevents the program from exiting instantly)
        sys.exit(app.exec_())

    # shows the initialization window
    def show_init_window(self):
        # create the init window and show
        init_window = InitWindow(self)
        init_window.show()

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

    if len(sys.argv) == 0:
        main.show_init_window()
