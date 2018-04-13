# Leetcode: Can Place Flowers     :BLOG:Amusing:


---

Can Place Flowers  

---

Similar Problems:  
-   [Review: Game Problems](https://code.dennyzhang.com/review-game)
-   [Review: Problems With Many Details](https://code.dennyzhang.com/review-manydetails)
-   Tag: [#manydetails](https://code.dennyzhang.com/tag/manydetails), [#game](https://code.dennyzhang.com/tag/game)

---

Suppose you have a long flowerbed in which some of the plots are planted and some are not. However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.  

Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.  

    Example 1:
    Input: flowerbed = [1,0,0,0,1], n = 1
    Output: True

    Example 2:
    Input: flowerbed = [1,0,0,0,1], n = 2
    Output: False

Note:  
1.  The input array won't violate no-adjacent-flowers rule.
2.  The input array size is in the range of [1, 20000].
3.  n is a non-negative integer which won't exceed the input array size.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/can-place-flowers)  

Credits To: [leetcode.com](https://leetcode.com/problems/can-place-flowers/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://code.dennyzhang.com/can-place-flowers
    ## Basic Ideas: Find consecutive 0s
    ##              For a range of n 0s
    ##                  If the range in the middle, we can place (n-1)/2 flowers
    ##              Add a virtual '0' to the head, add a virtual '0' and '1' to the end
    ##
    ## Complexity: Time O(n), Space O(1)
    class Solution(object):
        def canPlaceFlowers(self, flowerbed, n):
            """
            :type flowerbed: List[int]
            :type n: int
            :rtype: bool
            """
            total_flower, counter = 0, 0
            length = len(flowerbed)
            for i in range(-1, length+2):
                if i == -1 or i == length: num = 0
                elif i == length + 1:
                    num = 1
                else:
                    num = flowerbed[i]
    
                # caculate how many flowers we can plant
                if num == 0: counter += 1
                else: total_flower, counter = total_flower + (counter-1)/2, 0
            return total_flower >= n
    
    # s = Solution()
    # s = s.canPlaceFlowers([0,0,1,0,1], 1) # true