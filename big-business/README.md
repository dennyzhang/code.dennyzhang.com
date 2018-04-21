# LintCode: Big Business     :BLOG:Basic:


---

Identity number which appears exactly once.  

---

Similar Problems:  
-   Tag: [#greedy](https://code.dennyzhang.com/tag/greedy)

---

Given two arrays a and b. a[i] stands for the royalties of the film i, b[i] represents the money that the movie i can sell, now we have principal k, find how much money can be earned in the end.(Each movie only needs to be bought once and can only be sold once.)  

Notice  
-   All the input does not exceed 100000
-   The size of array does not exceed 10000.
-   Have you met this question in a real interview?

Example  

    Given a = [3,1,5], b = [4,3,100], k = 1,return 4.
    
    Explanation:
    Buy the second video first, then sell it, buy the first video, sell it again, and finally the principal becomes 4.

    Given a = [3,1,5], b = [4,3,100], k = 10,return 108.
    
    Explanation:
    Buy all the videos, sell them, and finally the principal becomes 108.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/big-business)  

Credits To: [lintcode.com](http://www.lintcode.com/en/problem/big-business/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://code.dennyzhang.com/big-business
    class Solution:
        """
        @param a: The cost of the film
        @param b: The price of the selling of the film
        @param k: The principal
        @return: The answer
        """
        def bigBusiness(self, a, b, k):
            ## Basic Ideas: sort a
            ##    From left to right, stop when we can't afford it
            ##    Note: there might be movie which might lose money 
            ## Complexity: Time O(n*log(n)), Space O(n)
            res = k
            c = list(zip(a, b))
            c.sort()
            for (royalty, earn) in c:
                if royalty > res: break
                if earn > royalty:
                    res += earn - royalty
            return res