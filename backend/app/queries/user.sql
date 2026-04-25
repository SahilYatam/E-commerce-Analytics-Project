-- Top customers

SELECT 
    u.id,
    u.name,
    SUM(o.total_price) AS total_spent
FROM orders o
INNER JOIN users u
    ON o.user_id = u.id
WHERE o.order_status = 'completed'
GROUP BY u.id, u.name
ORDER BY total_spent DESC
LIMIT 10;


-- Lifetime value

SELECT 
    u.id,
    u.name,
    SUM(o.total_price) AS lifetime_value
FROM orders o
INNER JOIN users u
    ON o.user_id = u.id
WHERE o.order_status = 'completed'
GROUP BY u.id, u.name;

-- New User vs Returning User

SELECT
    COUNT(CASE WHEN order_count = 1 THEN 1 END) AS new_users,
    COUNT(CASE WHEN order_count > 1 THEN 1 END) AS returning_users
FROM (
    SELECT
        user_id,
        COUNT(*) AS order_count
    FROM orders
    WHERE order_status = 'completed'
    GROUP BY user_id
) AS user_orders;


