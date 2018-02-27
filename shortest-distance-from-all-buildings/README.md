# Leetcode: Shortest Distance from All Buildings     :BLOG:Medium:


---

Shortest Distance from All Buildings  

---

Similar Problems:  
-   [Walls and Gates](https://brain.dennyzhang.com/walls-and-gates)
-   [Review: BFS Problems](https://brain.dennyzhang.com/review-bfs), [Tag: #bfs](https://brain.dennyzhang.com/tag/bfs)

---

You want to build a house on an empty land which reaches all buildings in the shortest amount of distance. You can only move up, down, left and right. You are given a 2D grid of values 0, 1 or 2, where:  

-   Each 0 marks an empty land which you can pass by freely.
-   Each 1 marks a building which you cannot pass through.
-   Each 2 marks an obstacle which you cannot pass through.

For example, given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2):  

    1 - 0 - 2 - 0 - 1
    |   |   |   |   |
    0 - 0 - 0 - 0 - 0
    |   |   |   |   |
    0 - 0 - 1 - 0 - 0

The point (1,2) is an ideal empty land to build a house, as the total travel distance of 3+3+1=7 is minimal. So return 7.  

Note:  
There will be at least one building. If it is not possible to build such house according to the above rules, return -1.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/shortest-distance-from-all-buildings)  

Credits To: [leetcode.com](https://leetcode.com/problems/shortest-distance-from-all-buildings/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/shortest-distance-from-all-buildings