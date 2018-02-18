# Leetcode: Classes More Than 5 Students     :BLOG:Medium:


---

Classes More Than 5 Students  

---

Similar Problems:  
-   Tag: [#sql](https://brain.dennyzhang.com/tag/sql)

---

There is a table courses with columns: student and class  

Please list out all classes which have more than or equal to 5 students.  

For example, the table:  

    +---------+------------+
    | student | class      |
    +---------+------------+
    | A       | Math       |
    | B       | English    |
    | C       | Math       |
    | D       | Biology    |
    | E       | Math       |
    | F       | Computer   |
    | G       | Math       |
    | H       | Math       |
    | I       | Math       |
    +---------+------------+

Should output:  

    +---------+
    | class   |
    +---------+
    | Math    |
    +---------+

Note:  
The students should not be counted duplicate in each course.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/classes-more-than-5-students)  

Credits To: [leetcode.com](https://leetcode.com/problems/classes-more-than-5-students/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/classes-more-than-5-students
    
    select class from courses
    group by class having count(distinct student)>=5;