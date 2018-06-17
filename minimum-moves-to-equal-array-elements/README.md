# Leetcode: Minimum Moves to Equal Array Elements     :BLOG:Amusing:


---

Minimum Moves to Equal Array Elements  

---

Similar Problems:  
-   [Review: Math Problems](https://code.dennyzhang.com/review-math)
-   Tag: [math](https://code.dennyzhang.com/tag/math)

---

Given a non-empty integer array of size n, find the minimum number of moves required to make all array elements equal, where a move is incrementing n - 1 elements by 1.  

    Example:
    
    Input:
    [1,2,3]
    
    Output:
    3
    
    Explanation:
    Only three moves are needed (remember each move increments two elements):
    
    [1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/minimum-moves-to-equal-array-elements)  

Credits To: [leetcode.com](https://leetcode.com/problems/minimum-moves-to-equal-array-elements/description/)  

Leave me comments, if you have better ways to solve.  

---

    // Blog link: https://code.dennyzhang.com/minimum-moves-to-equal-array-elements
    // Basic Ideas: Math
    // First of all, for all input, we can always find one possible way to make all numbers equal
    //   Let's say, we have A B C D. And it's in ascending order
    //   Keep increase group of (A, B, C), untilsome of the element is D now.
    //   So we have (D D E F). Apparently D is no smaller than E, F
    //   Then keep incase (D D F). We will get (G G E E). Then we can get (H H H I).
    //   Then we get (O O O O)
    //
    // For each move, the mininum value will still be the mininum
    // For each move, the mininum value will add 1
    //
    // Complexity:
    func minMoves(nums []int) int {
        sum, min := 0, 1<<31 - 1
        for _, num := range nums {
            sum += num
            if (num < min) { min = num }
        }
        return sum - min*len(nums)
    }