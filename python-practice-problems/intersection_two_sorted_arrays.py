class Solution:
    def intersection(self, arr1, arr2):
        final_list = list(set(arr1).intersection(set(arr2)))
        final_list.sort()
        return final_list
    
