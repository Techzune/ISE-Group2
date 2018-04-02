# title: CountingSort
# author: Avan Patel, Kohler Smallwood, Azlin Reed, Jordan Stremming, Steven Huynh, Zach Butterbaugh, Thea Furby
# purpose: algorithm;

import Utils
from Algorithm.Algorithm import Algorithm
from GUI.CodeHighlightWindow import CodeHighlightWindow
from GUI.VisualizationWindow import VisualizationWindow


class CountingSort(Algorithm):

    def __init__(self, viz_window: VisualizationWindow, cod_window: CodeHighlightWindow):

        # run the standard init
        super().__init__(viz_window, cod_window)

        # setup code window
        self.cod_window.set_alg_name("Counting Sort")
        self.cod_window.add_lines_from_file("Algorithm/CountingSortCode.txt")

    def sort(self, num_list):

        if self.steps_enabled:
            wait_signal = Utils.WaitSignal(self.cod_window.signal_step)
        maximum = max(num_list)
        minimum = min(num_list)
        count = [0]*(maximum-minimum+1)

        for a in num_list:

            if self.highlight_enabled:
                self.cod_window.highlight_line(0)
            if self.steps_enabled:
                wait_signal.wait()

            count[a-minimum] += 1

            if self.highlight_enabled:
                self.cod_window.highlight_line(1)
            if self.steps_enabled:
                wait_signal.wait()

        sorted = []

        for i in range(minimum, maximum+1):
            if self.highlight_enabled:
                self.cod_window.highlight_line(2)
            if self.steps_enabled:
                wait_signal.wait()

            if count[i-minimum] > 0:

                if self.highlight_enabled:
                    self.cod_window.highlight_line(3)
                if self.steps_enabled:
                    wait_signal.wait()

                for j in range(0, count[i-minimum]):

                    if self.highlight_enabled:
                        self.cod_window.highlight_line(4)
                    if self.steps_enabled:
                        wait_signal.wait()

                    sorted.append(i)

                if self.highlight_enabled:
                    self.cod_window.highlight_line(5)
                if self.steps_enabled:
                    wait_signal.wait()


        num_list = sorted

        return (num_list)

