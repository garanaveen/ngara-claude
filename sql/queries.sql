-- Useful example queries against the playground schema

-- 1. All active employees with their department
SELECT
    e.id,
    e.first_name || ' ' || e.last_name AS full_name,
    e.email,
    e.role,
    e.salary,
    d.name AS department
FROM employees e
LEFT JOIN departments d ON d.id = e.department_id
WHERE e.active = TRUE
ORDER BY d.name, e.last_name;

-- 2. Average salary per department (active employees only)
SELECT
    d.name AS department,
    COUNT(e.id)           AS headcount,
    ROUND(AVG(e.salary), 2) AS avg_salary,
    MIN(e.salary)         AS min_salary,
    MAX(e.salary)         AS max_salary
FROM employees e
JOIN departments d ON d.id = e.department_id
WHERE e.active = TRUE
GROUP BY d.name
ORDER BY avg_salary DESC;

-- 3. Top-selling products by revenue
SELECT
    p.name AS product,
    SUM(oi.quantity)                        AS units_sold,
    SUM(oi.quantity * oi.unit_price)        AS total_revenue
FROM order_items oi
JOIN products p ON p.id = oi.product_id
JOIN orders o ON o.id = oi.order_id
WHERE o.status NOT IN ('cancelled')
GROUP BY p.name
ORDER BY total_revenue DESC;

-- 4. Orders placed in the last 30 days with status breakdown
SELECT
    status,
    COUNT(*) AS order_count,
    SUM(total) AS total_value
FROM orders
WHERE created_at >= NOW() - INTERVAL '30 days'
GROUP BY status
ORDER BY order_count DESC;

-- 5. Employees who haven't placed any orders
SELECT
    e.first_name || ' ' || e.last_name AS full_name,
    e.email
FROM employees e
LEFT JOIN orders o ON o.employee_id = e.id
WHERE o.id IS NULL
  AND e.active = TRUE;

-- 6. Running total of revenue by order date
SELECT
    DATE(o.created_at) AS order_date,
    SUM(o.total)       AS daily_revenue,
    SUM(SUM(o.total)) OVER (ORDER BY DATE(o.created_at)) AS running_total
FROM orders o
WHERE o.status = 'delivered'
GROUP BY order_date
ORDER BY order_date;
