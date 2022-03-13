# Write your MySQL query statement below


with all_calls as 
(	select caller_id
		,extract(day from call_time)
	    ,call_time
	    ,recipient_id
	    
	   -- ,rank() over(partition by caller_id , extract(day from call_time) order by call_time desc)
	    , case when (rank() over(partition by caller_id , extract(day from call_time) order by call_time desc) )= 1 then 1 else 0 end last_call
	    , case when (rank() over(partition by caller_id , extract(day from call_time) order by call_time asc) )= 1 then 1 else 0 end first_call
	from (select caller_id , recipient_id, call_time from calls union select  recipient_id,caller_id , call_time from calls) X
	order by call_time

)
,
first_call as (
 select cast(call_time as date) call_date
 		, caller_id
 		,recipient_id
 		from all_calls 
 		where first_call = 1
 		
 		),
 		
last_call as (
 select cast(call_time as date) call_date
 		, caller_id
 		,recipient_id
 		from all_calls 
 		where last_call = 1
 		
 		)
 		
 		

 		
 		
 		
 		select  F.caller_id as user_id
 		from first_call F
 		join last_call L
 		ON F.call_date = L.call_date 
 		and F.caller_id  = L.caller_id
 		and F.recipient_id = l.recipient_id
 		group by 1


