with cte as
(select employee_id, experience, sum(salary) over(partition by experience order by salary) as sum_sal
from candidates01) 

select employee_id from cte where experience='Senior' and sum_sal<=70000
union 
select employee_id from cte where experience='Junior' and sum_sal < (70000-coalesce((select sum_sal from cte where experience='Senior' and sum_sal<=70000 order by sum_sal desc limit 1),0))

--- 