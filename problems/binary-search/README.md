
# Leetcode: Binary Search     :BLOG:Basic:

---

Binary Search  

---

Similar Problems:  

-   Tag: [#binarysearch](https://code.dennyzhang.com/tag/binarysearch)

---

Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search target in nums. If target exists, then return its index, otherwise return -1.  

Example 1:  

    Input: nums = [-1,0,3,5,9,12], target = 9
    Output: 4
    Explanation: 9 exists in nums and its index is 4

Example 2:  

    Input: nums = [-1,0,3,5,9,12], target = 2
    Output: -1
    Explanation: 2 does not exist in nums so return -1

Note:  

1.  You may assume that all elements in nums are unique.
2.  n will be in the range [1, 10000].
3.  The value of each element in nums will be in the range [-9999, 9999].

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/binary-search)  

Credits To: [leetcode.com](https://leetcode.com/problems/binary-search/description/)  

Leave me comments, if you have better ways to solve.  

---

-   Solution:

    // Blog link: https://code.dennyzhang.com/binary-search
    // Basic Ideas:
    // Complexity: Time O(log(n)), Space O(1)
    func search(nums []int, target int) int {
        var m int
        l, r := 0, len(nums)-1
        for l<=r {
    	m = l + (r-l)/2
    	if nums[m] == target { return m }
    	if nums[m] > target {
    	    r = m-1
    	} else {
    	    l = m+1
    	}
        }
        return -1
    }

