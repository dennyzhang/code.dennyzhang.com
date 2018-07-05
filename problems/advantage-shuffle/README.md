
# Leetcode: Advantage Shuffle     :BLOG:Medium:

---

Advantage Shuffle  

---

Similar Problems:  

-   [Review: Linked List Problems](https://code.dennyzhang.com/review-linkedlist)
-   Tag: [#binarysearch](https://code.dennyzhang.com/tag/binarysearch), [#greedy](https://code.dennyzhang.com/tag/greedy), [#array](https://code.dennyzhang.com/tag/array)

---

Given two arrays A and B of equal size, the advantage of A with respect to B is the number of indices i for which A[i] > B[i].  

Return any permutation of A that maximizes its advantage with respect to B.  

Example 1:  

    Input: A = [2,7,11,15], B = [1,10,4,11]
    Output: [2,11,7,15]

Example 2:  

    Input: A = [12,24,8,32], B = [13,25,32,11]
    Output: [24,32,8,12]

Note:  

1.  1 <= A.length = B.length <= 10000
2.  0 <= A[i] <= 10^9
3.  0 <= B[i] <= 10^9

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/advantage-shuffle)  

Credits To: [leetcode.com](https://leetcode.com/problems/advantage-shuffle/description/)  

Leave me comments, if you have better ways to solve.  

---

-   Solution:

    // Blog link: https://code.dennyzhang.com/advantage-shuffle
    // Basic Ideas: Greedy + binary search
    // For which B[i], it won't be worse, if we try our best to satisfy it
    // - If we have available values in A which is bigger than B[i], choose the min candidates
    // - Otherwise select the min value
    // Complexity: Time O(n*log(n)), Space O(n)
    import (
        "sort"
    )
    func advantageCount(A []int, B []int) []int {
        res := []int{}
        sort.Ints(A)
        var left, right, middle int
        for _, num := range B {
    	// binary search: find the first value which is bigger than the target
    	left, right = 0, len(A)-1
    	for left < right {
    	    middle = left + (right-left)/2
    	    if A[middle] > num {
    		right = middle
    	    } else {
    		left = middle+1
    	    }
    	}
    	// no candidate
    	if A[left] <= num { left = 0 }
    	// select the value
    	res = append(res, A[left])
    	// update A
    	if left == 0 { 
    	    A = A[1:]
    	} else {
    	    A = append(A[0:left], A[left+1:]...)
    	}
        }
        return res
    }

