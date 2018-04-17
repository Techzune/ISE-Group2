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

        # used to see how many recursive calls/graphs are nested into each other
        self.depth = -1

        # keeps track of the type of bucket being interacted with
        # Default: -1 (unchosen)
        # Left Bucket = 2
        # Right Bucket = 0
        # Equals = 1
        self.which_bucket = 0

    def sort(self, num_list):

        # tracking depth
        self.depth += 1

        # eject if num_list is dead
        if not num_list:
            return num_list

        i = 0
        # STEPPING -- wait condition and signaling
        if self.steps_enabled:
            wait_signal = Utils.WaitSignal(self.cod_window.signal_step)

        # creation of the buckets
        less_than = []
        equals = []
        greater_than = []

        # Initialized the visualization list
        if self.viz_enabled:

            if self.depth == 0:
                self.viz_window.add_graph(0, "Main Graph")
                self.viz_window.add_nodes(num_list, 0)
                self.viz_window.add_graph(((self.depth + 1) * 3) - 2, "Left Bucket " + str(self.depth + 1))
                self.viz_window.add_graph(((self.depth + 1) * 3) - 1, "Equals Bucket " + str(self.depth + 1))
                self.viz_window.add_graph(((self.depth + 1) * 3) - 0, "Right Bucket " + str(self.depth + 1))

            if self.depth > 0:

                self.viz_window.add_graph(((self.depth + 1) * 3) - 2, "Left Bucket " + str(self.depth + 1))
                self.viz_window.add_graph(((self.depth + 1) * 3) - 1, "Equals Bucket " + str(self.depth + 1))
                self.viz_window.add_graph(((self.depth + 1) * 3) - 0, "Right Bucket " + str(self.depth + 1))

        # STEP -- wait for next click
        if self.steps_enabled:
                wait_signal.wait()

        # DELAY
        # (there are 2 GUI changes, so divide delay by 2 and sleep 2 times)
        # delay after graph creations
        if self.delay:
            Utils.sleep_qt(self.delay * 1000 / 2)


        # creation of cur_bucket
        if self.depth > 0:
            cur_bucket = (self.depth * 3) - self.which_bucket
        else:
            cur_bucket = 0

        # there are actually numbers to sort
        if len(num_list) > 1:

            # CODE -- highlight "finding pivot"
            if self.highlight_enabled:
                self.cod_window.highlight_line(0)

            # ----------------
            # SETTING UP PIVOT
            # ----------------
            # using the first number as a pivot for simplicity
            pivot = num_list[0]

            # VISUAL -- highlighting default node
            if self.viz_enabled:
                self.viz_window.highlight_node(0, True, cur_bucket)

            # If there are more than 4 numbers
            if len(num_list) > 4:

                # Choose the middle of three numbers
                # Using: First number, middle number, and last number

                first = num_list[0]
                second = num_list[int(len(num_list)/2)]
                third = num_list[len(num_list)-1]

                # checking to see which one is the middle value
                if second <= first < third or third <= first < second:
                    # first entry of list is pivot
                    pivot = first

                    # gui & delay
                    if self.viz_enabled:
                        self.viz_window.highlight_node(0, False, cur_bucket)
                        self.viz_window.highlight_node(0, True, cur_bucket)
                    if self.steps_enabled:
                        wait_signal.wait()
                    if self.delay:
                        Utils.sleep_qt(self.delay * 1000 / 2)

                if first <= second < third or third <= second < first:
                    # middle entry of list is pivot
                    pivot = second

                    # gui & delay
                    if self.viz_enabled:
                        self.viz_window.highlight_node(0, False, cur_bucket)
                        self.viz_window.highlight_node(int(len(num_list) / 2), True, cur_bucket)
                    if self.steps_enabled:
                        wait_signal.wait()
                    if self.delay:
                        Utils.sleep_qt(self.delay * 1000 / 2)

                if first <= third < second or second <= third < first:
                    # last entry of list is pivot
                    pivot = third

                    # gui & delay
                    if self.viz_enabled:
                        self.viz_window.highlight_node(0, False, cur_bucket)
                        self.viz_window.highlight_node(len(num_list) - 1, True, cur_bucket)
                    if self.steps_enabled:
                        wait_signal.wait()
                    if self.delay:
                        Utils.sleep_qt(self.delay * 1000 / 2)
            # ---------------------
            # END OF PIVOT CHOOSING
            # ---------------------

            # ----------------------------
            # SORTING NUMBERS INTO BUCKETS
            # ----------------------------
            # dumping some numbers into some buckets with labels

            # CODE - Highlight the Start of our Sorting
            if self.highlight_enabled:
                self.cod_window.highlight_line(1)

            # counter
            k = -1
            for i in num_list:
                # counter counting
                k += 1

                # CODE - comparing number to pivot
                if self.highlight_enabled:
                    self.cod_window.highlight_line(2)

                # VISUAL -- highlighting the number being looked at
                # Blinks for when it is looking at the pivot
                if self.viz_enabled:
                    self.viz_window.highlight_node(k, False, cur_bucket)
                    Utils.sleep_qt(self.delay * 1000 / 3 / 3)
                    self.viz_window.highlight_node(k, True, cur_bucket)
                    Utils.sleep_qt(self.delay * 1000 / 3 / 3)
                    self.viz_window.highlight_node(k, False, cur_bucket)
                    Utils.sleep_qt(self.delay * 1000 / 3 / 3)
                    self.viz_window.highlight_node(k, True, cur_bucket)

                    # These are used for keeping track of the range of new lists being made
                    left = 0
                    right = 0
                    equal = 0

                # delay based around 3 total delays for moving things around buckets
                # ignoring the blinking of the nodes
                if self.delay:
                    Utils.sleep_qt(self.delay * 1000 / 3)

                # dumps numbers less than the pivot into a bucket

                if i < pivot:
                    less_than.append(i)

                    # CODE - placing into bucket
                    if self.highlight_enabled:
                        self.cod_window.highlight_line(3)

                    # delay & gui
                    if self.steps_enabled:
                        wait_signal.wait()
                    if self.delay:
                        Utils.sleep_qt(self.delay * 1000 / 3)
                    if self.viz_enabled:
                        self.viz_window.highlight_node(k, False, cur_bucket)
                        self.viz_window.add_node(i, ((self.depth + 1) * 3) - 2)
                        left += 1

                # dumps equivalent numbers into one bucket

                if i == pivot:
                    equals.append(i)

                    # CODE - placing into bucket
                    if self.highlight_enabled:
                        self.cod_window.highlight_line(3)

                    # delay & gui
                    if self.steps_enabled:
                        wait_signal.wait()
                    if self.delay:
                        Utils.sleep_qt(self.delay * 1000 / 3)
                    if self.viz_enabled:
                        self.viz_window.add_node(i, ((self.depth + 1) * 3) - 1)
                        equal += 1

                # dumps numbers greater than the pivot into a bucket

                if i > pivot:
                    greater_than.append(i)

                    # CODE - placing into bucket
                    if self.highlight_enabled:
                        self.cod_window.highlight_line(3)

                    # delay & gui
                    if self.steps_enabled:
                        wait_signal.wait()
                    if self.delay:
                        Utils.sleep_qt(self.delay * 1000 / 3)
                    if self.viz_enabled:
                        self.viz_window.highlight_node(k, False, cur_bucket)
                        self.viz_window.add_node(i, ((self.depth + 1) * 3))
                        right += 1

            # ----------------------
            # END OF BUCKET CREATION
            # ----------------------

            # putting the output together
            # Less Than Bucket
            self.which_bucket = 2
            if self.viz_enabled:
                # blinks current node being worked with
                # this is for when the pivot is the one being selected
                if left > 0:
                    for j in range(0, left - 1):
                        self.viz_window.highlight_node(j, True, cur_bucket + 1)
                    Utils.sleep_qt(self.delay * 1000 / 2 / 3)
                    for j in range(0, left - 1):
                        self.viz_window.highlight_node(j, False, cur_bucket + 1)
                    Utils.sleep_qt(self.delay * 1000 / 2 / 3)
                    for j in range(0, left - 1):
                        self.viz_window.highlight_node(j, True, cur_bucket + 1)
                    Utils.sleep_qt(self.delay * 1000 / 2 / 3)
                    for j in range(0, left - 1):
                        self.viz_window.highlight_node(j, False, cur_bucket + 1)

            # CODE - Highlight line that signifies recursive call
            if self.highlight_enabled:
                self.cod_window.highlight_line(4)

            # Sorting the less_than bucket
            less_output = self.sort(less_than)

            # Correcting depth
            self.depth -= 1

            if self.delay:
                Utils.sleep_qt(self.delay * 1000 / 2)

            # Equals Bucket
            self.which_bucket = 1
            if self.viz_enabled:
                # blinks current node being worked with
                # this is for when the pivot is the one being selected
                if equal > 0:
                    for j in range(0, left - 1):
                        self.viz_window.highlight_node(j, True, cur_bucket + 1)
                    Utils.sleep_qt(self.delay * 1000 / 2 / 3)
                    for j in range(0, left - 1):
                        self.viz_window.highlight_node(j, False, cur_bucket + 1)
                    Utils.sleep_qt(self.delay * 1000 / 2 / 3)
                    for j in range(0, left - 1):
                        self.viz_window.highlight_node(j, True, cur_bucket + 1)
                    Utils.sleep_qt(self.delay * 1000 / 2 / 3)
                    for j in range(0, left - 1):
                        self.viz_window.highlight_node(j, False, cur_bucket + 1)
            eq_output = equals

            if self.delay:
                Utils.sleep_qt(self.delay * 1000 / 2)

            # Greater Than Bucket
            self.which_bucket = 0
            if self.viz_enabled:
                # blinks current node being worked with
                # this is for when the pivot is the one being selected
                if right > 0:
                    for j in range(0, left - 1):
                        self.viz_window.highlight_node(j, True, cur_bucket + 1)
                    Utils.sleep_qt(self.delay * 1000 / 2 / 3)
                    for j in range(0, left - 1):
                        self.viz_window.highlight_node(j, False, cur_bucket + 1)
                    Utils.sleep_qt(self.delay * 1000 / 2 / 3)
                    for j in range(0, left - 1):
                        self.viz_window.highlight_node(j, True, cur_bucket + 1)
                    Utils.sleep_qt(self.delay * 1000 / 2 / 3)
                    for j in range(0, left - 1):
                        self.viz_window.highlight_node(j, False, cur_bucket + 1)

            # CODE - Highlight line that signifies recursive call
            if self.highlight_enabled:
                self.cod_window.highlight_line(4)

            # sorting the greater_than bucket
            great_output = self.sort(greater_than)

            # correcting depth
            self.depth -= 1

            if self.delay:
                Utils.sleep_qt(self.delay * 1000 / 2)

            # VISUALS -- Moving everything up
            if self.viz_enabled:

                self.viz_window.remove_graph(cur_bucket)

                if self.depth == 0:
                    self.viz_window.add_graph(0, "Sorted List")
                else:
                    self.viz_window.add_graph(cur_bucket, "Sorted Sub-list")

                # adding the nodes to our new buckets
                if less_output:
                    Utils.sleep_qt(self.delay * 1000 / 2 / 3)
                    self.viz_window.add_nodes(less_output, cur_bucket)
                    if self.steps_enabled:
                        wait_signal.wait()
                if eq_output:
                    Utils.sleep_qt(self.delay * 1000 / 2 / 3)
                    self.viz_window.add_nodes(eq_output, cur_bucket)
                    if self.steps_enabled:
                        wait_signal.wait()
                if great_output:
                    Utils.sleep_qt(self.delay * 1000 / 2 / 3)
                    self.viz_window.add_nodes(great_output, cur_bucket)
                    if self.steps_enabled:
                        wait_signal.wait()

                # deletion of old, useless buckets
                if self.delay:
                    Utils.sleep_qt(self.delay * 1000 / 2)

                self.viz_window.remove_graph(((self.depth + 1) * 3) + 0)  # Useless right bucket
                self.viz_window.remove_graph(((self.depth + 1) * 3) - 1)  # Useless equal bucket
                self.viz_window.remove_graph(((self.depth + 1) * 3) - 2)  # Useless left bucket

                if self.delay:
                    Utils.sleep_qt(self.delay * 1000 / 2)

            # CODE - Highlight line that signifies recursive call
            if self.highlight_enabled:
                self.cod_window.highlight_line(5)

            output = less_output + eq_output + great_output

            return output
        # only 1 number
        else:

            # highlight to signify which graph we are on
            if self.viz_enabled:
                self.viz_window.highlight_node(0, True, cur_bucket)

            # pause before deletion
            if self.delay:
                Utils.sleep_qt(self.delay * 1000 / 2)
            # delete the graphs created
            # deletion of old, useless buckets
            if self.viz_enabled:
                self.viz_window.remove_graph((self.depth + 1) * 3)  # Useless right bucket
                self.viz_window.remove_graph(((self.depth + 1) * 3) - 1)  # Useless equal bucket
                self.viz_window.remove_graph(((self.depth + 1) * 3) - 2)  # Useless left bucket

            # pause after deletion
            if self.delay:
                Utils.sleep_qt(self.delay * 1000 / 2)

            # undoing the highlight that signified which graph we are on
            if self.viz_enabled:
                self.viz_window.highlight_node(0, False, cur_bucket)

            if self.steps_enabled:
                wait_signal.wait()

            return num_list
