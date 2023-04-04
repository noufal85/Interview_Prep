-- aggregate in 3 hour intervals 
SELECT DATE_TRUNC('hour', my_timestamp_column - INTERVAL '1 hour' * MOD(EXTRACT(hour FROM my_timestamp_column), 3)) AS three_hour_interval,
       COUNT(*),
       SUM(my_value_column)
FROM my_table
GROUP BY 1
ORDER BY 1;
