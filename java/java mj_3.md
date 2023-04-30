# 객체지향 프로그래밍1
### 객체지향 프로그래밍(Object Oriented Programming)
- 객체란?
  - 주체가 아닌 것, 주체가 활용하는 것
- 객체지향 프로그래밍이란?
  - 주변의 많은 것들을 객체화해서 프로그래밍하는 것

### 객체지향 프로그래밍의 장점
- 블록 형태의 모듈화된 프로그래밍
  - 신뢰성&uarr;
  - 추가/수정/삭제가 용이
  - 재사용성&uarr;

### 현실 세계 객체/클래스, 프로그램의 객체(instance, object)의 관계
- 현실의 객체가 갖는 속성과 기능은 **추상화(abstraction)**되어 클래스에 정의된다
- 클래스는 **구체화**되어 **프로그램의 객체**가 된다
- 상태, 속성: 변수, 필드
- 기능, 행위: 메서드, 함수  
<img width="627" alt="image" src="https://user-images.githubusercontent.com/108309396/229339016-ddbfee07-8ad9-40cd-bb6f-b206025066a7.png">  

- 클래스
  - 객체를 정의 해놓은 것 즉 객체의 설계도, 틀
  - 클래스는 직접 사용할 수 없고, 직접 사용되는 객체를 만들기 위한 틀을 제공할 뿐
  - 클래스 이름이 곧 타입이 됨
- 객체(instance, object)
  - 클래스를 데이터 타입으로 메모리에 생성된 것  
<img width="829" alt="image" src="https://user-images.githubusercontent.com/108309396/229339585-3e2f5356-04f1-4ec4-bb58-87b3817d4659.png">

## 객체 생성과 메모리
### JVM의 메모리 구조
<img width="768" alt="image" src="https://user-images.githubusercontent.com/108309396/229339648-4327fe58-5530-4073-83b3-3e007e194f36.png">

### 객체의 생성과 메모리 할당
<img width="826" alt="image" src="https://user-images.githubusercontent.com/108309396/229339676-c70fad2c-cf70-422b-8600-0eb1d1468956.png">

# 변수
- 타입에 따른 분류  
<img width="694" alt="image" src="https://user-images.githubusercontent.com/108309396/229361203-1f1c0cfd-5170-422e-b266-99c22184dbaa.png">  
- 선언 위치에 따른 분류  
<img width="730" alt="image" src="https://user-images.githubusercontent.com/108309396/229361237-d85622e3-a5fd-46e5-8080-1de2aabfaeb6.png">  

## 인스턴스 멤버 변수의 특징
- 선언 위치: 클래스 {}영역에 선언
- 변수의 생성: 객체가 만들어질 때 객체 별로 생성됨
  - 생성 메모리 영역: heap
- 변수의 초기화: 타입 별로 default 초기화
- 변수에의 접근: 객체 생성 후(메모리에 올린 후) 객체 이름(소속)으로 접근
  - 객체 별로 생성되기 때문에 객체마다 고유한 상태(변수 값) 유지
- 소멸 시점: Garbage Collector에 의해 객체가 없어질 때 &rarr; 프로그래머가 명시적으로 소멸시킬 수 X

## 클래스 멤버 변수의 특징
- 선언 위치: 클래스 {}영역에 선언, `static` 키워드를 붙임
- 변수의 생성: 클래스 영역에 클래스 로딩 시 메모리 등록 &rarr; 개별 객체의 생성과 무관, 모든 객체가 공유하게 됨(공유 변수라고도 불림)
- 변수의 초기화: 타입 별로 default 초기화
- 변수에의 접근: 객체 생성과 무관하게 클래스 이름(소속)으로 접근
  - 객체를 생성하고 객체 이름으로 접근도 가능하나 static에 부합한 표현은 아님
- 소멸 시점: 프로그램 종료 시

## 지역 변수 & 파라미터 변수
- 선언 위치: 클래스 {}영역 이외의 모든 중괄호 안에 선언되는 변수들
  - 메서드, 생성자, 초기화 블록
- 변수의 생성: 선언된 라인이 실행될 때
  - 생성 메모리 영역: thread별로 생성된 stack 영역
- 변수의 초기화: 사용하기 전 명시적 초기화 필요
- 변수에의 접근: 외부에서는 접근이 불가능하므로 소속 불필요
  - 내부에서는 이름에 바로 접근
- 소멸 시점: 선언된 영역인 {}을 벗어날 때

