# Abstract Class(추상 클래스)
![image](https://user-images.githubusercontent.com/108309396/232356418-254e9f13-27e0-4551-ae83-ba3fd8613deb.png)  
- 자손 클래스에서 반드시 재정의해서 사용되기 때문에 조상 클래스에서 메서드의 구현이 무의미
  - **메서드의 선언부만 남기고 구현부는 세미콜론(;)으로 대체**
  - 구현부가 없다는 의미로 `abstract` 키워드를 메서드 선언부에 추가
  - **객체를 생성할 수 없는 클래스**라는 의미로 클래스 선언부에 `abstract`를 추가  
  ![image](https://user-images.githubusercontent.com/108309396/232356574-bef1ab36-41b7-4aca-b0e3-fcace8ef0c9c.png)  
  - &rarr; **abstract method design pattern**

## 추상 클래스의 특징
- abstract 클래스는 상속 전용의 클래스
  - 클래스에 구현부가 없는 메서드가 있으므로 객체를 생성할 수 없음
  - 하지만 상위 클래스 타입으로써 자식을 참조할 수는 있음  
  ![image](https://user-images.githubusercontent.com/108309396/232357218-46f0e73b-6bbd-407f-8ac2-06e09907468d.png)
  - 조상 클래스에서 상속받은 `abstract` 메서드를 재정의하지 않은 경우
    - 클래스 내부에 abstract 메서드가 있는 상황이므로 **자식 클래스는 abstract 클래스로 선언되어야 함**

## 추상 클래스를 사용하는 이유
- abstract 클래스는 **구현의 강제를 통해 프로그램의 안정성 향상**  
![image](https://user-images.githubusercontent.com/108309396/232356933-31014b6b-5f7a-4a5b-ba97-a2227165e47b.png)
- interface에 있는 메서드 중 구현할 수 있는 메서드를 구현해 개발의 편의 지원


# Interface
- 최고 수준의 추상화 단계: 일반 메서드는 모두 abstract 형태
- 형태
  - 클래스와 유사하게 interface 선언
  - 멤버 구성
    - 모든 멤버변수는 `public static final`이며 생략 가능
    - 모든 메서드는 `publice abstract이`며 생략 가능  
    ![image](https://user-images.githubusercontent.com/108309396/232357936-452f13ae-d61e-43d0-98c1-d9eee38673c2.png)  

## 인터페이스 상속
- 인터페이스도 `extends`를 이용해 상속이 가능
- 클래스와 다른 점은 인터페이스는 다중 상속이 가능(메서드 구현 자체가 없기 때문)   
![image](https://user-images.githubusercontent.com/108309396/232358172-9cd303ce-ee73-4adb-bdb8-736a1009b274.png)      
![image](https://user-images.githubusercontent.com/108309396/232358204-5f00c398-40d5-42b2-8110-67fa42b523b8.png)

## 인터페이스 구현과 객체 참조
- 클래스에서 `implements` 키워드를 사용해서 interface 구현
- `implements`한 클래스는
  - 모든 abstract 메서드를 override해서 구현하거나
  - 구현하지 않을 경우 abstract 클래스로 표시해야 함
- 여러 개의 `interface implements` 가능  
![image](https://user-images.githubusercontent.com/108309396/232358610-c6445ee9-e2f2-4394-8999-2ba3e3823e76.png)
- 다형성은 조상 클래스뿐 아니라 조상 인터페이스에도 적용  
![image](https://user-images.githubusercontent.com/108309396/232358925-9c83572a-e0b2-4355-806b-b57a841913fc.png)

## 인터페이스의 필요성
- 구현의 강제로 표준화 처리
  - `abstract` 메서드 사용  
- 인터페이스를 통한 간접적인 클래스 사용으로 **손쉬운 모듈 교체 지원**  
![image](https://user-images.githubusercontent.com/108309396/232363945-7250270e-d3e2-4976-ab9e-ee98e6a4eef8.png)
- 서로 상속의 관계가 없는 클래스들에게 인터페이스를 통한 관계 부여로 다형성 확장  
![image](https://user-images.githubusercontent.com/108309396/232364058-80b68740-b13c-41ca-94ea-70ce8c32c99c.png)
- 모듈 간 독립적 프로그래밍 가능 &rarr; 개발 기간 단축  
![image](https://user-images.githubusercontent.com/108309396/232364180-36f1b96e-057f-48a3-b1b8-d98890b6d64f.png)

### default method
- 인터페이스에 선언된 구현부가 있는 일반 메서드
  - 메서드 선언부에 default modifier 추가 후 메서드 구현부 작성
  - 접근 제한자는 public으로 한정됨(생략 가능)
- 필요성
  - 기존에 interface 기반으로 동작하는 라이브러리의 interface에 추가해야 하는 기능 발생
  - 기존 방식으로라면 모든 구현체들이 추가되는 메서드를 override해야 함
  - default 메서드는 abstract가 아니므로 반드시 구현해야 할 필요는 없어짐  
![image](https://user-images.githubusercontent.com/108309396/232364374-5c0b6cd2-ab2c-47b2-9471-77bcf67bceef.png)
- default method의 충돌
  - JDK8부터 default method가 생기면서 동일한 이름을 갖는 구현부가 있는 메서드가 충돌
  - method 우선 순위
    - super class의 method 우선: super class가 구체적인 메서드를 갖는 경우 default method는 무시됨
    - interface 간의 충돌: 하나의 interface에서 default method를 제공하고 다른 interface에서도 같은 이름의 메서드(default 유무와 무관)가 있을 때 sub class는 반드시 override해서 충돌 해결  
  ![image](https://user-images.githubusercontent.com/108309396/232365017-3291fce3-c32b-4fd9-a1ff-1b2eba2d5d56.png)

### static method
- interface에 선언된 static method
  - 일반 static 메서드와 마찬가지로 별도의 객체가 필요 없음
  - 구현체 클래스 없이 바로 인터페이스 이름으로 메서드에 접근해서 사용 가능  
 ![image](https://user-images.githubusercontent.com/108309396/232365200-02d01763-4148-4877-8f40-a547af4a881f.png)

 # Generic
 - 다양한 타입의 객체를 다루는 메서드, 컬렉션 클래스에서 **컴파일 시에 타입 체크**
 - 미리 사용할 타입을 명시해서 형 변환을 하지 않아도 되게 함
   - 객체의 타입에 대한 안전성 향상 및 형 변환의 번거로움 감소

### 표현
- 클래스 또는 인터페이스 선언시 `<>`에 타입 파라미터 표시
```java
public class Class_Name<T>{}
public interface Interface_Name<T>{}
```
  - `Class_Name`: Raw type
  - `Class_Name<T>`: Generic type
- 타입 파라미터
  - 특별한 의미의 알파벳보다는 단순히 임의의 참조형 타입을 말함
  - T: reference Type, E: Element, K: Key, V: Value  
  ![image](https://user-images.githubusercontent.com/108309396/232365800-a4ed782d-f0bb-45e1-a9e5-35c056935d75.png)
- 객체 생성
  - 변수 쪽과 생성 쪽의 타입은 반드시 같아야 함  
  ![image](https://user-images.githubusercontent.com/108309396/232365870-804e9ac4-0573-4dfd-a39f-8f6a4869c200.png)

### 클래스 생성
![image](https://user-images.githubusercontent.com/108309396/232365991-74bd974b-3ff5-471f-b587-3fdcd64e7e0f.png)

### 사용
- 컴파일 타입에 타입 파라미터들이 대입된 타입으로 대체됨  
- ![image](https://user-images.githubusercontent.com/108309396/232366181-e4bb6b88-7504-4c5f-894d-da6a79746fab.png)  

### type parameter의 제한
- 필요에 따라 구체적인 타입 제한 필요
  - type parameter 선언 뒤 `extends`와 함께 상위 타입 명시  
  ![image](https://user-images.githubusercontent.com/108309396/232366397-aef9f5cb-b42c-4413-a921-d5f838ef184b.png)  
- 인터페이스로 제한할 경우도 `extends` 사용
- 클래스와 함께 인터페이스 제약 조건을 이용할 경우 `&`로 연결  
  ![image](https://user-images.githubusercontent.com/108309396/232366557-ecbadc4c-470c-4127-9531-b03ca26dee1a.png)

### Generic Type 객체를 할당 받을 때 와일드 카드(`?`) 이용
- generic type에서 구체적인 타입 대신 사용  
![image](https://user-images.githubusercontent.com/108309396/232366644-3b834155-0ac2-48b8-a805-deab8a8d087b.png)

## Generic Method
- 파라미터와 리턴타입으로 type paremeter를 갖는 메서드
  - 메서드 리턴 타입 앞에 타입 파라미터 변수 선언  
![image](https://user-images.githubusercontent.com/108309396/232366870-f8c9f823-bf21-4462-8969-7d30e636564d.png)  
![image](https://user-images.githubusercontent.com/108309396/232366900-1d083164-7f52-4243-ba58-6959bccfc452.png)  
