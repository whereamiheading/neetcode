# Write your MySQL query statement below
select name as Customers
from customers c
left join orders o on o.customerid = c.id
where o.id is null