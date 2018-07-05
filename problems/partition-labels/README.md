
# Leetcode: Partition Labels     :BLOG:Basic:

---

Partition Labels  

---

A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.  

    Example 1:
    Input: S = "ababcbacadefegdehijhklij"
    Output: [9,7,8]
    Explanation:
    The partition is "ababcbaca", "defegde", "hijhklij".
    This is a partition so that each letter appears in at most one part.
    A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.

Note:  

-   S will have length in range [1, 500].
-   S will consist of lowercase letters ('a' to 'z') only.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/partition-labels)  

Credits To: [leetcode.com](https://leetcode.com/problems/partition-labels/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/partition-labels
    ## Basic Ideas:
    ##       letter_dict:
    ##             a -> max 20
    ##             b -> max 30
    ## Complexity:
    class Solution(object):
        def partitionLabels(self, S):
    	"""
    	:type S: str
    	:rtype: List[int]
    	"""
    	letter_dict = {}
    	for ch in map(chr, range(ord('a'), ord('z')+1)):
    	    letter_dict[ch] = -1
    
    	length = len(S)
    	for i in xrange(length):
    	    ch = S[i]
    	    if i > letter_dict[ch]:
    		letter_dict[ch] = i
    
    	res = []
    	i = 0
    	print letter_dict
    	while i < length:
    	    ch = S[i]
    	    # print("ch: %s" % (ch))
    	    previous_index = i
    	    max_index = letter_dict[ch]
    	    while max_index > previous_index:
    		v = max_index
    		for k in range(previous_index, max_index):
    		    index = letter_dict[S[k]]
    		    max_index = max(max_index, index)
    		previous_index = v
    
    	    res.append(max_index - i + 1)
    	    # print("s: %s" % (S[i:max_index+1]))
    	    i = max_index + 1
    	return res
    
    # s = Solution()
    # # print s.partitionLabels("eaaaabaaec")
    # print s.partitionLabels("ababcbacadefegdehijhklij") # [9, 7, 8]
    # print s.partitionLabels("qiejxqfnqceocmy") # [13, 1, 1]

