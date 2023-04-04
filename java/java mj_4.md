# 객체지향 프로그래밍2
## 객체지향 언어의 특징
&rarr; OOP is APIE
- **Abstraction(추상화)**: 현실의 객체를 추상화해서 클래스를 구성한다.
- **Polymorphism(다형성)**: 하나의 객체를 여러 가지 타입(형)으로 참조할 수 있다.
- **Inheritance(상속)**: 부모 클래스의 자산을 물려받아 자식을 정의함으로써 코드의 재사용이 가능하다.
- **Encapsulation(데이터 은닉과 보호)**: 데이터를 외부에 직접 노출시키지 않고 메서드를 이용해 보호할 수 있다.

# 상속(Inheritance)
- 기존 클래스의 자산(멤버)을 자식 클래스에서 재사용하기 위한 것
  - 부모의 생성자와 초기화 블록은 상속X
- 기존 클래스의 멤버를 물려받기 때문에 코드의 절감
  - 부모의 코드를 변경하면 모든 자식들에게도 적용 &rarr; 유지 보수성 향상
- 상속의 적용: `extends` 키워드 사용
![image](https://user-images.githubusercontent.com/108309396/229653367-0b76ea9a-82bd-4708-9d77-c203362c0caf.png)

## Object 클래스
- 모든 클래스의 조상 클래스
  - 별도의 extends 선언이 없는 클래스들은 `extends Object`가 생략됨
  - 따라서 모든 클래스에는 Object 클래스에 정의된 메서드가 있음
![image](https://user-images.githubusercontent.com/108309396/229654019-7948e6b7-0404-4ad5-b3d3-f9d4a3d08ce5.png)     
![image](https://user-images.githubusercontent.com/108309396/229657222-5c2f547d-add7-43d1-bb29-29ac417383e4.png)

### `toString` 메서드
- 객체를 문자열로 변경하는 메서드
```java
public String toString() {
  return getClass().getName() + "@" + Integer.toHexString(hashCode());
}
```
- 정작 궁금한 내용은 주소값이 아닌 내용
```java
@Override
public String toString() {
  return "Person: name: " + this.name;
}
```

### `equals` 메서드
- 두 객체가 같은지를 비교하는 메서드: 주소값을 비교함
```java
public boolean equals(Object obj) {
  return (this == obj);
}
```
- 객체의 주소 비교: `==` 활용
- 객체의 내용 비고: `equals` 재정의

### hashCode
- 객체의 해시 코드: 시스템에서 객체를 구별하기 위해 사용되는 정수 값
- HashSet, HashMap 등에서 객체의 동일성을 확인하기 위해 사용
- `equals` 메서드를 재정의할 때는 반드시 hashCode도 재정의할 것
  - 미리 작성된 String이나 Number 등에서 재정의된 hashCode 활용 권장

## 다양한 상속관계
- 상속의 관계는 is a 관계라고 함
  - Person is a Object, SpiderMan is a Person

### 단일 상속(Single Inheritance)
- 다중 상속의 경우 여러 클래스의 기능을 물려받을 수 있으나 관계가 매우 복잡해짐
  - 동일한 이름의 메서드가 두 부모에게 있다면 자식은 어떤 메서드를 쓸 것인가?
- 자바는 **단일 상속만** 지원
  - 대신 **interface**와 **포함 관계**로 단점 극복

### 포함 관계
- 상속 외에 클래스를 재활용 하는 방법
  - 2개 이상의 클래스에서 특성을 가져올 떄 하나는 상속, 나머지는 멤버 변수로 처리
- 포함 관계의 UML 표현: 실선
  - UML(Unified Modeling Language)
- Spider의 코드를 수정하면 SpiderMan에도 반영되므로 유지 보수성 확보
- 어떤 클래스를 상속 받고 어떤 클래스를 포함해야 하는가?
  - 상속: `is a` 관계가 성립하는가?
  - 포함: `has a` 관계가 성립하는가?

# 메서드 재정의
## 메서드 오버라이딩(Overriding)
- 조상 클래스에 정의된 메서드를 자식 클래스에서 적합하게 수정하는 것
- 오버라이딩의 조건
  - 메서드 이름이 같아야 한다.
  - 매개 변수의 개수, 타입, 순서가 같아야 한다.
  - 리턴 타입이 같아야 한다.
  - 접근 제한자는 부모보다 범위가 넓거나 같아야 한다.
  - 조상보다 더 큰 예외를 던질 수 없다.

## Annotation
- 사전적 의미: 주석
- 컴파일러, JVM, 프레임워크 등이 보는 주석
- 소스코드에 메타 데이터를 삽입하는 형태
  - 소스 코드에 붙여놓은 라벨
  - 코드에 대한 정보 추가 &rarr; 소스 코드의 구조 변경, 환경 설정 정보 추가 등의 작업 진행

### JDK 1.5의 기본 annotation의 예
- `@Deprecated`
  - 컴파일러에게 해당 메서드가 deprecated되었다고 알려줌
  - 명령 혹은 문장이 다른 것으로 대체되었거나 될 수 있으니 주의해서 사용하라는 뜻
  - 취소선이 생김
- `@Override`
  - 컴파일러에게 해당 메서드는 override한 메서드임을 알려줌
  - @Override가 선언된 경우 반드시 super class에 선언되어있는 메서드여야 함
- `@SupperessWarnings`
  - 컴파일러에게 사소한 warning의 경우 신경쓰지 말라고 알려줌

## `super` 키워드
- `this` 통해 멤버에 접근했듯이 `super`를 통해 조상 클래스 멤버 접근
  - `super.`을 이용해 조상의 메서드 호출로 조상의 코드 재사용
![image](https://user-images.githubusercontent.com/108309396/229661540-4f05e137-f1d3-434a-b140-e9452f192f3f.png)  
- 변수의 scope
  - 사용된 위치에서 점점 확장해가며 처음 만난 선언부에 연결됨
  - method 내부 &rarr; 해당 클래스 멤버 변수 &rarr; 조상 클래스 멤버 변수  
![image](https://user-images.githubusercontent.com/108309396/229661608-f8bd195f-be33-46c4-a0de-b5b12d82787f.png)
- `this()`가 해당 클래스의 다른 생성자를 호출하듯 `super()`는 조상 클래스의 생성자 호출
  - 조상 클래스에 선언된 멤버들은 조상 클래스의 생성자에서 초기화가 이뤄지므로 재활용
  - 자식 클래스에 선언된 멤버들만 자식 클래스 생성자에서 초기화
- `super()`는 자식 클래스 생성자의 맨 첫 줄에서만 호출 가능
  - 즉 생성자의 첫 줄에만 `this()` 또는 `super()`가 올 수 있다.
- 명시적으로 `this()` 또는 `super()`를 호출하지 않은 경우 컴파일러가 `super()` 삽입
  - 결론적으로 맨 상위의 Object까지 객체가 다 만들어지는 구조  
![image](https://user-images.githubusercontent.com/108309396/229662595-dec3070f-3f60-4757-a8bf-15cf01ace34a.png)
- 생성자 호출과 객체 생성의 단계
![image](https://user-images.githubusercontent.com/108309396/229663180-36f818ad-1bb5-47ec-818c-a823c6a67be1.png)  
- **static method는 상속X**, hiding

# package & import
## Package
- PC의 많은 파일 관리 &rarr; 폴더 이용
  - 유사한 목적의 파일을 기준으로 작성
  - 이름은 의미있는 이름으로, 계층적 접근
- 프로그램의 많은 클래스 &rarr; 패키지 이용
  - 패키지의 이름은 의미 있는 이름으로 만들고, `.`를 통해 계층적 접근
  - 물리적으로 패키지는 클래스 파일을 담고 있는 디렉터리
  - package name + class name으로 클래스 구분 &rarr; fully qulified name
- package의 선언
  - `package package_name;`
  - 주석, 공백을 제외한 첫 번째 문장에 하나의 패키지만 선언
  - 모든 클래스는 반드시 하나의 패키지에 속한다.
    - 생략 시 default package에 속하는데 default package는 가급적 사용하지 않는다.
- 일반적인 package naming 룰: 소속.프로젝트.용도  
![image](https://user-images.githubusercontent.com/108309396/229665361-0c3c3f97-67be-4983-91e6-4f807c5775c4.png)


## import
- 다른 패키지에 선언된 클래스를 사용하기 위한 키워드
  - 패키지와 클래스 선언 사이에 위치
  - 패키지와 달리 여러번 선언 가능
- 선언 방법
  - `import 패키지명.클래스명;`
  - `import 패키지명.*;`: 하위 패키지까지 import 하지는 않는다.
- import한 package의 클래스 이름이 동일하여 명확히 구분해야 할 때
  - 클래스 이름 앞에 전체 패키지 명을 입력
  - `java.util.list list = new java.util.ArrayList();`
- dafault import package
  - `java.lang.*`

### static import
- static member에 대한 import  
![image](https://user-images.githubusercontent.com/108309396/229665894-07b1ff26-b0fa-4001-91ff-ec187be6cfe8.png)
- 주로 단위테스트에 필요한 항목들이다.

## 일반적인 클래스 레이아웃
![image](https://user-images.githubusercontent.com/108309396/229665816-360c8218-fc92-472c-906d-9381433e48e4.png)


# 제한자(modifier)
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
![image](https://user-images.githubusercontent.com/108309396/229666497-766e5dc3-fbc6-4e01-a84f-c474330e4640.png)    
![image](https://user-images.githubusercontent.com/108309396/229666719-9ccf8f92-24bf-43f6-aff1-b0dd7dbd8dd5.png)