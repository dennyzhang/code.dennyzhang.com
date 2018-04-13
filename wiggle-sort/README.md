# Leetcode: Wiggle Sort     :BLOG:Medium:


---

Wiggle Sort  

---

Similar Problems:  
-   [LintCode: Rearrange](https://code.dennyzhang.com/rearrange)
-   [Wiggle Sort II](https://code.dennyzhang.com/wiggle-sort-ii)
-   [Tag: #wigglesort](https://code.dennyzhang.com/tag/wigglesort)

---

    Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....
    
    For example, given nums = [3, 5, 2, 1, 6, 4], one possible answer is [1, 6, 2, 5, 3, 4].

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/wiggle-sort)  

Credits To: [leetcode.com](https://leetcode.com/problems/wiggle-sort/description/)  

Leave me comments, if you have better ways to solve.  

    // Blog link: https://code.dennyzhang.com/wiggle-sort
    // Basic Ideas: Compare current node with the previous node
    // Complexity: Time O(n), Space O(1)
    func wiggleSort(nums []int)  {
        for i := 1; i<len(nums); i++ {
            if i%2 == 1 {
                if nums[i] < nums[i-1] {
                    nums[i-1], nums[i] = nums[i], nums[i-1]
                }
            } else {
                if nums[i] > nums[i-1] {
                    nums[i-1], nums[i] = nums[i], nums[i-1]
                }
            }
        }
    }