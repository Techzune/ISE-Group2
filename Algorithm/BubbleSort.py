# Title: BubbleSort
# Author: Avan Patel, Kohler Smallwood, Azlin Reed, Jordan Stremming, Steven Huynh, Zach Butterbaugh, Thea Furby
# Purpose: Take in List and check the element at index I and I+1. If element i > i+1, then it swap the element.
# At the end of 1st run, the last element in the array will be largest..


from Algorithm.Algorithm import Algorithm
import Utils
from GUI.CodeHighlightWindow import CodeHighlightWindow
from GUI.VisualizationWindow import VisualizationWindow


class BubbleSort(Algorithm):

    def __init__(self, viz_window: VisualizationWindow, cod_window: CodeHighlightWindow):
        """
        Initializes the Example Algorithm.
        """

        # run the standard init
        super().__init__(viz_window, cod_window)

        # setup code window
        self.cod_window.set_alg_name("Bubble Sort")
        self.cod_window.add_lines_from_file("Algorithm/BubbleSortCode.txt")

    def sort(self, element):

        # STEP -- wait signal setup
        if self.steps_enabled:
            wait_signal = Utils.WaitSignal(self.cod_window.signal_step)

        n = len(element)
        value = True
        for each in range(n):

            if self.highlight_enabled:
                self.cod_window.highlight_line(0)
            if self.steps_enabled:
                wait_signal.wait()
            if self.delay:
                Utils.sleep_qt(self.delay * 1000 / 7)

            # Go Through the Element in Array
            for i in range(0, n-each-1):

                if self.highlight_enabled:
                    self.cod_window.highlight_line(1)
                if self.steps_enabled:
                    wait_signal.wait()
                if self.delay:
                    Utils.sleep_qt(self.delay * 1000 / 7)

                # After first run last element is sorted so you want to skip going that far
                if element[i] > element[i+1]:

                    if self.highlight_enabled:
                        self.cod_window.highlight_line(2)
                    if self.steps_enabled:
                        wait_signal.wait()
                    if self.delay:
                        Utils.sleep_qt(self.delay * 1000 / 7)

                    # If i > i+1 then swap it
                    element[i], element[i+1] = element[i+1], element[i]

                    if self.highlight_enabled:
                        self.cod_window.highlight_line(3)
                    if self.steps_enabled:
                        wait_signal.wait()
                    if self.delay:
                        Utils.sleep_qt(self.delay * 1000 / 7)

                    value = False
                    if self.highlight_enabled:
                        self.cod_window.highlight_line(4)
                    if self.steps_enabled:
                        wait_signal.wait()
                    if self.delay:
                        Utils.sleep_qt(self.delay * 1000 / 7)

            # If array already sorted then Break
            if value is True:
                if self.highlight_enabled:
                    self.cod_window.highlight_line(5)
                if self.steps_enabled:
                    wait_signal.wait()
                if self.delay:
                    Utils.sleep_qt(self.delay * 1000 / 7)

                print("Array already sorted")

                if self.highlight_enabled:
                    self.cod_window.highlight_line(6)
                if self.steps_enabled:
                    wait_signal.wait()
                if self.delay:
                    Utils.sleep_qt(self.delay * 1000 / 7)
                break

        # VISUAL -- finished
        if self.highlight_enabled:
            self.cod_window.highlight_last()

        return element



# element = [12, 5, 2, 6, 7, 3]               # Random Testing Numbers
# array = []                                  # Taking an input from File
# filename = input("What is the name of input file? ")
# with open(filename) as f:
#     for line in f:
#         array.append(line)                  # Appending each element of file to List as string
#
#
# array = list(map(int, array))               # Converting list to string
# sort(array)                                 # Calling Function
#
#
# # Print out Element in Array
# for each in range(len(array)):
#     print(array[each])
#


