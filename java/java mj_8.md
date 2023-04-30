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
<img width="429" alt="image" src="https://user-images.githubusercontent.com/108309396/235342488-842aa8ef-b808-4270-8967-3027bcbe0d4f.png">

## Collection - List 계열의 특징
- 순서 O
- 중복 O
- 주요 매서드
  - <img width="662" alt="image" src="https://user-images.githubusercontent.com/108309396/235308175-ce85e82d-7f3f-46ca-8077-85f3af955614.png">

## ArrayList
- 배열의 장점
  - 간단하고 사용이 쉬움
  - 접근 속도가 빠름
- 배열의 단점
  - 크기를 바꿀 수 없기 때문에 추가 데이터를 위해 새로운 배열을 만들고 복사해야 함
  - 비 순차적 데이터의 추가, 삭제에 많은 시간이 걸림
- 배열을 사용하는 `ArrayList`도 배열의 장단점을 그대로 가짐

## LinkedList
- 각 요소를 Node로 정의하고 Node는 다음 요소의 참조값과 데이터로 구성
  - 연속적으로 구성될 필요X
  - <img width="694" alt="image" src="https://user-images.githubusercontent.com/108309396/235308674-53bb1931-8e2e-40d2-ab26-b96667f2b424.png">
- 데이터 삭제 및 추가
  - <img width="670" alt="image" src="https://user-images.githubusercontent.com/108309396/235308696-fcdc8f46-5bbe-41a3-b04d-6dcf5ee7ad69.png">

## LinkedList와 ArrayList의 용도
- <img width="709" alt="image" src="https://user-images.githubusercontent.com/108309396/235308719-c900b57e-eea2-42b9-95b2-1c197f919887.png">
- 결론
  - 정적인 데이터 활용, 단순한 데이터 조회용: `ArrayList`
  - 동적인 데이터 추가, 삭제가 많은 작업: `LinkedList`

## 자료 삭제 시 주의 사항
- index를 이용한 for문에서 요소가 삭제되면 size가 줄어들기 때문에 주의한다
- 해결) 거꾸로 접근
- `forEach`구문은 collection 크기가 불변해야 함


# Collection Framework - Set 계열
## Set interface의 특징
- 순서 X
- 중복 허용 X
- <img width="521" alt="image" src="https://user-images.githubusercontent.com/108309396/235341762-9326f9bb-6c9d-4085-a280-ca2d0cffce9c.png">

## Set interface의 주요 메서드
<img width="404" alt="image" src="https://user-images.githubusercontent.com/108309396/235342535-8074c9ef-e07e-4e86-8a73-7253d6a3ffe9.png">

## 동일한 데이터의 기준
- `equals()`가 `true`를 리턴하고 `hashCode()` 값이 같을 것  
<img width="329" alt="image" src="https://user-images.githubusercontent.com/108309396/235342577-a5bd08c3-63c3-47ab-89da-a2340c2f84be.png">


# Collection Framework - Map 계열
## Map interface의 특징
- key와 value를 하나의 entry로 묶어서 데이터 관리
  - Key: Object 형태로 데이터 중복 허용 X
  - Value: Object 형태로 데이터 중복 허용 O
  - <img width="517" alt="image" src="https://user-images.githubusercontent.com/108309396/235342019-294d5143-16ce-404e-9bbb-d538a8d1a01e.png">
- 관련 클래스 관계도  
<img width="517" alt="image" src="https://user-images.githubusercontent.com/108309396/235341883-e6eb4465-bcc7-430d-9fe0-ef0fde9f7ccb.png">

## Map interface의 주요 메서드
<img width="776" alt="image" src="https://user-images.githubusercontent.com/108309396/235342127-4f8cf795-a327-4f94-ba08-ff86bfc48f11.png">
<img width="516" alt="image" src="https://user-images.githubusercontent.com/108309396/235342608-447c86de-28e3-42ed-be10-bf3fec411833.png">

# 정렬
- 요소를 특정 기준에 대한 내림차순 또는 오름차순으로 배치
- **순서를 가지는 Collection들만 정렬 가능**
  - List 계열
  - Set 계열: SortedSet의 자식 객체
  - Map 계열: SortedMap의 자식 객체(key 기준)
- Collections의 `sort()`를 이용한 정렬
  - `sort(List<T> list)`: 객체가 Comparable을 구현하고 있는 경우 내장 알고리즘을 통해 정렬
  - <img width="490" alt="image" src="https://user-images.githubusercontent.com/108309396/235342712-9cfb2875-e3ef-49a6-9f89-55c5f155ad8e.png">