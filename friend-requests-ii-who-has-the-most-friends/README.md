# Leetcode: Friend Requests II: Who Has the Most Friends     :BLOG:Medium:


---

Friend Requests II: Who Has the Most Friends  

---

Similar Problems:  
-   [Friend Requests I: Overall Acceptance Rate](https://brain.dennyzhang.com/friend-requests-i-overall-acceptance-rate)
-   [Review: SQL Problems](https://brain.dennyzhang.com/review-sql)

---

In social network like Facebook or Twitter, people send friend requests and accept others' requests as well.  
Table request\_accepted holds the data of friend acceptance, while requester\_id and accepter\_id both are the id of a person.  

    | requester_id | accepter_id | accept_date|
    |--------------|-------------|------------|
    | 1            | 2           | 2016_06-03 |
    | 1            | 3           | 2016-06-08 |
    | 2            | 3           | 2016-06-08 |
    | 3            | 4           | 2016-06-09 |

Write a query to find the the people who has most friends and the most friends number. For the sample data above, the result is:  

    | id | num |
    |----|-----|
    | 3  | 3   |

Note:  
-   It is guaranteed there is only 1 people having the most friends.
-   The friend request could only been accepted once, which mean there is no multiple records with the same requester\_id and accepter\_id value.

Explanation:  
The person with id '3' is a friend of people '1', '2' and '4', so he has 3 friends in total, which is the most number than any others.  

Follow-up:  
In the real world, multiple people could have the same most number of friends, can you find all these people in this case?  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/friend-requests-ii-who-has-the-most-friends)  

Credits To: [leetcode.com](https://leetcode.com/problems/friend-requests-ii-who-has-the-most-friends/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/friend-requests-ii-who-has-the-most-friends
    select t.id, sum(t.num) as num
    from (
          (select requester_id as id, count(1) as num
           from request_accepted
           group by requester_id)
          union all
           (select accepter_id as id, count(1) as num
            from request_accepted
            group by accepter_id)) as t
    group by t.id
    order by num desc
    limit 1