CREATE TABLE zoo (
  name TEXT NOT NULL,
  eat TEXT NOT NULL,
  weight INT NOT NULL,
  height INT,
  age INT
);

INSERT INTO zoo VALUES 
('gorilla', 'omnivore', 215, 180, 5),
('tiger', 'carnivore', 220, 115, 3),
('elephant', 'herbivore', 3800, 280, 10),
('dog', 'omnivore', 8, 20, 1),
('panda', 'herbivore', 80, 90, 2),
('pig', 'omnivore', 70, 45, 5);

BEGIN;
  DELETE FROM zoo
  WHERE weight < 100;
ROLLBACK;
BEGIN;
  DELETE FROM zoo
  WHERE eat = 'omnivore';
COMMIT;

SELECT COUNT(*)
FROM zoo;


-- 실행결과로 omivore를 먹지 않는 tiger, elephant, panda의 데이터만 남고 나머지는 삭제된다.

-- INSERT문 실행 후 총 6개의 행(데이터)가 추가된다.
-- 이후 BEGIN문의 시작으로 트랜잭션을 처리하게 된다.
-- 처음에는 weight이 100보다 작은 데이터들이 삭제됐지만 COMMIT하기 이전이므로 ROLLBACK;을 통해 다시 복구한다.
-- ROLLBACK이란 작업 중 문제가 발생해 트랜잭션의 처리과정에서 발생한 변경사항을 취소하는 명령어이다. 이를 사용하면
-- 마지막 COMMIT을 완료한 시점으로 다시 돌아갈 수 있다.
-- COMMIT이란 처리과정 이후를 DB에 영구 저장하는 것이고 하나의 트랜잭션 과정을 종료하며 이전 데이터가 완전히 UPDATE된다.
-- ROLLBACK 후 다시 eat의 값이 omnivore인 데이터들이 삭제되고 그 이후에 COMMIT문을 통해 최종적으로 데이터베이스에 저장하게 된다.