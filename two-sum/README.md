# Leetcode: Two Sum     :BLOG:Numbers:


---

Pic 2 numbers to get the target sum.  

---

Given an array of integers, return **indices** of the two numbers such that they add up to a specific target.  

You may assume that each input would have **exactly** one solution, and you may not use the same element twice.  

Example:  

    Given nums = [2, 7, 11, 15], target = 9,
    
    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].

Blog link: <http://brain.dennyzhang.com/two-sum>  

Github: challenges-leetcode-interesting  

Credits To: leetcode.com  

Leave me comments, if you know how to solve.  

    ## Basic Ideas: sort the array, and two pointers. 1. From left to right, 2. From right to left
    ## Complexity: Time O(n), Space O(1)
    class Solution(object):
        def twoSum(self, nums, target):
            """
            :type nums: List[int]
            :type target: int
            :rtype: List[int]
            """
            nums2 = sorted(nums)
            i = 0
            j = len(nums2)-1
            has_matched = False
            while i<j:
                current_sum = nums2[i]+nums2[j]
                if current_sum == target:
                    has_matched = True
                    break
                elif current_sum > target:
                    j -= 1
                else:
                    i += 1
    
                # avoid point to the same location
                if i == j:
                    i += 1
    
            if has_matched is True:
                value1 = nums2[i]
                value2 = nums2[j]
    
                index1 = None
                index2 = None
                for i in range(0, len(nums)):
                    if nums[i] == value1 and index1 is None:
                        index1 = i
                    else:
                        if nums[i] == value2 and index2 is None:
                            index2 = i
    
                return [index1, index2]
            else:
                return [None, None]
    
    if __name__ == '__main__':
        s = Solution()
        print s.twoSum([3, 2, 4], 6)
        print s.twoSum([1, 2, 3], 5)
        print s.twoSum([2, 7, 11, 15], 9)

More Reading:  
-   [[<http://brain.dennyzhang.com/two-sum>