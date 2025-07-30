class Solution:

	
	def removeDuplicates(self, s):
	    final_string = ""
	    for i in s:
	      if i not in final_string:
	          final_string += i
	           
	    return final_string
