# Leetcode: Kth Largest Element in an Array     :BLOG:Basic:


---

Kth Largest Element in an Array  

---

Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.  
For example,  
Given [3,2,1,5,6,4] and k = 2, return 5.  

Note:  
You may assume k is always valid, 1 <= k <= array's length.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/kth-largest-element-in-an-array)  

Credits To: [leetcode.com](https://leetcode.com/problems/kth-largest-element-in-an-array/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: http://brain.dennyzhang.com/kth-largest-element-in-an-array
    ## Basic Ideas: heap
    ##
    ## Complexity: Time O(n*log(n)), Space O(n)
    import heapq
    class Solution(object):
        def findKthLargest(self, nums, k):
            """
            :type nums: List[int]
            :type k: int
            :rtype: int
            """
            q = []
            for num in nums: heapq.heappush(q, num)
            return heapq.nlargest(k, q)[-1]
    
    s = Solution()
    print s.findKthLargest([3,2,1,5,6,4], 2) # 5