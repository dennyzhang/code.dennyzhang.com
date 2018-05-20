# Leetcode: Get Highest Answer Rate Question     :BLOG:Medium:


---

Get Highest Answer Rate Question  

---

Similar Problems:  
-   [Review: SQL Problems](https://code.dennyzhang.com/review-sql), [Tag: #sql](https://code.dennyzhang.com/tag/sql)

---

Get the highest answer rate question from a table survey\_log with these columns: uid, action, question\_id, answer\_id, q\_num, timestamp.  

uid means user id; action has these kind of values: "show", "answer", "skip"; answer\_id is not null when action column is "answer", while is null for "show" and "skip"; q\_num is the numeral order of the question in current session.  

Write a sql query to identify the question which has the highest answer rate.  

Example:  
Input:  

    +------+-----------+--------------+------------+-----------+------------+
    | uid  | action    | question_id  | answer_id  | q_num     | timestamp  |
    +------+-----------+--------------+------------+-----------+------------+
    | 5    | show      | 285          | null       | 1         | 123        |
    | 5    | answer    | 285          | 124124     | 1         | 124        |
    | 5    | show      | 369          | null       | 2         | 125        |
    | 5    | skip      | 369          | null       | 2         | 126        |
    +------+-----------+--------------+------------+-----------+------------+

Output:  

    +-------------+
    | survey_log  |
    +-------------+
    |    285      |
    +-------------+

Explanation:  
question 285 has answer rate 1/1, while question 369 has 0/1 answer rate, so output 285.  

Note: The highest answer rate meaning is: answer number's ratio in show number in the same question.  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/get-highest-answer-rate-question)  

Credits To: [leetcode.com](https://leetcode.com/problems/get-highest-answer-rate-question/description/)  

Leave me comments, if you have better ways to solve.  

---

    ## Blog link: https://code.dennyzhang.com/get-highest-answer-rate-question
    select question_id as survey_log
    from (
        select question_id, 
            sum(case when action='show' then 1 else 0 end) as show_count,
            sum(case when action='answer' then 1 else 0 end) as answer_count
        from survey_log
        group by question_id) as t
    order by answer_count/show_count desc
    limit 1