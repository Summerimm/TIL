-- 1. 조건에 명시된 표에 맞는 zoo 테이블을 생성하고 sqlite 명령어인 .schema zoo 를 이용하여 zoo 테이블의 스키마를 확인해보시오.
CREATE TABLE zoo (
  name TEXT NOT NULL,
  eat TEXT NOT NULL,
  weight INTEGER NOT NULL,
  height INTEGER,
  age INTEGER
);

-- 2. INSERT 문법을 이용하여 zoo 테이블에 아래의 데이터를 추가하시오.
INSERT INTO zoo
VALUES
  ('gorilla', 'omnivore', 215, 180, 5),
  ('rabbit', 'herbivore', 3, 150, NULL),
  ('tiger', 'carnivore', 220, 115, 3),
  ('elephant', 'omnivore', 3800, 280, 10),
  ('dog', 'omnivore', 8, 20, 1),
  ('eagle', 'carnivore', 8, 75, NULL),
  ('dolphin', 'carnivore', 210, NULL, 3),
  ('alligator', 'carnivore', 250, 50, NULL),
  ('panda', 'herbivore', 80, 90, 2),
  ('pig', 'omnivore', 70, 45, 5);

-- 3.모든 동물의 이름과 키를 조회하시오.
SELECT name, height FROM zoo;

-- 4. 토끼의 키를 15로 수정하고 토끼의 데이터를 조회하여 수정되었는지 확인해보시오.
UPDATE zoo
SET height=15
WHERE name='rabbit';

SELECT * FROM zoo
WHERE name='rabbit';

-- 5.잡식 동물(omnivore) 데이터만 삭제하고 전체 데이터를 조회하시오.
DELETE FROM zoo
WHERE eat='omnivore';

SELECT * FROM zoo;