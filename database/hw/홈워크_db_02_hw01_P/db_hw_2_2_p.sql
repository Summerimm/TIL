CREATE TABLE zoo (
  name TEXT NOT NULL,
  eat TEXT NOT NULL,
  weight INT NOT NULL,
  height INT,
  age INT
);

-- 1) 
-- sqlite3가 flexible하게 동작하여 오류가 발생하지는 않지만 name, eat, weight, height, age 순서대로 들어가지 않는다.
-- 따라서 table 생성 시 순서대로 데이터를 기입하거나, 명시적으로 어떤 순서인지 추가해서 해결할 수 있다.
INSERT INTO zoo (age, weight, height, name, eat) VALUES 
(5, 180, 210, 'gorilla', 'omnivore');

-- 2) 
-- rowid는 UNIQUE constraint인데 10으로 중복되기 때문
-- rowid 두 개를 서로 다르게 설정하면 해결 가능
INSERT INTO zoo (rowid, name, eat, weight, age) VALUES
(10,'dolphin', 'carnivore', 210, 3),
(12, 'alligator', 'carnivore', 250, 50);

-- 3) 
-- weight가 NOT NULL값으로 데이터 추가 시 반드시 값을 지정해 주어야 한다.
-- 임의로 weight를 설정하면 해결 가능
INSERT INTO zoo (name, eat, age, weight) VALUES
('dolphin', 'carnivore', 3, 50);