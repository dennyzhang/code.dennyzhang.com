#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 brain.dennyzhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <http://brain.dennyzhang.com/contact>
## Tags: #redo, #amusing
## Description:
##     https://leetcode.com/problems/rotate-array/description/
##    ,-----------
##    | Rotate an array of n elements to the right by k steps.
##    | 
##    | For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].
##    | 
##    | Note:
##    | Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
##    | 
##    | [show hint]
##    | 
##    | Related problem: Reverse Words in a String II
##    | 
##    | Credits:
##    | Special thanks to @Freezen for adding this problem and creating all test cases.
##    `-----------
##
## Basic Idea:
## Complexity:
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-23 18:22:04>
##-------------------------------------------------------------------
class Solution(object):
    def rotate(self, nums, k):
        # self.rotate_1(nums, k)
        # self.rotate_2(nums, k)
        self.rotate_3(nums, k)

    # O(n) extra space
    def rotate_1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if k<=0:
            return
        length = len(nums)
        k = k % length
        if k == 1 and length == 1:
            return
        nums2 = [0] * length
        for i in range(0, length):
            nums2[(i+k) % length] = nums[i]
        for i in range(0, length):
            nums[i] = nums2[i]

    # O(k) extra space:
    # get a tmp array of k items, in order to get extra space, then shift right.
    def rotate_2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if k<=0:
            return
        length = len(nums)
        k = k % length
        if k == 1 and length == 1:
            return
        tmp_list = [0]*k
        j = 0
        for i in range(length-k, length):
            tmp_list[j] = nums[i]
            j += 1

        for i in range(length-1, k-1, -1):
            nums[i] = nums[i-k]

        for i in range(0, k):
            nums[i] = tmp_list[i]

    # O(1) extra space
    def rotate_3(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if k<=0:
            return
        length = len(nums)
        k = k % length
        if k == 1 and length == 1:
            return

        for i in range(0, k):
            j = i

            tmp_value = None
            while j < length:
                next_index = (j+k) % length
                if tmp_value is None:
                    tmp_value = nums[next_index]
                    nums[next_index] = nums[j]
                else:
                    # swap value
                    tmp_value2 = nums[next_index]
                    nums[next_index] = tmp_value
                    tmp_value = tmp_value2
                j = j + k

if __name__ == '__main__':
    s = Solution()
    s.rotate([1,2,3,4,5,6,7], 3)
    s.rotate([-1], 2)
## File: test.py ends
