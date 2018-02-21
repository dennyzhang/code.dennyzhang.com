# Leetcode: Second Highest Salary     :BLOG:Medium:


---

Second Highest Salary  

---

Similar Problems:  
-   [Review: SQL Problems](https://brain.dennyzhang.com/review-sql)
-   Tag: [#sql](https://brain.dennyzhang.com/tag/sql)

---

Write a SQL query to get the second highest salary from the Employee table.  

    +----+--------+
    | Id | Salary |
    +----+--------+
    | 1  | 100    |
    | 2  | 200    |
    | 3  | 300    |
    +----+--------+

For example, given the above Employee table, the query should return 200 as the second highest salary. If there is no second highest salary, then the query should return null.  

    +---------------------+
    | SecondHighestSalary |
    +---------------------+
    | 200                 |
    +---------------------+

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/second-highest-salary)  

Credits To: [leetcode.com](https://leetcode.com/problems/second-highest-salary/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/second-highest-salary
    select ifnull((
           select Salary from Employee
           group by Salary order by Salary desc limit 1,1), null) as SecondHighestSalary