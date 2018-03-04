# Leetcode: Longest Substring with At Most Two Distinct Characters     :BLOG:Hard:


---

Longest Substring with At Most Two Distinct Characters  

---

Similar Problems:  
-   [Longest Substring with At Most K Distinct Characters](https://brain.dennyzhang.com/longest-substring-with-at-most-k-distinct-characters)
-   [Tag: #string](https://brain.dennyzhang.com/tag/string)

---

Given a string, find the length of the longest substring T that contains at most 2 distinct characters.  

For example, Given s = “eceba”,  

T is "ece" which its length is 3.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/longest-substring-with-at-most-two-distinct-characters)  

Credits To: [leetcode.com](https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/longest-substring-with-at-most-two-distinct-characters
    ## Basic Ideas:
    ## Complexity: Time O(n), Space O(1)
    class Solution:
        def lengthOfLongestSubstringTwoDistinct(self, s):
            """
            :type s: str
            :rtype: int
            """
            import collections
            import sys
    
            length = len(s)
            d = collections.defaultdict(lambda: 0)
    
            # initialize sliding window
            index, res = length, -1
            for i in range(length):
                ch = s[i]
                if ch in d: d[ch] += 1
                else:
                    if len(d) == 2:
                        index = i
                        break
                    else:
                        d[ch] += 1
            res = max(res, sum([d[ch] for ch in d]))
            # move sliding window
            i = 0
            for j in range(index, length):
                d[s[j]] += 1
                while len(d) == 3:
                    ch = s[i]
                    i += 1
                    d[ch] -= 1
                    if d[ch] == 0: del d[ch]
                res = max(res, sum([d[ch] for ch in d]))
    
            return res
    
    # s = Solution()
    # print(s.lengthOfLongestSubstringTwoDistinct("bacc")) # 3