# Leetcode: Next Greater Element I     :BLOG:Medium:


---

Next Greater Element I  

---

Similar Problems:  
-   [Leetcode: Daily Temperatures](https://brain.dennyzhang.com/daily-temperatures)
-   Tag: [monotone](https://brain.dennyzhang.com/tag/monotone)

---

You are given two arrays (without duplicates) nums1 and nums2 where nums1's elements are subset of nums2. Find all the next greater numbers for nums1's elements in the corresponding places of nums2.  

The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, output -1 for this number.  

    Example 1:
    Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
    Output: [-1,3,-1]
    Explanation:
        For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
        For number 1 in the first array, the next greater number for it in the second array is 3.
        For number 2 in the first array, there is no next greater number for it in the second array, so output -1.

    Example 2:
    Input: nums1 = [2,4], nums2 = [1,2,3,4].
    Output: [3,-1]
    Explanation:
        For number 2 in the first array, the next greater number for it in the second array is 3.
        For number 4 in the first array, there is no next greater number for it in the second array, so output -1.

Note:  
1.  All elements in nums1 and nums2 are unique.
2.  The length of both nums1 and nums2 would not exceed 1000.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/next-greater-element-i)  

Credits To: [leetcode.com](https://leetcode.com/problems/next-greater-element-i/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/next-greater-element-i
    ## Basic Ideas: Descending stack
    ##
    ## Complexity: Time O(n), Space O(n)
    class Solution(object):
        def nextGreaterElement(self, findNums, nums):
            """
            :type findNums: List[int]
            :type nums: List[int]
            :rtype: List[int]
            """
            length = len(nums)
            index_list = [-1]*length
            stack = []
            for i in xrange(length):
                # If nums[i] is bigger than the top of stack, 
                #  it's the next bigger number of the stack top
                while len(stack) != 0 and nums[i]>nums[stack[-1]]:
                    k = stack.pop()
                    index_list[k] = i
                stack.append(i)
    
            # get the result
            res = []
            m = {} # the length of nums2 won't exceed 1000
            for i in xrange(length):
                m[nums[i]] = i
            for num in findNums:
                index = m[num]
                next_big_index = index_list[index]
                if next_big_index != -1:
                    res.append(nums[next_big_index])
                else:
                    res.append(-1)
            return res