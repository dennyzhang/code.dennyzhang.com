# https://leetcode.com/problems/classes-more-than-5-students/description/

select class
from (select class, count(distinct student) as num from courses group by class) as t
where t.num >= 5;

SELECT class
FROM courses
GROUP BY class HAVING COUNT(DISTINCT student)>=5;