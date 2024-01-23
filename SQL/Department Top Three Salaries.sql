/*

Table: Employee
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| id           | int     |
| name         | varchar |
| salary       | int     |
| departmentId | int     |
+--------------+---------+
id is the primary key (column with unique values) for this table.
departmentId is a foreign key (reference column) of the ID from the Department table.
Each row of this table indicates the ID, name, and salary of an employee. It also contains the ID of their department.
 

Table: Department

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table indicates the ID of a department and its name.
 

A company's executives are interested in seeing who earns the most money in each of the company's departments. A high earner in a department is an employee who has a salary in the top three unique salaries for that department.

Write a solution to find the employees who are high earners in each of the departments.

Return the result table in any order.

The result format is in the following example.
*/

select d.name as department, e.name as employee, e.salary
from Employee e
join Department d on e.departmentId = d.id
where (select count(distinct salary) from Employee where departmentId = d.id and salary > e.salary) < 3

-- USING RANK 

select department,employee,salary
from (
    select d.name as department, e.name as employee, e.salary
    ,dense_rank() over(partition by d.name order by  e.salary desc ) as rnk
    from Employee e
    join Department d on e.departmentId = d.id
) A
where rnk <4
--- dense rank assigns same rank for same salary
-- rank assigns same rank for same salary but skips the next rank 1,2,2,4 like that 
-- row number assigns unique rank for each row 1,2,3,4 like that 