# DO NOT INCLUDE THIS FILE IN FINAL PRODUCT!!

"""
This is a simple algorithm file that doesn't really sort anything.
Instead, this file demonstrates how to implement the Algorithm interface.
"""
from Algorithm.Algorithm import Algorithm


class ExampleAlgorithm(Algorithm):

    def sort(self, num_list):
        """
        Doesn't actually sort!
        Multiplies each number in a list by 2.

        :param num_list: the list to "sort"
        :return: the resulting list
        """
        result = []

        for num in num_list:
            result.append(num * 2)

        return result
