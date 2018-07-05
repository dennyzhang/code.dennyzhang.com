
# Leetcode: Perfect Number     :BLOG:Medium:

---

numbers  

---

Similar Problems:  

-   [Review: sqrt Problems](https://code.dennyzhang.com/review-sqrt)
-   Tag: [sqrt](https://code.dennyzhang.com/tag/sqrt)

---

We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.  

Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.  

    Example:
    Input: 28
    Output: True
    Explanation: 28 = 1 + 2 + 4 + 7 + 14

Note: The input number n will not exceed 100,000,000. (1e8)  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/perfect-number)  

Credits To: [leetcode.com](https://leetcode.com/problems/perfect-number/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/perfect-number
    ## Basic Ideas: sqrt(num)
    ##     Sample Data:
    ##         1 2 7
    ## Complexity:
    class Solution(object):
        def checkPerfectNumber(self, num):
    	"""
    	:type num: int
    	:rtype: bool
    	"""
    	if num <= 1:
    	    return False
    	import math
    	sum = 1
    	for i in range(2, int(math.sqrt(num))+1):
    	    if num % i == 0:
    		sum += i
    		if i != num/i:
    		    sum += num/i
    	return sum == num

