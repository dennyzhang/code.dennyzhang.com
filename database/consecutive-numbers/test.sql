# https://leetcode.com/problems/consecutive-numbers/description/

SET @group_number=0;
SET @id_number1=0;
SET @id_number2=0;

select distinct Num as ConsecutiveNums
from
    (select group_id, Num, count(1) as item_count
    from
        (select Num, new_group, (if(new_group=1, @group_number:=@group_number+1, @group_number)) AS group_id
        from 
            (select t1.Id, t1.Num, if(t1.Num=t2.Num, 0, 1) as new_group
            from
            (select *, (@id_number1:=@id_number1+1) as id_number
            from Logs) as t1 left join 
            (select *, (@id_number2:=@id_number2+1) as id_number
            from Logs) as t2
            on t1.id_number = t2.id_number + 1) as t3
        order by t3.Id asc) as t4
    group by group_id, Num
    having count(1)>=3) as t5
group by Num
