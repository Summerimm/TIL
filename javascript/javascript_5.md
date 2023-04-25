# 동기와 비동기
## 동기(Synchronous)
- 모든 일을 **순서대로 하나씩** 처리하는 것
- 이전 작업이 끝나면 다음 작업을 시작
- 예) Python

## 비동기(Asynchronous)
- 작업을 시작한 후 **결과를 기다리지 않고** 다음 작업을 처리하는 것(병렬적 수행)
- 시간이 필요한 작업들은 요청을 보낸 뒤 응답이 빨리 오는 작업부터 처리

### 비동기를 사용하는 이유
- **사용자 경험**: 동기식 처리는 마치 프로그램이 응답하지 않는 듯한 사용자 경험을 만듦
- **비동기로 처리한다면 먼저 처리되는 부분부터 보여줄 수 있음**


# JavaScript의 비동기 처리 
## Single Thread 언어, JavaScript
- JavaScript는 한 번에 하나의 일만 수행할 수 있는 **Single Thread 언어**로 동시에 여러 작업을 처리할 수 없음
- [참고] Thread란? 작업을 처리할 때 실제로 작업을 수행하는 주체로, multi-thread라면 업무를 수행할 수 있는 주체가 여러 개라는 의미

## JavaScript Runtime
- JavaScript 자체는 Single Thread이므로 비동기 처리를 하도록 도와주는 환경이 필요
- JavaScript Engine의 Call Stack(알바)
- Web API(주방장)
- Task Queue(요리 대기실)
- Event Loop(사장님)

### 비동기 처리 방식
1. 모든 작업은 `Call Stack`으로 들어간 후 처리된다.
2. 오래 걸리는 작업이 `Call Stack`으로 들어오면 `Web API`로 보내 별도로 처리하도록 한다.
3. `Web API`에서 처리가 끝난 작업들은 곧바로 `Call Stack`으로 들어가지 못하고 `Task Queue`에 순서대로 들어간다.
4. `Event Loop`가 `Call Stack`이 비어 있는 것을 계속 체크하고 `Call Stack`이 빈다면 `Task Queue`에서 가장 오래된 `Call Stack`으로 보낸다.

## 비동기 처리 동작 요소
1. `Call Stack`
   - 요청이 들어올 때마다 순차적으로 처리하는 stack
   - 기본적인 JavaScript의 Single Thread 작업 처리
2. `Web API`
   - 브라우저에서 제공하는 runtime 환경
   - 시간이 소요되는 작업을 처리(setTimeout, DOM Event, AJAX 요청 등)
3. `Task Queue`
   - 비동기 처리된 Callback 함수가 대기하는 Queue
4. `Event Loop`
   - Call Stack과 Task Queue를 지속적으로 모니터링
   - Call Stack이 비어있는지 확인 후 비어있다면 Task Queue에서 대기 중인 오래된 작업을 Call Stack으로 Push

# Axios
- JavaScript의 HTTP 웹 통신을 위한 라이브러리
- 확장 가능한 인터페이스와 쉽게 사용할 수 있는 비동기 통신 기능을 제공
- node 환경은 npm을 이용해서 설치 후 사용, browser 환경은 CDN을 이용해서 사용

## Axios 사용해보기  
![image](https://user-images.githubusercontent.com/108309396/234159271-0b9f9357-ec9f-476f-beeb-e5a8fbed3be4.png)
- `get, post` 등 여러 method 사용 가능
- `then`을 이용해서 성공하면 수행할 로직 작성
- `catch`를 이용해서 실패하면 수행할 로직 작성

# Callback과 Promise
## 비동기 처리의 단점
- 개발자 입장에서 코드의 실행 순서가 불명확하다는 단점 존재
- 실행 결과를 예상하면서 코드를 작성할 수 없게 함 &rarr; 콜백 함수 사용

## Callback Function
### Callback Hell
- 콜백 함수는 연쇄적으로 발생하는 **비동기 작업을 순차적으로 동작**할 수 있게 함
- 보통 어떤 기능의 실행 결과를 받아 다른 기능을 수행하기 위해 많이 사용하는데, 작성하다보면 비슷한 패턴이 계속 발생
- Callback Hell: 비동기 처리를 위한 콜백을 작성할 때 마주하는 문제, 코드 작성 형태가 마치 "피라미드와 같다"고 해서 "Pyramid of doom(파멸의 피라미드)"라고도 부름

## Promise
- Callback Hell 문제를 해결하기 위해 등장한 비동기 처리를 위한 객체
- "작업이 끝나면 실행시켜줄게"라는 약속
- **비동기 작업의 완료 또는 실패를 나타내는 객체**
- 예시) Axios 라이브러리 &rarr; 성공에 대한 약속 `then`, 실패에 대한 약속 `catch`

### `then & catch`
1. `then(callback)`
   - 요청한 작업이 성공하면 callback 실행
   - callback은 이전 작업의 성공 결과를 인자로 전달 받음
2. `catch(callback)`
   - `then`이 하나라도 실패하면 callback 실행
   - `callback`은 이전 작업의 실패 객체를 인자로 전달 받음
- `then`과 `catch` 모두 항상 `promise` 객체를 반환 &rarr; 즉, 계속해서 **chaining** 가능
- **axios로 처리한 비동기 로직은 항상 promise 객체를 반환**  
![image](https://user-images.githubusercontent.com/108309396/234160976-3f80fb61-eeca-42c5-95a7-e040185289b0.png)

### 비동기 Callback vs Promise
![image](https://user-images.githubusercontent.com/108309396/234161290-358620be-23d6-4dae-999f-e193848d93e1.png)

### Promise가 보장하는 것(vs 비동기 콜백)
1. callback 함수는 JavaScript의 Event Loop가 현재 실행 중인 Call Stack을 완료하기 이전에는 절대 호출X
   - Promise callback 함수는 Event Queue에 배치되는 엄격한 순서로 호출
2. 비동기 작업이 성공하거나 실패한 뒤에 `.then()` 메서드를 이용하여 추가한 경우에도 1번과 똑같이 동작
3. `.then()`을 여러 번 사용하여 여러 개의 callback 함수를 추가할 수 있음(Chaining)
   - 각각의 callback은 주어진 순서대로 하나하나 실행하게 됨
   - Chaining은 Promise의 가장 뛰어난 장점