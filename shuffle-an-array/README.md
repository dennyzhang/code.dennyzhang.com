# Leetcode: Shuffle an Array     :BLOG:Medium:


---

Shuffle an Array  

---

Similar Problems:  
-   Tag: [#designquestion](https://brain.dennyzhang.com/tag/designquestion)

---

Shuffle a set of numbers without duplicates.  

Example:  

    // Init an array with set 1, 2, and 3.
    int nums = {1,2,3};
    Solution solution = new Solution(nums);
    
    // Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
    solution.shuffle();
    
    // Resets the array back to its original configuration [1,2,3].
    solution.reset();
    
    // Returns the random shuffling of array [1,2,3].
    solution.shuffle();

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/shuffle-an-array)  

Credits To: [leetcode.com](https://leetcode.com/problems/shuffle-an-array/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/shuffle-an-array
    ## Basic Ideas:
    ##        What if nums only has 0 or 1 element?
    ##
    ## Complexity: Time ?, Space O(n)
    
    import copy
    import random
    class Solution:
    
        def __init__(self, nums):
            """
            :type nums: List[int]
            """
            self.length = len(nums)
            self.nums = nums
            self.original = copy.deepcopy(nums)
    
        def reset(self):
            """
            Resets the array to its original configuration and return it.
            :rtype: List[int]
            """
            if self.length <= 1: return self.original
            self.nums = copy.deepcopy(self.original)
            return self.nums
    
        def shuffle(self):
            """
            Returns a random shuffling of the array.
            :rtype: List[int]
            """
            if self.length <= 1: return self.original
    
            # How to map value to nums[i] and num[j]? What is the time complexity?
            max_value = (self.length*(self.length-1))/2
            random_v = random.randint(1, max_value)
            v, i = 0, 0
            while i < self.length-1:
                v = v + (self.length-1-i)
                if v >= random_v: break
                i += 1
    
            # revert
            v = random_v - (v - (self.length-1-i))
            j = v+i
    
            # swap nums[i] and nums[j]
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
            return self.nums