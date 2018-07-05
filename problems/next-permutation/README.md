# Leetcode: Next Permutation     :BLOG:Medium:


---

Next Permutation  

---

Similar Problems:  
-   [Permutation Sequence](https://code.dennyzhang.com/permutation-sequence)
-   [Review: Combinations and Permutations Problems](https://code.dennyzhang.com/review-combination)
-   Tag: [#combination](https://code.dennyzhang.com/tag/combination)

---

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.  

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).  

The replacement must be in-place, do not allocate extra memory.  

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.  

    1,2,3 -> 1,3,2
    3,2,1 -> 1,2,3
    1,1,5 -> 1,5,1

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/next-permutation)  

Credits To: [leetcode.com](https://leetcode.com/problems/next-permutation/description/)  

Leave me comments, if you have better ways to solve.  

---

---

Related Readings:  
-   [Next lexicographical permutation algorithm](https://www.nayuki.io/page/next-lexicographical-permutation-algorithm)
-   [Wikipedia:Permutation](https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order)

![img](//raw.githubusercontent.com/DennyZhang/images/master/code/next-permutation-algorithm.png)  

    // Blog link: https://code.dennyzhang.com/next-permutation
    // Basic Ideas:
    //   1. From right to left, find the longest non-increasing subsequence
    //   2. Swap items
    //   3. Reverse the subsequence
    //
    //   0 1 2 5 3 3 0
    //   0 1 3 5 3 2 0
    //   0 1 3 0 2 3 5
    // Complexity:
    func nextPermutation(nums []int)  {
        if len(nums) == 0 {
            return
        }
        var i = len(nums) - 2
        for ; i>=0; i-- {
            if nums[i] < nums[i+1] {
                break
            }
        }
        if i == -1 {
            sort.Ints(nums)
            return
        }
        var index = i
        // find element to swap
        i = len(nums) - 1
        for ; i>=0; i-- {
            if nums[i] > nums[index] {
                break
            }
        }
        nums[i], nums[index] = nums[index], nums[i]
        // reverse
        var l, r = index+1, len(nums)-1
        for l<r {
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l+1, r-1
        }
    }