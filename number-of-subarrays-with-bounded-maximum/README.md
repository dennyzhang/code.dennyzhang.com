# Leetcode: Number of Subarrays with Bounded Maximum     :BLOG:Medium:


---

Number of Subarrays with Bounded Maximum  

---

Similar Problems:  
-   [Tag: #subarray](https://brain.dennyzhang.com/tag/subarray)

---

We are given an array A of positive integers, and two positive integers L and R (L <= R).  

Return the number of (contiguous, non-empty) subarrays such that the value of the maximum array element in that subarray is at least L and at most R.  

Example :  

    Input: 
    A = [2, 1, 4, 3]
    L = 2
    R = 3
    Output: 3
    Explanation: There are three subarrays that meet the requirements: [2], [2, 1], [3].

Note:  

-   L, R  and A[i] will be an integer in the range [0, 10^9].
-   The length of A will be in the range of [1, 50000].

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/number-of-subarrays-with-bounded-maximum)  

Credits To: [leetcode.com](https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/number-of-subarrays-with-bounded-maximum
    ## Basic Ideas:
    ##
    ##  Separate by values which is greater than R
    ##
    ## Complexity: Time O(n*n), Space O(1)
    class Solution:
        def numSubarrayBoundedMax(self, A, L, R):
            """
            :type A: List[int]
            :type L: int
            :type R: int
            :rtype: int
            """
            length = len(A)
            myList = []
            res = 0
            for i in range(length+1):
                if i == length:
                    res += self.myNumSubarrayBoundedMax(myList, L)
                else:
                    if A[i] > R:
                        res += self.myNumSubarrayBoundedMax(myList, L)
                        myList = []
                    else:
                        myList.append(A[i])
            return res
    
        def myNumSubarrayBoundedMax(self, myList, L):
            length = len(myList)
            res = 0
            for i in range(length):
                # find the first item which is no smaller than L
                index = -1
                for j in range(i, length):
                    if myList[j] >= L:
                        index = j
                        break
                if index == -1: continue
                res += length-j
            return res
    
    # s = Solution()
    # print(s.numSubarrayBoundedMax([2,9,2,5,6], 2, 8)) # 7