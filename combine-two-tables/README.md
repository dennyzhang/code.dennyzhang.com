# Leetcode: Combine Two Tables     :BLOG:Medium:


---

Combine Two Tables  

---

Similar Problems:  
-   [Review: SQL Problems](https://brain.dennyzhang.com/review-sql)

---

Table: Person  

    +-------------+---------+
    | Column Name | Type    |
    +-------------+---------+
    | PersonId    | int     |
    | FirstName   | varchar |
    | LastName    | varchar |
    +-------------+---------+
    PersonId is the primary key column for this table.

Table: Address  

    +-------------+---------+
    | Column Name | Type    |
    +-------------+---------+
    | AddressId   | int     |
    | PersonId    | int     |
    | City        | varchar |
    | State       | varchar |
    +-------------+---------+
    AddressId is the primary key column for this table.

Write a SQL query for a report that provides the following information for each person in the Person table, regardless if there is an address for each of those people:  

FirstName, LastName, City, State  

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/combine-two-tables)  

Credits To: [leetcode.com](https://leetcode.com/problems/combine-two-tables/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/combine-two-tables
    select Person.FirstName, Person.LastName, Address.City, Address.State
    from Person left join Address on Person.PersonId = Address.PersonId;