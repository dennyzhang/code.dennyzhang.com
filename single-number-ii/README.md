# Leetcode: Single Number II     :BLOG:Medium:


---

Identity number which appears exactly once.  

---

Given an array of integers, every element appears three times except for one, which appears exactly once. Find that single one.  

Note:  
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/single-number-ii)  

Credits To: [leetcode.com](https://leetcode.com/problems/single-number-ii/description/)  

Hint: Time O(n), Space O(1)  

Leave me comments, if you know how to solve.  

    ## Blog link: http://brain.dennyzhang.com/single-number-ii
    class Solution(object):
        def singleNumber(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            ## Idea: Use memory in the list
            ## Complexity: Time O(n), Space O(1)
            ## Sample Data:
            ##    1 1 0 1
            ##    1 1 0 1
            ##    1 1 0 1
            ##    0 1 1 1
            ## Asummption: Integer is 64 bits. Any negative values?
            length = 64
            bit_list = [0]*length
            for num in nums:
                for i in xrange(length):
                    bit_list[i] += num % 2
                    bit_list[i] = bit_list[i] % 3
                    num = num >> 1
    
            bit_list.reverse()
            res = 0
            is_positive = True
            if bit_list[0] == 1:
                is_positive = False
                bit_list = map(lambda x:(x+1)%2, bit_list)
            for i in xrange(length):
                res = res << 1
                res = res | bit_list[i]
    
            if is_positive is True: return res else: return -(res+1)