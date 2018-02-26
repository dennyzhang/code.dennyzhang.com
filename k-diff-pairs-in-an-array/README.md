# Leetcode: K-diff Pairs in an Array     :BLOG:Basic:


---

K-diff Pairs in an Array  

---

Similar Problems:  
-   [3Sum](https://brain.dennyzhang.com/3sum)
-   [Review: TwoPointers Problems](https://brain.dennyzhang.com/review-twopointer)

---

Given an array of integers and an integer k, you need to find the number of unique k-diff pairs in the array. Here a k-diff pair is defined as an integer pair (i, j), where i and j are both numbers in the array and their absolute difference is k.  

Example 1:  

    Input: [3, 1, 4, 1, 5], k = 2
    Output: 2
    Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
    Although we have two 1s in the input, we should only return the number of unique pairs.

Example 2:  

    Input:[1, 2, 3, 4, 5], k = 1
    Output: 4
    Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).

Example 3:  

    Input: [1, 3, 1, 5, 4], k = 0
    Output: 1
    Explanation: There is one 0-diff pair in the array, (1, 1).

Note:  
1.  The pairs (i, j) and (j, i) count as the same pair.
2.  The length of the array won't exceed 10,000.
3.  All the integers in the given input belong to the range: [-1e7, 1e7].

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/k-diff-pairs-in-an-array)  

Credits To: [leetcode.com](https://leetcode.com/problems/k-diff-pairs-in-an-array/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/k-diff-pairs-in-an-array
    class Solution:
        ## Basic Ideas: Hashmap
        ## Complexity: Time O(n), Space O(n)
        def findPairs(self, nums, k):
            """
            :type nums: List[int]
            :type k: int
            :rtype: int
            """
            if k < 0: return 0
            import collections
            d = collections.defaultdict(lambda: 0)
            for num in nums: d[num] += 1
    
            res = 0
            for num in d:
                if k == 0:
                    if d[num] >= 2: res += 1
                else:
                    if num+k in d and d[num+k] >= 1: res += 1
            return res
    
        ## Basic Ideas: Two pointer
        ##
        ## Complexity: Time O(n*log(n)), Space O(1)
        def findPairs_v1(self, nums, k):
            """
            :type nums: List[int]
            :type k: int
            :rtype: int
            """
            nums.sort()
            length = len(nums)
            if length <= 1: return 0
            if k == 0:
                res = 0
                for i in range(0, length-1):
                    # skip duplicate
                    if i != 0 and nums[i] == nums[i-1]: continue
                    if nums[i] == nums[i+1]: res += 1
                return res
            else:
                res, left = 0, 0
                for right in range(1, length):
                    if nums[right] == nums[right-1]: continue
                    # If distance too big
                    while left < right and nums[right]-nums[left] > k:
                        left += 1
    
                    # skip duplicate
                    while left+1 < right and nums[left]==nums[left+1]:
                        left += 1
    
                    # get one candidate
                    if left < right and nums[right]-nums[left] == k:
                        res += 1
    
                return res