# Variable
- 데이터를 저장할 메모리의 위치를 나타내는 이름
- 메모리 상에 데이터를 보관할 수 있는 공간을 확보
- 적절한 메모리 공간을 확보하기 위해 변수의 타입 등장
- '='을 통해서 CPU에게 연산 작업 의뢰
- 메모리의 단위: 1byte(8bit)

# Datatype and Operator
## Datatype
- **기본 자료형(Primitive Type)**
  - 미리 정해진 크기의 Memory Size 표현, 변수 자체에 값 저장  
  ![기본자료형](https://user-images.githubusercontent.com/108309396/216208020-d27b0b5c-252e-4824-849f-3bf0dae053b6.png)
  - int: `5`
  - double: `1.1 `
  - String: `"Hello"`
  - char: `'H'`
- **참조 자료형(Reference Type)**: 기본 자료형 8가지 외 모든 것(String은 철수라는 이름을 0x0001이라는 주소에 저장하고 그 주소를 읽어옴)


- 선언: 자료형 변수명;(`int age;`)
- 저장(할당): 변수명 = 저장할 값;(`age = 30;`)
- 초기화: 자료형 변수명 = 저장할 값;(`int age = 30;`)

## Operator
- 단항 연산자
  - 증감 연산자 `++, --`
    - 전위형(prefix) `++i`: 먼저 변수값을 변화시키고 사용
    - 후위형(postfix) `i--`: 먼저 변수값을 사용하고 변화
  - 부호 연산자 `+, -`
    - `+` : 양수임을 표시
    - `-` : 피연산자 부호를 반대로 변경한 결과 반환
  - 논리 부정 연산자 `!`
  - 비트 부정 연산자 `~`
  - 형 변환 연산자(type): 명시적 형변환
- 산술 연산자
  - `+, -, *, /, %` 
  - 정수와 정수의 연산 = 정수
  - 정수와 실수의 연산 = 실수
- 비교 연산자
  - 대소 비교 연산 `>, >=, <, <=`
  - 동등 비교 연산 `==, !=`
    - `==` 참조형 변수는 주소값을 비교함
    - String 변수 비교할 때는 `equals()` 사용
  - 객체 타입 비교 연산 `instanceof`
- 논리 연산자
  - `&&` : AND
  - `||` : OR
  - `!` : NOT
  - AND와 OR은 short circuit evaluation 가능(AND의 경우 앞이 F이면 무조건 F, OR의 경우 앞이 T면 무조건 T)
- 삼항 연산자
  - `조건식 ? 식1: 식2`
  - 조건식이 참일 경우 식1 수행
  - 조건식이 거짓일 경우 식2 수행
- 복합 대입 연산자
  - `+=, -=, *=, /=`
- `Math.floor / Math.ceil`: 내림, 올림
- `Math.PI`: 3.1415926535

## String
- String concatenation: `+`
- `[String].length();`
- `[String].replace("old", "new")`

# Type Casting
- 자동(암묵적) 형변환이 가능한 방향
  - 메모리의 크기와 상관없이 범위가 큰 순서  
![화면 캡처 2023-02-02 103023](https://user-images.githubusercontent.com/108309396/216208917-53046013-547f-4413-8147-446630ec23d2.png)
- **Implicit Casting(암묵적)**
  - 범위가 넓은 데이터 형에 좁은 데이터 형을 대입하는 것
- **Explicit Casting(명시적)**
  - 범위가 좁은 데이터 형에 넓은 데이터 형을 대입하는 것
  - 형 변환 연산자 사용 - (타입) 값;

- `double a = 1`: 가능(암묵적)
- `int b = 1.1`: 불가능
- `int b = (int) 1.1`: Casting / loss 발생(명시적)




- 1 to String: `Integer.toString(1)`
- `A.getClass()`: type 반환