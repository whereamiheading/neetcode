# Write your MySQL query statement below
select u.name, sum(case when distance is null then 0 else distance end) as travelled_distance
from users u
left join rides r on u.id = r.user_Id
group by u.id
order by 2 desc , 1 asc