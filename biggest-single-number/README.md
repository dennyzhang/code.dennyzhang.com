# Leetcode: Second Highest Salary     :BLOG:Medium:


---

Second Highest Salary  

---

Similar Problems:  
-   [Review: SQL Problems](https://brain.dennyzhang.com/review-sql)

---

Table number contains many numbers in column num including duplicated ones.  
Can you write a SQL query to find the biggest number, which only appears once.  

    +---+
    |num|
    +---+
    | 8 |
    | 8 |
    | 3 |
    | 3 |
    | 1 |
    | 4 |
    | 5 |
    | 6 |

For the sample data above, your query should return the following result:  

    +---+
    |num|
    +---+
    | 6 |

Note:  
If there is no such number, just output null.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/biggest-single-number)  

Credits To: [leetcode.com](https://leetcode.com/problems/biggest-single-number/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/biggest-single-number
    select ifnull((
        select num
        from number
        group by num
        having count(1) = 1
        order by num desc
        limit 0, 1), null) as num