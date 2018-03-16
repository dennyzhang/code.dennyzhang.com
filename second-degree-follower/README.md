# Leetcode: Second Degree Follower     :BLOG:Basic:


---

Second Degree Follower  

---

Similar Problems:  
-   [Review: SQL Problems](https://brain.dennyzhang.com/review-sql), [Tag: #sql](https://brain.dennyzhang.com/tag/sql)

---

In facebook, there is a follow table with two columns: followee, follower.  

Please write a sql query to get the amount of each follower's follower if he/she has one.  

For example:  

    +-------------+------------+
    | followee    | follower   |
    +-------------+------------+
    |     A       |     B      |
    |     B       |     C      |
    |     B       |     D      |
    |     D       |     E      |
    +-------------+------------+

should output:  

    +-------------+------------+
    | follower    | num        |
    +-------------+------------+
    |     B       |  2         |
    |     D       |  1         |
    +-------------+------------+

Explaination:  
Both B and D exist in the follower list, when as a followee, B's follower is C and D, and D's follower is E. A does not exist in follower list.  

Note:  
Followee would not follow himself/herself in all cases.  
Please display the result in follower's alphabet order.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/second-degree-follower)  

Credits To: [leetcode.com](https://leetcode.com/problems/second-degree-follower/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/second-degree-follower