--Q1. ---------------------------------------------------------------
-------what %age of products have both low fat and recycable---
select --product_id, case when is_low_fat = 1 and is_recyclable = 1 then 1 else 0 end as total_count
 sum(case when is_low_fat = 1 and is_recyclable = 1 then 1 else 0 end) * 100.0 / count(*) as percentage
from product

--Q2.  ---------------------------------------------------------------
 -------find top 5 sales products having promotions-------------
 select top 5 product_id from sales
 where promotion_id is not null
 group by product_id
 order by sum(store_cost * units_sold) desc

--Q3.     ---------------------------------------------------------------
------- what %age of sales happened on first and last day of the promotion-------
select s.promotion_id,
 round((sum(case when s.transaction_date = (p.promo_start_date) 
            or s.transaction_date = (p.promo_end_date) then (store_cost * units_sold) else 0 end) * 100.0
 / sum((store_cost * units_sold))),2)
 from sales s inner join  promotion p on p.promotion_id = s.promotion_id
 group by s.promotion_id

--Q4.  -------Which product had the highest sales with promotions-------
 select s.product_id, p.product_name, sum (s.store_cost * s.units_sold) 
 from sales s, product p
 where s.product_id = p.product_id and s.product_id is not null
 group by s.product_id , p.product_name
 order by sum (s.store_cost * s.units_sold) desc
 
--Q8. ------------------------------------------------------------
-------top 3 product classes by total sales----------------
select top 3 p.product_class_name, sum(s.units_sold * s.store_cost) as total_sale
from sales s, product p
where p.product_id = s.product_id
group by p.product_class_name
order by sum(s.units_sold * s.store_cost) desc 