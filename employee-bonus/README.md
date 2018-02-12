# Leetcode: Employee Bonus     :BLOG:Medium:


---

Employee Bonus  

---

Similar Problems:  
-   Tag: [#sql](https://brain.dennyzhang.com/tag/sql)

---

Select all employee's name and bonus whose bonus is < 1000.  

Table:Employee  

    +-------+--------+-----------+--------+
    | empId |  name  | supervisor| salary |
    +-------+--------+-----------+--------+
    |   1   | John   |  3        | 1000   |
    |   2   | Dan    |  3        | 2000   |
    |   3   | Brad   |  null     | 4000   |
    |   4   | Thomas |  3        | 4000   |
    +-------+--------+-----------+--------+
    empId is the primary key column for this table.

Table: Bonus  

    +-------+-------+
    | empId | bonus |
    +-------+-------+
    | 2     | 500   |
    | 4     | 2000  |
    +-------+-------+
    empId is the primary key column for this table.

Example ouput:  

    +-------+-------+
    | name  | bonus |
    +-------+-------+
    | John  | null  |
    | Dan   | 500   |
    | Brad  | null  |
    +-------+-------+

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/employee-bonus)  

Credits To: [leetcode.com](https://leetcode.com/problems/employee-bonus/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/employee-bonus