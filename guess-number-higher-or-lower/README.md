# Leetcode: Guess Number Higher or Lower     :BLOG:Amusing:


---

Guess number quickly  

---

We are playing the Guess Game. The game is as follows:  

I pick a number from 1 to n. You have to guess which number I picked.  

Every time you guess wrong, I'll tell you whether the number is higher or lower.  

You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):  

    -1 : My number is lower
     1 : My number is higher
     0 : Congrats! You got it!

Example:  

    n = 10, I pick 6.
    
    Return 6.

Credits To: [Leetcode.com](https://leetcode.com/problems/guess-number-higher-or-lower/description/)  

Leave me comments, if you know how to solve.  

    class Solution(object):
        def checkPerfectNumber(self, num):
            """
            :type num: int
            :rtype: bool
            """
            ## Idea: sqrt(num)
            ## Complexity:
            ## Sample Data:
            ##    1 2 7
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

More Reading:  
-   [Kids Puzzles](http://brain.dennyzhang.com/tag/kids/)