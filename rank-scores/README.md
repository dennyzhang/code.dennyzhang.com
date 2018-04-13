# Leetcode: Rank Scores     :BLOG:Medium:


---

Rank Scores  

---

Similar Problems:  
-   [Review: SQL Problems](https://code.dennyzhang.com/review-sql), [Tag: #sql](https://code.dennyzhang.com/tag/sql)

---

Write a SQL query to rank scores. If there is a tie between two scores, both should have the same ranking. Note that after a tie, the next ranking number should be the next consecutive integer value. In other words, there should be no "holes" between ranks.  

    +----+-------+
    | Id | Score |
    +----+-------+
    | 1  | 3.50  |
    | 2  | 3.65  |
    | 3  | 4.00  |
    | 4  | 3.85  |
    | 5  | 4.00  |
    | 6  | 3.65  |
    +----+-------+

For example, given the above Scores table, your query should generate the following report (order by highest score):  

    +-------+------+
    | Score | Rank |
    +-------+------+
    | 4.00  | 1    |
    | 4.00  | 1    |
    | 3.85  | 2    |
    | 3.65  | 3    |
    | 3.65  | 3    |
    | 3.50  | 4    |
    +-------+------+

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/rank-scores)  

Credits To: [leetcode.com](https://leetcode.com/problems/rank-scores/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://code.dennyzhang.com/rank-scores
    set @rownr=0;
    select t1.Score, t2.rank as Rank
    from Scores as t1 inner join
          (select @rownr:=@rownr+1 as rank, t.Score
          from (select * from Scores 
          group by Score order by Score desc) as t) As t2
    on t1.Score = t2.Score
    order by t1.Score desc
    
    # -------------- separator ---------
    
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