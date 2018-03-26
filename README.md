# SWEG2 - Home
Software Engineering Group 2 project written in Python and PyQt5.

## Before you code...
Open a terminal and run the following command lines:
```
pip3 install pyqt5
pip3 install pyqt5-tools
```
This installs the PyQt5 dependency that is used in this project.

## Setting up GitHub with PyCharm
DO NOT sync PyCharm XML/property files!

## Running the software
You can simply run "main.py" to open the initialization GUI.

If you prefer a manual approach, you can use the terminal to add attributes to launch main.py:
```
python main.py [-f [FILEPATH] | -m NUM,BY,COMMAS | -r SIZEOFN] [-a ALGORITHMNAME]
  EXTRA ATTRIBUTES:
    -v        Show animations
    -s        Enable step-by-step
    -d [SEC]  Enable delay in seconds

  EXAMPLES:
    python main.py
      (Shows Initialization Window)
    python main.py -f ~/ASDF.txt -a merge -v -d 2
      (Sort numbers from ASDF.txt with Merge Sort, show visualizations, delay each operation by 2 seconds)
    python main.py -m 10,2,3,4,5 -a binary -v -s
      (Sort numbers 10,2,3,4,5 with Binary Sort, show visualizations, enable step-by-step)
    python main.py -r 10000 -a insertion
      (Sort random number list of size 10000 with Insertion Sort)
```
