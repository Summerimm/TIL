## 참조 타입
# 함수
## 함수의 정의
### 1. 함수 선언식(Function declaration)
- 일반적인 프로그래밍 언어의 함수 정의 방식  
```javascript
function 함수명() {
  // do something
}
```
- 예시  
```javascript
function add(num1, num2) {
  return num1 + num2
}

add(2, 7)
```

### 2. 함수 표현식
- 표현식 내에서 함수를 정의하는 방식
- 함수 표현식은 함수의 이름을 생략한 익명 함수로 정의 가능
```javascript
변수키워드 함수명 = function() {
  // do somethig
}
```
- 예시
```javascript
const sub = function (num1, num2) {
  return num1 - num2
}
```
- 표현식에서 함수 이름을 명시하는 것도 가능
- 다만 이 경우 함수 이름은 호출에 사용되지 못하고 디버깅 용도로 사용됨
```javascript
const mySub = function namedSub(num1, num2) {
  return num1 - num2
}

mySub(1, 2)   // -1
namedSub(1, 2)  // ReferenceError: namedSub is not defined
```

### 기본 인자(Default arguments)
- 인자 작성 시 '=' 문자 뒤 기본 인자 선언 가능  
![image](https://user-images.githubusercontent.com/108309396/232933871-a4ed32f0-23f1-4bfa-a220-89fad1dcd8be.png)

### 매개변수와 인자의 개수 불일치 허용
- 매개변수보다 인자의 개수가 많을 경우  
![image](https://user-images.githubusercontent.com/108309396/232934180-d885b91d-5e83-4524-aada-b784a6d2e117.png)
- 매개변수보다 인자의 개수가 적을 경우  
![image](https://user-images.githubusercontent.com/108309396/232934530-00a7bded-ac60-4eb7-9454-c626c43e45f3.png)

### Spread syntax(`...`)
- 전개 구문
- 배열이나 문자열과 같이 반복 가능한 객체를 배열의 경우는 요소, 함수의 경우는 인자로 확장 가능
  - 배열과의 사용(배열 복사)  
    ![image](https://user-images.githubusercontent.com/108309396/232934967-271782e1-7fe9-4935-9ad1-ac0723943dfe.png)
  - 함수와의 사용(Rest parameters)  
    ![image](https://user-images.githubusercontent.com/108309396/232935024-79f82919-6912-48c9-b6ca-4d63e4bb0b86.png)

### 함수의 타입
- 선언식 함수와 표현식 함수 모두 타입은 `function`으로 동일  
![image](https://user-images.githubusercontent.com/108309396/232935113-595c0084-5653-4016-a73d-e9ca59788bb2.png)

### 호이스팅
- 함수 선언식으로 정의한 함수는 var로 정의한 변수처럼 **호이스팅**이 발생
- 즉 함수 호출 이후에 선언해도 동작  
![image](https://user-images.githubusercontent.com/108309396/232935180-172c05ef-e30e-4e35-81b0-138bc1787ea6.png)
- 함수 표현식으로 선언한 함수는 함수 정의 전에 호출 시 에러 발생
- 함수 표현식으로 정의된 함수는 변수로 평가되어 변수의 scope 규칙을 따름  
![image](https://user-images.githubusercontent.com/108309396/232935292-c3306c0c-964a-4c2d-a683-2091d383aa90.png)  

### 선언식과 표현식 정리  
![image](https://user-images.githubusercontent.com/108309396/232935332-d430c6ff-8df4-41c5-8abc-9619dcb8341f.png)

## Arrow Function(화살표 함수)
- 함수를 비교적 간결하게 정의할 수 있는 문법
1. `function` 키워드 생략 가능
2. 함수의 매개변수가 하나 뿐이라면 매개변수의 `()` 생략 가능
3. 함수의 내용이 한 줄이라면 `{}`와 `return`도 생략 가능
- 화살표 함수는 항상 익명 함수
  - `===`함수 표현식에서만 사용 가능
- 예시  
![image](https://user-images.githubusercontent.com/108309396/232935633-6b41dd27-2187-418a-a93d-3d39676f0eab.png)  
- 응용  
![image](https://user-images.githubusercontent.com/108309396/232935748-553b1622-77c2-40fd-97e1-ca60557949e7.png)

# `this`
- 어떠한 object를 가리키는 키워드
  - java에서의 this와 python에서의 self는 인스턴스 자기자신을 가리킴
- JavaScript의 함수는 호출될 때 this를 암묵적으로 전달 받음
- JavaScript에서의 this는 일반적인 this와 다르게 동작
- JavaScript는 해당 **함수 호출 방식**에 따라 this에 바인딩 되는 객체가 달라짐
- 즉, 함수를 선언할 때가 아닌 **호출할 때** 함수가 어떻게 호출되었는지에 따라 **동적으로 결정됨**

## 1. 전역 문맥에서의 this
- 브라우저의 전역 객체인 window를 가리킴
  - 전역객체는 모든 객체의 유일한 최상위 객체를 의미
```javascript
console.log(this) // window
```

## 2. 함수 문맥에서의 this
1. 단순 호출
   - 전역 객체를 가리킴 &rarr; 브라우저에서 전역은 window를 의미  
  ![image](https://user-images.githubusercontent.com/108309396/232936344-fa0fa3d2-2ad4-4ce0-8219-caf3da6c190c.png)  
2. Method(Function in Object, 객체의 메서드로서)
   - 메서드로 선언하고 호출한다면, 객체의 메서드이므로 해당 객체가 바인딩  
  ![image](https://user-images.githubusercontent.com/108309396/232936459-a594c20b-b184-4228-9bcc-8a4c93227058.png)
3. Nested (Function 키워드)
   - forEach의 콜백 함수에서의 this가 메서드의 객체를 가리키지 못하고 전역 객체 window를 가리킴
   - 단순 호출 방식으로 사용되었기 때문
   - 이를 해결하기 위해 등장한 함수 표현식이 바로 **화살표 함수**  
  ![image](https://user-images.githubusercontent.com/108309396/232937045-4ee041fb-50cf-4975-a1d9-bd93ac9c4c39.png)
4. Nested (화살표 함수)
   - 이전에 일반 function 키워드와 달리 메서드의 객체를 잘 가리킴
   - 화살표 함수에서 this는 자신을 감싼 정적 범위
   - 자동으로 한 단계 상위의 scope의 context를 바인딩  
  ![image](https://user-images.githubusercontent.com/108309396/232937185-55d15c25-afc1-4c3e-a8bd-0a58eba20883.png)


### 화살표 함수
- 호출의 위치와 상관없이 상위 스코프를 가리킴(Lexical scope this)
- `Lexical scope`
  - 함수를 어디서 호출하는지가 아닌 **어디에 선언**하였는지에 따라 결정
  - Static scope라고도 하며 대부분의 프로그래밍 언어에서 따르는 방식
- 따라서 함수 내의 함수 상황에서 화살표 함수를 쓰는 것을 권장   
![image](https://user-images.githubusercontent.com/108309396/232941951-044b8b56-659a-4a65-a5d9-087a830e9498.png)

### `this` 정리
- 함수를 하나만 만들어 여러 객체에서 재사용할 수 있다는 것은 장점
- but 유연함이 실수로 이어질 수 있다는 것은 단점

# Array
## 배열 메서드 기초  
![image](https://user-images.githubusercontent.com/108309396/232943241-21834dd5-e207-4016-affb-a147c4000324.png)
1. `array.reverse()`  
![image](https://user-images.githubusercontent.com/108309396/232943312-1c01258f-1b53-4afe-b90d-bf985706d654.png)
2. `array.push()`, `array.pop()`  
![image](https://user-images.githubusercontent.com/108309396/232943355-9d13888f-c5b8-493a-816c-77ea09f5f225.png)
3. `array.includes(value)`  
![image](https://user-images.githubusercontent.com/108309396/232943421-49a76e12-102f-4451-b691-1360e2a1addf.png)
4. `array.indexOf(value)`  
![image](https://user-images.githubusercontent.com/108309396/232943496-5f42a0b0-d908-405a-94fb-719301889e80.png)

## 배열 메서드 심화
### Array Helper Methods
- 배열을 순회하며 특정 로직을 수행하는 메서드
- 메서드 호출 시 인자로 **callback 함수**를 받는 것이 특징
  - callback 함수: 다른 함수의 인자로 전달되는 함수  
![image](https://user-images.githubusercontent.com/108309396/232943676-f45badba-884e-449f-9156-15b723fe7a38.png)

1. `forEach`  
![image](https://user-images.githubusercontent.com/108309396/232944101-54d0abb1-62e9-42fc-9565-012624196aa3.png)
- `array.forEach(callback(element[, index[, array]]))`
- 인자로 주어지는 콜백 함수를 배열의 각 요소에 대해 **한 번씩** 실행
  - element: 배열의 요소
  - index: 배열 요소의 인덱스
  - array: 배열 자체
- **반환 값(return) 없음**  
![image](https://user-images.githubusercontent.com/108309396/232944593-74de72b2-a2d3-4017-b91e-25a474546cce.png)    

2. `map`  
![image](https://user-images.githubusercontent.com/108309396/232945146-ce7cdc2b-7160-4de7-a701-8c19ce95683d.png)  
- `array.map(callback(element[, index[, array]]))`
- 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행
- **콜백 함수의 반환 값을 요소로 하는 새로운 배열 반환**
- 기존 배열 전체를 다른 형태로 바꿀 때 유용
  - `forEach + return`  
![image](https://user-images.githubusercontent.com/108309396/232944767-fc134a6f-a2ac-4b0d-963c-41c3a4aeb824.png)

3. `filter`  
![image](https://user-images.githubusercontent.com/108309396/232945221-7bf8b8b4-e3b9-4121-b8a3-3afb4c7944de.png)  
- `array.filter(callback(element[, index[, array]]))`
- 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행
- **콜백 함수의 반환 값이 true인 요소들만 모아서 새로운 배열 반환**
- 기존 배열의 요소들을 필터링할 때 유용  
![image](https://user-images.githubusercontent.com/108309396/232944900-ae57df3b-5685-44fe-9b63-4431343d7cfd.png)

4. `reduce`  
![image](https://user-images.githubusercontent.com/108309396/232945269-21a57cf8-6f7e-49bd-85bc-de9c198d9e47.png)
- `array.reduce(callback(acc, element[, index[, array]])[, initialValue])`
- 인자로 주어지는 함수(콜백 함수)를 배열의 각 요소에 대해 한 번씩 실행해서, 하나의 결과값을 반환
- 배열의 하나의 값으로 계산하는 동작이 필요할 때 사용(총합, 평균 등)
- `map, filter` 등 여러 배열 메서드 동작을 대부분 대체할 수 있음
- 주요 매개변수
  - `acc`: 이전 callback 함수의 반환 값이 누적되는 변수
  - `initialValue(optional)`: 최초 callback 함수 호추 시 acc에 할당되는 값, default값은 배열의 첫 번째 값
- 빈 배열의 경우 initialValue를 제공하지 않으면 에러 발생  
![image](https://user-images.githubusercontent.com/108309396/232945759-aa889375-c93f-4861-933b-912a356b4d7e.png)
- `reduce` 동작 방식    
![image](https://user-images.githubusercontent.com/108309396/232945864-86f831ab-9b1e-4243-a103-93fac34863a2.png)

5. `find`  
![image](https://user-images.githubusercontent.com/108309396/232945917-b6105785-a4d4-48a9-873f-308b1479d2bf.png)
- `array.find(callback(element[, index[, array]]))`
- 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행
- 콜백 함수의 반환 값이 true면, 조건을 만족하는 첫 번째 요소를 반환
- 찾는 값이 배열에 없으면 `undefined` 반환  
![image](https://user-images.githubusercontent.com/108309396/232946081-0cf9f80e-7bb2-4d68-9ecc-f123dbd531c4.png)

6. `some`  
![image](https://user-images.githubusercontent.com/108309396/232946147-804d1994-e859-41b8-89bd-c8c9dc413492.png)
- `array.some(callback(element[, index[, array]]))`
- 배열의 **요소 중 하나라도** 주어진 판별 함수를 통과하면 true 반환
- 모든 요소가 통과하지 못하면 false 반환
- 빈 배열은 항상 false 반환  
![image](https://user-images.githubusercontent.com/108309396/232946265-50087f10-82fe-43f1-9ba0-8a413c5a92ab.png)

7. `every`  
![image](https://user-images.githubusercontent.com/108309396/232946446-f07eac5e-8e55-4ec2-9193-4bafd9b65458.png)  
- `array.every(callback(element[, index[, array]]))`
- 배열의 **모든 요소가** 주어진 판별 함수를 통과하면 true 반환
- 하나의 요소라도 통과하지 못하면 false 반환
- 빈 배열은 항상 true 반환  
![image](https://user-images.githubusercontent.com/108309396/232946393-b701da5a-9204-4020-8f10-8c24df20c39b.png)

### 배열 순회 비교
![image](https://user-images.githubusercontent.com/108309396/232946499-5e0f9da0-2342-4ddb-a264-8796875ca76e.png)

# Object
- 객체는 속성으로 함수를 정의할 수 있음(메서드)  
![image](https://user-images.githubusercontent.com/108309396/232946679-945bebe7-0847-495e-844b-99404b4e7d32.png)

### [참고] 생성자 함수
- 동일한 구조의 객체를 여러 개 만들고 싶을 경우
- `new` 연산자로 사용하는 함수
- 함수 이름은 반드시 대문자로 시작  
![image](https://user-images.githubusercontent.com/108309396/232949374-12388c18-5260-4f13-ad92-1c9bc0d65ef3.png)

## 객체 관련 문법
1. 속성명 축약
   - 객체를 정의할 때 key와 할당하는 변수의 이름이 같으면 축약 가능  
  ![image](https://user-images.githubusercontent.com/108309396/232949624-7483a3da-6a7f-4ec2-85b9-9e7950eb45f7.png)  
2. 메서드명 축약
   - 메서드 선언 시 function 키워드 생략 가능  
  ![image](https://user-images.githubusercontent.com/108309396/232949693-2af92e46-4bb5-4fb6-b357-cc4bd49466f8.png)
3. 계산된 속성명 사용하기
   - 객체를 정의할 때 key의 이름을 표현식을 이용하여 동적으로 생성 가능  
  ![image](https://user-images.githubusercontent.com/108309396/232949772-27b166f2-d508-4417-8642-7292013b6d6e.png)
4. 구조 분해 할당
   - 배열 또는 객체를 분해하여 속성을 변수에 쉽게 할당할 수 있는 문법  
  ![image](https://user-images.githubusercontent.com/108309396/232949836-f5a758a0-2fdf-4c0f-bb59-5fb847e30096.png)  
5. 객체 전개 구문(Spread Operator)
   - 배열과 마찬가지로 전개구문을 사용해 객체 내부에서 객체 전개 가능
   - 얕은 복사에 활용 가능  
  ![image](https://user-images.githubusercontent.com/108309396/232949959-f1c4c1f9-83bb-4bf0-9e8a-c1748f245185.png)

### JSON
- Key-Value 형태로 이루어진 자료 표기법
- JavaScript의 Object와 유사한 구조를 가지고 있으나, Object는 그 자체로 타입이고, JSON은 형식이 있는 "문자열"
- **즉, JSON을 Object로 사용하기 위해서는 변환 작업이 필요**
- JSON 변환  
![image](https://user-images.githubusercontent.com/108309396/232950322-6620e3b5-6a71-4601-8bd2-8965598ba0de.png)

### 배열은 객체다
- 배열은 키와 속성들을 담고 있는 참조 타입의 객체
- 배열은 인덱스를 키로 가지며 length 프로퍼티를 갖는 특수한 객체  
![image](https://user-images.githubusercontent.com/108309396/232950407-163a0546-0c57-4bf3-9701-037d61796166.png)