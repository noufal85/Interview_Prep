# Write your MySQL query statement below


select id ,visit_date, people  
from 
	(
	select id,visit_date, people 
	,case when people>= 100 then 1 else 0 end C1
	,case when lead(people) over (order by id) >= 100  then 1
		 else 0 end day_1
	,case when lead(people,2) over (order by id) >= 100 then 1
		  else 0 end day_2

	,case when lag(people) over (order by id) >= 100  then 1
		 else 0 end day_11
	,case when lag(people,2) over (order by id) >= 100 then 1
		  else 0 end day_21

	from stadium 
	) X
where 1=1
and C1 = 1
and (( day_1 +day_2  > 1) or ( day_11 +day_21  > 1)or (day_1+day_11) > 1)
