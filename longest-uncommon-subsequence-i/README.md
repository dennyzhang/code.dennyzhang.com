# Leetcode: Longest Uncommon Subsequence I     :BLOG:Medium:


---

Longest Uncommon Subsequence I  

---

Similar Problems:  
-   [Longest Uncommon Subsequence II](https://brain.dennyzhang.com/longest-uncommon-subsequence-ii)

---

Given a group of two strings, you need to find the longest uncommon subsequence of this group of two strings. The longest uncommon subsequence is defined as the longest subsequence of one of these strings and this subsequence should not be any subsequence of the other strings.  

A subsequence is a sequence that can be derived from one sequence by deleting some characters without changing the order of the remaining elements. Trivially, any string is a subsequence of itself and an empty string is a subsequence of any string.  

The input will be two strings, and the output needs to be the length of the longest uncommon subsequence. If the longest uncommon subsequence doesn't exist, return -1.  

Example 1:  

    Input: "aba", "cdc"
    Output: 3
    Explanation: The longest uncommon subsequence is "aba" (or "cdc"), 
    because "aba" is a subsequence of "aba", 
    but not a subsequence of any other strings in the group of two strings.

Note:  

Both strings' lengths will not exceed 100.  
Only letters from a ~ z will appear in input strings.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/longest-uncommon-subsequence-i)  

Credits To: [leetcode.com](https://leetcode.com/problems/longest-uncommon-subsequence-i/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/longest-uncommon-subsequence-i
    ## Basic Ideas: If length is different, get the bigger one
    ##              If length is the same, compare whether they are the same
    ##                 If not, return either one
    ##
    ## Notice: what if one string is empty?
    ##              
    ## Complexity: Time O(n), Space O(n)
    class Solution:
        def findLUSlength(self, a, b):
            """
            :type a: str
            :type b: str
            :rtype: int
            """
            if a == b: return -1
            return max(len(a), len(b))
    
    # s = Solution()
    # print(s.findLUSlength("aefawfawfawfaw", "aefawfeawfwafwaef")) # 17