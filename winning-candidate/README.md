# Winning Candidate     :BLOG:Medium:


---

Winning Candidate  

---

Similar Problems:  
-   [Review: SQL Problems](https://brain.dennyzhang.com/review-sql), [Tag: #sql](https://brain.dennyzhang.com/tag/sql)

---

Table: Candidate  

    +-----+---------+
    | id  | Name    |
    +-----+---------+
    | 1   | A       |
    | 2   | B       |
    | 3   | C       |
    | 4   | D       |
    | 5   | E       |
    +-----+---------+

Table: Vote  

    +-----+--------------+
    | id  | CandidateId  |
    +-----+--------------+
    | 1   |     2        |
    | 2   |     4        |
    | 3   |     3        |
    | 4   |     2        |
    | 5   |     5        |
    +-----+--------------+

id is the auto-increment primary key,  
CandidateId is the id appeared in Candidate table.  
Write a sql to find the name of the winning candidate, the above example will return the winner B.  

    +------+
    | Name |
    +------+
    | B    |
    +------+

Notes:  
You may assume there is no tie, in other words there will be at most one winning candidate.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/winning-candidate)  

Credits To: [leetcode.com](https://leetcode.com/problems/winning-candidate/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/winning-candidate
    select Name
    from Candidate where
    id = (select CandidateId
         from Vote
         group by CandidateId
         order by count(1) desc
         limit 1)
    
    ## Assumtion: if we have two candidates with the same votes, we choose the one who get the first vote
    # select Name
    # from Candidate inner join
    #     (select CandidateId
    #     from Vote
    #     group by CandidateId
    #     order by count(1) desc
    #     limit 1) as t
    # on Candidate.id = t.CandidateId