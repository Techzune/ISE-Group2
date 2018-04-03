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

        if self.viz_enabled:
            # create the graphs
            self.viz_window.add_graph(g_index=0, name="Original")
            self.viz_window.add_graph(g_index=1, name="Sorted")
            self.viz_window.add_graph(g_index=2, name="Count")

            # create the nodes
            self.viz_window.add_nodes(num_list, g_index=0)
            self.viz_window.add_nodes(count, g_index=2)
        for a in num_list:

            if self.highlight_enabled:
                self.cod_window.highlight_line(0)
            if self.steps_enabled:
                wait_signal.wait()
            if self.delay:
                Utils.sleep_qt(self.delay * 1000 / 3)

            count[a-minimum] += 1
            if self.viz_enabled:
                self.viz_window.set_node(a-minimum, count[a-minimum], g_index=2)

            if self.highlight_enabled:
                self.cod_window.highlight_line(1)
            if self.steps_enabled:
                wait_signal.wait()
            if self.delay:
                Utils.sleep_qt(self.delay * 1000 / 3)

        sorted = []

        for i in range(minimum, maximum+1):
            if self.highlight_enabled:
                self.cod_window.highlight_line(2)
            if self.steps_enabled:
                wait_signal.wait()
            if self.delay:
                Utils.sleep_qt(self.delay * 1000 / 3)



            if count[i-minimum] > 0:

                if self.highlight_enabled:
                    self.cod_window.highlight_line(3)
                if self.steps_enabled:
                    wait_signal.wait()
                if self.delay:
                    Utils.sleep_qt(self.delay * 1000 / 3)

                for j in range(0, count[i-minimum]):
                    if self.viz_enabled:
                        k = num_list.index(i)
                        self.viz_window.highlight_node(k, True, g_index=0)
                    if self.delay:
                        Utils.sleep_qt(self.delay * 1000 / 3)

                    if self.highlight_enabled:
                        self.cod_window.highlight_line(4)
                    if self.steps_enabled:
                        wait_signal.wait()
                    if self.delay:
                        Utils.sleep_qt(self.delay * 1000 / 3)

                    sorted.append(i)
                    if self.highlight_enabled:
                        self.cod_window.highlight_line(5)
                    if self.steps_enabled:
                        wait_signal.wait()
                    if self.viz_enabled:
                        self.viz_window.add_node(i, g_index=1)
                        k = num_list.index(i)
                        self.viz_window.highlight_node(k, False, g_index=0)
                    if self.delay:
                        Utils.sleep_qt(self.delay * 1000 / 3)

        num_list = sorted

        return (num_list)

