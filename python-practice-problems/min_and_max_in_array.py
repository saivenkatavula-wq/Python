class Solution:
    def get_min_max(self, arr):
        min_value = max_value = arr[0]
        for num in arr:
            if num < min_value:
                min_value = num
            if num > max_value:
                max_value = num
        return(min_value, max_value)
