# title: Utils
# author: Avan Patel, Kohler Smallwood, Azlin Reed, Jordan Stremming, Steven Huynh, Zach Butterbaugh, Thea Furby
# purpose: Provides various utility functions to our program
from random import Random

from PyQt5.QtCore import QEventLoop, QTimer
from PyQt5.QtWidgets import QMessageBox


def isInt(val):
    """
    Tries to convert value into an integer

    :param val: the value to be converted
    :return: True, if the conversion succeeded
    """
    try:
        int(val)
        # conversion succeeded
        return True
    except ValueError:
        # conversion failed
        return False


def file_to_nums(file_path):
    """
    Converts a file of numbers into a list of numbers.
    Assumes numbers are separated by new-lines.

    :param file_path: the path to the file
    :return: the list of numbers
    """

    # create an empty list
    num_list = []

    # open the path as "file" -- this automatically closes the file
    with open(file_path) as file:
        # get each line in the file
        for i, line in enumerate(file, 1):
            # strip the line of "\n"
            line = line.rstrip()

            # check if the line is an integer
            if isInt(line):
                # if int, add to list
                num_list.append(int(line))
            else:
                # otherwise, skip the line
                print("*!* line", i, "skipped in file || not an int:", line, "*!*")

    # return the list
    return num_list


def commas_to_nums(comma_string):
    """
    Converts a list of ints separated by commas into a Python list of ints.

    :param comma_string: the comma-separated int string
    :return: a Python list of ints
    """

    # define the list of ints to return
    num_list = []

    # remove all spaces
    space_free = comma_string.replace(" ", "")

    # split the string by commas
    comma_split = space_free.split(",")

    # for each part in the split
    for part in comma_split:
        # check if the part is an integer
        if isInt(part):
            # append the part
            num_list.append(int(part))
        else:
            print("*!* part skipped || not an integer:", part, "*!*")

    # return the list
    return num_list


def generate_ints(size_n):
    """
    Generates a list of size N consisting of random integers.
    Ranges from -N to +N; no duplicates.

    :param size_n: size N
    :return: the list of random integers
    """

    # make sure that N isn't less than 0
    if size_n < 0:
        raise Exception("size n cannot be less than zero!")

    # creates a Random making object
    random = Random()

    # return the random list
    return random.sample(range(-size_n, size_n), size_n)


def error_message(msg):
    """
    Displays a PyQt Message Box with supplied message

    :param msg: the message to display
    """

    # create the message box
    m_box = QMessageBox()

    # set the title and text
    m_box.setWindowTitle("Hold up!")
    m_box.setText(msg)

    # start the message box
    m_box.exec()


def sleep_qt(msec):
    """
    PyQt-friendly sleep (sleeps while updating GUI events)
    USE THIS INSTEAD OF time.sleep(sec)!

    :param msec: the time to sleep in milliseconds
    """

    loop = QEventLoop()
    QTimer.singleShot(msec, loop.quit)
    loop.exec_()


class WaitSignal:
    """
    Used to wait for a signal to emit itself
    Prevents GUI freezing
    """

    def __init__(self, signal):
        # when the signal emits, run quit()
        signal.connect(self.quit)

        # set the waiting to True
        self.waiting = True

    def wait(self):
        """
        Wait for the signal to emit
        """
        # set the waiting to True
        self.waiting = True

        # sleep while waiting
        while self.waiting:
            sleep_qt(100)

    def quit(self):
        """
        Sets waiting to False,
        (stops the wait() function)
        """
        # set waiting to false
        self.waiting = False
