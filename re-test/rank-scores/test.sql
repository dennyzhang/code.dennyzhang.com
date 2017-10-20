# https://leetcode.com/problems/rank-scores/description/

set @rownr=0;
select t1.Score, t2.rank as Rank
from Scores as t1 inner join
      (select @rownr:=@rownr+1 as rank, t.Score
      from (select * from Scores 
      group by Score order by Score desc) as t) As t2
on t1.Score = t2.Score
order by t1.Score desc
