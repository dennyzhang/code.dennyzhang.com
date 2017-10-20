# https://leetcode.com/problems/department-highest-salary/description/

select Department.Name as Department, t3.Name as Employee, t3.Salary
from Employee as t3 inner join
     (select t1.Salary, t1.DepartmentId, count(1) as rank
        from (select distinct Salary, DepartmentId from Employee) as t1
             inner join
             (select distinct Salary, DepartmentId from Employee) as t2
             on t1.DepartmentId = t2.DepartmentId
        where t1.Salary <= t2.Salary
        group by t1.Salary, t1.DepartmentId) as t4
      inner join Department
      on t3.DepartmentId = t4.DepartmentId and t3.Salary = t4.Salary 
      and t3.DepartmentId = Department.Id
where t4.rank<4
order by t3.DepartmentId asc, t3.Salary desc;