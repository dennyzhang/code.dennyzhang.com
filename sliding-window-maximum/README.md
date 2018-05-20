# Leetcode: Sliding Window Maximum     :BLOG:Basic:


---

Sliding Window Maximum  

---

Similar Problems:  
-   [Min Stack](https://code.dennyzhang.com/min-stack)
-   [Review: Monotone Stack Or Monotone Queue Problems](https://code.dennyzhang.com/review-monotone), Tag: [monotone](https://code.dennyzhang.com/tag/monotone)

---

Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.  

For example,  

    Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.
    
    Window position                Max
    ---------------               -----
    [1  3  -1] -3  5  3  6  7       3
     1 [3  -1  -3] 5  3  6  7       3
     1  3 [-1  -3  5] 3  6  7       5
     1  3  -1 [-3  5  3] 6  7       5
     1  3  -1  -3 [5  3  6] 7       6
     1  3  -1  -3  5 [3  6  7]      7
    Therefore, return the max sliding window as [3,3,5,5,6,7].

Note:  
You may assume k is always valid, ie: 1 <= k <= input array's size for non-empty array.  

Follow up:  
Could you solve it in linear time?  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/sliding-window-maximum)  

Credits To: [leetcode.com](https://leetcode.com/problems/sliding-window-maximum/description/)  

Leave me comments, if you have better ways to solve.  

---

Useful link: [monotonic queue problem](https://leetcode.com/problems/sliding-window-maximum/discuss/65885/This-is-a-typical-monotonic-queue-problem)  

    ## Blog link: https://code.dennyzhang.com/sliding-window-maximum
    ## Basic Ideas: sliding window with decreasing sequence
    ##
    ## Complexity: Time O(n), Space O(k)
    class Solution:
        def maxSlidingWindow(self, nums, k):
            """
            :type nums: List[int]
            :type k: int
            :rtype: List[int]
            """
            import collections
            res = []
            queue = collections.deque()
            for i in range(len(nums)):
                # remove the number
                if len(queue)!=0 and queue[0] == i-k:
                    queue.popleft()
    
                # keep the window decreasing
                while len(queue) != 0 and nums[i] >= nums[queue[-1]]:
                    queue.pop()
    
                # we need to add the new number in all cases
                queue.append(i)
    
                # already have k numbers
                if i >= k-1: res.append(nums[queue[0]])
            return res