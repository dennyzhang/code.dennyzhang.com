# Leetcode: Letter Combinations of a Phone Number     :BLOG:Basic:


---

Letter Combinations of a Phone Number  

---

Given a digit string, return all possible letter combinations that the number could represent.  

A mapping of digit to letters (just like on the telephone buttons) is given below.  

    Input:Digit string "23"
    Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Note:  
Although the above answer is in lexicographical order, your answer could be in any order you want.  

Blog link: <http://brain.dennyzhang.com/letter-combinations-of-a-phone-number>  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/letter-combinations-of-a-phone-number)  

Credits To: [leetcode.com](https://leetcode.com/problems/letter-combinations-of-a-phone-number/description)  

Leave me comments, if you know how to solve.  

    class Solution(object):
        def letterCombinations(self, digits):
            """
            :type digits: str
            :rtype: List[str]
            """
            ## Basic Ideas:
            ## Complexity:
            ## Assumptions: For "0" and "1", map to empty string
            ## Sample Data:
            ch_dict = {"1":"", "2":"abc", "3":"def", 
                       "4":"ghi", "5":"jkl", "6":"mno",
                       "7":"pqrs", "8":"tuv", "9":"wxyz", "0":""}
            res = []
            for digit in digits:
                # print("digit:%s. res: %s" % (digit, res))
                ch_list = ch_dict[digit]
                if len(res) == 0:
                    for ch in ch_list:
                        res.append(ch)
                else:
                    item_list = []
                    for ch in ch_list:
                        for item in res:   
                            item = "%s%s" % (item, ch)
                            item_list.append(item)
                    res = item_list
            return res
    
    s = Solution()
    print s.letterCombinations("23")