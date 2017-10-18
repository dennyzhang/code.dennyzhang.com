;; https://leetcode.com/problems/delete-duplicate-emails/description/

delete t1 from Person as t1 inner join Person as t2
on t1.Email = t2.Email
where t1.Id > t2.Id
