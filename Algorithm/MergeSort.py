# title: MergeSort
# author: Avan Patel, Kohler Smallwood, Azlin Reed, Jordan Stremming, Steven Huynh, Zach Butterbaugh, Thea Furby
# purpose: algorithm;
import Utils
from Algorithm.Algorithm import Algorithm
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

        #loop while right and left list are not empty
        while len(list_right)>0 and len(list_left)>0:
            #if left value is greater than right value
            if list_left[L] > list_right[R]:
                #append right value to merge list
                merge_list.append(list_right[R])
                #remove right value from right list
                list_right.remove(list_right[R])

            #else if right value is greater than left value
            else:
                #append left value to merge list
                merge_list.append(list_left[L])
                #remove left value from left list
                list_left.remove(list_left[L])

        #if right list is empty
        if len(list_right)<=0:
            #add left list to merge list
            merge_list = merge_list + list_left

        #elif left list is empty
        elif len(list_left)<=0:
            #add right list to merge list
            merge_list = merge_list + list_right

        return merge_list

    def sort(self, num_list):
        if self.steps_enabled:
            wait_signal = Utils.WaitSignal(self.cod_window.signal_step)

        listLeft = []
        listRight = []

        sortedLeft = []
        sortedRight = []

        #if list has more than 2 values
        if len(num_list) >= 2:

            if self.highlight_enabled:
                self.cod_window.highlight_line(0)
            if self.steps_enabled:
                wait_signal.wait()

            #split list; create left list
            listLeft = num_list[:len(num_list)//2]

            if self.highlight_enabled:
                self.cod_window.highlight_line(1)
            if self.steps_enabled:
                wait_signal.wait()

            #split list; create right list
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


