# https://leetcode.com/problems/rank-scores/description/

set @rownr=0;
select t1.Score, t2.rank as Rank
from Scores as t1 inner join
      (select @rownr:=@rownr+1 as rank, t.Score
      from (select * from Scores 
      group by Score order by Score desc) as t) As t2
on t1.Score = t2.Score
order by t1.Score desc

# -- --8<-------------------------- separator -----------------------

select ranking.Score as Score, ranking.Ranking as Rank
    from Scores inner join
      (select t1.Score as Score, count(1) as Ranking
        from
            (select distinct Score from Scores) as t1 inner join
            (select distinct Score from Scores) as t2
        where t1.Score <= t2.Score
        group by t1.Score) as ranking
    on Scores.Score = ranking.Score
    order by ranking.Score desc