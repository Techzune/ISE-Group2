# title: MergeSort
# author: Avan Patel, Kohler Smallwood, Azlin Reed, Jordan Stremming, Steven Huynh, Zach Butterbaugh, Thea Furby
# purpose: algorithm;
from Algorithm.Algorithm import Algorithm
import Utils
from GUI.CodeHighlightWindow import CodeHighlightWindow
from GUI.VisualizationWindow import VisualizationWindow




class MergeSort(Algorithm):

    def __init__(self, viz_window: VisualizationWindow, cod_window: CodeHighlightWindow):
        """
        Initializes the Example Algorithm.
        """

        # run the standard init
        super().__init__(viz_window, cod_window)

        # setup code window
        self.cod_window.set_alg_name("Merge Sort")
        self.cod_window.add_lines_from_file("Algorithm/MergeSortCode.txt")

    def mergeFunction(self, list_left, list_right):

        #create new empty merge list
        merge_list = []

        #set L and R indices
        L = 0
        R = 0

        #loop
        while len(list_right)>0 and len(list_left)>0:
            if list_left[L] > list_right[R]:
                merge_list.append(list_right[R])
                list_right.remove(list_right[R])

            else:
                merge_list.append(list_left[L])
                list_left.remove(list_left[L])

        if len(list_right)<=0:
            merge_list = merge_list + list_left

        elif len(list_left)<=0:
            merge_list = merge_list + list_right

        return merge_list

    def sort(self, num_list):
        if self.steps_enabled:
            wait_signal = Utils.WaitSignal(self.cod_window.signal_step)

        listLeft = []
        listRight = []

        sortedLeft = []
        sortedRight = []

        if len(num_list) >= 2:

            if self.highlight_enabled:
                self.cod_window.highlight_line(0)
            if self.steps_enabled:
                wait_signal.wait()

            listLeft = num_list[:len(num_list)//2]

            if self.highlight_enabled:
                self.cod_window.highlight_line(1)
            if self.steps_enabled:
                wait_signal.wait()

            listRight = num_list[len(num_list)//2:]

            if self.highlight_enabled:
                self.cod_window.highlight_line(2)
            if self.steps_enabled:
                wait_signal.wait()

            #recurse left side
            sortedLeft = self.sort(listLeft)

            if self.highlight_enabled:
                self.cod_window.highlight_line(3)
            if self.steps_enabled:
                wait_signal.wait()

            #recurse right side
            sortedRight = self.sort(listRight)

            if self.highlight_enabled:
                self.cod_window.highlight_line(4)
            if self.steps_enabled:
                wait_signal.wait()

            #merge lists
            sortedList = self.mergeFunction(sortedLeft, sortedRight)

            if self.highlight_enabled:
                self.cod_window.highlight_line(5)
            if self.steps_enabled:
                wait_signal.wait()

            #return sorted list
            return sortedList

        else:
            return num_list


