# Write your MySQL query statement below
select d.name as Department , e.name as Employee , e.salary as Salary 
from employee as e 
join department as d
on e.departmentID = d.id
join (select departmentID , max(salary) as max_salary from employee group by departmentID ) as m
on e.departmentID = m.departmentID
where e.salary = m.max_salary;