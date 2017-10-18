;; https://leetcode.com/problems/duplicate-emails/description/

select Email
from Person
group by Email
having count(Email)>1;