## [예제] Compiling
![image2](https://user-images.githubusercontent.com/108309396/229537357-13fe8786-df7f-4460-90f3-e97e7c222bea.png)

# 메서드
## 메서드 정의와 필요성
- 메서드란?
  - 현실의 객체가 하는 동작을 프로그래밍화
  - 어떤 작업을 수행하는 명령문의 집합
- 메서드를 작성하는 이유
  - 반복적으로 사용되는 코드의 중복 방지
  - 코드의 양을 줄일 수 있고 유지 보수가 용이함
- 메서드의 작성 방법
  - 어떤 값을 입력받아서(파라미터 &rarr; 생략 가능)
  - 작업을 진행하고(실행 문장)
  - 결과를 돌려주는 역할(리턴 값 &rarr; 생략 가능)

### Variable arguments
- 메서드 선언 시 몇 개의 인자가 들어올 지 예상할 수 없을 경우(또는 가변적)
  - 배열 타입을 선언할 수 있으나 메서드 호출 전 배열을 생성, 초기화해야하는 번거로움
  - `...`을 이용해 파라미터를 선언하면 호출 시 넘겨준 값의 개수에 따라 자동으로 배열 생생 및 초기화  
<img width="280" alt="image" src="https://user-images.githubusercontent.com/108309396/229362141-035ff573-b1c2-4126-862b-0bad4c1291b8.png">

## 메서드 호출
- 메서드를 호출할 때는 메서드의 선언부에 맞춰 호출해야 함
  - 메서드 이름: 반드시 동일
  - 파라미터: 선언된 파라미터의 개수는 반드시 동일, 타입은 promotion 적용 가능
- 메서드 접근
  - 멤버 변수와 마찬가지로 static(메모리에 올라가 있음) 또는 non static 상태를 구분해서 호출  
<img width="705" alt="image" src="https://user-images.githubusercontent.com/108309396/229362306-11b76777-006c-4624-a1c1-e27360a08385.png">

### class 멤버와 instance 멤버 간의 참조와 호출
- 가장 중요한 것은 호출하려는 멤버가 있는가?
  - 메모리에 있으면 호출 가능
  - 메모리에 없으면 호출 불가-먼저 메모리에 로딩 후 사용해야 함  
- static member &rarr; 언제나 메모리에 있음
  - 클래스 로딩 시 자동 등록
- instance member &rarr; 객체 생성 전에는 메모리에 없음
  - 객체 생성 시 모든 일반 멤버들은 메모리에 생성
  - 객체 즉 레퍼런스를 통해 접근

## 메서드 호출 스택
<img width="712" alt="image" src="https://user-images.githubusercontent.com/108309396/229362708-ade1afae-de3d-4004-8460-911ead2dcb5b.png">  

- 스택(stack)
  - FILO
- 메서드 호출 스택
  - 각각의 메서드 호출 시 메서드 동작을 위한 메모리 상자를 하나씩 할당
    - 상자 내부에 메서드를 위한 파라미터 변수 등 로컬 변수 구성
  - A메서드에서 새로운 메서드 B 호출 시 B 실행을 위한 메모리 상자를 쌓음
    - 언제나 맨 위에 있는 메모리 상자(B)만 활성화
    - 이때 A메서드는 동작이 끝나지 않고 잠시 정지된 상태
    - B가 리턴하게 되면 B를 위한 상자가 제거되며 메모리 반납
    - A가 최상위가 되어 다시 동작 재개

## 기본형 변수와 참조형 변수
- 메서드 호출 시 파라미터로 입력된 값을 **복사해서** 전달  
<img width="857" alt="image" src="https://user-images.githubusercontent.com/108309396/229362943-c26372d9-175a-4c9b-b78d-18a6f64d239a.png">

## 메서드 오버로딩
- overloading: 동일한 기능을 수행하는 메서드의 추가 작성
  - 일반적으로 메서드 이름은 기능별로 의미 있게 정함
  - 동일한 기능을 여러 형태로 정의해야 할 때 사용
- 장점: 기억해야 할 메서드가 감소하고 중복 코드에 대한 효율적인 관리가 가능
- 방법
  - 메서드 이름은 동일
  - 파라미터의 개수 또는 순서, 타입이 달라야 함(파라미터가 같으면 중복 선언 오류 발생)
  - 리턴 타입은 의미 없음

# 생성자
- 객체를 생성할 때 호출하는 메서드 비슷한 것
  - new 키워드와 함꼐 호출하는 것
  - 일반 멤버 변수의 초기화나 객체 생성 시 실행돼야 하는 작업 정리
- 작성 규칙
  - 메서드와 비슷하나 리턴 타입이 없고 이름은 클래스 이름과 동일  
<img width="543" alt="image" src="https://user-images.githubusercontent.com/108309396/229363290-4c781a0a-965e-48e5-954e-b664bae302a1.png">

## 생성자의 종류
- 기본 생성자(default constructor)
  - 파라미터가 없고 구현부가 비어있는 상태
  - 생성자 코드가 없으면 컴파일러가 기본 생성자 제공
```java
public DefaultPerson() {}
```
- 파라미터가 있는 생성자
  - 생성자의 목적이 일반 멤버 변수의 초기화 &rarr; 생성자 호출 시 값을 넘겨줘서 초기화
  - 주의! 파라미터가 있는 생성자를 만들면 기본 생성자는 추가되지 않는다.
```java
ParameterPerson(String n, int a, boolean i) {
  String name = n;
  int age = a;
  boolean isHungry = i;
}
```

### this의 용법
- 참조 변수로써 객체 자신을 가리킴
  - 참조 변수를 통해 객체의 멤버에 접근했던 것처럼 `this`를 이용해 자신의 멤버에 접근 가능
- 용도
  - 로컬 변수와 멤버 변수의 이름이 동일할 경우 멤버 변수임을 명시적으로 나타냄
  - 명시적으로 멤버임을 나타낼 경우 사용  
<img width="327" alt="image" src="https://user-images.githubusercontent.com/108309396/229363732-dbbc1db3-e401-4bd4-a3f1-fbcff8eac8dc.png">
- `this`는 객체에 대한 참조이기 때문에 `static` 영역에서 `this` 사용 불가  
<img width="381" alt="image" src="https://user-images.githubusercontent.com/108309396/229363756-959b87dd-4e88-4ddb-9ed7-6a3789ffb764.png">

### this()
- 메서드와 마찬가지로 생성자도 오버로딩 가능
  - 객체 생성 시 필요한 멤버변수만 초기화 진행 &rarr; 생성자 별 코드의 중복 발생
  - 한 생성자에서 다른 생성자를 호출할 때 사용
- 반드시 첫 줄에서만 호출이 가능  
<img width="688" alt="image" src="https://user-images.githubusercontent.com/108309396/229364449-6fb7ccdb-3b5a-4d24-b431-c6f28481d105.png">