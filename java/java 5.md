# 객체 지향 프로그래밍(Object Oriented Programming, OOP)
- 객체: 사물과 같이 유형적인 것과 개념이나 논리와 같은 무형적인 것들
  - 속성: 데이터 &rarr; 변수
  - 행위: 알고리즘 &rarr; 메서드
- 클래스(Class): 객체를 만드는 설계도(Blueprint) or 형틀(template)
- 인스턴스(Instance): 클래스를 통해 생성된 객체
- 장점: 모듈화된 프로그래밍, 재사용성&uarr;

## 객체지향 프로그래밍 특징(A PIE)
- Abstraction(추상화))
- Polymorphism(다형성)
- Inheritance(상속)
- Encapsulation(캡슐화)

## 클래스(Class)
- 관련 있는 변수와 함수를 묶어서 만든 사용자정의 <자료형>
- 각 객체들이 어떤 특징(속성과 동작)을 가지고 있을지 결정한다.
- 클래스 구성
  - 속성(Attribute) - 필드: 변수, 데이터
  - 동작(Behavior) - 메서드
  - 생성자(Constructor)
  - 중첩 클래스(클래스 내부의 클래스)
```java
/*
[접근제한자][활용제한자]class 클래스명(PascalCase){
  속성 정의(필드);
  기능 정의(메서드);
  생성자;
*/
public class Person{
  String name;
  int age;

  public void eat(){
  }

  public Person(){
  }
}  
```
- 클래스명 변수명(camelCase)  = new 클래스명();
- 변수명.필드명;
- 변수명.메서드명();
- `.`은 멤버연산자
```java
package test01;
// 모든 클래스는 특정 패키지(폴더)에 속해 있음
// 패키지: 클래스가 모여있는 폴더

// class 키워드를 사용
public class Person {
    // 속성, 데이터, 필드, 변수
    String name;
    int age;

    // 생성자
    // 클래스명과 같다.
    // 반환형을 지정X(메서드와 다름)
    public  Person(){

    }

    // 메서드
    public  void eat(){
        System.out.println(name+"이 식사를 합니다.");
    }

}

```
```java
package test01;

public class PersonTest {
    public static void main(String[] args) {
        Person p1 = new Person(); // 객체의 생성: new 키워드 + 생성자 호출
        p1.age = 25;
        p1.name = "김싸피";
        p1.eat();

        Person p2 = new Person();
        p2.age = 21;
        p2.name = "김코딩";
        p2.eat();
    }
}
```

## 변수
- 클래스 변수(class variable)
  - 클래스 영역 선언(static 키워드)
  - 생성시기: 클래스가 메모리에 올라갔을 때
  - 모든 인스턴스가 공유
- 인스턴스 변수(Instance variable)
  - 클래스 영역 선언
  - 생성시기: 인스턴스가 생성되었을 때(new)
  - 인스턴스 별로 생성됨
- 지역 변수(local variable)
  - 클래스 영역 이외(메서드, 생성자...)
  - 생성시기: 선언되었을 때