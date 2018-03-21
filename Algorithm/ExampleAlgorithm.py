# DO NOT INCLUDE THIS FILE IN FINAL PRODUCT!!

"""
This is a simple algorithm file that doesn't really sort anything.
Instead, this file demonstrates how to implement the Algorithm interface.
"""
import time

from Algorithm.Algorithm import Algorithm
from GUI.CodeHighlightWindow import CodeHighlightWindow
from GUI.VisualizationWindow import VisualizationWindow


class ExampleAlgorithm(Algorithm):
    # the multiplier to use
    multiplier = 2

    def __init__(self, viz_window: VisualizationWindow, cod_window: CodeHighlightWindow):
        """
        Initializes the Example Algorithm.
        """

        # run the standard init
        super().__init__(viz_window, cod_window)

        # setup code window and show
        self.cod_window.set_alg_name("Example Algorithm")
        self.cod_window.add_lines_from_file("Algorithm/ExampleAlgorithmCode.txt")
        self.cod_window.show()

    def sort(self, num_list):
        """
        Doesn't actually sort!
        Multiplies each number in a list by 2.

        :param num_list: the list to "sort"
        :return: the resulting list
        """

        # create an empty result list
        result = []

        for num in num_list:
            # GUI: highlight "get_number()"
            self.cod_window.highlight_line(0)

            # ALGORITHM: do the actual multiplication
            result.append(self._multiply(num, self.multiplier))

            # sleep (there are 2 line changes, so divide by 2 and sleep twice)
            time.sleep(self.delay / 2)

            # GUI: highlight "number * 2"
            self.cod_window.highlight_line(1)

            # sleep
            time.sleep(self.delay / 2)

        # GUI: highlight "FINISHED"
        self.cod_window.highlight_line(2)

        # return the result list
        return result

    def _multiply(self, a1, a2):
        """
        Private function that multiplies two numbers

        :param a1: the first number
        :param a2: the second number
        :return: the product
        """
        return a1 * a2
