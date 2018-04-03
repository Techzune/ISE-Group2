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

        # run the standard init
        super().__init__(viz_window, cod_window)

        # setup code window
        self.cod_window.set_alg_name("Insertion Sort")
        self.cod_window.add_lines_from_file("Algorithm/InsertionSortCode.txt")

    def sort(self, num_list):

        if self.viz_enabled:
            # create the graphs
            self.viz_window.add_graph(g_index=0, name="Original")
            self.viz_window.add_nodes(num_list, g_index=0)

        if self.steps_enabled:
            wait_signal = Utils.WaitSignal(self.cod_window.signal_step)

        # Traverse through 1 to len(num_list)
        for i in range(1, len(num_list)):

            if self.highlight_enabled:
                self.cod_window.highlight_line(0)
            if self.steps_enabled:
                wait_signal.wait()
            if self.delay:
                Utils.sleep_qt(self.delay * 1000 / 3)

            # current_value variable refers to [i] in the array used for this algorithm
            current_value = num_list[i]

            if self.viz_enabled:
                self.viz_window.highlight_node(i, True)
            if self.highlight_enabled:
                self.cod_window.highlight_line(1)
            if self.steps_enabled:
                wait_signal.wait()
            if self.delay:
                Utils.sleep_qt(self.delay * 1000 / 3)

            # j is decremented of i
            j = i - 1

            if self.viz_enabled:
                self.viz_window.highlight_node(j, True)
            if self.highlight_enabled:
                self.cod_window.highlight_line(2)
            if self.steps_enabled:
                wait_signal.wait()
            if self.delay:
                Utils.sleep_qt(self.delay * 1000 / 3)

            # Move elements of num_list[0..i-1], that are
            # greater than current_value, to one position ahead
            # of their current position
            while j >= 0 and current_value < num_list[j]:

                if self.highlight_enabled:
                    self.cod_window.highlight_line(3)
                if self.steps_enabled:
                    wait_signal.wait()
                if self.delay:
                    Utils.sleep_qt(self.delay * 1000 / 3)
                if self.viz_enabled:
                    self.viz_window.highlight_node(j, False)
                # j is incremented
                num_list[j + 1] = num_list[j]
                if self.viz_enabled:
                    self.viz_window.highlight_node(j, True)
                    self.viz_window.highlight_node(j+1, True)
                    self.viz_window.swap_nodes(j, j+1)
                    self.viz_window.highlight_node(j, False)
                    self.viz_window.highlight_node(j + 1, False)
                if self.highlight_enabled:
                    self.cod_window.highlight_line(4)
                if self.steps_enabled:
                    wait_signal.wait()
                if self.delay:
                    Utils.sleep_qt(self.delay * 1000 / 3)

                # j is decremented
                j -= 1

                if self.highlight_enabled:
                    self.cod_window.highlight_line(5)
                if self.steps_enabled:
                    wait_signal.wait()
                if self.delay:
                    Utils.sleep_qt(self.delay * 1000 / 3)
            # j is incremented, j and current_value are set equal to each other
            num_list[j + 1] = current_value
            if self.viz_enabled:
                self.viz_window.highlight_node(j + 1, True)
                self.viz_window.set_node(j+1,current_value)
                self.viz_window.highlight_node(j + 1, False)
            if self.highlight_enabled:
                self.cod_window.highlight_line(6)
            if self.steps_enabled:
                wait_signal.wait()
            if self.delay:
                Utils.sleep_qt(self.delay * 1000 / 3)

        # return the sorted list
        return num_list


# Driver code to test above
#num_list = [12, 11, 13, 5, 6]
#insertionSort(num_list)
#print ("Sorted array is:")
#for i in range(len(num_list)):
#  print ("%d" %num_list[i])