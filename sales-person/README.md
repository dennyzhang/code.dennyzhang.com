# Leetcode: Sales Person     :BLOG:Medium:


---

Sales Person  

---

Similar Problems:  
-   [Review: SQL Problems](https://brain.dennyzhang.com/review-sql)

---

Description  

Given three tables: salesperson, company, orders.  
Output all the names in the table salesperson, who didn't have sales to company 'RED'.  

Example  
Input  

Table: salesperson  

    +----------+------+--------+-----------------+-----------+
    | sales_id | name | salary | commission_rate | hire_date |
    +----------+------+--------+-----------------+-----------+
    |   1      | John | 100000 |     6           | 4/1/2006  |
    |   2      | Amy  | 120000 |     5           | 5/1/2010  |
    |   3      | Mark | 65000  |     12          | 12/25/2008|
    |   4      | Pam  | 25000  |     25          | 1/1/2005  |
    |   5      | Alex | 50000  |     10          | 2/3/2007  |
    +----------+------+--------+-----------------+-----------+

The table salesperson holds the salesperson information. Every salesperson has a sales\_id and a name.  
Table: company  

    +---------+--------+------------+
    | com_id  |  name  |    city    |
    +---------+--------+------------+
    |   1     |  RED   |   Boston   |
    |   2     | ORANGE |   New York |
    |   3     | YELLOW |   Boston   |
    |   4     | GREEN  |   Austin   |
    +---------+--------+------------+

The table company holds the company information. Every company has a com\_id and a name.  
Table: orders  

    +----------+----------+---------+----------+--------+
    | order_id |  date    | com_id  | sales_id | amount |
    +----------+----------+---------+----------+--------+
    | 1        | 1/1/2014 |    3    |    4     | 100000 |
    | 2        | 2/1/2014 |    4    |    5     | 5000   |
    | 3        | 3/1/2014 |    1    |    1     | 50000  |
    | 4        | 4/1/2014 |    1    |    4     | 25000  |
    +----------+----------+---------+----------+--------+

The table orders holds the sales record information, salesperson and customer company are represented by sales\_id and com\_id.  
output  

    +------+
    | name | 
    +------+
    | Amy  | 
    | Mark | 
    | Alex |
    +------+

Explanation  

According to order '3' and '4' in table orders, it is easy to tell only salesperson 'John' and 'Alex' have sales to company 'RED',  
so we need to output all the other names in table salesperson.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/sales-person)  

Credits To: [leetcode.com](https://leetcode.com/problems/sales-person/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/sales-person
    select name
    from salesperson
    where name not in
        (select distinct salesperson.name
        from salesperson, orders, company
        where company.name = 'RED'
        and salesperson.sales_id = orders.sales_id
        and orders.com_id = company.com_id)