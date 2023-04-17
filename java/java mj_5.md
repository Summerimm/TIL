# Encapsulation(데이터 은닉과 보호)
## 제한자(modifier)
- 클래스, 변수, 메서드 선언부에 함께 사용되어 부가적인 의미 부여
- 종류
  - 접근 제한자: `public, protected, (default = package), private`
  - 그 외 제한자
    - `static`: 클래스 레벨의 요소 설정
    - `final`: 요소를 더 이상 수정할 수 없게 함
    - `abstract`: 추상 메서드 및 추상 클래스 작성
    - `synchronized`: 멀티스레드에서의 동기화 처리
- 하나의 대상에 여러 제한자를 조합 가능하나 접근 제한자는 하나만 사용 가능
- 순서는 무관하나 일반적으로 접근 제한자를 맨앞에 배치

### `final`
- 마지막, 더 이상 바뀔 수 없음
- 용도
  - `final class` - 더 이상 확장할 수 없음: 상속 금지 &rarr; 오버라이드 방지
  - `final method` - 더 이상 재정의할 수 없음: overriding 금지
  - `final variable` - 더 이상 값을 바꿀 수 없음: 상수화

## 접근 제한자(Access modifier)
- 멤버 등에 사용되며 해당 요소를 외부에서 사용할 수 있는지 설정  
<img width="542" alt="image" src="https://user-images.githubusercontent.com/108309396/232309412-00bbe4c7-c2d4-4202-9699-86a9827c68d7.png">  
<img width="530" alt="image" src="https://user-images.githubusercontent.com/108309396/232309437-80fe2ab0-487d-40d8-b3f3-f3d211cb3bf1.png">  

## Encapsulation(데이터 은닉과 보호)
- 변수는 `private` 접근으로 막기
- 공개되는 메서드를 통한 접근 통로 마련: `setter/getter`
  - 메서드에 정보 보호 로직 작성

## Singleton Design Pattern
- 객체의 생성을 제한하는 경우, 싱글톤 디자인 패턴을 사용함
  1. 여러 개의 객체가 필요없는 경우
    - 객체를 구별할 필요가 없는 경우 = 수정 가능한 멤버 변수가 없고 기능만 있는 경우
    - stateless한 객체라고 함
  2. 객체를 계속 생성/삭제하는데 많은 비용이 들어서 재사용이 유리한 경우
- 싱글톤 디자인 패턴
  - 외부에서 생성자에 접근 금지 &rarr; 생성자의 접근 제한자를 private으로 설정
  - 내부에서는 private에 접근 가능하므로 직접 객체 생성 &rarr; 멤버 변수이므로 private 설정
  - 외부에서 private member에 접근 가능한 getter 생성 &rarr; setter는 필요X
  - 객체 없이 외부에서 접근할 수 있도록 getter와 변수에 `static` 추가
  - &rarr; 외부에서는 언제나 getter를 통해 객체를 참조하므로 하나의 객체를 재사용하게 됨
```java
class SingletonClass {
  private static SingletonClass instance = new SingletonClass();
  private SingletonClass() {}

  public static SingletonClass getInstance() {
    return instance;
  }
}
```


# 다형성(Polymorphism)
- 하나의 객체가 많은 형(타입)을 가질 수 있는 성질
- **상속 관계**에 있을 때 *조상 클래스의 타입으로 자식 클래스 객체를 레퍼런스* 할 수 있다

## 다형성의 활용 예시
1. 다른 타입의 객체를 다루는 배열
   - 배열의 특징: 같은 타입의 데이터를 묶음으로 다룬다.
   - 다형성으로 다른 타입의 데이터를 하나의 배열로 관리 가능  
    <img width="502" alt="image" src="https://user-images.githubusercontent.com/108309396/232312270-19547645-e450-4691-adb6-98c8f6b1ebb1.png">    
   - Object는 모든 클래스의 조상이므로  Object의 배열은 어떤 타입의 객체라도 저장 가능  
   - `objs[3] = 3`: autoboxing 기능에 의해 가능(기본형은 Object를 상속받지 않지만 `Integer.valueOf(3)`을 autoboxing) 
