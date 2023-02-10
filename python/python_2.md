# Control Statement
- 순차, 선택, 반복
- 파이썬은 기본적으로 위에서부터 아래로 차례대로 명령을 수행
- 특정 상황에 따라 코드를 선택적으로 실행(분기/조건)하거나 계속하여 실행(반복)하는 제어가 필요
- 순서도(flowchart)로 표현 가능

## 코드 스타일 가이드
- 코드를 어떻게 작성할지에 대한 가이드 라인
- PEP8, Google Style guide
- 들여쓰기
  - Space Sensitive
  - 한 코드 안에서는 반드시 한 종류의 들여쓰기를 사용(space키 4칸 or Tab키 1번)

## 조건문
- 참 / 거짓을 판단할 수 있는 조건식과 함께 사용
- 복수 조건문(`elif/else 활용`)
- 중첩 조건문
- 조건 표현식(Conditional Expression)
  - 일반적으로 조건에 따라 값을 정할 때 활용
  - 삼항 연산자(Ternary Operator)라고도 함
  - `val1 if 조건 else val2`

## 반복문
### while문
- 종료 조건에 해당하는 코드를 통해 반복문을 종료
- 조건식이 참인 경우 반복적으로 코드 실행
### for문
- 반복 가능한 객체를 모두 순회하면 종료(별도의 종료 조건 필요X)
- 시퀀스(string, tuple, list, range)를 포함한 iterable의 요소를 모두 순회
- Iterable
  - 순회할 수 있는 자료형(`string, tuple, list, range, set, dict` 등)
  - 순회형 함수(`range, enumerate`)
  - `enumerate(iterable, start=1)`: (index, value) 형태의 tuple로 구성된 열거 객체를 반환, start를 지정하면 해당 값부터 인덱스가 순차적으로 증가
- List/Dictionary Comprehension
  - 간결하게 생성하는 방법
  - [code for 변수 in iterable if 조건식]
  - {key: value for 변수 in iterable if 조건식}
### 반복 제어
- `break`: 반복문 종료
- `continue`: continue 이후의 코드 블록은 수행하지 않고, 다음 반복을 수행
- `for-else`: 끝까지 반복문을 실행한 이후에 else문 실행
  - break를 통해 중간에 종료되는 경우 else문은 실행되지 않음
- `pass`: 아무것도 하지 않음
  - 문법적으로 필요하지만, 할 일이 없을 때 사용
  - 반복문이 아니어도 사용 가능  
![1](https://user-images.githubusercontent.com/108309396/217986678-0c00ea72-d485-45e7-a198-904eedb867e5.png)  
![2](https://user-images.githubusercontent.com/108309396/217986684-08af1dbf-3334-4c34-934a-f686d610d5c8.png)
