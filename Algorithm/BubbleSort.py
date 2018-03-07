# Title: BubbleSort
# Author: Avan Patel, Kohler Smallwood, Azlin Reed, Jordan Stremming, Steven Huynh, Zach Butterbaugh, Thea Furby
# Purpose: Take in List and check the element at index I and I+1. If element i > i+1, then it swap the element.
# At the end of 1st run, the last element in the array will be largest..


from Algorithm.Algorithm import Algorithm


class BubbleSort(Algorithm):

    def sort(self, element):
        n = len(element)
        value = True
        for each in range(n):                   # Go Through the Element in Array
            for i in range(0, n-each-1):        # After first run last element is sorted so you want to skip going that far
                if element[i] > element[i+1]:   # If i > i+1 then swap it
                    element[i], element[i+1] = element[i+1], element[i]
                    value = False
            # If array already sorted then Break
            if value is True:
                print("Array already sorted")
                break
        return element



# element = [12, 5, 2, 6, 7, 3]               # Random Testing Numbers
# array = []                                  # Taking an input from File
# filename = input("What is the name of input file? ")
# with open(filename) as f:
#     for line in f:
#         array.append(line)                  # Appending each element of file to List as string
#
#
# array = list(map(int, array))               # Converting list to string
# sort(array)                                 # Calling Function
#
#
# # Print out Element in Array
# for each in range(len(array)):
#     print(array[each])
#


