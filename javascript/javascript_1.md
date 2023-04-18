# JavaScript란?
- JavaScript는 클라이언트 측 웹(**브라우저**)에서 실행
- JavaScript는 **쉽게 배울 수 있고** 강력한 스크립트 언어
- 웹 페이지가 **이벤트 발생 시** 어떻게 작동하는지 디자인 / 프로그래밍
- **웹 페이지 동작을 제어**하는데 널리 사용

###  Web 기술의 기반이 되는 언어
- HTML 문서의 콘텐츠를 **동적으로 변경**할 수 있는 언어
- Web이라는 공간에서 채팅, 게임 등 다양한 동작을 할 수 있게 된 기반

## JavaScript Engine
- 자바스크립트 코드를 실행하는 프로그램 또는 인터프리터
- 여러 목적으로 자바스크립트 엔진을 사용하지만, **대체적으로 웹 브라우저**에서 사용
  - 웹 브라우저의 역할: HTML/CSS/JavaScript를 이해한 뒤 해석해서 사용자에게 하나의 화면으로 보여줌
  - 각 브라우저마다 자체 JavaScript Engine을 개발, 사용하고 있음

## JavaScript 실행 환경 구성
- Web Browser로 실행하기
  - HTML 파일에 직접 JavaScript 코드를 작성 후 웹 브라우저로 파일 열기  
  ![image](https://user-images.githubusercontent.com/108309396/232660848-6cacda33-06e5-4c2d-baed-50e9e6664706.png)
  - Chrome의 개발자 도구 - Console 탭에서 결과 확인 가능
  - 웹 브라우저의 console에서 바로 JavaScript를 입력해도 됨
  - `.js` 확장자를 가진 파일에 JavaScript를 작성하고, 해당 파일을 HTML에 포함 가능  
  ![image](https://user-images.githubusercontent.com/108309396/232676304-93db3d65-c09b-444c-a7d0-50dbd93783cf.png)
  - 특별하게 웹 브라우저에서 바로 실행할 수 있는 JavaScript 문법들을 `Vanilla javaScript`라고 부름(순수한 JavaScript라는 의미)

## JavaScript를 시작하기에 앞서
- ECMAScript란, Ecma International이 ECMA-262 규격에 따라 정의하고 이쓴ㄴ 표준화된 스크립트 프로그래밍 언어를 뜻함
- JavaScript를 표준화하기 위해 만들어짐 &rarr; ECMAScript

### 주석
- 한 줄 주석(`//`)과 여러 줄 주석(`/* */`)

### 들여쓰기와 코드 블럭
- JavaScript는 2칸 들여쓰기 사용
- **블럭(block)**은 if, for, 함수에서 중괄호 `{}`내부를 말함

### 세미콜론(semicolon)
- 자바스크립트는 세미콜론을 선택적으로 사용 가능
- 세미콜론이 없으면 ASI(Automatic Semicolon Insertion)에 의해 자동으로 세미콜론이 삽입됨

# JavaScript 기초 문법
## 변수와 식별자
- 식별자(identifier)는 변수를 구분할 수 있는 변수명을 말함
- 식별자는 반드시 문자, 달러($) 또는 밑줄(_)로 시작
- 예약어 사용 불가능(for, if, function 등)
- camelCase(변수, 객체, 함수에 사용)  
![image](https://user-images.githubusercontent.com/108309396/232677824-8f7cbc18-8dd6-4b24-80e3-4a638cf70d77.png)  
- PascalCase(클래스, 생성자에 사용)  
![image](https://user-images.githubusercontent.com/108309396/232677854-ddbc0223-ad6c-4c14-9f6b-bbdd64411d74.png)  
- SNAKE_CASE(상수(constants)에 사용)  
![image](https://user-images.githubusercontent.com/108309396/232677895-7f3cad86-bb9b-4076-a697-fd20a8c10636.png)

### 변수 선언 키워드
1. `let`
   - 블록 스코프 지역 변수를 선언(추가로 동시에 값을 초기화)
   - 재할당 가능 & 재선언 불가능
2. `const`
   - 블록 스코프 읽기 전용 상수를 선언(추가로 동시에 값을 초기화)
   - 재할당 불가능 & 재선언 불가능
3. `var`
   - 변수를 선언(추가로 동시에 값을 초기화)
   - 재할당 가능 & 재선언 가능
   - 호이스팅되는 특성으로 인해 예기치 못한 문제 발생 가능 &rarr; const와 let 사용 권장
   - 함수 스코프(function scope)를 가짐

### [참고] 선언, 할당, 초기화
- 선언(declaration): 변수를 생성하는 행위 또는 시점
- 할당(assignment): 선언된 변수에 값을 저장하는 행위 또는 시점
- 초기화(initialization): 선언된 변수에 **처음으로** 값을 저장하는 행위 또는 시점  
![image](https://user-images.githubusercontent.com/108309396/232678250-6e19dd2f-b2f5-45c2-bd32-be6db4732ae4.png)

### [참고] 블록 스코프(block scope)
- if, for, 함수 등의 중괄호 내부를 가리킴
- 블록 스코프를 가지는 변수는 블록 바깥에서 접근 불가능  
![image](https://user-images.githubusercontent.com/108309396/232678685-b9c4783c-4e6e-4d4d-8993-15bb9ca0d925.png)

### [참고] 함수 스코프(function scope)
- 함수의 중괄호 내부를 가리킴
- 함수 스코프를 가지는 변수는 함수 바깥에서 접근 불가능  
![image](https://user-images.githubusercontent.com/108309396/232679121-92a7a2b5-7e37-4a07-b795-e5a5b0b4354d.png)

### [참고] 호이스팅(hoisting)
- 변수를 선언 이전에 참조할 수 있는 현상
- var로 선언된 변수는 선언 이전에 참조가능 &rarr; 변수 선언 이전의 위치에서 접근 시 `undefined`를 반환
- 실제 실행 시 코드의 최상단으로 끌어 올려지게 되고 이러한 이유 때문에 var로 선언된 변수는 선언시에 `undefined`로 값이 초기화되는 과정이 동시에 일어남
- 이는 코드의 논리적인 프름을 꺠뜨리는 행위  
![image](https://user-images.githubusercontent.com/108309396/232679589-2affac78-47ed-4135-9761-b810adb3ba6b.png)

# 데이터 타입  
![image](https://user-images.githubusercontent.com/108309396/232680163-03ec77d5-7fd1-43cd-8f44-b534d988443c.png)

## 원시 타입(Premitive type)
1. Number - 정수 또는 실수형 숫자   
![image](https://user-images.githubusercontent.com/108309396/232680485-ba14f16a-38ef-476c-ae03-50b879d7bede.png)
   - `NaN`을 반환하는 경우
     - 숫자로서 읽을 수 없음(`parseInt("어쩌구")`, `Number(undefined)`)
     - 결과가 허수인 수학 계산식(`Math.sqrt(-1)`)
     - 피연산자가 `NaN`(`7 ** NaN`)
     - 정의할 수 없는 계산식(`0 * Infinity`)
     - 문자열을 포함하면서 덧셈이 아닌 계산식(`"가"/3`) 
2. String - 문자열
   - 작은 따옴표 또는 큰 따옴표 모두 가능
   - 곱셈, 나눗셈, 뺄셈은 안 되지만 덧셈을 통해 문자열끼리 붙일 수 있음
   - 따옴표 사용 시 선언 시에 줄 바꿈 불가능
   - 대신 escape sequence `\n` 사용
   - **Template Literal**(\`)을 사용하면 줄 바꿈 가능, 문자열 사이에 변수도 삽입 가능(==python의 f-string)  
    ![image](https://user-images.githubusercontent.com/108309396/232682282-f992a827-1b7b-4b69-9530-4305ddfe8d96.png)
3. null - 값이 없음을 의도적으로 표현  
   - null은 원시타입 but `typeof null` &rarr; object(설계 상 버그)  
   ![image](https://user-images.githubusercontent.com/108309396/232682723-eb2c2fb1-c222-4335-9230-c7f9b2940cec.png)
4. undefined - 값이 정의되어 있지 않음을 표현
   - 변수 선언 이후 직접 값을 할당하지 않으면 자동으로 할당됨  
    ![image](https://user-images.githubusercontent.com/108309396/232682670-d090c178-2528-49cb-875c-ba1db615d5f8.png)
5. Boolean - 참과 거짓 , `true와 false`
6. Symbol - 유일한 값을 표현하는 자료형

## 참조 타입(Reference type)
1. Object - 이름과 값을 가진 속성(property)들의 집합으로 이루어진 자료구조
   - 중괄호 내부에 key와 value의 쌍으로 표현
   - key: 문자열 타입만 가능, 이름에 띄어쓰기 등의 구분자가 있으면 따옴표로 묶어서 표현
   - value: 모든 타입(함수 포함) 가능
   - 객체 요소 접근: `.`또는 `[]`로 가능, key 이름에 구분자가 있으면 대괄호 접근만 가능  
    ![image](https://user-images.githubusercontent.com/108309396/232684056-8d6e1d79-bc3f-44a9-b7cd-e87000336fb8.png)
2. Array - 여러 개의 값을 순서대로 저장하는 자료구조
   - 키와 속성들을 담고 있는 참조타입의 객체
   - 순서를 보장
   - 주로 대괄호(`[]`)를 이용하여 생성, 0을 포함한 양의 정수 인덱스로 접근 가능
   - 배열의 길이는 `array.length` 형태로 접근 가능(마지막 원소는 `array.length-`로 접근)
3. function - function 키워드를 통해 생성하며, 호출 시 실행될 코드를 정의
   - 함수 선언식(function delcaration)  
    ![image](https://user-images.githubusercontent.com/108309396/232684492-078bb1a7-a784-4c2a-b3db-02ffb0105e41.png)
   - 함수 표현식(function expression)  
    ![image](https://user-images.githubusercontent.com/108309396/232684592-00d1a024-422c-4d6e-a85b-c2454de48d2f.png)  
    ![image](https://user-images.githubusercontent.com/108309396/232684729-2fc286cc-43fd-48fe-8dea-f3197666b467.png)  

### ToBoolean Conversions(자동 형변환)  
![image](https://user-images.githubusercontent.com/108309396/232684853-2d5789ec-4045-4262-9d91-fc3e95711fe2.png)


# 연산자
1. 할당 연산자: `=`, `+=`, `-=`, `++`, `--`...
2. 비교 연산자: `>`, `<=`
3. 일치 연산자: `===`
4. 논리 연산자: `&&`, `||`, `!`... 단축 평가도 지원 (ex. `false && true => false`)
5. 삼항 연산자(Ternary Operator): `true ? 1:2 => 1`, 조건식이 참이면 `:`앞의 값, 거짓이면 `:`뒤의 값이 반환
6. 스프레드 연산자(Spread Operator): 배열이나 객체를 전개하여 각 요소를 개별적인 값으로 분리
  - 주로 함수 호출 시 매개변수로 배열이나 객체 전달할 때 사용
  - 얕은 복사를 위해서도 활용 가능  
  ![image](https://user-images.githubusercontent.com/108309396/232686407-718a7138-f8e7-493a-811f-c878817d7868.png)

# 조건문(`if` statement)  
![image](https://user-images.githubusercontent.com/108309396/232686805-abc056a3-84dd-4053-86a5-e9e2b174f0a5.png)

# 반복문
1. `while`  
![image](https://user-images.githubusercontent.com/108309396/232687025-2dba74dc-5480-4279-9c93-e77940b1fafc.png)
2. `for`  
![image](https://user-images.githubusercontent.com/108309396/232687145-ddf254bd-301a-451a-aa17-4cfec877e2ce.png)
3. `for...in`: 객체의 속성을 순회할 때 사용, 배열도 순회 가능 but 순서대로 순회한다는 보장 없으므로 권장X  
![image](https://user-images.githubusercontent.com/108309396/232687506-5d337e9b-55ab-4463-9e17-86e5cdfb88aa.png)
4. `for...of`: 반복 가능한 객체를 순회할 때 사용(Array, Set, String 등)  
![image](https://user-images.githubusercontent.com/108309396/232687695-d9413355-fe97-4dd7-8190-ff29677d7508.png)
  - `for...in`은 "속성 이름"을 통해 반복, `for...of`는 "속성 값"을 통해 반복  
  ![image](https://user-images.githubusercontent.com/108309396/232688021-9829e2b9-af24-4728-baeb-8cd943ef5dac.png)  
  ![image](https://user-images.githubusercontent.com/108309396/232688135-7cb81342-3756-43a5-92ae-dc3547df2b91.png)
5. `Array.forEach`: 배열의 메서드들 중 하나  
![image](https://user-images.githubusercontent.com/108309396/232688686-3244fa11-92f7-4022-95cf-7488d5cf1f05.png)


### [참고] `for...in`, `for...of`와 `const`
- for문
  - `for(let i=0; i<arr.length; i++){...}` : 최초 정의한 i를 재할당하면서 사용하기 때문에 const 사용 시 에러 발생
- `for...in`, `for...of`
  - 재할당이 아니라, 매 반복 시 해당 변수를 새로 정의하여 사용하므로 에러 발생X


## 조건문과 반복문 정리  
![image](https://user-images.githubusercontent.com/108309396/232688774-8f872657-d821-44a3-9f42-acc3417a24ba.png)

### optional chaining
```javascript
// optional chaining
const a = obj.b?.value ?? 'hoho'
const obj = {
  a:1
}

console.log(obj.a.b)
console.log(obj.b?.a)
```