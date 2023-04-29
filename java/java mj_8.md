# Collection Framework - List 계열
## 배열
- homogeneous collection: *동일한 데이터 타입*만 관리 가능
- polymorphism: Object를 이용하면 모든 객체 참조 가능 &rarr; **Collection Framework**
  - 담을 때는 편리하지만 빼낼 때는 Object로만 가져올 수 있음
  - 런타임에 실제 객체의 타입 확인 후 사용해야 하는 번거로움
- Generic을 이용한 타입 한정
  - 컴파일 타임에 저장하려는 타입 제한 &rarr; 형변환의 번거로움 제거

## Collection Framework
- `java.util` 패키지
  - 다수의 데이터를 쉽게 처리하는 방법 제공 &rarr; DB처럼 CRUD 기능 중요
  - collection framework 핵심 interface
  - <img width="842" alt="image" src="https://user-images.githubusercontent.com/108309396/235307807-be7c4d6a-3d86-4d2c-8419-196b384f363d.png">

## Collection interface의 주요 메서드(CRUD)
<img width="755" alt="image" src="https://user-images.githubusercontent.com/108309396/235307939-42facada-de6b-4c48-92e1-ef8524373af6.png">

## Collection - List 계열의 특징
- 순서가 있는 데이터의 집합
- 순서가 있으므로 데이터의 중복을 허락
- 주요 매서드
  - <img width="662" alt="image" src="https://user-images.githubusercontent.com/108309396/235308175-ce85e82d-7f3f-46ca-8077-85f3af955614.png">

