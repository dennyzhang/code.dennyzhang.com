# Leetcode: Number of Islands II     :BLOG:Medium:


---

Number of Islands II  

---

Similar Problems:  
-   Tag: [#graph](https://code.dennyzhang.com/tag/graph)

---

A 2d grid map of m rows and n columns is initially filled with water. We may perform an addLand operation which turns the water at position (row, col) into a land. Given a list of positions to operate, count the number of islands after each addLand operation. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.  

Example:  

Given m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]].  
Initially, the 2d grid grid is filled with water. (Assume 0 represents water and 1 represents land).  

    0 0 0
    0 0 0
    0 0 0

Operation #1: addLand(0, 0) turns the water at gridinto a land.  

    1 0 0
    0 0 0   Number of islands = 1
    0 0 0

Operation #2: addLand(0, 1) turns the water at gridinto a land.  

    1 1 0
    0 0 0   Number of islands = 1
    0 0 0

Operation #3: addLand(1, 2) turns the water at gridinto a land.  

    1 1 0
    0 0 1   Number of islands = 2
    0 0 0

Operation #4: addLand(2, 1) turns the water at gridinto a land.  

    1 1 0
    0 0 1   Number of islands = 3
    0 1 0

We return the result as an array: [1, 1, 2, 3]  

Challenge:  

Can you do it in time complexity O(k log mn), where k is the length of the positions?  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/number-of-islands-ii)  

Credits To: [leetcode.com](https://leetcode.com/problems/number-of-islands-ii/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://code.dennyzhang.com/number-of-islands-ii

<div id="footnotes">
<h2 class="footnotes">Footnotes: </h2>
<div id="text-footnotes">

<div class="footdef"><sup><a id="fn.1" name="fn.1" class="footnum" href="#fnr.1">1</a></sup> <p>DEFINITION NOT FOUND.</p></div>

<div class="footdef"><sup><a id="fn.2" name="fn.2" class="footnum" href="#fnr.2">2</a></sup> <p>DEFINITION NOT FOUND.</p></div>

<div class="footdef"><sup><a id="fn.3" name="fn.3" class="footnum" href="#fnr.3">3</a></sup> <p>DEFINITION NOT FOUND.</p></div>


</div>
</div>