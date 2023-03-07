# 객체지향 프로그래밍 Part2
## 패키지(package)
- 프로그램의 많은 클래스를 관리하기 위해 패키지를 사용
- 마치 PC의 많은 파일을 관리하기 위해 폴더를 이용하는 것과 동일
- 패키지는 클래스와 관련 있는 인터페이스들을 모아두기 위한 namespace
- 패키지의 구분은 .(dot) 연산자를 이용
- 패키지의 이름은 시중에 나와있는 패키지들과 구분되게 지어야 함
- 일반적으로 소속이나 회사의 도메인을 사용(`com.ssafy.project_이름.module_이름`)

## Import
- import를 선언할 때는 import 키워드 뒤에 package 이름과 클래스 이름을 모두 입력
- 혹은 해당 패키지의 모든 클래스를 포함할 때는 '*'을 사용
```java
import package_name.class_name;
import package_name.*;
```
```java
package pkg1;

import pkg1.pkg2.Person; // 패키지명을 생략하고 쓰겠다는 의미

public class PackageTest{
  public static void main(String[] args){
    // 서로 다른 패키지에 있는 클래스 중에서 하나를 골라서 쓸 때
    Person p1 = new Person();
    System.out.println(p1.pkg);

    // 만약에 서로 다른 패키지에 있는 이름이 같은 클래스를
    // 두 개 이상 사용하고 싶다면
    // 패키지 생략 불가능
    // 패키지명.클래스명 => 풀패키지 이름
    pkg1.Person p1 = new pkg1.Person();
    pkg1.pkg2.Person p2 = new pkg1.pkg2.Person();
    Person p3 = new Person();

    System.out.println()
  }
}
// pkg1
// pkg1.pkg2
// pkg1.pkg2
```

## 캡슐화(Encapsulation)
- 객체의 속성(data fields)과 행위(methods)를 하나로 묶고 실제 구현 내용 일부를 외부에 감추어 은닉

### 접근 제한자(access modifier)
- 클래스(public or default만 가능), 멤버 변수, 멤버 메서드 등의 선언부에서 접근 허용 범위를 지정하는 역할의 키워드
- 종류
  - public: **모든 위치에서** 접근 가능
  - protected: **같은 패키지에서** 접근이 가능. 단, 다른 패키지의 클래스와 **상속관계**가 있을 경우는 다른 패키지도 접근 가능
  - (default): **같은 패키지에서만** 접근이 허용. 선언 안 되었을 경우 기본 적용
  - private: **자신 클래스에서만** 접근이 허용
- 그 외 제한자
  - static: 클래스 레벨의 요소 설정
  - final: 요소를 더 이상 수정할 수 없게 함
  - abstract: 추상 메서드 및 추상 클래스 작성

### 접근자(getter)/설정자(setter)
- 클래스에서 선언된 변수 중 접근제한에 의해 접근할 수 없는 변수의 경우 다른 클래스에서 접근할 수 없기 때문에, 
- 접근하기 위한 메서드(getter and setter)를 public으로 선언하여 사용
- getter: 접근자
- setter: 설정자
```java
public class Person{
  private String name;
  private int age;

  public String getName(){
    return name;
  }

  public void setName(String name){
    this.name = name;
  }

  public int getAge(){
    return age;
  }

  public void setAge(int age){
    this.age = age;
  }
}
```

### 싱클턴 패턴(Singleton Pattern)
- 기존에는 클래스를 만들어 놓으면 객체를 무한 생성 가능.
- 소프트웨어 디자인 패턴에서 싱클턴 패턴을 따르는 클래스는 생성자가 여러 차례 호출되더라도 
- 실제로 생성되는 객체는 하나이고 최초 생성 이후에 호출된 생성자는 최초의 생성자가 생성한 객체를 리턴함
```java
public class Manager{

  // static: 객체를 생성하지 않고, 클래스 이름으로 접근하기 위함
  private static Manager manger = new Manager();  // 자기 자신 객체를 1번만 생성

  // 외부에서 새로운 객체를 생성할 수 없도록 생성자를 private으로 막음
  private Manager() {
    this.name = "유일한 사람";
    this.age = 24;
  }

  // 유일한 객체에 접근할 수 있는 메서드(public)
  public static Manager getManager(){
    return manager;
  }
}
```

## JVM 메모리 구조
- Java 언어는 메모리 관리를 개발자가 하지 않음
- GC(Garbage Collection)가 메모리 관리  
<img width="998" alt="image" src="https://user-images.githubusercontent.com/108309396/223443503-1a9d52f7-2fcf-4774-b4f0-c213d834833b.png">

### static 특징
1. 로딩 시점
  - `static`: 클래스 로딩 시
  - `non-static`: 객체 생성 시
2. 메모리 상의 차이
  - `static`: 클래스 당 하나의 메모리 공간만 할당
  - `non-static`: 인스턴스 당 메모리가 별도로 할당
3. 문법적 특징
  - `static`: 클래스 이름으로 접근
  - `non-static`: 객체 생성 후 접근
4. static 영역에서는 non-static 영역을 직접 접근이 불가능
5. non-static 영역에서는 static 영역에 대한 접근이 가능

## 객체 배열 관리
- 정보 관리 시스템
- 캡슐화를 이용하여 클래스 작성
- DB 대신 배열을 사용해 객체의 정보를 저장
- 객체의 조회, 추가, 수정, 삭제(CRUD)를 구현
- 싱글턴 패턴을 사용하여 정보 관리 일원화