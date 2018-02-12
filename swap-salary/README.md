# Leetcode: Swap Salary     :BLOG:Medium:


---

Swap Salary  

---

Similar Problems:  
-   Tag: [#sql](https://brain.dennyzhang.com/tag/sql)

---

Given a table salary, such as the one below, that has m=male and f=female values. Swap all f and m values (i.e., change all f values to m and vice versa) with a single update query and no intermediate temp table.  
For example:  

    | id | name | sex | salary |
    |----|------|-----|--------|
    | 1  | A    | m   | 2500   |
    | 2  | B    | f   | 1500   |
    | 3  | C    | m   | 5500   |
    | 4  | D    | f   | 500    |

After running your query, the above salary table should have the following rows:  

    | id | name | sex | salary |
    |----|------|-----|--------|
    | 1  | A    | f   | 2500   |
    | 2  | B    | m   | 1500   |
    | 3  | C    | f   | 5500   |
    | 4  | D    | m   | 500    |

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/swap-salary)  

Credits To: [leetcode.com](https://leetcode.com/problems/swap-salary/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/swap-salary
    update salary
    set sex =
        case
        when sex = 'm' then 'f'
        when sex = 'f' then 'm'
        end;