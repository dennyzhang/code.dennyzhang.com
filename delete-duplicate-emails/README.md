# Leetcode: Delete Duplicate Emails     :BLOG:Medium:


---

Delete Duplicate Emails  

---

Similar Problems:  
-   [Review: SQL Problems](https://brain.dennyzhang.com/review-sql)

---

Write a SQL query to delete all duplicate email entries in a table named Person, keeping only unique emails based on its smallest Id.  

    +----+------------------+
    | Id | Email            |
    +----+------------------+
    | 1  | john@example.com |
    | 2  | bob@example.com  |
    | 3  | john@example.com |
    +----+------------------+
    Id is the primary key column for this table.

For example, after running your query, the above Person table should have the following rows:  

    +----+------------------+
    | Id | Email            |
    +----+------------------+
    | 1  | john@example.com |
    | 2  | bob@example.com  |
    +----+------------------+

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/delete-duplicate-emails)  

Credits To: [leetcode.com](https://leetcode.com/problems/delete-duplicate-emails/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/delete-duplicate-emails
    delete t1 from Person as t1 inner join Person as t2
    on t1.Email = t2.Email
    where t1.Id > t2.Id