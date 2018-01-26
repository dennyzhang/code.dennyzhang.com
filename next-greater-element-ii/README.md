# Leetcode: Next Greater Element II     :BLOG:Medium:


---

Next Greater Element II  

---

Similar Problems:  
-   [Leetcode: Leetcode: Next Greater Element I](https://brain.dennyzhang.com/next-greater-element-i)
-   Tag: [#monotonestack](https://brain.dennyzhang.com/tag/monotonestack)

---

Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.  

    Example 1:
    Input: [1,2,1]
    Output: [2,-1,2]
    Explanation: The first 1's next greater number is 2; 
    The number 2 can't find next greater number; 
    The second 1's next greater number needs to search circularly, which is also 2.

Note: The length of given array won't exceed 10000.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/next-greater-element-ii)  

Credits To: [leetcode.com](https://leetcode.com/problems/next-greater-element-ii/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/next-greater-element-ii
    ## Basic Idea: Descending stack
    ##
    ## Complexity: Time O(n), Space O(n)
    class Solution(object):
        def nextGreaterElements(self, nums):
            """
            :type nums: List[int]
            :rtype: List[int]
            """
            length = len(nums)
            stack = []
            res = [None]*length
            for i in xrange(length*2):
                i = i % length
                # if current element is bigger, it's the target of previous undecided elements
                while len(stack) != 0 and nums[i] > nums[stack[-1]]:
                    k = stack.pop()
                    res[k] = nums[i]
                # No need to check if already examined
                if res[i] is None:
                    stack.append(i)
    
            for i in xrange(length):
                if res[i] is None: res[i] = -1
            return res