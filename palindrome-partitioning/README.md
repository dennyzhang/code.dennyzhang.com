# Leetcode: Palindrome Partitioning     :BLOG:Basic:


---

Backtracking or DFS  

---

Similar Problems:  
-   [Review: Palindrome Problems](https://brain.dennyzhang.com/review-palindrome), [Tag: #palindrome](https://brain.dennyzhang.com/tag/palindrome)

---

Given a string s, partition s such that every substring of the partition is a palindrome.  

Return all possible palindrome partitioning of s.  

For example, given s = "aab",  
Return  

    [
      ["aa","b"],
      ["a","a","b"]
    ]

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/palindrome-partitioning)  

Credits To: [leetcode.com](https://leetcode.com/problems/palindrome-partitioning/description/)  

    ## Blog link: https://brain.dennyzhang.com/palindrome-partitioning
    ## Basic Ideas: Divide and conquer
    ## Complexity: Time O(), Space O()
    ## Assumptions:
    ## Sample Data:
    class Solution(object):
        def partition(self, s):
            """
            :type s: str
            :rtype: List[List[str]]
            """
            res = []
            for i in range(0, len(s)-1):
                if self.is_palindrome(s[0:i+1]):
                    l = self.partition(s[i+1:])
                    # print("s: %s, s1: %s, l: %s" % (s, s[i+1:], l))
                    for element in l:
                        element.insert(0, s[0:i+1])
                        res.append(element)
            if self.is_palindrome(s):
                res.append([s])
    
            # print("s:%s, res: %s" % (s, res))
            return res
    
        def is_palindrome(self, s):
            return s == s[::-1]