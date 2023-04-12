-- 1. 위 테이블 스키마 정보를 보고 users 테이블을 생성하시오.
CREATE TABLE users (
  id INTEGER PRIMARY KEY,
  first_name TEXT,
  last_name TEXT NOT NULL,
  age INTEGER NOT NULL,
  country TEXT NOT NULL,
  phone TEXT,
  balance INTEGER NOT NULL
);

-- 2. 위에 주어진 데이터를 users 테이블에 추가하시오.
INSERT INTO users
VALUES
  (1, '미현', '김', 19, '경기도', '011-211-8482', 300),
  (2, NULL, '최', 33, '제주특별자치도', NULL, 300),
  (3, '미숙', '이', 21, '서울특별시', '010-2122-4958', 480),
  (4, '남석', '박', 18, '경기도', '011-484-8667', 260),
  (5, '철수', '박', 22, '경상남도', '016-295-8989', 500),
  (6, NULL, '박', 45, '전라북도', NULL, 320),
  (7, '민준', '이', 35, '전라남도', '019-965-8833', 350),
  (8, NULL, '남', 24, '충청남도', '010-5882-5969', 210),
  (9, '신', '유', 29, '경상북도', '010-4949-2848', 290),
  (10, NULL, '김', 18, '대전광역시', NULL, 300);

SELECT * FROM users;

-- 3. 나이가 25 미만인 사람들의 id, age 그리고 balance 정보를 age는 내림차순 balance는 오름차순으로 확인하시오.
SELECT id, age, balance FROM users
WHERE age<25
ORDER BY age DESC, balance ASC;

-- 4. first_name 이 존재하는 사람들 중 balance가 400 보다 큰 사람의 first_name과 balance를 확인하시오.
SELECT first_name, balance FROM users
WHERE first_name IS NOT NULL AND balance>400;

-- 5. phone 의 값이 null 인 사람들의 phone 정보를 '알 수 없음' 으로 수정하고 수정여부를 전체 데이터를 조회하여 확인하시오.
UPDATE users
SET phone="알 수 없음"
WHERE phone IS NULL;

SELECT * FROM users;