# title: InsertionSort
# author: Avan Patel, Kohler Smallwood, Azlin Reed, Jordan Stremming, Steven Huynh, Zach Butterbaugh, Thea Furby
# purpose: algorithm;
#cited source: https://www.geeksforgeeks.org/insertion-sort/

from Algorithm.Algorithm import Algorithm

class InsertionSort(Algorithm):

    def sort(self, num_list):
        # Traverse through 1 to len(num_list)
        for i in range(1, len(num_list)):

            current_value = num_list[i]

            # Move elements of num_list[0..i-1], that are
            # greater than current_value, to one position ahead
            # of their current position
            j = i - 1
            while j >= 0 and current_value < num_list[j]:
                num_list[j + 1] = num_list[j]
                j -= 1
            num_list[j + 1] = current_value
        return num_list


# Driver code to test above
#num_list = [12, 11, 13, 5, 6]
#insertionSort(num_list)
#print ("Sorted array is:")
#for i in range(len(num_list)):
#  print ("%d" %num_list[i])