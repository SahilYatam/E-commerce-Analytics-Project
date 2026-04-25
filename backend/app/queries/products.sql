-- Top 10 Selling Products

SELECT
    p.id,
    p.name,
    p.price,
    SUM(oi.quantity) AS total_sold
FROM order_items oi
INNER JOIN orders o
    ON oi.order_id = p.id
INNER JOIN products p
    ON oi.product_id = p.id
WHERE o.status = 'completed'
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

SELECT
    o.id,
    o.total_item,
    o.total_price,
    o.order_status,
    o.created_at
FROM orders o
WHERE o.order_status = 'completed'
INNER JOIN products p


