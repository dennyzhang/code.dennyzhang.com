
# Leetcode: Candy     :BLOG:Hard:

---

Candy  

---

Similar Problems:  

-   [Review: Greedy Problems](https://code.dennyzhang.com/review-greedy), [Tag: #greedy](https://code.dennyzhang.com/tag/greedy)

---

There are N children standing in a line. Each child is assigned a rating value.  

You are giving candies to these children subjected to the following requirements:  

Each child must have at least one candy.  
Children with a higher rating get more candies than their neighbors.  
What is the minimum candies you must give?  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/candy)  

Credits To: [leetcode.com](https://leetcode.com/problems/candy/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/candy
    ## Basic Ideas:
    ##
    ##   Assign each child 1 candy
    ##   From left to right, if the latter one has a bigger value, change the latter value
    ##   From right to left, if the former one has a bigger value, change the former value
    ##   Collect the result
    ##
    ##   Assumption: if the same rating, they don't have to get the same amount of candies
    ## Complexity: Time O(n), Space O(n)
    class Solution:
        def candy(self, ratings):
    	"""
    	:type ratings: List[int]
    	:rtype: int
    	"""
    	length = len(ratings)
    	l = [1] * length
    	for i in range(length-1):
    	    if ratings[i+1] > ratings[i]: l[i+1] = l[i]+1
    
    	for i in range(length-1, 0, -1):
    	    if ratings[i-1] > ratings[i] and l[i-1]<=l[i]:
    		l[i-1] = l[i]+1
    
    	return sum(l)

