# 객체지향 프로그래밍 - Part 1
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

## Class
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

## Variable
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
```java
package test02;

public class Person {
    // static 키워드 -> 클래스 변수
    // 이 클래스로 생성되는 모든 인스턴스가 공유
    static String species = "호모 사피엔스 사피엔스";
    
    // static 키워드가 없으면 -> 인스턴스 변수
    String name;
    int age;

    // 생성자를 만들지 않고..
    // 만약에 설계도에 생성자가 하나도 없다면
    // JVM이 기본 생성자를 추가해줌
    // Person(){
    public void eat(){
        // 지역 변수
        String dish = "짜장면";
    }
}
```
```java
package test02;

public class PersonTest {
    public static void main(String[] args) {
        Person p1 = new Person();
        Person p2 = new Person();
        Person p3 = new Person();

        System.out.println(Person.species); // 클래스 변수이므로 클래스명.으로 접근 가능
        System.out.println(p1.species); // 호모 사피엔스 사피엔스
        System.out.println(p2.name); // null
        System.out.println(p3.age); // 0
    }
}
```
## Method
- 객체가 할 수 있는 행동을 정의
- 어떤 작업을 수행하는 명령문의 집합에 이름을 붙여 놓은 것
- 메소드의 이름은 소문자로 시작하는 것이 관례(camelCase)
```java
/*
[접근제한자][활용제한자] 반환값 메소드이름([매개변수들]){
  행위 기술...
}
*/
public static void main(String [] args){
  
}
```
```java
package test04;

public class Person {
    // 메서드의 종료
    // - 블록의 끝을 만날 때
    // - return문을 만날 때(void에서도 return문을 쓸 수 있음)
    public void study(String subject){
        double probability = Math.random();
        System.out.println(subject+"를 공부합니다.");
        System.out.println("알고리즘 문제를 풉니다.");
        if(probability < 0.5)
            return;
        System.out.println("게임을 합니다.");
        System.out.println("롤 영상을 시청합니다.");
    }
}
```

### Method Overloading
- 이름이 같고 매개변수가 다른 메소드를 여러 개 정의하는 것
- 중복 코드에 대한 효율적 관리 가능
- 파라미터의 개수 또는 순서, 타입이 달라야 할 것(파라미터 이름만 다른 것은 X)
- return 타입이 다른 것은 의미X
```java
package test04;

public class Person {
    // ...
    // 메서드 오버로딩: 이름이 같은 메서드 여러 개를 만들 수 있다.
    // 파라미터가 달라야 함!
    // 장점: 다양한 자료형에 대해 메서드를 만들 때 이름을 똑같이 할 수 있음
    public int add(int a, int b){
        return a + b;
    }
    public double add(double a, double b){
        return a + b;
    }

    // 메서드 오버로딩
    public void eat(){
        System.out.println("식사를 합니다.");
    }
    public void eat(String dish){
        System.out.println(dish+"를 먹습니다.");
    }
    public void eat(String dish, int times){
        System.out.println(dish+"를 "+times+"번 먹습니다.");
    }
    // 파라미터의 순서가 바뀌어도 가능
    public void eat(int times, String dish){
        System.out.println(times+"번 "+dish+"를 먹습니다.");
    }
}
```
```java
package test04;

public class PersonTest {
    public static void main(String[] args) {
        Person p1 = new Person();
        // add method
        int sum = p1.add(4, 5);
        double sum2 = p1.add(4.5, 5.5);
        System.out.println(sum);
        System.out.println(sum2);
        // eat method
        p1.eat();
        p1.eat("탕수육");
        p1.eat("햄버거", 3);
        p1.eat(5, "피자");
    }
}
// 9
// 10.0
// 식사를 합니다.
// 탕수육를 먹습니다.
// 햄버거를 3번 먹습니다.
// 5번 피자를 먹습니다.
```

## 생성자 메서드(Constructor Method)
- new 키워드와 함께 호출하여 객체 생성
- 클래스명과 동일
- **결과형 리턴값을 갖지 않음(void도 쓰지 않음)**
- 객체가 생성될 때 반드시 하나의 생성자 호출
- 멤버필드의 초기화에 주로 사용
- 하나의 클래스 내부에 생성자가 하나도 없으면 자동적으로 default 생성자가 있는 것으로 인지  
  - default 생성자: 매개변수도 없고 내용도 없는 생성자
- 매개변수의 개수가 다르거나, 자료형이 다른 여러 개의 생성자가 있을 수 있음(**생성자 오버로딩**)
- 생성자의 첫번째 라인으로 this() 생성자를 사용하여 또 다른 생성자를 하나 호출 가능
```java
public class Dog{
  public Dog(){
    System.out.println("기본 생성자!");
    System.out.println("클래스 이름과 동일하고 반환타입X");
  }
}
```

### Default Constructor
- 클래스 내에 생성자가 하나도 정의되어 있지 않은 경우 JVM이 자동으로 제공하는 생성자
- 형태: 매개변수가 없는 형태, 클래스명(){}

### 파라미터가 있는 생성자
- 생성자의 목적이 **필드 초기화**
- 생성자 호출 시 값을 넘겨주어야 함
- 해당 생성자를 작성하면 JVM에서 기본 생성자를 추가X

### this
- 참조 변수로써 객체 자신을 가리킴
- this를 이용하여 자신의 멤버 접근 가능(변수, 메서드) &rarr; `this.eat()`, `this.name`
- 지역변수(매개변수)와 필드의 이름이 동일할 경우 필드임을 식별할 수 있게 함
  - `this.name = name`
  - 왼쪽 `this.name`의 `name`은 필드, 오른쪽의 `name`은 지역변수 혹은 매개변수
- 객체에 대한 참조이므로 static 영역(클래스 단위)에서 this 사용 불가

### this의 활용
- `this.멤버변수`
- this( [인자값..] ) : 생성자 호출
- this 생성자 호출 시 제한사항
  - 생성자 내에서만 호출이 가능
  - 생성자 내에서 첫 번째 구문에 위치해야함
```java
    // 파라미터가 있는 생성자
    public Person(String name, int age){
        // this 키워드: 인스턴스의 멤버에 접근
        this.name = name;
        this.age = age;
    }
    public Person(){
        this("정민우", 31); // Person("정민우", 31);
    }

    public void sleep(){
        System.out.println("잠을 잡니다.");
    }

    public void eat(){
        System.out.println("식사를 합니다.");
        this.sleep();
    }
```