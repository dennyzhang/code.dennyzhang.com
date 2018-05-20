# Leetcode: Random Pick Index     :BLOG:Medium:


---

Random Pick Index  

---

Similar Problems:  
-   Tag: [#reservoirsampling](https://code.dennyzhang.com/tag/reservoirsampling)

---

Given an array of integers with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.  

Note:  
The array size can be very large. Solution that uses too much extra space will not pass the judge.  

Example:  

    int[] nums = new int[] {1,2,3,3,3};
    Solution solution = new Solution(nums);
    
    // pick(3) should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
    solution.pick(3);
    
    // pick(1) should return 0. Since in the array only nums[0] is equal to 1.
    solution.pick(1);

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/random-pick-index)  

Credits To: [leetcode.com](https://leetcode.com/problems/random-pick-index/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/random-pick-index
    ## Basic Ideas: Reservior Sampling
    ##
    ## Complexity: Time O(n), Space O(1)
    import random
    class Solution:
    
        def __init__(self, nums):
            """
            :type nums: List[int]
            """
            self.nums = nums
    
        def pick(self, target):
            """
            :type target: int
            :rtype: int
            """
            i, count, res = 0, 0, -1
            for i in range(0, len(self.nums)):
                if self.nums[i] == target:
                    res = i
                    count += 1
                    break
    
            for i in range(res+1, len(self.nums)):
                if self.nums[i] == target:
                    count += 1
                    random_v = random.randint(1, count)
                    if random_v == 1:
                        res = i
            return res
    
    # Your Solution object will be instantiated and called as such:
    # obj = Solution(nums)
    # param_1 = obj.pick(target)