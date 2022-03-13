# Write your MySQL query statement below

select p.player_id , coalesce(R.consec, 0) as longest_streak

from     (select distinct player_id from matches) P
left join 
(select player_id, max(consec) consec
from (
	select player_id , grouped ,result, count(*) consec
	from 
		(
		select player_id    , match_day , result 
			,sum(case when  result = 'Win' then 0 else 1 end ) over(partition by player_id order by match_day asc) grouped
		from Matches
	 )P
	 
    where result = 'Win'
    group by 1,2,3
	 ) F
	 group by 1
     
 ) R   
 on p.player_id = R.player_id