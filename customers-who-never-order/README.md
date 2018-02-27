# Leetcode: Customers Who Never Order     :BLOG:Medium:


---

Customers Who Never Order  

---

Similar Problems:  
-   [Review: SQL Problems](https://brain.dennyzhang.com/review-sql), [Tag: #sql](https://brain.dennyzhang.com/tag/sql)

---

Suppose that a website contains two tables, the Customers table and the Orders table. Write a SQL query to find all customers who never order anything.  

Table: Customers.  

    +----+-------+
    | Id | Name  |
    +----+-------+
    | 1  | Joe   |
    | 2  | Henry |
    | 3  | Sam   |
    | 4  | Max   |
    +----+-------+

Table: Orders.  

    +----+------------+
    | Id | CustomerId |
    +----+------------+
    | 1  | 3          |
    | 2  | 1          |
    +----+------------+

Using the above tables as example, return the following:  

    +-----------+
    | Customers |
    +-----------+
    | Henry     |
    | Max       |
    +-----------+

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/customers-who-never-order)  

Credits To: [leetcode.com](https://leetcode.com/problems/customers-who-never-order/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/customers-who-never-order
    select Customers.Name as Customers
    from Customers left join Orders on Customers.Id = Orders.CustomerId
    where Orders.CustomerId is Null;