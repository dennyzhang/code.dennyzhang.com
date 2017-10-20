# https://leetcode.com/problems/department-top-three-salaries/description/

{"headers": ["Department", "Employee", "Salary"], "values":
[["IT", "Max", 90000],
["IT", "Joe", 70000],
["Sales", "Henry", 80000],
["Sales", "Sam", 60000]]}

select Department.Name as Department, Employee.Name as Employee, Employee.Salary
from Employee inner join Department
on Employee.DepartmentId = Department.Id
group by Employee.DepartmentId
having 