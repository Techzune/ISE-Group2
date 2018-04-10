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

        # STEPPING - create the wait signal
        if self.steps_enabled:
            wait_signal = Utils.WaitSignal(self.cod_window.signal_step)

        # store the maximum of the list
        maximum = max(num_list)
        minimum = min(num_list)

        # create a list of zeros
        count = [0]*(maximum-minimum+1)

        # VISUALIZATION -- initialization
        if self.viz_enabled:
            # create the graphs
            self.viz_window.add_graph(g_index=0, name="Original")
            self.viz_window.add_graph(g_index=1, name="Sorted")
            self.viz_window.add_graph(g_index=2, name="Count")

            # create the nodes
            self.viz_window.add_nodes(num_list, g_index=0)
            self.viz_window.add_nodes(count, g_index=2)

        # iterate through the list to sort
        for a in num_list:

            # HIGHLIGHT/STEPPING/DELAY
            if self.highlight_enabled:
                self.cod_window.highlight_line(0)
            if self.steps_enabled:
                wait_signal.wait()
            if self.delay:
                Utils.sleep_qt(self.delay * 1000 / 3)

            count[a-minimum] += 1

            # VISUALIZATION -- update the node
            if self.viz_enabled:
                self.viz_window.set_node(a-minimum, count[a-minimum], g_index=2)

            # HIGHLIGHT/STEPPING/DELAY
            if self.highlight_enabled:
                self.cod_window.highlight_line(1)
            if self.steps_enabled:
                wait_signal.wait()
            if self.delay:
                Utils.sleep_qt(self.delay * 1000 / 3)

        # create a list for the sorted numbers
        sorted = []

        # iterate through a range from minimum to maximum + 1
        for i in range(minimum, maximum+1):

            # HIGHLIGHT/STEPPING/DELAY
            if self.highlight_enabled:
                self.cod_window.highlight_line(2)
            if self.steps_enabled:
                wait_signal.wait()
            if self.delay:
                Utils.sleep_qt(self.delay * 1000 / 3)

            if count[i-minimum] > 0:

                # HIGHLIGHT/STEPPING/DELAY
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

                    # HIGHLIGHT/STEPPING/DELAY
                    if self.highlight_enabled:
                        self.cod_window.highlight_line(4)
                    if self.steps_enabled:
                        wait_signal.wait()
                    if self.delay:
                        Utils.sleep_qt(self.delay * 1000 / 3)

                    sorted.append(i)

                    # HIGHLIGHT/STEPPING/VISUALIZATION/DELAY
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

        # return the sorted list
        return sorted

