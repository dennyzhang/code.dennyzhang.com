# https://leetcode.com/problems/second-highest-salary/description/

select ifnull((
       select Salary from Employee
       group by Salary order by Salary desc limit 1,1), null) as SecondHighestSalary
