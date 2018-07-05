
# Leetcode: Find Cumulative Salary of an Employee     :BLOG:Hard:

---

Find Cumulative Salary of an Employee  

---

Similar Problems:  

-   [Review: SQL Problems](https://code.dennyzhang.com/review-sql), [Tag: #sql](https://code.dennyzhang.com/tag/sql)

---

The Employee table holds the salary information in a year.  

Write a SQL to get the cumulative sum of an employee's salary over a period of 3 months but exclude the most recent month.  

The result should be displayed by 'Id' ascending, and then by 'Month' descending.  

Example  
Input  

    | Id | Month | Salary |
    |----|-------|--------|
    | 1  | 1     | 20     |
    | 2  | 1     | 20     |
    | 1  | 2     | 30     |
    | 2  | 2     | 30     |
    | 3  | 2     | 40     |
    | 1  | 3     | 40     |
    | 3  | 3     | 60     |
    | 1  | 4     | 60     |
    | 3  | 4     | 70     |

Output  

    | Id | Month | Salary |
    |----|-------|--------|
    | 1  | 3     | 90     |
    | 1  | 2     | 50     |
    | 1  | 1     | 20     |
    | 2  | 1     | 20     |
    | 3  | 3     | 100    |
    | 3  | 2     | 40     |

Explanation  
Employee '1' has 3 salary records for the following 3 months except the most recent month '4': salary 40 for month '3', 30 for month '2' and 20 for month '1'  
So the cumulative sum of salary of this employee over 3 months is 90(40+30+20), 50(30+20) and 20 respectively.  

    | Id | Month | Salary |
    |----|-------|--------|
    | 1  | 3     | 90     |
    | 1  | 2     | 50     |
    | 1  | 1     | 20     |

Employee '2' only has one salary record (month '1') except its most recent month '2'.  

    | Id | Month | Salary |
    |----|-------|--------|
    | 2  | 1     | 20     |

Employ '3' has two salary records except its most recent pay month '4': month '3' with 60 and month '2' with 40. So the cumulative salary is as following.  

    | Id | Month | Salary |
    |----|-------|--------|
    | 3  | 3     | 100    |
    | 3  | 2     | 40     |

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/find-cumulative-salary-of-an-employee)  

Credits To: [leetcode.com](https://leetcode.com/problems/find-cumulative-salary-of-an-employee/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/find-cumulative-salary-of-an-employee

