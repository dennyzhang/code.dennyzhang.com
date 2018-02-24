# Leetcode: Consecutive Available Seats     :BLOG:Medium:


---

Consecutive Available Seats  

---

Similar Problems:  
-   [Review: SQL Problems](https://brain.dennyzhang.com/review-sql)

---

Several friends at a cinema ticket office would like to reserve consecutive available seats.  
Can you help to query all the consecutive available seats order by the seat\_id using the following cinema table?  

    | seat_id | free |
    |---------|------|
    | 1       | 1    |
    | 2       | 0    |
    | 3       | 1    |
    | 4       | 1    |
    | 5       | 1    |

Your query should return the following result for the sample case above.  

    | seat_id |
    |---------|
    | 3       |
    | 4       |
    | 5       |

Note:  
-   The seat\_id is an auto increment int, and free is bool ('1' means free, and '0' means occupied.).
-   Consecutive available seats are more than 2(inclusive) seats consecutively available.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/consecutive-available-seats)  

Credits To: [leetcode.com](https://leetcode.com/problems/consecutive-available-seats/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/consecutive-available-seats
    select distinct t1.seat_id
    from cinema as t1 join cinema as t2
    on abs(t1.seat_id-t2.seat_id)=1
    where t1.free='1' and t2.free='1'
    order by t1.seat_id