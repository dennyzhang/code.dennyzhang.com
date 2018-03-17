# Leetcode: Find Median Given Frequency of Numbers     :BLOG:Hard:


---

Find Median Given Frequency of Numbers  

---

Similar Problems:  
-   [Median Employee Salary](https://brain.dennyzhang.com/median-employee-salary)
-   [Review: SQL Problems](https://brain.dennyzhang.com/review-sql)
-   [Review: Median Problems](https://brain.dennyzhang.com/review-median)
-   Tag: [getmedian](https://brain.dennyzhang.com/tag/getmedian), [#sql](https://brain.dennyzhang.com/tag/sql)

---

The Numbers table keeps the value of number and its frequency.  

    +----------+-------------+
    |  Number  |  Frequency  |
    +----------+-------------|
    |  0       |  7          |
    |  1       |  1          |
    |  2       |  3          |
    |  3       |  1          |
    +----------+-------------+

In this table, the numbers are 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 3, so the median is (0 + 0) / 2 = 0.  

    +--------+
    | median |
    +--------|
    | 0.0000 |
    +--------+

Write a query to find the median of all numbers and name the result as median.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/find-median-given-frequency-of-numbers)  

Credits To: [leetcode.com](https://leetcode.com/problems/find-median-given-frequency-of-numbers/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/find-median-given-frequency-of-numbers
    select avg(t3.Number) as median
    from Numbers as t3 
    inner join 
        (select t1.Number, 
            abs(sum(case when t1.Number>t2.Number then t2.Frequency else 0 end) -
                sum(case when t1.Number<t2.Number then t2.Frequency else 0 end)) as count_diff
        from numbers as t1, numbers as t2
        group by t1.Number) as t4
    on t3.Number = t4.Number
    where t3.Frequency>=t4.count_diff