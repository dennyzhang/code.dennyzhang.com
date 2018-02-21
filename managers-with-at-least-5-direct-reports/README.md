# Leetcode: Managers with at Least 5 Direct Reports     :BLOG:Medium:


---

Managers with at Least 5 Direct Reports  

---

Similar Problems:  

-   [Review: SQL Problems](https://brain.dennyzhang.com/review-sql)
-   Tag: [#sql](https://brain.dennyzhang.com/tag/sql)

---

The Employee table holds all employees including their managers. Every employee has an Id, and there is also a column for the manager Id.  

    +------+----------+-----------+----------+
    |Id    |Name      |Department |ManagerId |
    +------+----------+-----------+----------+
    |101   |John      |A          |null      |
    |102   |Dan       |A          |101       |
    |103   |James     |A          |101       |
    |104   |Amy       |A          |101       |
    |105   |Anne      |A          |101       |
    |106   |Ron       |B          |101       |
    +------+----------+-----------+----------+

Given the Employee table, write a SQL query that finds out managers with at least 5 direct report. For the above table, your SQL query should return:  

    +-------+
    | Name  |
    +-------+
    | John  |
    +-------+

Note:  
No one would report to himself.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/managers-with-at-least-5-direct-reports)  

Credits To: [leetcode.com](https://leetcode.com/problems/managers-with-at-least-5-direct-reports/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/managers-with-at-least-5-direct-reports
    select Employee.Name
    from (select ManagerId
        from Employee
        group by ManagerId
        having count(1) >= 5) as t
        inner join
        Employee
    on t.ManagerId = Employee.Id