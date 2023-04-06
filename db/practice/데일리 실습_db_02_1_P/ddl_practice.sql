-- 1.   다음 표를 보고 animals 라는 테이블을 생성하고 sqlite 명령어 .schema animals 로 생성된 테이블의 스키마를 확인하시오.
CREATE TABLE animals (
  animal_name TEXT NOT NULL,
  height INTEGER NOT NULL,
  weight INTEGER NOT NULL,
  age INTEGER
);

-- 2.   식성을 저장하기위한 meal 칼럼을 추가하고 데이터 타입은 TEXT 이며 NULL 값은 허용하시오. 
-- 해당 칼럼을 추가 후 sqlite 명령어.schema animals 로 테이블의 스키마를 확인하시오.
ALTER TABLE animals ADD COLUMN meal TEXT;

-- 3.   첫 번째 칼럼인 animal_name의 명칭을 name으로 수정한 후 sqlite 명령어 .schema animals 로 테이블의 스키마를 확인하시오.
ALTER TABLE animals RENAME COLUMN animal_name TO name;

-- 4.   테이블의 명칭을 animals 에서 zoo로 변경 후 sqlite 명령어 .tables 로 테이블의 이름을 확인하시오.
ALTER TABLE animals RENAME TO zoo;

-- 5.   zoo 테이블을 삭제 후 sqlite 명령어 .tables 로 테이블의 이름을 확인하시오.
DROP TABLE zoo;