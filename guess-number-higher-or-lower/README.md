# Leetcode: Guess Number Higher or Lower     :BLOG:Amusing:


---

Guess number quickly  

---

Similar Problems:  
-   [Review: Game Problems](https://code.dennyzhang.com/review-game), [Tag: #game](https://code.dennyzhang.com/tag/game)

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

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/guess-number-higher-or-lower)  

Credits To: [leetcode.com](https://leetcode.com/problems/guess-number-higher-or-lower/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/guess-number-higher-or-lower
    ## Basic Ideas: binary search
    ##      1 1 1 0 -1 -1 -1
    ## Complexity: Time O(log(n)), Space O(1)
    
    # The guess API is already defined for you.
    # @param num, your guess
    # @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
    # def guess(num):
    
    class Solution(object):
        def guessNumber(self, n):
            """
            :type n: int
            :rtype: int
            """
            left, right = 1, n
            while left <= right:
                mid = int(left + (right-left)/2)
                v = guess(mid)
                if v == 0:
                    return mid
                elif v == 1:
                    left = mid + 1
                else:
                    right = mid - 1
            return None