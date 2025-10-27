#sliding window method
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        seen = set()
        left = 0
        max_len = 0

        for right in range(len(s)):
            ch = s[right]

            while ch in seen:
                seen.remove(s[left])
                left += 1
            
            seen.add(ch)
            max_len = max(max_len, right - left + 1)
        return max_len

# brute force method
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        word_list = []
        best_list = []
        best = 0
        if len(s) == 0:
            best_list.append(best)
        for i in range(len(s)):
            if s[i] not in word_list:
                word_list.append(s[i])
                best += 1
                best_list.append(best)
            else:
                duplicate_index = word_list.index(s[i])
                word_list = word_list[duplicate_index + 1:]
                word_list.append(s[i])
                best = len(word_list)
                best_list.append(best) 

        return max(best_list)
      
