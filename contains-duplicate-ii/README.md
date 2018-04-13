# Leetcode: Contains Duplicate II     :BLOG:Medium:


---

Contains Duplicate II  

---

Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/contains-duplicate-ii)  

Credits To: [leetcode.com](https://leetcode.com/problems/contains-duplicate-ii/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://code.dennyzhang.com/contains-duplicate-ii
    ## Basic Ideas: sliding window
    ##              Keep a window of k+1 elements. Maintain a Set with the window
    ##              Move the window towards the end.
    ##              If found an existing
    ##
    ## Complexity: Time O(n), Space O(k)
    class Solution(object):
        def containsNearbyDuplicate(self, nums, k):
            """
            :type nums: List[int]
            :type k: int
            :rtype: bool
            """
            length = len(nums)
            if length <= 1: return False
            if k == 0: return False
            s = set([])
    
            for i in xrange(length):
                if i > k:
                    # sliding window shall have k+1 element
                    s.remove(nums[i-k-1])
                if nums[i] in s:
                    return True
                s.add(nums[i])
            return False
    
    # s = Solution()
    # print s.containsNearbyDuplicate([-1, -1], 1) # True
    # print s.containsNearbyDuplicate([99, 99], 1) # True
    # print s.containsNearbyDuplicate([1, 2, 1], 0) # False