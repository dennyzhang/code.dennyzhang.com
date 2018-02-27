# Leetcode: Shortest Distance in a Line     :BLOG:Medium:


---

Shortest Distance in a Line  

---

Similar Problems:  
-   [Review: SQL Problems](https://brain.dennyzhang.com/review-sql), [Tag: #sql](https://brain.dennyzhang.com/tag/sql)

---

Table point holds the x coordinate of some points on x-axis in a plane, which are all integers.  
Write a query to find the shortest distance between two points in these points.  

    | x   |
    |-----|
    | -1  |
    | 0   |
    | 2   |

The shortest distance is '1' obviously, which is from point '-1' to '0'. So the output is as below:  

    | shortest|
    |---------|
    | 1       |

Note: Every point is unique, which means there is no duplicates in table point.  

Follow-up: What if all these points have an id and are arranged from the left most to the right most of x axis?  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/shortest-distance-in-a-line)  

Credits To: [leetcode.com](https://leetcode.com/problems/shortest-distance-in-a-line/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/shortest-distance-in-a-line
    select t1.x-t2.x as shortest
    from point as t1 join point as t2
    where t1.x>t2.x
    order by (t1.x-t2.x) asc
    limit 1