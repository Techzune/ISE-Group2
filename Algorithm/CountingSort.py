# title: CountingSort
# author: Avan Patel, Kohler Smallwood, Azlin Reed, Jordan Stremming, Steven Huynh, Zach Butterbaugh, Thea Furby
# purpose: algorithm;

from Algorithm.Algorithm import Algorithm
import Utils
from GUI.CodeHighlightWindow import CodeHighlightWindow
from GUI.VisualizationWindow import VisualizationWindow



class CountingSort(Algorithm):

    def __init__(self, viz_window: VisualizationWindow, cod_window: CodeHighlightWindow):
        """
        Initializes the Example Algorithm.
        """

        # run the standard init
        super().__init__(viz_window, cod_window)

        # setup code window
        self.cod_window.set_alg_name("Counting Sort")
        self.cod_window.add_lines_from_file("Algorithm/CountingSortCode.txt")

    def sort(self, num_list):

        if self.steps_enabled:
            wait_signal = Utils.WaitSignal(self.cod_window.signal_step)


        n = len(num_list)
        m = max(num_list)
        count = [0] * m
        for a in range(n):

            if self.highlight_enabled:
                self.cod_window.highlight_line(0)
            if self.steps_enabled:
                wait_signal.wait()

            num_list[a] += 1

            if self.highlight_enabled:
                self.cod_window.highlight_line(1)
            if self.steps_enabled:
                wait_signal.wait()

        i = 0

        if self.highlight_enabled:
            self.cod_window.highlight_line(2)
        if self.steps_enabled:

            wait_signal.wait()

        for a in range(m):
            if self.highlight_enabled:
                self.cod_window.highlight_line(3)
            if self.steps_enabled:

                wait_signal.wait()

            for c in range(num_list[a]):
                if self.highlight_enabled:
                    self.cod_window.highlight_line(4)
                if self.steps_enabled:
                    wait_signal.wait()

                num_list[i] = a

                if self.highlight_enabled:
                    self.cod_window.highlight_line(5)
                if self.steps_enabled:
                    wait_signal.wait()

                i += 1

                if self.highlight_enabled:
                    self.cod_window.highlight_line(6)
                if self.steps_enabled:
                    wait_signal.wait()

        return num_list

