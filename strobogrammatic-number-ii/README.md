# Leetcode: Strobogrammatic Number II     :BLOG:Medium:


---

Strobogrammatic Number II  

---

Similar Problems:  
-   [Unique Binary Search Trees II](https://brain.dennyzhang.com/unique-binary-search-trees-ii)
-   [Strobogrammatic Number](https://brain.dennyzhang.com/strobogrammatic-number)
-   Tag: [#string](https://brain.dennyzhang.com/tag/string)

---

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).  

Find all strobogrammatic numbers that are of length = n.  

For example,  
Given n = 2, return ["11","69","88","96"].  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/strobogrammatic-number-ii)  

Credits To: [leetcode.com](https://leetcode.com/problems/strobogrammatic-number-ii/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/strobogrammatic-number-ii
    ## Basic Ideas: Recursive
    ##       From f(n-2) and f(2) --> f(n)
    ##
    ##  Notice:  00 is invalid for n=2, but 8008 is valid for n=4
    ##
    ## Complexity: Time O(n), Space O(k). k is the final result
    class Solution(object):
        def findStrobogrammatic(self, n):
            """
            :type n: int
            :rtype: List[str]
            """
            return self.myFindStrobogrammatic(n)[0]
    
        def myFindStrobogrammatic(self, n):
            if n == 0: return [[], []]
            if n == 1: return [['0', '1', '8'], []]
            if n == 2: return [['11', '69', '88', '96'], ['00']]
            res_l1, res_l2 = [], []
            [l1, l2] = self.myFindStrobogrammatic(n-2)
            for p in self.findStrobogrammatic(2):
                [start_ch, end_ch] = list(p)
                for q in l1+l2:
                    res_l1.append("%s%s%s" % (start_ch, q, end_ch))
    
            for q in l1+l2: res_l2.append("0%s0" % q)
            return [res_l1, res_l2]
    
    s = Solution()
    print(s.findStrobogrammatic(6))