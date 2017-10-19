# https://leetcode.com/problems/trips-and-users/description/

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
