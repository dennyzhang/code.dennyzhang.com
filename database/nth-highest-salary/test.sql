# https://leetcode.com/problems/nth-highest-salary/description/

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  DECLARE M INT;
  DECLARE column_name varchar(100);
  set M=N-1;
  set column_name = CONCAT('getNthHighestSalary', N, ')');
  RETURN (
     select DISTINCT Salary as column_name
     from Employee
     order by Salary desc
     LIMIT M, 1
   );
END
