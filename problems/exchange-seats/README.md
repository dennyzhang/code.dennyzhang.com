
# Leetcode: Exchange Seats     :BLOG:Medium:

---

Exchange Seats  

---

Similar Problems:  

-   [Review: SQL Problems](https://code.dennyzhang.com/review-sql), [Tag: #sql](https://code.dennyzhang.com/tag/sql)

---

Mary is a teacher in a middle school and she has a table seat storing students' names and their corresponding seat ids.  

The column id is continuous increment.  
Mary wants to change seats for the adjacent students.  
Can you write a SQL query to output the result for Mary?  

    +---------+---------+
    |    id   | student |
    +---------+---------+
    |    1    | Abbot   |
    |    2    | Doris   |
    |    3    | Emerson |
    |    4    | Green   |
    |    5    | Jeames  |
    +---------+---------+

For the sample input, the output is:  

    +---------+---------+
    |    id   | student |
    +---------+---------+
    |    1    | Doris   |
    |    2    | Abbot   |
    |    3    | Green   |
    |    4    | Emerson |
    |    5    | Jeames  |
    +---------+---------+

Note:  
If the number of students is odd, there is no need to change the last one's seat.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/exchange-seats)  

Credits To: [leetcode.com](https://leetcode.com/problems/exchange-seats/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/exchange-seats
    select s1.id as id, s2.student as student
    from seat as s1 join seat as s2
    where (s1.id % 2 = 1 and s2.id = s1.id + 1) or (s1.id % 2 = 0 and s1.id = s2.id + 1)
    or (s1.id %2 = 1 and s1.id = s2.id and s1.id in (select max(id) from seat))
    order by s1.id asc

