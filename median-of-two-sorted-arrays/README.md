# Leetcode: Median of Two Sorted Arrays     :BLOG:Amusing:


---

Median of Two Sorted Arrays  

---

Similar Problems:  
-   Tag: [getmedian](https://code.dennyzhang.com/tag/getmedian)

---

There are two sorted arrays nums1 and nums2 of size m and n respectively.  

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).  

    Example 1:
    nums1 = [1, 3]
    nums2 = [2]
    
    The median is 2.0

    Example 2:
    nums1 = [1, 2]
    nums2 = [3, 4]
    
    The median is (2 + 3)/2 = 2.5

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/median-of-two-sorted-arrays)  

Credits To: [leetcode.com](https://leetcode.com/problems/median-of-two-sorted-arrays/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://code.dennyzhang.com/median-of-two-sorted-arrays
    ## Basic Ideas: merge 2 sorted array to one, find 2 values
    ## Complexity: O(m+n)
    class Solution(object):
        def findMedianSortedArrays(self, nums1, nums2):
            """
            :type nums1: List[int]
            :type nums2: List[int]
            :rtype: float
            """
            m = len(nums1)
            n = len(nums2)
            nums3 = [0] * (m+n)
            i = 0
            j = 0
            k = 0
            while i<m and j<n:
                if nums1[i] <nums2[j]:
                    nums3[k] = nums1[i]
                    k += 1
                    i += 1
                else:
                    nums3[k] = nums2[j]
                    k += 1
                    j += 1
    
            while i<m:
                nums3[k] = nums1[i]
                k += 1
                i += 1
    
            while j<n:
                nums3[k] = nums2[j]
                k += 1
                j += 1
    
            ret = -1
            if (m+n)%2 == 1:
                ret = float(nums3[(m+n-1)/2])
            else:
                ret = float(nums3[(m+n)/2-1] + nums3[(m+n)/2])/2
            return ret
    
    # s = Solution()
    # print s.findMedianSortedArrays([1, 3], [2])
    # print s.findMedianSortedArrays([1, 2], [3, 4])