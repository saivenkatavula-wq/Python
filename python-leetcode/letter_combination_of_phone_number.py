class Solution(object):
    def letterCombinations(self, digits):
        result = [""]
        thisDict = {
            "2" : ["a", "b", "c"],
            "3" : ["d", "e", "f"],
            "4" : ["g", "h", "i"],
            "5" : ["j", "k", "l"],
            "6" : ["m", "n", "o"],
            "7" : ["p", "q", "r", "s"],
            "8" : ["t", "u", "v"],
            "9" : ["w", "x", "y", "z"]
        }
        
        for d in digits:
            letters = thisDict[d]
            new_list = []
            for old in result:
                for letter in letters:
                    new_list.append(old+letter)
            result = new_list

        return result
