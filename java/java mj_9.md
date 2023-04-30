### < File I/O >
# 1. 노드 스트림
### I/O와 Stream
- I/O? 데이터의 입력(input)과 출력(output)
- 데이터는 한 쪽에서 주고 한 쪽에서 받는 구조
  - 입력과 출력의 끝단: 노드(Node)
  - 두 노드를 연결하고 데이터를 전송할 수 있는 개념: 스트림(stream)
  - 스트림은 **단방향으로만** 통신이 가능, 하나의 스트림으로 입력과 출력을 같이 처리 불가
  - <img width="575" alt="image" src="https://user-images.githubusercontent.com/108309396/235343154-ba2fc3b1-3183-42e9-bcfd-238583e4884d.png">

## Node Stream의 종류와 naming
- Node Stream: node에 연결되는 스트림  
<img width="742" alt="image" src="https://user-images.githubusercontent.com/108309396/235343242-6ea0555e-8049-4bbb-829d-f31527ff7bd3.png">

## InputStream의 주요 메서드
<img width="749" alt="image" src="https://user-images.githubusercontent.com/108309396/235343278-22fca1a6-090c-402f-9750-07daeedc114c.png">  
<img width="750" alt="image" src="https://user-images.githubusercontent.com/108309396/235353634-8b4d084d-3104-4e71-b954-c74ce069ffd4.png">

## Reader의 주요 메서드
<img width="965" alt="image" src="https://user-images.githubusercontent.com/108309396/235353795-ca90aa8b-2e9c-489c-854a-443e7aecf94b.png">  
<img width="939" alt="image" src="https://user-images.githubusercontent.com/108309396/235353946-5c09d515-bbd7-4a33-b7f0-4f6a3f7efcc6.png">

## OutputStream의 주요 메서드
<img width="957" alt="image" src="https://user-images.githubusercontent.com/108309396/235353969-5f5e8fba-37a1-42c7-a55c-1510c27bc0c3.png">  
<img width="957" alt="image" src="https://user-images.githubusercontent.com/108309396/235354003-87bb33fa-cc3c-4e4f-8e90-634947fe3389.png">

## File
- 가장 기본적인 입출력 장치 중 하나로 파일과 디렉터리를 다루는 클래스
<img width="948" alt="image" src="https://user-images.githubusercontent.com/108309396/235354069-a6599baf-542c-4ee7-a260-a09d78105fd6.png">  
<img width="953" alt="image" src="https://user-images.githubusercontent.com/108309396/235354091-4c600ed4-1abf-46ab-984b-ae63b6d7ec13.png">

## FileInputStream, FileOutputStream
<img width="946" alt="image" src="https://user-images.githubusercontent.com/108309396/235354492-f7033162-0daf-4689-b96f-7e33fd9c49c8.png">

- String name 대신 File 객체 사용 가능  
<img width="938" alt="image" src="https://user-images.githubusercontent.com/108309396/235354706-f4c596cc-256f-42f6-abf6-eaa71f111272.png">

# 2. 보조 스트림
- 보조스트림: Filter Stream, Processing Stream  
- 다른 스트림에 부가적인 기능을 제공하는 스트림  
<img width="671" alt="image" src="https://user-images.githubusercontent.com/108309396/235356031-15d2ec63-588b-4c47-b944-780faa47e960.png">

## 스트림 체이닝(Stream Chaining)  
- 필요에 따라 여러 보조 스트림을 연결해서 사용 가능
<img width="510" alt="image" src="https://user-images.githubusercontent.com/108309396/235356210-4bc590d3-ece9-4f6d-b645-79a49df42072.png"> 

## 보조스트림의 종류  
<img width="854" alt="image" src="https://user-images.githubusercontent.com/108309396/235356305-a4133322-5cad-4cbe-91be-3679c84f9197.png">

