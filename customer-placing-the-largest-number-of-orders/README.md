# Leetcode: Customer Placing the Largest Number of Orders     :BLOG:Medium:


---

Customer Placing the Largest Number of Orders  

---

Similar Problems:  
-   [Review: SQL Problems](https://code.dennyzhang.com/review-sql), [Tag: #sql](https://code.dennyzhang.com/tag/sql)

---

Query the customer\_number from the orders table for the customer who has placed the largest number of orders.  

It is guaranteed that exactly one customer will have placed more orders than any other customer.  

The orders table is defined as follows:  

    | Column            | Type      |
    |-------------------|-----------|
    | order_number (PK) | int       |
    | customer_number   | int       |
    | order_date        | date      |
    | required_date     | date      |
    | shipped_date      | date      |
    | status            | char(15)  |
    | comment           | char(200) |

Sample Input  

    | order_number | customer_number | order_date | required_date | shipped_date | status | comment |
    |--------------|-----------------|------------|---------------|--------------|--------|---------|
    | 1            | 1               | 2017-04-09 | 2017-04-13    | 2017-04-12   | Closed |         |
    | 2            | 2               | 2017-04-15 | 2017-04-20    | 2017-04-18   | Closed |         |
    | 3            | 3               | 2017-04-16 | 2017-04-25    | 2017-04-20   | Closed |         |
    | 4            | 3               | 2017-04-18 | 2017-04-28    | 2017-04-25   | Closed |         |

Sample Output  

    | customer_number |
    |-----------------|
    | 3               |

Explanation  

    The customer with number '3' has two orders, which is greater than either customer '1' or '2' because each of them  only has one order. 
    So the result is customer_number '3'.

Follow up: What if more than one customer have the largest number of orders, can you find all the customer\_number in this case?  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/customer-placing-the-largest-number-of-orders)  

Credits To: [leetcode.com](https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/customer-placing-the-largest-number-of-orders
    
    # assume: only one match
    select customer_number from orders
    group by customer_number
    order by count(1) desc
    limit 1
    
    ## assum: multiple matches
    ##  1 1
    ##  2 1
    ##  3 1
    ##
    ##  1 1 1 1
    ##  1 1 2 1
    ##  1 1 3 1
    ##
    ##  select t1.customer_number
    ##  from (select customer_number, count(1) as count
    ##        from orders group by customer_number) as t1,
    ##        (select customer_number, count(1) as count
    ##        from orders group by customer_number) as t2
    ##  group by t1.customer_number
    ##  having max(t1.count) = max(t2.count)