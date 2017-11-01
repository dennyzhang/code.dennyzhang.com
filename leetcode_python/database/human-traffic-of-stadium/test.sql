# https://leetcode.com/problems/human-traffic-of-stadium/description/

SET @group_number=0;

select distinct stadium.id, stadium.date, stadium.people
from stadium inner join
    (select min(id) as min_id, max(id) as max_id, group_id
    from (select t3.*, if(below_100 != next_day_below_100 , @group_number:=@group_number+1, @group_number) as group_id
          from (select t1.*, t2.below_100 as next_day_below_100
             from
             (select id, date, people, if(people<100, 1, 0) as below_100
             from stadium) t1 left join  
             (select id, date, people, if(people<100, 1, 0) as below_100
             from stadium) t2
             on t1.id = t2.id + 1
             order by t1.id asc) t3) as t4
    group by group_id
    having count(1)>=3) as t5
where stadium.id >= min_id and stadium.id <= max_id
order by stadium.id asc