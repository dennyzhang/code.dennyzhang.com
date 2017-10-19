;; https://leetcode.com/problems/rising-temperature/description/

select t1.Id
from Weather as t1 join Weather as t2
on DATE_ADD(t2.Date, INTERVAL 1 DAY) = t1.Date
where t1.Temperature > t2.Temperature;
