# Leetcode: Circular Array Loop     :BLOG:Amusing:


---

Circular Array Loop  

---

Similar Problems:  
-   Tag: [#inspiring](https://brain.dennyzhang.com/tag/inspiring)

---

You are given an array of positive and negative integers. If a number n at an index is positive, then move forward n steps. Conversely, if it's negative (-n), move backward n steps. Assume the first element of the array is forward next to the last element, and the last element is backward next to the first element. Determine if there is a loop in this array. A loop starts and ends at a particular index with more than 1 element along the loop. The loop must be "forward" or "backward'.  

Example 1: Given the array [2, -1, 1, 2, 2], there is a loop, from index 0 -> 2 -> 3 -> 0.  

Example 2: Given the array [-1, 2], there is no loop.  

Note: The given array is guaranteed to contain no element "0".  

Can you do it in O(n) time complexity and O(1) space complexity?  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/circular-array-loop)  

Credits To: [leetcode.com](https://leetcode.com/problems/circular-array-loop/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/circular-array-loop
    ## Basic Ideas: Loop from left to right
    ##        For current check, mark all visited element as 0
    ##        If the next candidate position is 0, we get a loop
    ##        If the previous element is not current element, the loop has more than 1 element.
    ##
    ## Sample Data: [1, -1] can't be a valid loop. 
    ##      Yes, it has 2 elements. But it should have only one direction. "forward" or "backward"
    ##
    ## Complexity: Time O(n), Space O(1)
    class Solution(object):
        def circularArrayLoop(self, nums):
            """
            :type nums: List[int]
            :rtype: bool
            """
            length = len(nums)
            if length <= 1: return False
            for i in range(0, length):
                # skip the checked elements
                if nums[i] == 0: continue
                # check current path
                k = i
                while nums[k] != 0:
                    print nums
                    prev = k
                    nums[k], k = 0, (k+nums[k]+length)%length
                if prev != k: return True
            return False
    
    # s = Solution()
    # print(s.circularArrayLoop([-2, 1, -1, -2, -2])) # False
    # print(s.circularArrayLoop([2, -1, 1, 2, 2])) # True
    # print(s.circularArrayLoop([-1, 2])) # False