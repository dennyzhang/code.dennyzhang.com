# Leetcode: Shuffle an Array     :BLOG:Medium:


---

Shuffle an Array  

---

Similar Problems:  
-   [Review: Object-Oriented Design Problems](https://brain.dennyzhang.com/review-oodesign), Tag: [oodesign](https://brain.dennyzhang.com/tag/oodesign)

---

Shuffle a set of numbers without duplicates.  

Example:  

    // Init an array with set 1, 2, and 3.
    int[] nums = {1,2,3};
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
    ## Basic Ideas: Fisher–Yates shuffle
    ##        What if nums only has 0 or 1 element?
    ##
    ##        What if you generate a value, and map it into nums[i] and num[j]. Then swap these two?
    ##        This won't work. Because the original combination will never be returned by shuffle() function.
    ##
    ## Complexity: Time O(n), Space O(n)
    
    import copy
    import random
    class Solution:
    
        def __init__(self, nums):
            """
            :type nums: List[int]
            """
            self.nums = nums
            self.original = copy.deepcopy(nums)
    
        def reset(self):
            """
            Resets the array to its original configuration and return it.
            :rtype: List[int]
            """
            return self.original
    
        def shuffle(self):
            """
            Returns a random shuffling of the array.
            :rtype: List[int]
            """
            for j in range(len(self.nums)-1, 0, -1):
                i = random.randint(0, j)
                self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
            return self.nums