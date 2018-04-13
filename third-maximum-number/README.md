# Leetcode: Third Maximum Number     :BLOG:Basic:


---

Third Maximum Number  

---

Similar Problems:  
-   [Review: Heap Problems](https://code.dennyzhang.com/review-heap)
-   [Review: Problems With Many Details](https://code.dennyzhang.com/review-manydetails)
-   Tag: [#manydetails](https://code.dennyzhang.com/tag/manydetails), [#heap](https://code.dennyzhang.com/tag/heap)

---

Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).  

    Example 1:
    Input: [3, 2, 1]
    
    Output: 1
    
    Explanation: The third maximum is 1.

    Example 2:
    Input: [1, 2]
    
    Output: 2
    
    Explanation: The third maximum does not exist, so the maximum (2) is returned instead.

    Example 3:
    Input: [2, 2, 3, 1]
    
    Output: 1
    
    Explanation: Note that the third maximum here means the third maximum distinct number.
    Both numbers with value 2 are both considered as second maximum.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/third-maximum-number)  

Credits To: [leetcode.com](https://leetcode.com/problems/third-maximum-number/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://code.dennyzhang.com/third-maximum-number
    ## Basic Ideas: minheap
    ##
    ## Complexity: O(n), Space O(1)
    import heapq
    class Solution(object):
        def thirdMax(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            q = []
            for num in nums:
                if num not in q:
                    heapq.heappush(q, num)
                if len(q) > 3: heapq.heappop(q)
    
            l = []
            while len(q) != 0:
                l.insert(0, heapq.heappop(q))
            return l[0] if len(l) != 3 else l[-1]
    
    # s = Solution()
    # print s.thirdMax([1, 2]) # 2
    # print s.thirdMax([3, 2, 1]) # 1
    # print s.thirdMax([1, 1, 2]) # 2
    # print s.thirdMax([1,2,2,5,3,5]) # 2