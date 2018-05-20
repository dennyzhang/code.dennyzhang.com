# Leetcode: Maximum Distance in Arrays     :BLOG:Basic:


---

Maximum Distance in Arrays  

---

Similar Problems:  
-   [Range Addition](https://code.dennyzhang.com/range-addition)
-   [Review: Problems With Many Details](https://code.dennyzhang.com/review-manydetails)
-   Tag: [#manydetails](https://code.dennyzhang.com/tag/manydetails), [#inspiring](https://code.dennyzhang.com/tag/inspiring)

---

Given m arrays, and each array is sorted in ascending order. Now you can pick up two integers from two different arrays (each array picks one) and calculate the distance. We define the distance between two integers a and b to be their absolute difference |a-b|. Your task is to find the maximum distance.  

Example 1:  

    Input: 
    [[1,2,3],
     [4,5],
     [1,2,3]]
    Output: 4
    Explanation: 
    One way to reach the maximum distance 4 is to pick 1 in the first or third array and pick 5 in the second array.

Note:  
1.  Each given array will have at least 1 number. There will be at least two non-empty arrays.
2.  The total number of the integers in all the m arrays will be in the range of [2, 10000].
3.  The integers in the m arrays will be in the range of [-10000, 10000].

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/maximum-distance-in-arrays)  

Credits To: [leetcode.com](https://leetcode.com/problems/maximum-distance-in-arrays/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/maximum-distance-in-arrays
    ## Basic Ideas:
    ##     Get the global min and global max.
    ##     If they happens in different rows, return directly.
    ##     Otherwise, check other rows. Get four possibilities.
    ##
    ## Complexity: Time O(n). Space O(1). n = len(arrays)
    class Solution:
        def maxDistance(self, arrays):
            """
            :type arrays: List[List[int]]
            :rtype: int
            """
            length = len(arrays)
            min_v, max_v = 10001, -10001
            for i in range(length):
                min_v = min(min_v, arrays[i][0])
                max_v = max(max_v, arrays[i][-1])
    
            l1, l2 = [], []
            for i in range(length):
                if arrays[i][0] == min_v: l1.append(i)
                if arrays[i][-1] == max_v: l2.append(i)
    
            if l1==l2 and len(l1) == 1:
                k = l1[0]
                max_distance = -1
                for i in range(length):
                    if i == k: continue
                    max_distance = max(max_distance, abs(arrays[k][0]-arrays[i][0]), \
                                        abs(arrays[k][0]-arrays[i][-1]), abs(arrays[k][-1]-arrays[i][0]), \
                                        abs(arrays[k][-1]-arrays[i][-1]))
            else:
                max_distance = max_v-min_v
            return max_distance