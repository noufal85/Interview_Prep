/*
SALES
* day <date yyyy-mm-dd>
* store_id
* product_id
* sales_amount
* customer_id

PRODUCTS
* prod_id
* prod_name

2021-08-01 100 123 12.50
2021-08-01 100 123 12.50
2021-08-01 102 123 12.50
2021-08-05 100 124 14.50
2021-08-01 103 123 12.50

123 ABC
124 XYZ
125 PGS

-- expected result

100
102
103


- the top 10 selling stores in August 2018
*/

select store_id,

select SUM(sales_amount) as total_sales,

DENSE_RANK() OVER (ORDER BY store_id DESC) as top_stores
from Sales where day BETWEEN '2018-08-01' AND '2018-08-30' ORDER BY sales_amount limit 10;

-- sales table 1 day of data , Find out products that has no sale on that day
-- expected result
ABC
XYZ

select p.prod_name
from


-- total sales from the table

select SUM(sales_amount) as total sales from SALES

-- total sales for each day
select SUM(sales_amount) as total sales, day from SALES GROUP BY day

08/01 100
08/02 500
08/03 300

-- Find out the day on which we have the most sales
select day, MAX(sales_amount) as Max_sales from SALES ORDER BY day, MAx_sales DESC;
