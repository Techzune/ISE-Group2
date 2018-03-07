# title: CountingSort
# author: Avan Patel, Kohler Smallwood, Azlin Reed, Jordan Stremming, Steven Huynh, Zach Butterbaugh, Thea Furby
# purpose: algorithm;
from Algorithm.Algorithm import Algorithm


class CountingSort(Algorithm):

    def sort(self, num_list):
        n = len(num_list)
        m = num_list.max()
        count = [0] * m
        for a in num_list:
            num_list[a] += 1
        i = 0
        for a in range(m):
            for c in range(num_list[a]):
                num_list[i] = a
                i += 1
        return num_list

