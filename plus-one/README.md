# Leetcode: Plus One     :BLOG:Basic:


---

Plus one to a big integer  

---

Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.  

You may assume the integer do not contain any leading zero, except the number 0 itself.  

The digits are stored such that the most significant digit is at the head of the list.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/plus-one)  

Credits To: [Leetcode.com](https://leetcode.com/problems/plus-one/description/)  

Leave me comments, if you know how to solve.  

    ## Basic Ideas: If the highest digit is 1, the value is negative
    ## Complexity: Time O(n), Space O(n)
    class Solution(object):
        def plusOne(self, digits):
            """
            :type digits: List[int]
            :rtype: List[int]
            """
            res = 
            has_carry = False
            if digits[-1] == 9:
                res.insert(0, 0)
                has_carry = True
            else:
                res.insert(0, digits[-1]+1)
    
            for i in range(len(digits)-2, -1, -1):
                if has_carry is False:
                    res.insert(0, digits[i])
                else:
                    if digits[i] == 9:
                        res.insert(0, 0)
                        has_carry = True
                    else:
                        res.insert(0, digits[i]+1)
                        has_carry = False
    
            if has_carry is True:
                res.insert(0, 1)
            return res