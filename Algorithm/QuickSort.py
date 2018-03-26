# title: QuickSort
# author: Avan Patel, Kohler Smallwood, Azlin Reed, Jordan Stremming, Steven Huynh, Zach Butterbaugh, Thea Furby
# purpose: algorithm;

import Utils
from Algorithm.Algorithm import Algorithm
from GUI.CodeHighlightWindow import CodeHighlightWindow
from GUI.VisualizationWindow import VisualizationWindow


class QuickSort(Algorithm):

    def __init__(self, viz_window: VisualizationWindow, cod_window: CodeHighlightWindow):
        """
        Initializes the Example Algorithm.
        """

        # run the standard init
        super().__init__(viz_window, cod_window)

        # setup code window
        self.cod_window.set_alg_name("Quick Sort")
        self.cod_window.add_lines_from_file("Algorithm/QuickSortCode.txt")

    def sort(self, num_list):

        i = 0
        # STEPPING -- wait condition and signaling
        if self.steps_enabled:
            wait_signal = Utils.WaitSignal(self.cod_window.signal_step)

        # creation of the buckets
        less_than = []
        equals = []
        greater_than = []

        #Initialized the visualization list
        """
        if self.viz_enabled:
            self.viz_window.add_nodes(num_list)



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

        
        if needed
        create the separation of the buckets in visualization
        PROBLEM: creating the bucket separation would cause difficulties
        when re-merging the buckets
        """


        # there are actually numbers to sort
        if len(num_list) > 1:
            # CODE -- highlight "finding pivot"
            if self.highlight_enabled:
                self.cod_window.highlight_line(0)
            if self.steps_enabled:
                wait_signal.wait()

            # setting the pivot
            # using the first number as a pivot for simplicity
            pivot = num_list[0]


            if len(num_list) > 4:
                first = num_list[0]
                second = num_list[int(len(num_list)/2)]
                third = num_list[len(num_list)-1]
                if second <= first < third:
                    pivot = first
                if first <= second < third:
                    pivot = second
                if first <= third < second:
                    pivot = third

            # the actual sorting
            # dumping some numbers into some buckets with labels
            for i in num_list:
                if i < pivot:
                    less_than.append(i)

                    if self.highlight_enabled:
                        self.cod_window.highlight_line(1)
                    if self.steps_enabled:
                        wait_signal.wait()
                    """
                    move the current object into the less_than bucket
                    """

                if i == pivot:
                    equals.append(i)

                    if self.highlight_enabled:
                        self.cod_window.highlight_line(2)
                    if self.steps_enabled:
                        wait_signal.wait()
                    """
                    move the current object into the equals object
                    """

                if i > pivot:
                    greater_than.append(i)

                    if self.highlight_enabled:
                        self.cod_window.highlight_line(3)
                    if self.steps_enabled:
                        wait_signal.wait()
                    """
                    move the current object into the greater_than bucket
                    """

            """
            If the bucket/separations were made earlier
            merge the buckets all back together into one list
            PROBLEM: Would need to change the visualization post 
            return statement. 
            """

            return self.sort(less_than) + equals + self.sort(greater_than)

        # only 1 number
        else:
            return num_list
