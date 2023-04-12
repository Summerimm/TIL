-- 데일리 실습 1-1
-- 1. users 라는 테이블을 생성하고 sqlite 명령어 .schema users 로 생성된 테이블의 스키마를 확인하시오.
CREATE TABLE users (
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  age INTEGER NOT NULL,
  country TEXT NOT NULL,
  phone TEXT NOT NULL,
  balance INT NOT NULL
);

-- 2. sqlite3 명령어를 이용하여 제공된 users.csv파일의 데이터를 users 테이블에 가져오시오.
-- sqlite3 database.sqlite3
-- .mode csv
-- .import users.csv users

-- 3. users 테이블에서 이름, 나이, 계좌 잔고를 나이가 어린순으로, 만약 같은 나이라면 계좌 잔고가 많은순으로 정렬해서 조회하는 쿼리문을 작성하시오.
SELECT first_name, age, balance FROM users
ORDER BY age, balance DESC;

-- 데일리 실습 1-2
-- 1. users의 데이터에서 이름과 나이를 이름을 오름차순으로 정렬한 뒤 나이가 많은 순으로 조회하시오.
SELECT first_name, age FROM users
ORDER BY first_name ASC, age DESC;

-- 데일리 실습 1-3
-- 1. users의 데이터에서 이름이 ‘건우’고, 지역 정보가 ‘경기도’ 인 데이터를 조회하시오.
SELECT first_name, country FROM users
WHERE first_name LIKE '건우' AND country LIKE '경기도';

-- 2. users의 데이터에서 경기도 혹은 강원도에 살지 않는 사람들 중 나이가 20살 이상, 30살 이하인 사람들의 데이터를 나이를 기준 오름차순으로 조회하시오.
SELECT * FROM users
WHERE country NOT IN ('경기도', '강원도') AND age BETWEEN 20 AND 30
ORDER BY age ASC;

-- 데일리 실습 1-4
-- 1. users의 데이터에서 전화번호 중간 4자리가 51로 시작하고 지역이 ‘서울’이 아닌 사람들의 이름과 전화번호를 조회하시오.
SELECT first_name, phone, country FROM users
WHERE phone LIKE '%-51__-%' AND country NOT LIKE '서울';

-- 데일리 실습 1-5
-- 1. 현재 등록된 회원 리스트를 나이가 어린 순서로 조회하는 관리자 페이지를 구현하고자 한다. 페이지 당 출력되는 데이터는 20개로 제한했을 때, 3번째 페이지를 조회하는 쿼리문을 작성하시오. 
SELECT * FROM users
ORDER BY age ASC
LIMIT 20 OFFSET 60;



-- 작동 안 됨
ALTER TABLE users ADD COLUMN test TEXT;
ALTER TABLE users DROP COLUMN test;