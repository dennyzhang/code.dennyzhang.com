# Leetcode: Trips and Users     :BLOG:Hard:


---

Trips and Users  

---

Similar Problems:  
-   Tag: [#sql](https://brain.dennyzhang.com/tag/sql)

---

The Trips table holds all taxi trips. Each trip has a unique Id, while Client\_Id and Driver\_Id are both foreign keys to the Users\_Id at the Users table. Status is an ENUM type of ('completed', 'cancelled\_by\_driver', 'cancelled\_by\_client').  

    +----+-----------+-----------+---------+--------------------+----------+
    | Id | Client_Id | Driver_Id | City_Id |        Status      |Request_at|
    +----+-----------+-----------+---------+--------------------+----------+
    | 1  |     1     |    10     |    1    |     completed      |2013-10-01|
    | 2  |     2     |    11     |    1    | cancelled_by_driver|2013-10-01|
    | 3  |     3     |    12     |    6    |     completed      |2013-10-01|
    | 4  |     4     |    13     |    6    | cancelled_by_client|2013-10-01|
    | 5  |     1     |    10     |    1    |     completed      |2013-10-02|
    | 6  |     2     |    11     |    6    |     completed      |2013-10-02|
    | 7  |     3     |    12     |    6    |     completed      |2013-10-02|
    | 8  |     2     |    12     |    12   |     completed      |2013-10-03|
    | 9  |     3     |    10     |    12   |     completed      |2013-10-03| 
    | 10 |     4     |    13     |    12   | cancelled_by_driver|2013-10-03|
    +----+-----------+-----------+---------+--------------------+----------+

The Users table holds all users. Each user has an unique Users\_Id, and Role is an ENUM type of ('client', 'driver', 'partner').  

    +----------+--------+--------+
    | Users_Id | Banned |  Role  |
    +----------+--------+--------+
    |    1     |   No   | client |
    |    2     |   Yes  | client |
    |    3     |   No   | client |
    |    4     |   No   | client |
    |    10    |   No   | driver |
    |    11    |   No   | driver |
    |    12    |   No   | driver |
    |    13    |   No   | driver |
    +----------+--------+--------+

Write a SQL query to find the cancellation rate of requests made by unbanned clients between Oct 1, 2013 and Oct 3, 2013. For the above tables, your SQL query should return the following rows with the cancellation rate being rounded to two decimal places.  

    +------------+-------------------+
    |     Day    | Cancellation Rate |
    +------------+-------------------+
    | 2013-10-01 |       0.33        |
    | 2013-10-02 |       0.00        |
    | 2013-10-03 |       0.50        |
    +------------+-------------------+

Github: [challenges-leetcode-interesting](https://github.com/DennyZhang/challenges-leetcode-interesting/tree/master/trips-and-users)  

Credits To: [leetcode.com](https://leetcode.com/problems/trips-and-users/description/)  

Leave me comments, if you have better ways to solve.  

    ## Blog link: https://brain.dennyzhang.com/trips-and-users
    select t1.Day as Day, round(COALESCE(t2.cancel_count, 0)/t1.total_count, 2) as 'Cancellation Rate' from
    (select Trips.Request_at as Day, count(1) as total_count
    from Trips inner join Users
    on Trips.Client_Id = Users.Users_Id
    where Users.Banned = 'No' and Users.Role = 'client'
    and Trips.Request_at >= '2013-10-01' and Trips.Request_at <= '2013-10-03'
    group by Trips.Request_at) t1 left join
    (select Trips.Request_at as Day,  count(1) as cancel_count
    from Trips inner join Users
    on Trips.Client_Id = Users.Users_Id
    where Users.Banned = 'No' and Users.Role = 'client'
    and Trips.Request_at >= '2013-10-01' and Trips.Request_at <= '2013-10-03'
    and Trips.Status != 'completed'
    group by Trips.Request_at) t2
    on t1.Day = t2. Day;