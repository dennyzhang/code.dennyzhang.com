# https://leetcode.com/problems/nth-highest-salary/description/

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
     set @start_num = N - 1;
     set @column_name = CONCAT('getNthHighestSalary(', N, ')');
     
     select Salary as @column_name
     from Employee
     # TODO; change this
     order by Salary desc
     LIMIT @start_num, 1
   );
END
