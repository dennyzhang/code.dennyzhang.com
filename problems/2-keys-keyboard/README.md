
# Leetcode: 2 Keys Keyboard     :BLOG:Amusing:

---

2 Keys Keyboard  

---

Similar Problems:  

-   [Integer Break](https://code.dennyzhang.com/integer-break)
-   [Review: Dynamic Programming Problems](https://code.dennyzhang.com/review-dynamicprogramming)
-   Tag: [#dynamicprogramming](https://code.dennyzhang.com/tag/dynamicprogramming)

---

Initially on a notepad only one character 'A' is present. You can perform two operations on this notepad for each step:  

1.  ****Copy All****: You can copy all the characters present on the notepad (partial copy is not allowed).
2.  ****Paste****: You can paste the characters which are copied last time.

Given a number n. You have to get exactly n 'A' on the notepad by performing the minimum number of steps permitted. Output the minimum number of steps to get n 'A'.  

Example 1:  

    Input: 3
    Output: 3
    Explanation:
    Intitally, we have one character 'A'.
    In step 1, we use Copy All operation.
    In step 2, we use Paste operation to get 'AA'.
    In step 3, we use Paste operation to get 'AAA'.

Note:  

-   The n will be in the range [1, 1000].

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/2-keys-keyboard)  

Credits To: [leetcode.com](https://leetcode.com/problems/2-keys-keyboard/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/2-keys-keyboard
    ## Basic Ideas: Dynamic programming
    ##
    ## Complexity: Time O(n*n), Space O(n)
    class Solution:
        def minSteps(self, n):
    	"""
    	:type n: int
    	:rtype: int
    	"""
    	d = list(range(0, n+1))
    	d[1] = 0
    	# from left to right
    	for i in range(2, n+1):
    	    for j in range(i-1, 1, -1):
    		# why this solution holds?
    		if i%j == 0:
    		    d[i]= d[j] + int(i/j)
    		    break
    	return d[n]

