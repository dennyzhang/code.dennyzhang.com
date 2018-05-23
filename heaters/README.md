# Leetcode: Heaters     :BLOG:Amusing:


---

Heaters  

---

Similar Problems:  
-   [Shortest Word Distance](https://code.dennyzhang.com/shortest-word-distance)
-   Tag: [#inspiring](https://code.dennyzhang.com/category/inspiring), [#classic](https://code.dennyzhang.com/category/classic)

---

Winter is coming! Your first job during the contest is to design a standard heater with fixed warm radius to warm all the houses.  

Now, you are given positions of houses and heaters on a horizontal line, find out minimum radius of heaters so that all houses could be covered by those heaters.  

So, your input will be the positions of houses and heaters seperately, and your expected output will be the minimum radius standard of heaters.  

Note:  
1.  Numbers of houses and heaters you are given are non-negative and will not exceed 25000.
2.  Positions of houses and heaters you are given are non-negative and will not exceed 10^9.
3.  As long as a house is in the heaters' warm radius range, it can be warmed.
4.  All the heaters follow your radius standard and the warm radius will the same.

Example 1:  

    Input: [1,2,3],[2]
    Output: 1
    Explanation: The only heater was placed in the position 2, and if we use the radius 1 standard, then all the houses can be warmed.

Example 2:  

    Input: [1,2,3,4],[1,4]
    Output: 1
    Explanation: The two heater was placed in the position 1 and 4. We need to use radius 1 standard, then all the houses can be warmed.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/heaters)  

Credits To: [leetcode.com](https://leetcode.com/problems/heaters/description/)  

Leave me comments, if you have better ways to solve.  

---

    // Blog link: https://code.dennyzhang.com/heaters
    // Basic Ideas: One pass
    // For each house, find the nearest heater
    // Complexity: Time O(n*log(n)), Space O(1)
    import "sort"
    func abs(v int) int {
        if v<0 { return -v }
        return v
    }
    
    func findRadius(houses []int, heaters []int) int {
        sort.Ints(houses)
        sort.Ints(heaters)
        res := 0
        i := 0
        for _, house := range houses {
            // find the nearest heater
            for i<len(heaters)-1 && abs(heaters[i]-house) >= abs(heaters[i+1]-house) {
                i++
            }
            if abs(heaters[i]-house) > res { res = abs(heaters[i]-house) }
        }
        return res
    }