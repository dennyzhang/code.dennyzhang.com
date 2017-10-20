# https://leetcode.com/problems/consecutive-numbers/description/

select *
from Logs as t1 inner join Logs as t2
order by t1.Id;
where t1.Num = t2.Num
