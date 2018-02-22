# Title: BubbleSort
# Author: Avan Patel, Kohler Smallwood, Azlin Reed, Jordan Stremming, Steven Huynh, Zach Butterbaugh
# Purpose: Take in List and check the element at index I and I+1. If element i > i+1, then it swap the element.
# At the end of 1st run, the last element in the array will be largest.;


def sort(element):
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


element = [0, 1, 2, 4]
sort(element)


# Print out Element in Array
for each in range(len(element)):
    print(element[each])



