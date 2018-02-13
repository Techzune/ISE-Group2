# title: SWEG2Application
# author: Avan Patel, Kohler Smallwood, Azlin Reed, Jordan Stremming, Steven Huynh, Zach Butterbaugh
# purpose: Primary application file; hub of application
import time


# initialize the program
def init():
    # print out header
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

    # print a hello world statement
    print("Hello world!")

    # wait 3 seconds
    time.sleep(3)


# run the init function
init()
