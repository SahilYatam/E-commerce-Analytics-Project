-- Top 10 Selling Products

SELECT
    p.id,
    p.name,
    p.price,
    SUM(oi.quantity) AS total_sold
FROM order_items oi
INNER JOIN orders o
    ON oi.order_id = o.id
INNER JOIN products p
    ON oi.product_id = p.id
WHERE o.order_status = 'completed'
GROUP BY p.id, p.name, p.price
ORDER BY total_sold DESC
LIMIT 10;

-- Low Stock Products

SELECT 
    id,
    name,
    stock_qty,
    price,
    category
FROM products
WHERE stock_qty > 0
    AND stock_qty < $1
ORDER BY stock_qty ASC
LIMIT 50;

-- Get Product by Category
SELECT 
    id,
    name,
    stock_qty,
    price,
    category
FROM products
WHERE category = $1;

-- Top category per month

SELECT month, category, total_revenue
FROM(
    SELECT
        DATE_TRUNC('month', o.created_at) AS month, p.category,
        SUM(oi.quantity * oi.price_at_time) AS total_revenue,
        RANK() OVER(
            PARTITION BY DATE_TRUNC('month', o.created_at)
            ORDER BY SUM(oi.quantity * oi.price_at_time) DESC
        ) AS rank
    FROM order_items oi
    INNER JOIN orders o
        ON oi.order_id = o.id
    INNER JOIN products p
        ON oi.product_id = p.id
    WHERE o.order_status = 'completed'
    GROUP BY month, p.category
) ranked
WHERE rank = 1
ORDER BY month;

