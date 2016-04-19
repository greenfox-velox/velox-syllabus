SELECT *
FROM todo.user
LIMIT 1, 2;

SELECT *
FROM todo.user
WHERE country='Hungary';

SELECT *
FROM todo.user
WHERE country LIKE 'U%';

SELECT count(user_id) AS 'count', country
FROM todo.user
GROUP BY country;

SELECT country, name
FROM todo.user
ORDER BY country, name;

SELECT count(user_id) AS 'count', country
FROM todo.user
GROUP BY country
HAVING count > 1;

SELECT *
FROM todo.todo LEFT JOIN todo.user
ON user.user_id = todo.user_id;

SELECT *
FROM todo.todo, todo.user
WHERE user.user_id = todo.user_id
