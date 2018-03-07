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

        """
        if needed
        create the separation of the buckets in visualization
        PROBLEM: creating the bucket separation would cause difficulties
        when re-merging the buckets
        """

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
            # dumping some numbers into some buckets with labels
            for i in num_list:
                if i < pivot:
                    less_than.append(i)

                    """
                    move the current object into the less_than bucket
                    """

                if i == pivot:
                    equals.append(i)

                    """
                    move the current object into the equals object
                    """

                if i > pivot:
                    greater_than.append(i)

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
