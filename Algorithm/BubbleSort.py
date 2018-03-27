# Title: BubbleSort
# Author: Avan Patel, Kohler Smallwood, Azlin Reed, Jordan Stremming, Steven Huynh, Zach Butterbaugh, Thea Furby
# Purpose: Take in List and check the element at index I and I+1. If element i > i+1, then it swap the element.
# At the end of 1st run, the last element in the array will be largest..


import Utils
from Algorithm.Algorithm import Algorithm
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

    def sort(self, num_list):

        # STEP -- wait signal setup
        if self.steps_enabled:
            wait_signal = Utils.WaitSignal(self.cod_window.signal_step)

        # VISUAL -- put numbers in visual gui
        self.viz_window.add_nodes(num_list)

        # the length of the list
        N = len(num_list)

        # if numbers are to be swapped
        could_swap = False

        # gui & delay
        if self.highlight_enabled:
            self.cod_window.highlight_line(0)
        if self.steps_enabled:
            wait_signal.wait()
        if self.delay:
            Utils.sleep_qt(self.delay * 1000 / 7)

        # for each index in list
        for i in range(N):

            # gui & delay
            if self.highlight_enabled:
                self.cod_window.highlight_line(1)
            if self.steps_enabled:
                wait_signal.wait()
            if self.delay:
                Utils.sleep_qt(self.delay * 1000 / 7)

            for j in range(0, N - i - 1):

                # gui & delay
                if self.highlight_enabled:
                    self.cod_window.highlight_line(2)
                if self.viz_enabled:
                    self.viz_window.highlight_node(j, True)
                    self.viz_window.highlight_node(j + 1, True)
                if self.steps_enabled:
                    wait_signal.wait()
                if self.delay:
                    Utils.sleep_qt(self.delay * 1000 / 7)

                # if current number is greater than the next
                if num_list[j] > num_list[j + 1]:

                    # gui & delay
                    if self.highlight_enabled:
                        self.cod_window.highlight_line(3)
                    if self.viz_enabled:
                        self.viz_window.swap_nodes(j, j + 1, delay=self.delay * 1000 / 7)
                    if self.steps_enabled:
                        wait_signal.wait()

                    # no need to delay if visual swap already delayed
                    if not self.viz_enabled and self.delay:
                        Utils.sleep_qt(self.delay * 1000 / 7)

                    # swap current number with the next
                    num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]

                    # gui & delay
                    if self.highlight_enabled:
                        self.cod_window.highlight_line(4)
                    if self.steps_enabled:
                        wait_signal.wait()
                    if self.delay:
                        Utils.sleep_qt(self.delay * 1000 / 7)

                    # numbers were swappable
                    could_swap = True

                if self.viz_enabled:
                    self.viz_window.highlight_node(j, False)
                    self.viz_window.highlight_node(j + 1, False)

            # gui & delay
            if self.highlight_enabled:
                self.cod_window.highlight_line(5)
            if self.steps_enabled:
                wait_signal.wait()
            if self.delay:
                Utils.sleep_qt(self.delay * 1000 / 7)

            # if swapping did not occur
            if not could_swap:

                # gui & delay
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

        return num_list

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
