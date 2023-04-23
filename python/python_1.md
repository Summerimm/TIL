# Python Basic
### 프로그래밍 언어의 구성
- 소스 코드
  - 프로그래밍 언어로 작성된 프로그램
- Interpreter or Compiler
  - 소스 코드를 컴퓨터가 이해할 수 있는 기계어로 번역
  - 파이썬의 경우 interpreter를 사용

### 파이썬의 특징
- 다른 언어에 비해 문법이 간단하고 엄격하지 않음
- 별도의 데이터 타입 지정이 필요없고 **재할당이 가능**
- 문장을 구분할 때 중괄호를 쓰지 않고 **들여쓰기(indentation)**를 사용
- 컴파일 과정 없이 바로 실행 가능
- OOP 언어로 모든 것이 객체로 구현되어 있음

# Python 기초 문법
## 변수와 식별자
### 1. 변수(Variable)
- 데이터를 저장하기 위해 사용
- 복잡한 값들을 쉽게 사용 가능(추상화)
 - 코드의 가독성 증가
 - 숫자를 직접 적지 않고 의미 단위로 작성 가능
 - 코드 수정 용이
- 동일 변수에 다른 데이터를 언제든 할당(저장)할 수 있기 때문에, '변수'라고 불림
- 변수의 할당
  - 변수는 할당 연산자(`=`)를 통해 값을 할당(assignment)
  - 같은 값을 동시에 할당 가능
  - 다른 값을 동시에 할당 가능

### 2. 식별자(Identifiers)
- 변수의 이름을 식별자라고 함(변수, 함수, 클래스...)
- 변수 이름 규칙
  - 영문 알파벳, 언더스코어(_), 숫자로 구성
  - 첫 글자에 숫자가 올 수 없음
  - 길이 제한X, 대소문자 구별
  - keywords는 예약어(reserved words)로, 사용할 수 없음  
![image](https://user-images.githubusercontent.com/108309396/217980714-fe8e2f1a-2919-4b38-b3ce-33d5fe7e2c3a.png)

### 3. 주석(comment)
- 코드의 실행에 영향을 미치지 않는 메모(`#`)
- 여러줄도 가능(`''' '''`)
- 코드에 대한 쉬운 이해
- 유지 보수, 협업 용이

### 4. 연산자
- 산술 연산자(Arithmetic Operator)
  - `+, -, *, /, //, **`

### 5. 자료형(Datatype)  
![2](https://user-images.githubusercontent.com/108309396/217981294-fa97f315-1f5a-496c-b51c-02cb4dcb565c.png)
![3](https://user-images.githubusercontent.com/108309396/217981291-e514ce38-a8e0-45ad-baec-f7e6bb766c80.png)
![4](https://user-images.githubusercontent.com/108309396/217981287-7c6675ba-283a-40b7-9bd4-8ab744149a9d.png)
- Numeric Type
  - int, float, complex
  - 진수 표현(2진수-0b, 8진수-0o, 16진수-0x)
  - 실수 연산 시 주의할 점(부동 소수점)
    - `3.2 - 3.1 != 1.2 - 1.1`
    - 2진수로 0.1을 표현하면 0.000110011...같이 무한대로 반복 &rarr; 근사값만 표시
    - Floating point rounding error
    - 매우 작은 수보다 작은 지를 확인하거나 math 모듈 활용

- String Type
  - `'`, `"`를 활용하여 표기
  - 문자열을 묶을 때 동일한 문장부호 활용
  - PEP8에서는 소스코드 내에서 하나의 문장부호를 선택하여 유지하도록 함
  - 중첩 따옴표 `"'Hello World'"`  &rarr; `'Hello World'`
  - 삼중 따옴표 &rarr; 따옴표 안에 따옴표를 넣을 때, 여러 줄을 나눠 입력할 때 편리
  - Escape Sequence: backslash 뒤에 특정한 문자가 와서 특정한 기능을 수행  
![1](https://user-images.githubusercontent.com/108309396/217982180-52c70d46-e01c-43a2-87c1-633eab509f16.png)
  - 문자열 연산(`+`: String Concatenation, `*`)
  - String Interpolation: 문자열을 변수로 활용하여 만드는 법(f-strings)
- None
  - 파이썬 자료형 중 하나
  - 값이 없음을 표현하기 위해 None 타입이 존재
  - 일반적으로 반환 값이 없는 함수에서 사용하기도 함

- Boolean Type
  - 논리 자료형으로 참과 거짓을 표현하는 자료형
  - True 또는 False
  - 비교/논리 연산에서 활용
  - 비교 연산자: True / False를 반환  
![2](https://user-images.githubusercontent.com/108309396/217982853-dae9e963-4619-463a-ba80-3da42a87dc9a.png)
  - is: 메모리 공간까지 동일한지
  - ==: 내용만 동일
  - 논리 연산자: `and, or, not`
    - False로 취급되는 값: 0, 0.0, (), [], {}, "", None

---
## 컨테이너(Container)
- 여러 개의 값(데이터)를 담을 수 있는 객체로, 서로 다른 자료형을 저장할 수 있음
- 분류
  - 순서가 있는 데이터(Ordered) vs 순서가 없는 데이터(Unordered)
  - 순서가 있다 != 정렬되어 있다  
![3](https://user-images.githubusercontent.com/108309396/217983997-ae3072da-8608-4a92-b3f4-8c52f66c9da1.png)

### Range
- 숫자의 시퀀스를 나타내기 위해 사용
- 주로 반복문과 함께 사용
- `range(n, m)`: n부터 m-1까지

### 슬라이싱 연산자
- 인덱스와 콜론을 사용해 문자열의 특정 부분만 잘라낼 수 있음
- `abcd[2:4]` &rarr; `cd`

---
## 형 변환(Typecasting)
- 데이터 형태는 서로 변환 가능
- 암시적 형 변환(Implicit)
  - 파이썬 내부적으로 자료형을 변환
  - `3 + 5.0` &rarr; `8.0`
- 명시적 형 변환(Explicit)
  - 사용자가 특정 함수를 활용해 의도적으로 자료형을 변환
  - `int('3') + 4` &rarr; `7`
- 컨티이너 형 변환  
![1](https://user-images.githubusercontent.com/108309396/217984851-554f3552-7f7a-4b48-ae99-185c5b4675fa.png)

---
### [참고] `==`와 `is`의 차이
- `==`: 정보가 같음
  - integer나 string 같은 경우 값이 같다면 같은 memory space 참조
```python
a = 'haha'
b = 'haha'
a == b # True
a is b # True
```
- `is`: 객체가 같음
  - container는 무조건 memory space가 다름
```python
a = [1, 2, 3]
b = [1, 2, 3]
a == b # True
a is b # False
```