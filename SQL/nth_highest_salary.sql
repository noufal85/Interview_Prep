'''
Table: Employee

+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
id is the primary key (column with unique values) for this table.
Each row of this table contains information about the salary of an employee.
 

Write a solution to find the nth highest salary from the Employee table. If there is no nth highest salary, return null.

The result format is in the following example.

 

Example 1:

Input: 
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
n = 2
Output: 
+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| 200                    |
+------------------------+
Example 2:

Input: 
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
+----+--------+
n = 2
Output: 
+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| null                   |
+------------------------+
'''


CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      SELECT distinct(sub.salary) from
      (
      select salary, dense_rank() over (order by salary DESC) as r
        from employee) as sub
        where sub.r = N
  );
END


CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  DECLARE M INT;
  SET M = IF(N > 1, N - 1, 0);
  RETURN (
    SELECT salary FROM Employee ORDER BY salary DESC LIMIT 1 OFFSET M
  );
END

-- improved version 
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  DECLARE M INT;
  SET M = IF(N > 1, N - 1, 0);
  SET @salary = (
    SELECT salary FROM Employee ORDER BY salary DESC LIMIT 1 OFFSET M
  );
  
  IF @salary IS NULL THEN
    RETURN NULL;
  ELSE
    RETURN @salary;
  END IF;
END