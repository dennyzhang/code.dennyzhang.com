# Leetcode: Consecutive Numbers     :BLOG:Medium:


---

Consecutive Numbers  

---

Similar Problems:  
-   [Review: SQL Problems](https://code.dennyzhang.com/review-sql), [Tag: #sql](https://code.dennyzhang.com/tag/sql)

---

Write a SQL query to find all numbers that appear at least three times consecutively.  

    +----+-----+
    | Id | Num |
    +----+-----+
    | 1  |  1  |
    | 2  |  1  |
    | 3  |  1  |
    | 4  |  2  |
    | 5  |  1  |
    | 6  |  2  |
    | 7  |  2  |
    +----+-----+

For example, given the above Logs table, 1 is the only number that appears consecutively for at least three times.  

    +-----------------+
    | ConsecutiveNums |
    +-----------------+
    | 1               |
    +-----------------+

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/consecutive-numbers)  

Credits To: [leetcode.com](https://leetcode.com/problems/consecutive-numbers/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/consecutive-numbers
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