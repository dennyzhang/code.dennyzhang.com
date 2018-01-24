# Leetcode: Non-decreasing Array     :BLOG:Numbers:


---

Modify one element to make array non-decreasing  

---

Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.  

We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).  

Example 1:  

    Input: [4,2,3]
    Output: True
    
    Explanation: You could modify the first 
    4
     to 
    1
     to get a non-decreasing array.

Example 2:  

    Input: [4,2,1]
    Output: False

Explanation: You can't get a non-decreasing array by modify at most one element.  
Note: The n belongs to [1, 10,000].  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/non-decreasing-array)  

Credits To: [leetcode.com](https://leetcode.com/problems/non-decreasing-array/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: http://brain.dennyzhang.com/non-decreasing-array
    ## Basic Ideas: If we have two decreasing couples, we can't fix it with one change. Right?
    ## Complexity: Time O(n), Space O(1)
    ##  1     4         2       3
    ##      index1   index2
    class Solution(object):
        def checkPossibility(self, nums):
            """
            :type nums: List[int]
            :rtype: bool
            """
            index1 = None
            index2 = None
            length = len(nums)
            for i in range(0, length - 1):
                if nums[i] > nums[i+1]:
                    if index1 is not None:
                        # already one decreasing
                        return False
                    index1 = i
                    index2 = i+1
    
            # print("index1: %d, index2: %d" % (index1, index2))
            if index1 is None:
                # no decreasing 
                return True
    
            ret = False
            if index2 == length -1:
                # last item
                ret = True
            elif index1 == 0:
                # first item
                ret = True
            else:
                #                 index1
                #                                   (index2+1)
                #   (index1-1)          
                #                          index2       
                #
                if nums[index1] <= nums[index2+1]:
                    # only change index2
                    ret = True
                if nums[index2] >= nums[index1-1]:
                    # only change index1
                    ret = True
            return ret
    
    if __name__ == '__main__':
        s = Solution()
        print s.checkPossibility([4,2,3])
        print s.checkPossibility([4,2,1])
        print s.checkPossibility([4])