- 생성: 이전 스트림을 생성자의 파라미터에 연결  
<img width="878" alt="image" src="https://user-images.githubusercontent.com/108309396/235356354-c2935642-c78e-4b52-a3ee-143b4d1c15b1.png">

- 종료: 보조스트림의 `close()`를 호출하면 노드스트림의 `close()`까지 호출됨

## 사용할 스트림의 결정 과정
- 노드가 무엇인가 &rarr; 타입은 문자열인가?바이트인가? &rarr; 방향이 무엇인가? &rarr; 추가 기능이 필요한가?

## 보조 스트림 활용 1
### `InputStreamReader & OutputStreamWriter`
- byte 기반 스트림을 char 기반으로 변경해주는 스트림
  - 문자열을 관리하기 위해서는 char 단위가 유리
  - 키보드에서 입력(byte stream) 받은 데이터를 처리할 경우에 쓰임
- 변환 시 encoding 지정 가능
<img width="938" alt="image" src="https://user-images.githubusercontent.com/108309396/235356555-b11ad609-1551-49a8-80b1-8c4e460adcc4.png">

### `Buffered` 계열
- 버퍼의 역할  
- <img width="552" alt="image" src="https://user-images.githubusercontent.com/108309396/235356774-5e1ab428-2538-4bb0-aad7-80147be4d427.png">
- 스트림의 입/출력 효율을 높이기 위해 버퍼를 사용하는 스트림
- <img width="933" alt="image" src="https://user-images.githubusercontent.com/108309396/235356813-cffe4ade-9156-4658-a648-7f46fe702193.png">

### `BufferedReader & BufferedWriter`
- <img width="698" alt="image" src="https://user-images.githubusercontent.com/108309396/235356978-9692ec36-086f-4ee2-a8b2-9d1d03a1fa33.png">
- BufferedReader: `readLine()` &rarr; 줄 단위로 데이터를 읽어들임 

## 보조 스트림 활용 2
### 객체 직렬화(serialization)
- 객체를 파일 등에 저장하거나 네트워크로 전송하기 위해 연속적인 데이터로 변환하는 것
- 반대는 역직렬화(deserialization)
- <img width="453" alt="image" src="https://user-images.githubusercontent.com/108309396/235357215-b7402f87-8c26-4fee-b5bd-acb07a8f7735.png">
- 직렬화 되기 위한 조건
  - `Serializable` 인터페이스를 구현할 것
  - 클래스의 모든 멤버가 `Serializable` 인터페이스를 구현해야 함
  - 직렬화에서 제외하려는 멤버는 `transient` 선언
  - <img width="344" alt="image" src="https://user-images.githubusercontent.com/108309396/235357258-ba7ebc9f-972a-4e1f-baec-36a2185cb01e.png">
- serialVersionUID
  - 클래스의 변경 여부를 파악하기 위한 유일 키
  - <img width="507" alt="image" src="https://user-images.githubusercontent.com/108309396/235357282-2dac976f-e2ae-40c0-aa33-c706a5ef2165.png">
  - 직렬화 할 때의 UID와 역직렬화 할 때의 UID가 다를 경우 예외 발생
  - 직렬화되는 객체에 UID가 설정되지 않았을 경우 컴파일러가 자동 생성
    - 멤버 변경으로 인한 컴파일 때마다 변경 &rarr; InvalidClassException 발생
  - 직렬화되는 객체에 대해서 serialVersionUID 설정 권장

### `ObjectInputStream & ObjectOutputStream`
- <img width="1126" alt="image" src="https://user-images.githubusercontent.com/108309396/235357407-f31289f2-1715-4dfc-9d96-a96810e8efee.png">

### `Scanner와 BufferedReader`
- char 형태의 데이터를 읽기 위한 클래스들
- Scanner: 자동 형 변환을 지원하는 등 사용이 간편하지만 속도가 느림
- BufferedReader: 직접 스트림을 구성해야 하는 등 번거롭지만 속도가 빠름