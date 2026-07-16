# Write your MySQL query statement below
select e.name as employee
from employee e
JOIN employee m
on e.managerID = m.id
where e.salary  > m.salary;