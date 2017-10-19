;; https://leetcode.com/problems/swap-salary/
update salary
set sex =
    case
    when sex = 'm' then 'f'
    when sex = 'f' then 'm'
    end;
