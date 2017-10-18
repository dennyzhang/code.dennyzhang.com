;; https://leetcode.com/problems/second-highest-salary/description/

select t.Salary as SecondHighestSalary from (select Salary from Employee order by Salary desc limit 2) as t limit 1 offset 1;