-- 문제1. users 테이블을 생성하는 쿼리문을 작성하시오.
-- CREATE TABLE users (
--   name TEXT NOT NULL,
--   phoneNumber TEXT NOT NULL,
--   email TEXT NOT NULL UNIQUE, 
--   age INTEGER,
--   gender TEXT,
--   address TEXT NOT NULL DEFAULT'no address'
-- );

CREATE TABLE users (
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  age INTEGER,
  country TEXT NOT NULL,
  phoneNumber TEXT NOT NULL,
  balance INT NOT NULL
);
-- 문제2. 제공된 users.csv 파일의 데이터를 users 테이블에 가져오시오.
-- sqlite> sqlite3 hw.sqlite3
-- sqlite> .mode csv
-- sqlite> .import users.csv users


-- 문제3. users 테이블에서 이름, 나이, 계좌 잔고를 나이가 어린순으로, 
-- 만약 같은 나이라면 계좌 잔고가 많은 순으로 정렬해서 조회하는 쿼리문 작성하시오.
SELECT first_name, last_name, age, balance FROM users 
ORDER BY age ASC, balance DESC;