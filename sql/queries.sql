-- Примеры SQL-запросов для портфолио

-- 1. Выборка всех пользователей
SELECT * FROM users;

-- 2. Выборка пользователей старше 18 лет
SELECT name, age, city FROM users WHERE age > 18;

-- 3. Объединение двух таблиц (пользователи и заказы)
SELECT u.name, o.order_date, o.total
FROM users u
JOIN orders o ON u.id = o.user_id;

-- 4. Группировка: сколько заказов у каждого пользователя
SELECT u.name, COUNT(o.id) AS order_count
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
GROUP BY u.name
ORDER BY order_count DESC;

-- 5. Поиск пользователей из Москвы
SELECT * FROM users WHERE city = 'Москва';
