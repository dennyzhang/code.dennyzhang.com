
# Leetcode: Remove K Digits     :BLOG:Medium:

---

Remove K Digits  

---

Similar Problems:  

-   [Monotone Increasing Digits](https://code.dennyzhang.com/monotone-increasing-digits)
-   [Review: Greedy Problems](https://code.dennyzhang.com/review-greedy), [Tag: #greedy](https://code.dennyzhang.com/tag/greedy)

---

Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.  

Note:  
The length of num is less than 10002 and will be ≥ k.  
The given num does not contain any leading zero.  
Example 1:  

    Input: num = "1432219", k = 3
    Output: "1219"
    Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

Example 2:  

    Input: num = "10200", k = 1
    Output: "200"
    Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.

Example 3:  

    Input: num = "10", k = 2
    Output: "0"
    Explanation: Remove all the digits from the number and it is left with nothing which is 0.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/remove-k-digits)  

Credits To: [leetcode.com](https://leetcode.com/problems/remove-k-digits/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/remove-k-digits
    ## Basic Ideas: Greedy
    ##    From left to right, if current digit decreases, we find one candiate
    ##    Why?
    ##       i-1, i, i +1
    ##       digit[i-1] <= digit[i] and digit[i] > digit[i+1]
    ##       Let's say we don't delete digit i.
    ##       If the final result has deleted digit i+1, the result won't be optimal. 
    ##         Since we can keep digit i+1 and delete digit i, with everything else unchanged.
    ##         The modified result would be smaller
    ##       If the final result hasn't deleted digit i+1
    ##         If the deletion has happened before i, it doesn't make sense
    ##         If the deletion has happened after i+1. 
    ##              We can find another combination which is better. 
    ##              Delete digit i and keep any other deletion.
    ##
    ## Complexity: Time O(n), Space O(1)
    class Solution:
        def removeKdigits(self, num, k):
    	"""
    	:type num: str
    	:type k: int
    	:rtype: str
    	"""
    	length = len(num)
    	l = []
    	for i in range(length):
    	    # delete the previous, if necessary
    	    while len(l) != 0 and k > 0:
    		if num[i] < l[-1]:
    		    del l[-1]
    		    k -= 1
    		else: break
    
    	    if k == 0:
    		l.append(num[i])
    	    else:
    		if i == length -1 or num[i] <= num[i+1]:
    		    l.append(num[i])
    		else:
    		    # should delete digit i
    		    k -= 1
    
    	# remove from the tail
    	while len(l) !=0 and k>0:
    	    del l[-1]
    	    k -= 1
    
    	res = ''.join(l).lstrip('0')
    	if res == '': res ='0'
    	return res
    
    # s = Solution()
    # print(s.removeKdigits("12", 1))

