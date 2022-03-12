select d.Name AS 'Department', e1.Name AS 'Employee', e1.Salary
from Employee e1
    Join Department D on e1.DepartmentId = d.Id
where 3 > 
      ( select count(distinct e2.salary)
       from Employee e2
       where e2.Salary> e1.Salary
        AND e1.DepartmentId = e2.DepartmentId
      )