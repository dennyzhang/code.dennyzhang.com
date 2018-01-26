# Leetcode: Jump Game     :BLOG:Basic:


---

Jump Game  

---

Given an array of non-negative integers, you are initially positioned at the first index of the array.  

Each element in the array represents your maximum jump length at that position.  

Determine if you are able to reach the last index.  

For example:  
A = [2,3,1,1,4], return true.  

A = [3,2,1,0,4], return false.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/jump-game)  

Credits To: [leetcode.com](https://leetcode.com/problems/jump-game/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/jump-game
    ## Basic Ideas: Greedy
    ##            maxIndex: the maximum index we can jump
    ##            We check from left to right, thus we won't need to move back
    ## Complexity:
    class Solution(object):
        def canJump(self, nums):
            """
            :type nums: List[int]
            :rtype: bool
            """
            length = len(nums)
            if length == 0:
                return None
    
            maxIndex = 0
            for i in xrange(length):
                # We can't move any further, or already reach the target
                if (i > maxIndex) or (maxIndex >= length -1):
                    break
                maxIndex = max(maxIndex, i+nums[i])
    
            return (maxIndex >= length -1)
    
    s = Solution()
    print s.canJump([2,3,1,1,4]) # true
    print s.canJump([3,2,1,0,4]) # false