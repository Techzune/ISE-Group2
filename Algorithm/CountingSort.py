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
        self.cod_window.set_alg_name("Bubble Sort")
        self.cod_window.add_lines_from_file("Algorithm/BubbleSortCode.txt")

    def sort(self, num_list):

        if self.steps_enabled:
            wait_signal = Utils.WaitSignal(self.cod_window.signal_step)


        n = len(num_list)
        m = max(num_list)
        count = [0] * m
        for a in range(n):
            num_list[a] += 1
        i = 0
        for a in range(m):
            for c in range(num_list[a]):
                num_list[i] = a
                i += 1
        return num_list

