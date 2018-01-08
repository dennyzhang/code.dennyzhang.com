#!/usr/bin/env python
##-------------------------------------------------------------------
## @copyright 2017 brain.dennyzhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: test.py
## Author : Denny <http://brain.dennyzhang.com/contact>
## Tags: #redo, #list
## Description:
##     https://leetcode.com/contest/weekly-contest-66/problems/find-anagram-mappings/
##    ,-----------
##    | Given two lists Aand B, and B is an anagram of A. B is an anagram of A means B is made by randomizing the order of the elements in A.
##    | 
##    | We want to find an index mapping P, from A to B. A mapping P[i] = j means the ith element in A appears in B at index j.
##    | 
##    | These lists A and B may contain duplicates. If there are multiple answers, output any of them.
##    | 
##    | For example, given
##    | 
##    | A = [12, 28, 46, 32, 50]
##    | B = [50, 12, 32, 46, 28]
##    | We should return
##    | [1, 4, 3, 2, 0]
##    | as P[0] = 1 because the 0th element of A appears at B[1], and P[1] = 4 because the 1st element of A appears at B[4], and so on.
##    | Note:
##    | 
##    | A, B have equal lengths in range [1, 100].
##    | A[i], B[i] are integers in range [0, 10^5].
##    `-----------
##    
## --
## Created : <2017-10-16>
## Updated: Time-stamp: <2017-10-24 17:21:30>
##-------------------------------------------------------------------
#!/usr/bin/env python
class Solution(object):
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        ## Basic Idea: 
        ## Complexity: Time O(n*n), Space O(1)
        ## Assumption: whether I can change B?
        length = len(A)
        selected_list = [0] * length
        result = []
        for item in A:
            print("item: %d" % (item))
            for i in xrange(length):
                if item == B[i]:
                    result.append(i)
                    B[i] = None
                    break
        return result

# s = Solution()
# print s.anagramMappings([21,5,74,5,74,21], [21,5,74,74,5,21])
