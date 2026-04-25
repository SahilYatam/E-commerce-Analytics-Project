-- "Status distribution" = How many orders exist for each status


SELECT 
    order_status,
    COUNT(*) AS total_orders
FROM orders
GROUP BY order_status;



-- Orders avarage size = Average number of items per order


SELECT
    AVG(o.total_item) AS avg_order_size
FROM orders o
WHERE o.order_status = 'completed';


-- Orders trend

SELECT
    DATE_TRUNC('day', o.created_at) AS day,
    COUNT(*) AS total_orders
FROM orders o
WHERE o.order_status = 'completed'
GROUP BY day
ORDER BY day;


