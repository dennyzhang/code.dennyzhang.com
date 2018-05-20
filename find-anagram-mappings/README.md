# Leetcode: Find Anagram Mappings     :BLOG:Medium:


---

Find Anagram Mappings  

---

Given two lists Aand B, and B is an anagram of A. B is an anagram of A means B is made by randomizing the order of the elements in A.  

We want to find an index mapping P, from A to B. A mapping P[i] = j means the ith element in A appears in B at index j.  

These lists A and B may contain duplicates. If there are multiple answers, output any of them.  

    For example, given
    
    A = [12, 28, 46, 32, 50]
    B = [50, 12, 32, 46, 28]
    We should return
    [1, 4, 3, 2, 0]
    as P[0] = 1 because the 0th element of A appears at B[1], and P[1] = 4 because the 1st element of A appears at B[4], and so on.

Note:  

1.  A, B have equal lengths in range [1, 100].
2.  A[i], B[i] are integers in range [0, 10^5].

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/find-anagram-mappings)  

Credits To: [leetcode.com](https://leetcode.com/problems/find-anagram-mappings/description/)  

Leave me comments, if you have better ways to solve.  

---

    #!/usr/bin/env python
    ## Blog link: https://code.dennyzhang.com/find-anagram-mappings
    ## Basic Ideas: 
    ## Complexity: Time O(n*n), Space O(1)
    ## Assumption: whether I can change B?
    class Solution(object):
        def anagramMappings(self, A, B):
            """
            :type A: List[int]
            :type B: List[int]
            :rtype: List[int]
            """
            length = len(A)
            selected_list = [0] * length
            result = []
            for item in A:
                # print("item: %d" % (item))
                for i in xrange(length):
                    if item == B[i]:
                        result.append(i)
                        B[i] = None
                        break
            return result
    
    # s = Solution()
    # print s.anagramMappings([21,5,74,5,74,21], [21,5,74,74,5,21])