# Leetcode: Remove Duplicates from Sorted Array II     :BLOG:Medium:


---

Remove Duplicates from Sorted Array II  

---

Similar Problems:  
-   [Review: Problems With Many Details](https://code.dennyzhang.com/review-manydetails)
-   Tag: [#manydetails](https://code.dennyzhang.com/tag/manydetails)

---

Follow up for "Remove Duplicates":  
What if duplicates are allowed at most twice?  

For example,  
Given sorted array nums = [1,1,1,2,2,3],  

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/remove-duplicates-from-sorted-array-ii)  

Credits To: [leetcode.com](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/remove-duplicates-from-sorted-array-ii
    ## Basic Ideas: compare v with the last 2nd element in the result
    ##              sliding window
    ##       1 1 1 2 2 3
    ## Complexity:
    class Solution(object):
        def removeDuplicates(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            i = 0
            for n in nums:
                if i < 2 or n > nums[i-2]:
                    nums[i] = n
                    i += 1
            return i
    
        ## Blog link: https://code.dennyzhang.com/remove-duplicates-from-sorted-array-ii
    ## Basic Ideas: Track previous element
        ##       duplicate_count: how many duplicate current element has appeared
        ##       previous_element
        def removeDuplicates_v1(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            length = len(nums)
            if length <= 1:
                return length
    
            index = 0
            duplicate_count, previous_element = 0, nums[0]
            for i in range(1, length):
                if nums[i] == previous_element:
                    duplicate_count += 1
                    continue
    
                # update list
                if duplicate_count == 0:
                    nums[index] = previous_element
                    index += 1
                else:
                    nums[index] = previous_element
                    index += 1
                    nums[index] = previous_element
                    index += 1
                previous_element = nums[i]
                duplicate_count = 0
    
            # update the last one
            if duplicate_count == 0:
                nums[index] = nums[-1]
                index += 1
            else:
                nums[index] = nums[-1]
                index += 1
                nums[index] = nums[-1]
                index += 1
            # print nums
            return index
    
    # s = Solution()
    # print s.removeDuplicates([1,1,1,2,2,3]) # 1, 1, 2, 2, 3
    # print s.removeDuplicates([1,1,1,2,2,3,3]) # 1, 1, 2, 2, 3, 3
    # print s.removeDuplicates([1, 1]) # 1