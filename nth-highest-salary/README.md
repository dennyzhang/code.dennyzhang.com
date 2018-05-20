# Leetcode: Nth Highest Salary     :BLOG:Medium:


---

Nth Highest Salary  

---

Similar Problems:  
-   [Review: SQL Problems](https://code.dennyzhang.com/review-sql), [Tag: #sql](https://code.dennyzhang.com/tag/sql)

---

Write a SQL query to get the nth highest salary from the Employee table.  

    +----+--------+
    | Id | Salary |
    +----+--------+
    | 1  | 100    |
    | 2  | 200    |
    | 3  | 300    |
    +----+--------+

For example, given the above Employee table, the nth highest salary where n = 2 is 200. If there is no nth highest salary, then the query should return null.  

    +------------------------+
    | getNthHighestSalary(2) |
    +------------------------+
    | 200                    |
    +------------------------+

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/nth-highest-salary)  

Credits To: [leetcode.com](https://leetcode.com/problems/nth-highest-salary/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/nth-highest-salary
    CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
    BEGIN
      DECLARE M INT;
      DECLARE column_name varchar(100);
      set M=N-1;
      set column_name = CONCAT('getNthHighestSalary', N, ')');
      RETURN (
         select DISTINCT Salary as column_name
         from Employee
         order by Salary desc
         LIMIT M, 1
       );
    END