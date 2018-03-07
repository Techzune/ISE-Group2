# title: MergeSort
# author: Avan Patel, Kohler Smallwood, Azlin Reed, Jordan Stremming, Steven Huynh, Zach Butterbaugh, Thea Furby
# purpose: algorithm;
from Algorithm.Algorithm import Algorithm


class MergeSort(Algorithm):

    def mergeFunction(self, list_left, list_right):

        #create new empty merge list
        merge_list = []

        #set L and R indices
        L = 0
        R = 0

        #loop
        while len(list_right)>0 and len(list_left)>0:
            if list_left[L] > list_right[R]:
                merge_list.append(list_right[R])
                list_right.remove(list_right[R])

            else:
                merge_list.append(list_left[L])
                list_left.remove(list_left[L])

        if len(list_right)<=0:
            merge_list = merge_list + list_left

        elif len(list_left)<=0:
            merge_list = merge_list + list_right

        return merge_list

    def sort(self, num_list):
        listLeft = []
        listRight = []

        sortedLeft = []
        sortedRight = []

        if len(num_list) >= 2:

            listLeft = num_list[:len(num_list)//2]
            listRight = num_list[len(num_list)//2:]

            #recurse left side
            sortedLeft = self.sort(listLeft)

            #recurse right side
            sortedRight = self.sort(listRight)

            #merge lists
            sortedList = self.mergeFunction(sortedLeft, sortedRight)

            #return sorted list
            return sortedList

        else:
            return num_list