2. 매개변수의 다형성
   - 메서드가 호출되기 위해서는 메서드 이름과 파라미터가 맞아야 함
   - 조상을 파라미터로 처리한다면 객체의 타입에 따라 메서드를 만들 필요가 없어진다.  
  <img width="200" alt="image" src="https://user-images.githubusercontent.com/108309396/232312699-a404a9c2-d2af-4d00-9a9d-d682b21c0b66.png">
  - 즉, API에서 파라미터로 Object를 받는다는 것은 모든 객체를 처리한다는 말 &rarr; 필요하다면 하위클래스에서 오버라이딩

## 참조형 객체의 형 변환
- 메모리에 있더라도 참조하는 변수의 타입에 따라 접근할 수 있는 내용이 제한됨  
  <img width="591" alt="image" src="https://user-images.githubusercontent.com/108309396/232313817-a6d88fb6-07bf-4cad-a953-6b1e7ff1f5de.png">
  - `Person person = new SpiderMan();`이라고 해도 person에서 fireWeb()을 사용하지 못 함
1. 작은 집(child)에서 큰 집(super)으로 &rarr; 묵시적 casting
   - 자손 타입의 객체를 조상 타입으로 참조: 형$ 변환 생략 가능
   - 조상의 모든 내용이 자식에 있기 때문  
    <img width="480" alt="image" src="https://user-images.githubusercontent.com/108309396/232313992-ea896208-631b-42df-bcef-47c99fc019a9.png">
2. 큰 집(super)에서 작은 집(child)으로 &rarr; 명시적 casting
   - 조상 타입을 자손 타입으로 참조할 경우 형 변환 생략 불가  
    <img width="431" alt="image" src="https://user-images.githubusercontent.com/108309396/232314011-f9fe26c4-9ee7-4ec9-8e49-e07cf6c1188c.png">

### 예시
- 무늬만 SpiderMan인 Person
```java
Person person = new Person();
SpiderMan sman = (SpiderMan) person;
sman.fireWeb();
```
- 메모리의 객체는 `fireWeb()`이 없음  
<img width="289" alt="image" src="https://user-images.githubusercontent.com/108309396/232314314-9f95998f-0cab-4b18-a779-7aadfd0c95a7.png">

- 오류 발생   
<img width="173" alt="image" src="https://user-images.githubusercontent.com/108309396/232314271-d28f5df5-1f5a-4785-8685-8653845de833.png">

- **조상을 무작정 자손으로 바꿀 수 없음** 
  - `instanceof` 연산자 사용: 실제 메모리에 있는 객체가 특정 클래스 타입인지 boolean으로 리턴
```java
Person person = new Person();

if (person instanceof SpiderMan) {
  SpiderMan sman = (SpiderMan) person;
}
```

## 참조 변수의 레벨에 따른 객체의 멤버 연결
<img width="510" alt="image" src="https://user-images.githubusercontent.com/108309396/232314507-176c4890-9393-4995-9f34-6382f75fbcc3.png">    

- 실행결과: sub / sub class method / super / sub class method


## 정적 바인딩과 동적 바인딩
1. 정적 바인딩(static binding)
   - 컴파일 단계에서 **참조 변수의 타입에 따라** 연결이 달라짐
   - 상속 관계에서 객체의 **멤버 변수(static/instance)가 중복**될 때 또는 static method
2. 동적 바인딩(dynamic binding)
   - 다형성을 이용해서 메서드 호출이 발생할 때 runtime에 메모리의 실제 객체의 타입으로 결정
   - 상속 관계에서 객체의 **instance method가 재정의 되었을 때** 마지막에 재정의된 **자식 클래스의 메서드가 호출됨**
     - 최대한 메모리에 생성된 실제 객체에 최적화된 메서드가 동작함   
    <img width="685" alt="image" src="https://user-images.githubusercontent.com/108309396/232315158-d3e7c630-f877-4319-aed4-65d7f47d38b0.png">
