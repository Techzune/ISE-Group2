# title: InsertionSort
# author: Avan Patel, Kohler Smallwood, Azlin Reed, Jordan Stremming, Steven Huynh, Zach Butterbaugh, Thea Furby
# purpose: algorithm;
#cited source: https://www.geeksforgeeks.org/insertion-sort/

import Utils
from Algorithm.Algorithm import Algorithm
from GUI.CodeHighlightWindow import CodeHighlightWindow
from GUI.VisualizationWindow import VisualizationWindow


class InsertionSort(Algorithm):

    def __init__(self, viz_window: VisualizationWindow, cod_window: CodeHighlightWindow):
        """
        Initializes the Example Algorithm.
        """

        # run the standard init
        super().__init__(viz_window, cod_window)

        # setup code window
        self.cod_window.set_alg_name("Insertion Sort")
        self.cod_window.add_lines_from_file("Algorithm/InsertionSortCode.txt")

    def sort(self, num_list):

        if self.steps_enabled:
            wait_signal = Utils.WaitSignal(self.cod_window.signal_step)

        # Traverse through 1 to len(num_list)
        for i in range(1, len(num_list)):

            if self.highlight_enabled:
                self.cod_window.highlight_line(0)
            if self.steps_enabled:
                wait_signal.wait()

            current_value = num_list[i]

            if self.highlight_enabled:
                self.cod_window.highlight_line(1)
            if self.steps_enabled:
                wait_signal.wait()

            # Move elements of num_list[0..i-1], that are
            # greater than current_value, to one position ahead
            # of their current position
            j = i - 1

            if self.highlight_enabled:
                self.cod_window.highlight_line(2)
            if self.steps_enabled:
                wait_signal.wait()

            while j >= 0 and current_value < num_list[j]:

                if self.highlight_enabled:
                    self.cod_window.highlight_line(3)
                if self.steps_enabled:
                    wait_signal.wait()

                num_list[j + 1] = num_list[j]

                if self.highlight_enabled:
                    self.cod_window.highlight_line(4)
                if self.steps_enabled:
                    wait_signal.wait()

                j -= 1

                if self.highlight_enabled:
                    self.cod_window.highlight_line(5)
                if self.steps_enabled:
                    wait_signal.wait()

            num_list[j + 1] = current_value

            if self.highlight_enabled:
                self.cod_window.highlight_line(6)
            if self.steps_enabled:
                wait_signal.wait()

        return num_list


# Driver code to test above
#num_list = [12, 11, 13, 5, 6]
#insertionSort(num_list)
#print ("Sorted array is:")
#for i in range(len(num_list)):
#  print ("%d" %num_list[i])