# Leetcode: Employees Earning More Than Their Managers     :BLOG:Medium:


---

Employees Earning More Than Their Managers  

---

Similar Problems:  
-   [Review: SQL Problems](https://brain.dennyzhang.com/review-sql), [Tag: #sql](https://brain.dennyzhang.com/tag/sql)

---

The Employee table holds all employees including their managers. Every employee has an Id, and there is also a column for the manager Id.  

    +----+-------+--------+-----------+
    | Id | Name  | Salary | ManagerId |
    +----+-------+--------+-----------+
    | 1  | Joe   | 70000  | 3         |
    | 2  | Henry | 80000  | 4         |
    | 3  | Sam   | 60000  | NULL      |
    | 4  | Max   | 90000  | NULL      |
    +----+-------+--------+-----------+

Given the Employee table, write a SQL query that finds out employees who earn more than their managers. For the above table, Joe is the only employee who earns more than his manager.  

    +----------+
    | Employee |
    +----------+
    | Joe      |
    +----------+

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/employees-earning-more-than-their-managers)  

Credits To: [leetcode.com](https://leetcode.com/problems/employees-earning-more-than-their-managers/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/employees-earning-more-than-their-managers
    select t1.Name as Employee
    from Employee as t1 inner join Employee as t2
    on t1.ManagerId = t2.Id
    where t1.Salary > t2.Salary;