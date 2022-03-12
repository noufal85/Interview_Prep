https://leetcode.com/problems/average-salary-departments-vs-company/

create table salary01 (
id int,
employee_id int,
amount int,
pay_date date)
;

create table employee01 (
employee_id int,
department_id int )
;

insert into  salary01 values(1,1,9000,'2017-03-31');
insert into  salary01 values(2,2,6000,'2017-03-31');
insert into  salary01 values(3,3,10000,'2017-03-31');
insert into  salary01 values(4,1,7000,'2017-02-28');
insert into  salary01 values(5,2,6000,'2017-02-28');
insert into  salary01 values(6,3,8000,'2017-02-28');


insert into employee01 values(1,1);
insert into employee01 values(2,2);
insert into employee01 values(3,2);
commit
;


select * from salary01


select pay_month
	,department_id 
	, case when dep_avg  > tot_avg  then 'higher'
		  when dep_avg  < tot_avg  then 'lower'
		  else 'same' end comparison
		from (

				select extract(year from pay_date)||'-'||extract(month from pay_date) pay_month
					,department_id 
					,avg(amount) over (partition by department_id,extract(year from pay_date)||'-'||extract(month from pay_date) ) as dep_avg
					,avg(amount) over (partition by extract(year from pay_date)||'-'||extract(month from pay_date)) tot_avg
				from salary01 s
				join employee01 e
				on s.employee_id = e.employee_id 
				order by pay_date 
				
				) D
	group by 1,2,3
