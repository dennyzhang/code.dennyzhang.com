# https://leetcode.com/problems/department-top-three-salaries/description/

select t4.Name as Department, t3.Name as Employee, t3.Salary
from
    (select t1.Id, t1.Name, t1.Salary, t1.DepartmentId, count(1) as rank
    from Employee as t1 inner join Employee as t2
    on t1.DepartmentId = t2.DepartmentId
    where t1.Salary <= t2.Salary
    group by t1.Id, t1.Name, t1.Salary, t1.DepartmentId) as t3
    inner join Department as t4
    on t3.DepartmentId = t4.Id
where rank<=3
order by t4.Name, t3.Salary desc
