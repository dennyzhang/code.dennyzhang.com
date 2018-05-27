# Leetcode: Max Chunks To Make Sorted     :BLOG:Medium:


---

Max Chunks To Make Sorted  

---

Similar Problems:  
-   [Max Chunks To Make Sorted II](https://code.dennyzhang.com/max-chunks-to-make-sorted-ii)
-   [Jump Game II](https://code.dennyzhang.com/jump-game-ii)
-   [Review: Greedy Problems](https://code.dennyzhang.com/review-greedy)
-   Tag: [#greedy](https://code.dennyzhang.com/tag/greedy), [#slidingwindow](https://code.dennyzhang.com/tag/slidingwindow)

---

Given an array arr that is a permutation of [0, 1, &#x2026;, arr.length - 1], we split the array into some number of "chunks" (partitions), and individually sort each chunk.  After concatenating them, the result equals the sorted array.  

What is the most number of chunks we could have made?  

Example 1:  

    Input: arr = [4,3,2,1,0]
    Output: 1
    Explanation:
    Splitting into two or more chunks will not return the required result.
    For example, splitting into [4, 3], [2, 1, 0] will result in [3, 4, 0, 1, 2], which isn't sorted.

Example 2:  

    Input: arr = [1,0,2,3,4]
    Output: 4
    Explanation:
    We can split into two chunks, such as [1, 0], [2, 3, 4].
    However, splitting into [1, 0], [2], [3], [4] is the highest number of chunks possible.

Note:  

-   arr will have length in range [1, 10].
-   arr[i] will be a permutation of [0, 1, &#x2026;, arr.length - 1].

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/max-chunks-to-make-sorted)  

Credits To: [leetcode.com](https://leetcode.com/problems/max-chunks-to-make-sorted/description/)  

Leave me comments, if you have better ways to solve.  

---

-   Solution: greedy

**General Thinkings:**  

    Find the boundry of each chunk. 
    
    Examine: 3 0 2 1 4
    
    For l[0] -> 3, the right border of current chunk is at least 3
    
    Now we have a sliding window of l[0], l[1], l[2], l[3]
    
    If any item of is bigger than 3, we need to enlarge the right border of the window.

This problem is similar with [Jump Game II](https://code.dennyzhang.com/jump-game-ii)  

    // Blog link: https://code.dennyzhang.com/max-chunks-to-make-sorted
    // Basic Ideas: Greedy
    // Complexity: Time O(n), Space O(1)
    func maxChunksToSorted(arr []int) int {
        res, rindex := 0, -1
        for i, v:= range arr{
            // Begining of a chunk
            if rindex == -1 { rindex = v }
            // Need to enlarge the sliding window
            if i<=rindex && v>rindex { rindex = v }
            // Get the end of a chunk
            if i==rindex {
                rindex = -1
                res++
            }
        }
        return res
    }

-   Solution: auxiliary array

    // Blog link: https://code.dennyzhang.com/max-chunks-to-make-sorted
    // Basic Ideas: Use an auxiliary array
    //
    // original: 0, 2, 1, 4, 3, 5, 7, 6
    // max:      0, 2, 2, 4, 4, 5, 7, 7
    // sorted:   0, 1, 2, 3, 4, 5, 6, 7
    // index:    0, 1, 2, 3, 4, 5, 6, 7
    //
    // Complexity: Time O(n), Space O(n)
    func maxChunksToSorted(arr []int) int {
        l := make([]int, len(arr))
        max := -1
        for i, v:= range arr{
            if v>max { max=v }
            l[i] = max
        }
        res := 0
        for i, v:= range l{
            if i==v { res++ }
        }
        return res
    }