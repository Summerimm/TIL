# [객체 지향 프로그래밍 1]
## 객체 지향 프로그래밍이란?
- Object-Oriented Programming, OOP &rarr; 컴퓨터 프로그래밍의 패러다임 중 하나
- OOP는 컴퓨터 프로그램을 **명령어의 목록으로 보는 시각에서 벗어나서** 여러 개의 독립된 단위, 즉 "객체"들의 모임으로 파악하고자 하는 것
- 각각의 객체는 메시지를 주고 받고, 데이터를 처리할 수 있다.

### 절차 지향 프로그래밍(Procedure Programming, PP)
- 프로그램 전체가 유기적인 흐름으로 연결
- 기능 중심의 프로그램
- 장점: 순서가 정해져 있어 실행이 빠르다
- 단점: 하드웨어가 발전함에 따라 소프트웨어도 점점 커지고 복잡한 설계가 요구됨(Software Crisis) &rarr; 생산성&darr;
- '절차' 대신 핵심이 되는 '데이터'를 중심으로 생각

### 객체 지향 프로그래밍(Object-Oriented Programming, OOP)
- 프로그램을 여러 개의 독립된 객체들과 그 객체 간의 상호작용으로 파악하는 프로그래밍 방법  
![123](https://user-images.githubusercontent.com/108309396/215364110-70a0f401-5b3b-4215-b444-a9ef33b8a923.png)
- 장점
  - 객체는 잘 만들어놓으면 계속해서 재사용이 가능
  - 객체는 그 자체로 데이터와 행동이 정의됨(독립적) == 개발자가 내부 구조를 몰라도 그냥 가져다가 다른 객체와 조립하면서 개발이 가능
  - 객체 단위로 모듈화시켜 개발할 수 있어 많은 인원이 참여하는 대규모 소프트웨어 개발 가능
  - **개발 용이성, 유지보수 편의성, 신회성을 바탕으로 생산성 대폭 &uarr;**
- 단점
  - 설계 시 다양한 객체들의 상호 작용 구조를 만들기 위한 많은 노력과 시간이 필요
  - 실행 속도가 상대적으로 느림
    - 절차 지향 프로그래밍이 컴퓨터의 처리구조와 비슷해 실행 속도가 빠르다

## OOP 기초
### 객체
- CS에서 객체 또는 Object는 **클래스에서 정의한 것을 토대로 메모리에 할당된 것**으로 프로그램에서 사용되는 데이터 또는 식별자에 의해 참조되는 공간을 의미하며, 변수, 자료 구조, 함수 또는 메서드가 될 수 있다.
- 속성(data)과 행동(method)으로 구성된 모든 것

### Class와 Instance
- 클래스: 객체들의 분류/설계도
- 인스턴스: 하나하나의 실체/예
- 클래스로 만든 객체를 인스턴스라고 함
- 객체와 인스턴스의 차이점
```python
test_data = 'Hello World'
type(test_data) # <class 'str'>
```
- test_data는 객체다==test_data의 타입이 str 클래스이다. == test_data는 str 클래스의 인스턴스이다.
- data type과 data structure은 모두 클래스였다.(str, int, list, dict...)
- 파이썬은 모든 것이 객체, 모든 object는 특정 타입의 instance이다.

### 객체의 특징
- type: 어떤 operator와 method가 가능한가?
- attribute: 어떤 상태(데이터)를 가지는가?
- method: 어떤 행위(함수)를 할 수 있는가?
- `Object = Attribute + Method`


## OOP 문법
- 클래스 정의 `class MyClass:`
- 인스턴스 생성 `my_instance = MyClass()`
- 메서드 호출 `my_instance.my_method()`
- 속성 접근 `my_instance.my_attribute`

### 객체 비교하기
- `==`
  - equal, 변수가 참조하는 객체가 동등한(내용이 같은) 경우 True
  - 두 객체가 같아 보이지만 실제로 동일한 대상을 가리키고 있지 않을 수 있음
- `is`
  - identical
  - 두 변수가 동일한 객체를 가리키는 경우 True

### Attribute
- 특정 데이터 타입/클래스의 객체들이 가지게 될 상태/데이터를 의미
- 클래스 변수/인스턴스 변수가 존재

### 인스턴스와 클래스 간의 namespace
- 클래스를 정의하면, 클래스와 해당하는 namespace 생성
- 인스턴스를 만들면, 인스턴스 객체가 생성되고 namespace 생성
- 인스턴스에서 특정 attribute에 접근하면, 인스턴스-클래스 순으로 탐색

### 인스턴스 변수
- 인스턴스가 개인적으로 가지고 있는 attribute
- 각 인스턴스들의 **고유한** 변수
- 생성자 메서드`(__init__)`에서 `self.<name>`으로 정의
- 인스턴스가 생성된 이후 `<instance>.<name>`으로 접근 및 할당  
![화면 캡처 2023-01-30 101606](https://user-images.githubusercontent.com/108309396/215368544-beae1b09-19c5-4691-b164-ff4db692a062.png)

### 클래스 변수
- 한 클래스의 모든 인스턴스가 공유하는 값
- 같은 클래스의 인스턴스들은 같은 값을 갖게 됨
- 클래스 선언 내부에서 정의
- `<classname>.<name>`으로 접근 및 할당
- 클래스 변수를 변경할 때는 항상 클래스.클래스변수 형식으로 변경

### OOP Method
- 특정 데이터 타입/클래스의 객체에 공통적으로 적용 가능한 함수
- Python Methods
  - Instance Methods(usually used)
    - must have self parameter
    - no decorator needed
    - can be accessed through object(instace of Class)
    - 인스턴스 변수를 사용하는 함수
  - Class Methods
    - doesn't need self parameter
    - need decorator
    - can be accessed directly through the class
    - doesn't need instance of class
    - 인스턴스와 상관없이 클래스 단위에서 공통적으로 사용하는 함수
  - Static Methods

### Instance method
- 인스턴스 변수를 사용하거나, 인스턴스 변수에 값을 설정하는 메서드
- 클래스 내부에 정의되는 메서드의 기본
- 호출 시, 첫 번째 인자로 self가 자동으로 전달
- **`self`**: 인스턴스 자기자신
  - 인스턴스 메서드는 호출 시 첫 번째 인자로 인스턴스 자신이 전달되게 설계
- `magic method`: Double underscore(\__)가 있는 메서드로 특수한 동작을 위해 만들어진 메서드
  - 특정 상황에 자동으로 불림
  - `__str__`: 이 객체를 문자열로 표현하면 어떻게 표현할지를 지정
    - print() 함수 등에서 객체를 출력하면 자동으로 호출되는 메서드
  - `__gt__`: 부등호 연산자(>, greater than)
- 생성자(constructor) 메서드
  - 인스턴스 객체가 생성될 때 자동으로 호출되는 메서드
  - 인스턴스 변수들의 초기값을 설정
- 인스턴스 메서드는 클래스 변수, 인스턴스 변수 둘 다 사용 가능

### Class Method
- 클래스가 사용할 메서드
- @classmethod 데코레이터를 사용하여 정의
- 호출 시, 첫 번째 인자로 클래스(cls)가 전달됨
```python
class MyClass:

  @classmethod
  def class_method(cls, arg1, ...):

MyClass.class_method(...)
```
- 클래스 메서드는 인스턴스 변수 사용이 불가능

### Decorator
- 함수를 어떤 함수로 꾸며서 새로운 기능을 부여
- @데코레이터(함수명) 형태로 함수 위에 작성
- 순서대로 적용되기 때문에 작성 순서가 중요

### Static Method
- 인스턴스 변수, 클래스 변수를 전혀 다루지 않는 메서드
  - 즉, 객체 상태나 클래스 상태를 수정할 수 없음
- 속성을 다루지 않고 단지 기능(행동)만을 하는 메서드를 정의할 때 사용
- @staticmethod 데코레이터를 사용하여 정의
- 일반 함수처럼 동작하지만, 클래스의 namespace에 귀속됨
  - 주로 함수를 해당 클래스로 한정하는 용도로 사용