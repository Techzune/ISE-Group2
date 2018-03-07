# title: QuickSort
# author: Avan Patel, Kohler Smallwood, Azlin Reed, Jordan Stremming, Steven Huynh, Zach Butterbaugh, Thea Furby
# purpose: algorithm;
from Algorithm.Algorithm import Algorithm


class QuickSort(Algorithm):

    def sort(self, num_list):

        # creation of the buckets
        less_than = []
        equals = []
        greater_than = []

        # there are actually numbers to sort
        if len(num_list) > 1:

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
            # dumping some numbers into some buckets
            for i in num_list:
                if i < pivot:
                    less_than.append(i)
                if i == pivot:
                    equals.append(i)
                if i > pivot:
                    greater_than.append(i)

                # UPDATE THE VISUALIZATION WINDOW

            return self.sort(less_than) + equals + self.sort(greater_than)

        # only 1 number
        else:
            return num_list
