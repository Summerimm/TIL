CREATE TABLE users (
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  age INTEGER NOT NULL,
  country TEXT NOT NULL,
  phone TEXT NOT NULL,
  balance INT NOT NULL
);

SELECT first_name, age, balance FROM users
ORDER BY age, balance DESC;

SELECT first_name, age FROM users
ORDER BY first_name ASC, age DESC;

SELECT first_name, country from users
WHERE first_name LIKE '건우' AND country LIKE '경기도';

SELECT * from users
WHERE age BETWEEN
