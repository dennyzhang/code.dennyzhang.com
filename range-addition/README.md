# Leetcode: Range Addition     :BLOG:Medium:


---

Range Addition  

---

Similar Problems:  
-   [Maximum Distance in Arrays](https://brain.dennyzhang.com/maximum-distance-in-arrays)
-   Tag: [#inspiring](https://brain.dennyzhang.com/tag/inspiring)

---

Assume you have an array of length n initialized with all 0's and are given k update operations.  

Each operation is represented as a triplet: [startIndex, endIndex, inc] which increments each element of subarray A[startIndex &#x2026; endIndex] (startIndex and endIndex inclusive) with inc.  

Return the modified array after all k operations were executed.  

Example:  

    Given:
    
        length = 5,
        updates = [
            [1,  3,  2],
            [2,  4,  3],
            [0,  2, -2]
        ]
    
    Output:
    
        [-2, 0, 3, 5, 3]

Explanation:  

    Initial state:
    [ 0, 0, 0, 0, 0 ]
    
    After applying operation [1, 3, 2]:
    [ 0, 2, 2, 2, 0 ]
    
    After applying operation [2, 4, 3]:
    [ 0, 2, 5, 5, 3 ]
    
    After applying operation [0, 2, -2]:
    [-2, 0, 3, 5, 3 ]

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/range-addition)  

Credits To: [leetcode.com](https://leetcode.com/problems/range-addition/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/range-addition
    ## Basic Ideas:
    ##
    ##         0  0  0  0  0  0    ([1, 3, 2])
    ##         0  2  0  0 -2  0    ([2, 4, 3])
    ##         0  2  3  0 -2 -3    ([0, 2, -2])
    ##        -2  2  3  2 -2 -3
    ## delta: -2  0  3  5  3  0
    ##
    ## Complexity: Time O(n+k), Space O(n)
    ##
    class Solution:
        def getModifiedArray(self, length, updates):
            """
            :type length: int
            :type updates: List[List[int]]
            :rtype: List[int]
            """
            delta_list = [0] * length
            for [start, end, inc] in updates:
                delta_list[start] += inc
                if end+1 < length:
                    delta_list[end+1] -= inc
    
            delta = 0
            for i in range(0, length):
                delta += delta_list[i]
                delta_list[i] = delta
            return delta_list