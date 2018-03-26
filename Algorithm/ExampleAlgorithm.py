# DO NOT INCLUDE THIS FILE IN FINAL PRODUCT!!

"""
This is a simple algorithm file that doesn't really sort anything.
Instead, this file demonstrates how to implement the Algorithm interface.
"""

import Utils
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

        # setup code window
        self.cod_window.set_alg_name("Example Algorithm")
        self.cod_window.add_lines_from_file("Algorithm/ExampleAlgorithmCode.txt")

    def sort(self, num_list):
        """
        Doesn't actually sort!
        Multiplies each number in a list by 2.

        :param num_list: the list to "sort"
        :return: the resulting list
        """

        # STEPPING -- wait condition and signaling
        if self.steps_enabled:
            wait_signal = Utils.WaitSignal(self.cod_window.signal_step)

        # create an empty result list
        result = []

        # add numbers to viz window
        if self.viz_enabled:
            self.viz_window.add_nodes(num_list)

        for i, num in enumerate(num_list):
            # CODE -- highlight "get_number()"
            if self.highlight_enabled:
                self.cod_window.highlight_line(0)

            # VISUAL -- highlight current node
            if self.viz_enabled:
                self.viz_window.highlight_node(i, True)

            # STEP -- wait for next click
            if self.steps_enabled:
                wait_signal.wait()

            # DELAY
            # (there are 2 GUI changes, so divide delay by 2 and sleep 2 times)
            if self.delay:
                Utils.sleep_qt(self.delay * 1000 / 2)

            # CODE -- highlight "number * 2"
            if self.highlight_enabled:
                self.cod_window.highlight_line(1)

            # do the multiplication
            new_val = self._multiply(num, self.multiplier)
            result.append(new_val)

            # VISUAL -- update current node to the new value
            if self.viz_enabled:
                self.viz_window.set_node(i, new_val)

            # STEP -- wait for next click
            if self.steps_enabled:
                wait_signal.wait()

            # DELAY
            if self.delay:
                Utils.sleep_qt(self.delay * 1000 / 2)

            # VISUAL -- un-highlight current node
            if self.viz_enabled:
                self.viz_window.highlight_node(i, False)

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
