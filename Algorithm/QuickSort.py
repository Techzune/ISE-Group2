# title: QuickSort
# author: Avan Patel, Kohler Smallwood, Azlin Reed, Jordan Stremming, Steven Huynh, Zach Butterbaugh, Thea Furby
# purpose: algorithm;
from Algorithm.Algorithm import Algorithm


class QuickSort(Algorithm):

    def sort(self, num_list):

        less_than = []
        equals = []
        greater_than = []

        if len(num_list) > 1:
            # there are actually numbers to sort

            # setting the pivot
            # using the first number as a pivot for simplicity
            pivot = num_list[0]

            # the actual sorting
            for i in num_list:
                if i < pivot:
                    less_than.append(i)
                if i == pivot:
                    equals.append(i)
                if i > pivot:
                    greater_than.append(i)

                # UPDATE THE VISUALIZATION WINDOW

            return less_than + equals + greater_than

        else:
            # only 1 number
            return num_list
