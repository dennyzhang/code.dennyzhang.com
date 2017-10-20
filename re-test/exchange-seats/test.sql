# https://leetcode.com/problems/exchange-seats/description/

select s1.id as id, s2.student as student
from seat as s1 join seat as s2
where (s1.id % 2 = 1 and s2.id = s1.id + 1) or (s1.id % 2 = 0 and s1.id = s2.id + 1)
or (s1.id %2 = 1 and s1.id = s2.id and s1.id in (select max(id) from seat))
order by s1.id asc
