-- Totoal Revenue
SELECT 
    SUM(total_price) AS total_revenue
FROM orders
WHERE status = 'completed'


-- Totoal Orders
SELECT COUNT(*) AS total_orders FROM orders

-- Avg Orders Value
SELECT 
    AVG(total_price) AS avg_order_value
FROM orders


-- Daily Revenue
SELECT
    DATE_TRUNC('day', created_at) AS day,
    SUM(total_price) AS total_revenue
FROM orders
WHERE status = 'completed'
GROUP BY day
ORDER BY day;


-- Monthly Revenue
SELECT
    DATE_TRUNC('month', created_at) AS month,
    SUM(total_price) AS total_revenue
FROM orders
WHERE status = 'completed'
GROUP BY month
ORDER BY month;

