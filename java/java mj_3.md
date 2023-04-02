# 객체지향 프로그래밍
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