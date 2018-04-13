# Leetcode: Strobogrammatic Number     :BLOG:Basic:


---

Strobogrammatic Number  

---

Similar Problems:  
-   [Reconstruct Original Digits from English](https://code.dennyzhang.com/reconstruct-original-digits-from-english)
-   [Review: Math Problems,](https://code.dennyzhang.com/review-math) Tag: [math](https://code.dennyzhang.com/tag/math)
-   [Review: String Problems](https://code.dennyzhang.com/review-string), Tag: [#string](https://code.dennyzhang.com/tag/string)

---

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).  

Write a function to determine if a number is strobogrammatic. The number is represented as a string.  

For example, the numbers "69", "88", and "818" are all strobogrammatic.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/strobogrammatic-number)  

Credits To: [leetcode.com](https://leetcode.com/problems/strobogrammatic-number/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://code.dennyzhang.com/strobogrammatic-number
    class Solution(object):
        ## Basic Ideas: One pass with two pointer + set
        ## Complexity: Time O(n), Space O(1)
        def isStrobogrammatic(self, num):
            """
            :type num: str
            :rtype: bool
            """
            maps = [('0', '0'), ('1', '1'), ('8', '8'), ('6', '9'), ('9', '6')]
            left, right = 0, len(num)-1
            while left<=right:
                if (num[left], num[right]) not in maps: return False
                left, right = left+1, right-1
            return True
    
        ## Basic Ideas: One pass with two pointer + hasmap
        ## Complexity: Time O(n), Space O(1)
        def isStrobogrammatic_v1(self, num):
            """
            :type num: str
            :rtype: bool
            """
            length = len(num)
            if length == 0: return False
            d = {'0':'0', '1':'1', '8':'8', '6':'9', '9':'6'}
            left, right = 0, length-1
            # We need to check left == right
            while left<=right:
                if (num[left] not in d) or (num[right] not in d): return False
                # 81, 18, 919
                # We don't need extra check the middle element
                if d[num[left]] != num[right]: return False
                left, right = left+1, right-1
            return True
    
        ## Basic Ideas: Reverse, change by character, than compare
        ##  0 1 2 3 4 5 6 7 8 9
        ##      0, 1, 8
        ##      6, 9
        ##      2, 3, 4, 5, 7
        ##
        ## Sample Data: 81, 18
        ## Complexity: Time O(n), Space O(n)
        def isStrobogrammatic_v2(self, num):
            """
            :type num: str
            :rtype: bool
            """
            length = len(num)
            if length == 0: return False
            d = {'0':'0', '1':'1', '8':'8', '6':'9', '9':'6'}
            num2 = ''
            for ch in num[::-1]:
                if ch not in d: return False
                num2 = '%s%s' % (num2, d[ch])
            return num == num2