
# Leetcode: Rising Temperature     :BLOG:Medium:

---

Rising Temperature  

---

Similar Problems:  

-   [Review: SQL Problems](https://code.dennyzhang.com/review-sql), [Tag: #sql](https://code.dennyzhang.com/tag/sql)

---

Given a Weather table, write a SQL query to find all dates' Ids with higher temperature compared to its previous (yesterday's) dates.  

    +---------+------------+------------------+
    | Id(INT) | Date(DATE) | Temperature(INT) |
    +---------+------------+------------------+
    |       1 | 2015-01-01 |               10 |
    |       2 | 2015-01-02 |               25 |
    |       3 | 2015-01-03 |               20 |
    |       4 | 2015-01-04 |               30 |
    +---------+------------+------------------+

For example, return the following Ids for the above Weather table:  

    +----+
    | Id |
    +----+
    |  2 |
    |  4 |
    +----+

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/rising-temperature)  

Credits To: [leetcode.com](https://leetcode.com/problems/rising-temperature/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/rising-temperature
    select t1.Id
    from Weather as t1 join Weather as t2
    on DATE_ADD(t2.Date, INTERVAL 1 DAY) = t1.Date
    where t1.Temperature > t2.Temperature;

