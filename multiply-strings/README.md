# Leetcode: Multiply Strings     :BLOG:Medium:


---

Multiply Strings  

---

Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2.  

Note:  

1.  The length of both num1 and num2 is < 110.
2.  Both num1 and num2 contains only digits 0-9.
3.  Both num1 and num2 does not contain any leading zero.
4.  You must **not use any built-in BigInteger library or convert the inputs to integer** directly.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/multiply-strings)  

Credits To: [leetcode.com](https://leetcode.com/problems/multiply-strings/description/)  

Leave me comments, if you know how to solve.  

    ## Blog link: http://brain.dennyzhang.com/multiply-strings
    ## Basic Ideas:
    ##       No more than 2 elements would be qualified.
    ## Complexity: Time O(n), Space O(1)
    ## Sample Data:
    ##    1 2 3 2 3 3
    ## Asummption:
    class Solution(object):
        def majorityElement(self, nums):
            """
            :type nums: List[int]
            :rtype: List[int]
            """
            length = len(nums)
            if length == 0:
                return []
            n1, n2 = None, None
            c1, c2 = 0, 0
            for num in nums:
                if num == n1:
                    c1 += 1
                elif num == n2:
                    c2 += 1
                elif c1 == 0:
                    n1, c1 = num, 1
                elif c2 == 0:
                    n2, c2 = num, 1
                else:
                    c1, c2 = c1 - 1, c2 - 1
            c1, c2 = 0, 0
            for num in nums:
                if num == n1:
                    c1 += 1
                elif num == n2:
                    c2 += 1
            # print("n1: %d, c1: %d, n2: %d, c2: %d. length: %d" % (n1, c1, n2, c2, length))
            res = []
            if c1 > length/3:
                res.append(n1)
            if c2 > length/3:
                res.append(n2)
            return res
    
    s = Solution()
    # print s.majorityElement([1, 2])
    # print s.majorityElement([1,2,1,1,1,3,3,4,3,3,3,4,4,4])
    print s.majorityElement([1,1,1,2,3,4,5,6])
    # print s.majorityElement([1, 2, 3, 2, 3, 3])