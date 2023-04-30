# Exception Handling(예외 처리)
## 에러와 예외
- 어떤 원인에 의해 오동작하거나 비정상적으로 종료되는 경우
- 심각도에 따른 분류
  - Error
    - 메모리 부족, stack overflow와 같이 일단 발생하면 복구할 수 없는 상황
    - 프로그램의 비정상적 종료를 막을 수 없음 &rarr; 디버깅 필요
  - Exception
    - 수습될 수 있는 비교적 상태가 약한 것들
    - 프로그램 코드에 의해 수습될 수 있는 상황
- exception handling(예외 처리)란
  - 예외 발생 시 프로그램의 비정상 종료를 막고 정상적인 실행 상태를 유지하는 것
  - **예외의 감지 및 예외 발생 시 동작할 코드 작성** 필요

## 예외 클래스의 계층
![image](https://user-images.githubusercontent.com/108309396/233765812-daae9d41-ce18-448a-8a19-a250eb9ca222.png)  
- checked exception : 에외에 대한 대처 코드가 없으면 컴파일 진행 X
- unchecked exception : 예외에 대한 대처 코드가 없더라도 컴파일은 진행

## `try ~ catch` 구문
<img width="483" alt="image" src="https://user-images.githubusercontent.com/108309396/233765906-7f5dc619-ab1a-481b-b70c-93cb35134f5d.png">
<img width="496" alt="image" src="https://user-images.githubusercontent.com/108309396/233766032-56b0ca0c-7325-4492-8923-5a1d1eb384b8.png">

## Exception 객체의 정보 활용
- Throwable의 주요한 메서드  
<img width="571" alt="image" src="https://user-images.githubusercontent.com/108309396/233765965-65779464-7089-47c5-9d4b-a6d7d56d163b.png">

## 다중 exception handling
- try 블록에서 여러 종류의 예외가 발생할 경우
  - 하나의 try 블록에 여러 개의 catch 블록 추가 가능(예외 종류 별로 catch 블록 구성)
- 다중 catch 문장 작성 순서 유의사항
  - JVM이 던진 예외는 catch 문장을 찾을 때는 다형성이 적용됨
  - 상위 타입의 예외가 먼저 선언되는 경우 뒤에 등장하는 catch 블록은 동작할 기회X
    - Unreachable catch block for Exception
  - 상속 관계가 없는 경우는 무관
  - **상속 관계에서는 작은 범위(자식)에서 큰 범위(조상)순으로 정의**  
<img width="296" alt="image" src="https://user-images.githubusercontent.com/108309396/233766245-386b78f2-f75b-4d41-9f75-6d8751184b87.png">  

## 다중 예외 처리를 이용한 Checked Exception 처리
- 처리하지 않으면 컴파일 불가: Checked Exception
- 예외 처리는 가능한 "구체적으로" 진행
- 가급적 예외 상황 별로 처리하는 것을 권장  
<img width="405" alt="image" src="https://user-images.githubusercontent.com/108309396/233766299-b2523368-7504-4438-be54-cfd83c70db42.png">  

- 심각하지 않은 예외를 굳이 세분화해서 처리하는 것도 낭비
  - `|`를 이용해 하나의 catch 구문에서 상속관계가 없는 여러 개의 exception 처리  
  <img width="443" alt="image" src="https://user-images.githubusercontent.com/108309396/233766393-7547fb8c-622d-4a6e-b7db-a7857ac90c70.png">

- `try ~ catch ~ finally` 구문을 이용한 예외 처리
  - `finally`는 예외 발생 여부와 상관없이 언제나 실행
  - 중간에 return을 만나는 경우도 `finally` 블록을 먼저 수행 후 리턴 실행  
  <img width="300" alt="image" src="https://user-images.githubusercontent.com/108309396/233766497-4dfa0f8c-a604-4cdf-965f-4f248151d8e5.png">

### `finally`를 이용한 자원 정리
<img width="487" alt="image" src="https://user-images.githubusercontent.com/108309396/233766825-cd84bbd9-29fb-4a84-9b3e-9cbb9b7ffd2c.png">  

- 주요 목적: try 블록에서 사용한 리소스 반납
- 생성한 시스템 자원을 반납하지 않으면 장래 resource leak 발생 가능 &rarr; `close` 처리
- `finally`에서 `close`를 통한 자원 반납  
<img width="465" alt="image" src="https://user-images.githubusercontent.com/108309396/233766951-06b1dca5-4a5a-4660-8fbe-b481d0f21d99.png">

- `close` 메서드 자체가 `IOException` 유발 가능
  - FileInputStream 생성자에서 IOException 발생 시 fileInput은 null인 상황

## `try-with-resources`
- JDK 1.7 이상에서 리소스의 자동 close 처리  
<img width="346" alt="image" src="https://user-images.githubusercontent.com/108309396/233767145-005754c6-a1a7-4bf6-b0b2-09e05807a84b.png">  

- try 선언문에 선언된 객체들에 대해 자동 close 호출(finally 역할)
  - 단, 해당 객체들이 AutoClosable interface를 구현할 것(각종 IO stream, socket, connection)  
  - <img width="109" alt="image" src="https://user-images.githubusercontent.com/108309396/233767156-20a50420-0d21-4df7-8c8f-55dcc225c4d1.png">
  - 해당 객체는 try 블록에서 다시 할당될 수 없음
  - <img width="369" alt="image" src="https://user-images.githubusercontent.com/108309396/233767163-1a8ffc18-d631-4b1c-a29c-b0a3234c7e20.png">


# `throws` 활용
## `throws` 키워드를 통한 처리 위임
- method에서 처리해야 할 하나 이상의 예외를 **호출한 곳으로** 전달(처리 위임)
  - 예외는 처리X, 단순히 전달
  - 예외를 전달받은 메서드는 다시 예외 처리의 책임 발생  
  - <img width="355" alt="image" src="https://user-images.githubusercontent.com/108309396/233767240-d9a82b74-e626-476a-a47b-e76866de79d4.png">
  - 처리하려는 예외의 조상 타입으로 throws 처리 가능

## checked exceptio과 throws
<img width="492" alt="image" src="https://user-images.githubusercontent.com/108309396/233767314-02c4e3c0-2517-474b-947e-a827d263ec2d.png">  

- checked exception은 반드시 try~catch 또는 throws 필요 
- runtime exception은 throws하지 않아도 되지만 결국은 try~catch로 처리해야 함

## 로그 분석과 예외의 추적
- Throwable의 printStackTrace는 메서드 호출 스택 정보 조회 가능
  - 최초 호출 메서드에서부터 예외 발생 메서드까지의 스택 정보 출력
- 꼭 확인해야 할 정보
  - 예외 종류, 예외 원인(예외 객체의 메시지는 무엇인지), 디버깅 출발점(어디서 발생했는지)
  - 디버깅 출발점 확인시 참조하는 라이브러리(java.xx 등)는 과감히 건너뛰고 직접 작성한 코드 위주로 확인

## throws의 목적과 API 활용
- API가 제공하는 많은 메서드들은 사전에 예외가 발생할 수 있음을 선언부에 명시하고 프로그래머가 그 예외에 대처하도록 강요함
<img width="492" alt="image" src="https://user-images.githubusercontent.com/108309396/233767504-0031547b-6b79-4a48-9f5e-8c6778aacf26.png">

## Method overriding과 throws
- 메서드 재정의 시 조상 클래스 메서드가 던지는 예외보다 부모 예외를 던질 수 없다.  
<img width="261" alt="image" src="https://user-images.githubusercontent.com/108309396/233767551-03366eb8-33fa-40a3-90ef-59719a3feb9f.png">

# 사용자 정의 예외
- API에 정의된 exception 이외에 필요에 따라 사용자 정의 예외 클래스 작성
- 대부분 Exception 또는 RuntimeException 클래스를 상속받아 작성
  - checked exception 활용: 명시적 예외 처리 또는 throws 필요
    - 코드는 복잡해지지만 처리 누락 등 오류 발생 가능성은 줄어듦
  - runtime exception 활용: 묵시적 예외 처리 가능
    - 코드가 간결해지지만 예외 처리 누락 가능성 발생
- 사용자 정의 예외를 만들어 처리하는 것의 장점
  - 객체의 활용 : 필요한 추가 정보, 기능 활용 가능
  - 코드의 재사용 : 동일한 상황에서 예외 객체 재사용 가능
  - throws 메커니즘의 이용 : 중간 호출 단계에서 return 불필요