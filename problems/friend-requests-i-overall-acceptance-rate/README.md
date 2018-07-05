
# Leetcode: Friend Requests I: Overall Acceptance Rate     :BLOG:Basic:

---

Friend Requests I: Overall Acceptance Rate  

---

Similar Problems:  

-   [Friend Requests II: Who Has the Most Friends](https://code.dennyzhang.com/friend-requests-ii-who-has-the-most-friends)
-   [Review: SQL Problems](https://code.dennyzhang.com/review-sql), [Tag: #sql](https://code.dennyzhang.com/tag/sql)

---

In social network like Facebook or Twitter, people send friend requests and accept others' requests as well. Now given two tables as below:  
Table: friend\_request  

    | sender_id | send_to_id |request_date|
    |-----------|------------|------------|
    | 1         | 2          | 2016_06-01 |
    | 1         | 3          | 2016_06-01 |
    | 1         | 4          | 2016_06-01 |
    | 2         | 3          | 2016_06-02 |
    | 3         | 4          | 2016-06-09 |

Table: request\_accepted  

    | requester_id | accepter_id |accept_date |
    |--------------|-------------|------------|
    | 1            | 2           | 2016_06-03 |
    | 1            | 3           | 2016-06-08 |
    | 2            | 3           | 2016-06-08 |
    | 3            | 4           | 2016-06-09 |
    | 3            | 4           | 2016-06-10 |

Write a query to find the overall acceptance rate of requests rounded to 2 decimals, which is the number of acceptance divide the number of requests.  
For the sample data above, your query should return the following result.  

    |accept_rate|
    |-----------|
    |       0.80|

Note:  

-   The accepted requests are not necessarily from the table friend\_request. In this case, you just need to simply count the total accepted requests (no matter whether they are in the original requests), and divide it by the number of requests to get the acceptance rate.
-   It is possible that a sender sends multiple requests to the same receiver, and a request could be accepted more than once. In this case, the 'duplicated' requests or acceptances are only counted once.
-   If there is no requests at all, you should return 0.00 as the accept\_rate.

Explanation: There are 4 unique accepted requests, and there are 5 requests in total. So the rate is 0.80.  

Follow-up:  

-   Can you write a query to return the accept rate but for every month?
-   How about the cumulative accept rate for every day?

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/friend-requests-i-overall-acceptance-rate)  

Credits To: [leetcode.com](https://leetcode.com/problems/friend-requests-i-overall-acceptance-rate/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/friend-requests-i-overall-acceptance-rate
    select ifnull((round(accepts/requests, 2)), 0.0) as accept_rate
    from
        (select count(distinct sender_id, send_to_id) as requests from friend_request) as t1,
        (select count(distinct requester_id, accepter_id) as accepts from request_accepted) as t2

