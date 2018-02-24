# DO NOT INCLUDE THIS FILE IN FINAL PRODUCT!!

"""
This is a simple algorithm file that doesn't really sort anything.
Instead, this file demonstrates how to implement the Algorithm interface.
"""
from Algorithm.Algorithm import Algorithm


class ExampleAlgorithm(Algorithm):
    multiplier = 2

    def sort(self, num_list):
        """
        Doesn't actually sort!
        Multiplies each number in a list by 2.

        :param num_list: the list to "sort"
        :return: the resulting list
        """
        result = []

        for num in num_list:
            result.append(self._multiply(num, self.multiplier))

        return result

    def _multiply(self, a1, a2):
        """
        Private function that multiplies two numbers

        :param a1: the first number
        :param a2: the second number
        :return: the product
        """
        return a1 * a2
