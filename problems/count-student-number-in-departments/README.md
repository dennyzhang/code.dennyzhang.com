
# Leetcode: Count Student Number in Departments     :BLOG:Medium:

---

Count Student Number in Departments  

---

Similar Problems:  

-   [Review: SQL Problems](https://code.dennyzhang.com/review-sql), [Tag: #sql](https://code.dennyzhang.com/tag/sql)

---

A university uses 2 data tables, student and department, to store data about its students and the departments associated with each major.  

Write a query to print the respective department name and number of students majoring in each department for all departments in the department table (even ones with no current students).  

Sort your results by descending number of students; if two or more departments have the same number of students, then sort those departments alphabetically by department name.  

The student is described as follow:  

    | Column Name  | Type      |
    |--------------|-----------|
    | student_id   | Integer   |
    | student_name | String    |
    | gender       | Character |
    | dept_id      | Integer   |

where student\_id is the student's ID number, student\_name is the student's name, gender is their gender, and dept\_id is the department ID associated with their declared major.  

And the **department** table is described as below:  

    | Column Name | Type    |
    |-------------|---------|
    | dept_id     | Integer |
    | dept_name   | String  |

where dept\_id is the department's ID number and dept\_name is the department name.  

Here is an example input:  
**student** table:  

    | student_id | student_name | gender | dept_id |
    |------------|--------------|--------|---------|
    | 1          | Jack         | M      | 1       |
    | 2          | Jane         | F      | 1       |
    | 3          | Mark         | M      | 2       |

**department** table:  

    | dept_id | dept_name   |
    |---------|-------------|
    | 1       | Engineering |
    | 2       | Science     |
    | 3       | Law         |

The Output should be:  

    | dept_name   | student_number |
    |-------------|----------------|
    | Engineering | 2              |
    | Science     | 1              |
    | Law         | 0              |

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/problems/count-student-number-in-departments)  

Credits To: [leetcode.com](https://leetcode.com/problems/count-student-number-in-departments/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/count-student-number-in-departments
    select dept_name, 
      sum(case when student_id is null then 0 else 1 end) as student_number
    from department left join student
    on department.dept_id = student.dept_id
    group by department.dept_id
    order by student_number desc, dept_name

