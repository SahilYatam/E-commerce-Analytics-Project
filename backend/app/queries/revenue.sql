-- Totoal Revenue
SELECT 
    SUM(total_price) 
FROM orders
WHERE status = 'completed'


-- Totoal Orders
SELECT COUNT(*) FROM orders

-- Avg Orders Value
SELECT 
    AVG(total_price) AS avg-value
FROM orders


-- Daily Revenue
SELECT
    DATE_TRUNC('day', created_at) AS day,
    SUM(total_price) AS Daily-Revenue
FROM orders
WHERE status = 'completed'
GROUP BY day
ORDER BY day;


-- Monthly Revenue
SELECT
    DATE_TRUNC('month', created_at) AS month,
    SUM(total_price) AS Monthly-Revenue
FROM orders
WHERE status = 'completed'
GROUP BY month
ORDER BY month;

