# Leetcode: Investments in 2016     :BLOG:Medium:


---

Median Employee Salary  

---

Similar Problems:  
-   [Review: SQL Problems](https://brain.dennyzhang.com/review-sql), [Tag: #sql](https://brain.dennyzhang.com/tag/sql)

---

Write a query to print the sum of all total investment values in 2016 (TIV\_2016), to a scale of 2 decimal places, for all policy holders who meet the following criteria:  

1.  Have the same TIV\_2015 value as one or more other policyholders.
2.  Are not located in the same city as any other policyholder (i.e.: the (latitude, longitude) attribute pairs must be unique).

Input Format:  
The insurance table is described as follows:  

    | Column Name | Type          |
    |-------------|---------------|
    | PID         | INTEGER(11)   |
    | TIV_2015    | NUMERIC(15,2) |
    | TIV_2016    | NUMERIC(15,2) |
    | LAT         | NUMERIC(5,2)  |
    | LON         | NUMERIC(5,2)  |

where PID is the policyholder's policy ID, TIV\_2015 is the total investment value in 2015, TIV\_2016 is the total investment value in 2016, LAT is the latitude of the policy holder's city, and LON is the longitude of the policy holder's city.  

Sample Input  

    | PID | TIV_2015 | TIV_2016 | LAT | LON |
    |-----|----------|----------|-----|-----|
    | 1   | 10       | 5        | 10  | 10  |
    | 2   | 20       | 20       | 20  | 20  |
    | 3   | 10       | 30       | 20  | 20  |
    | 4   | 10       | 40       | 40  | 40  |

Sample Output  

    | TIV_2016 |
    |----------|
    | 45.00    |

Explanation  

    The first record in the table, like the last record, meets both of the two criteria.
    The TIV_2015 value '10' is as the same as the third and forth record, and its location unique.
    
    The second record does not meet any of the two criteria. Its TIV_2015 is not like any other policyholders.
    
    And its location is the same with the third record, which makes the third record fail, too.
    
    So, the result is the sum of TIV_2016 of the first and last record, which is 45.

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/investments-in-2016)  

Credits To: [leetcode.com](https://leetcode.com/problems/investments-in-2016/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/investments-in-2016
    select sum(TIV_2016) as TIV_2016
    from insurance
    where concat(LAT, ',', LON)
        in (select concat(LAT, ',', LON)
           from insurance
           group by LAT, LON
           having count(1) = 1)
    and TIV_2015 in
        (select TIV_2015
        from insurance
        group by TIV_2015
        having count(1)>1)