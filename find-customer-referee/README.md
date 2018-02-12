# Leetcode: Find Customer Referee     :BLOG:Medium:


---

Find Customer Referee  

---

Similar Problems:  
-   Tag: [#sql](https://brain.dennyzhang.com/tag/sql)

---

Given a table customer holding customers information and the referee.  

    +------+------+-----------+
    | id   | name | referee_id|
    +------+------+-----------+
    |    1 | Will |      NULL |
    |    2 | Jane |      NULL |
    |    3 | Alex |         2 |
    |    4 | Bill |      NULL |
    |    5 | Zack |         1 |
    |    6 | Mark |         2 |
    +------+------+-----------+

Write a query to return the list of customers NOT referred by the person with id '2'.  

For the sample data above, the result is:  

    +------+
    | name |
    +------+
    | Will |
    | Jane |
    | Bill |
    | Zack |
    +------+

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/find-customer-referee)  

Credits To: [leetcode.com](https://leetcode.com/problems/find-customer-referee/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/find-customer-referee
    select name
    from customer
    where referee_id != '2' or referee_id is null;