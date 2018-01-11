# Leetcode: Find Minimum in Rotated Sorted Array     :BLOG:Medium:


---

Find Minimum in Rotated Sorted Array  

---

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.  

    (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.  

You may assume no duplicate exists in the array.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/find-minimum-in-rotated-sorted-array)  

Credits To: [Leetcode.com](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/)  

Leave me comments, if you know how to solve.  

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
                mid = left + (right-left)/2
                v = guess(mid)
                if v == 0:
                    return mid
                elif v == 1:
                    left = mid + 1
                else:
                    right = mid - 1
    
            return None