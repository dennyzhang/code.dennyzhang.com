# Leetcode: Shortest Distance in a Plane     :BLOG:Basic:


---

Shortest Distance in a Plane  

---

Similar Problems:  
-   [Review: SQL Problems](https://code.dennyzhang.com/review-sql), [Tag: #sql](https://code.dennyzhang.com/tag/sql)

---

Table point\_2d holds the coordinates (x,y) of some unique points (more than two) in a plane.  
Write a query to find the shortest distance between these points rounded to 2 decimals.  

    | x  | y  |
    |----|----|
    | -1 | -1 |
    | 0  | 0  |
    | -1 | -2 |

The shortest distance is 1.00 from point (-1,-1) to (-1,2). So the output should be:  

    | shortest |
    |----------|
    | 1.00     |

Note: The longest distance among all the points are less than 10000.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/shortest-distance-in-a-plane)  

Credits To: [leetcode.com](https://leetcode.com/problems/shortest-distance-in-a-plane/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://code.dennyzhang.com/shortest-distance-in-a-plane
    select round(min(sqrt((t1.x-t2.x)*(t1.x-t2.x) + (t1.y-t2.y)*(t1.y-t2.y))), 2) as shortest
    from point_2d as t1, point_2d as t2
    where t1.x!=t2.x or t1.y!=t2.y
    
    # select round(sqrt((t1.x-t2.x)*(t1.x-t2.x) + (t1.y-t2.y)*(t1.y-t2.y)), 2) as shortest
    # from point_2d as t1, point_2d as t2
    # where t1.x!=t2.x or t1.y!=t2.y
    # order by shortest asc
    # limit 1