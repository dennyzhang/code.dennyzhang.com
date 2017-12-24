# https://leetcode.com/problems/employees-earning-more-than-their-managers/description/

select t1.Name as Employee
from Employee as t1 inner join Employee as t2
on t1.ManagerId = t2.Id
where t1.Salary > t2.Salary;