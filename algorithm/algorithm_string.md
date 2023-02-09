# String(문자열)

### Big-Endian / Little-Endian
- 대부분의 컴퓨터는 Little-Endian
- 네트워크 등에서는 Big-Endian을 사용하기도 함
- 메모리의 1000번지에 30을 저장, 1001번지에 00을 저장 &rarr; Big-Endian
- - 메모리의 1000번지에 00을 저장, 1001번지에 30을 저장 &rarr; Little-Endian


### 유니코드 인코딩(UTF: Unicode Transformation Format)
- UTF-8 (in web)
  - MIN: 8bit, MAX: 32bit(1 Byte * 4)
- UTF-16 (in windows, java)
  - MIN: 16bit, MAX: 32bit(2 Byte * 2)
- UTF-32 (in unix)
  - MIN: 32bit, MAX: 32bit(4 Byte * 1)

### CRLF
- `0D`: CR(Carriage Return)
- `0A`: LF(NL Line Feed, new line) 

### 문자열의 분류
- fixed length
- variable length
  - length controlled: java
  - delimited: c
![java](https://user-images.githubusercontent.com/108309396/217408213-fefff510-fcf4-4035-b334-5ff04fd165c0.png)  
![c](https://user-images.githubusercontent.com/108309396/217408207-6b2564be-e9b8-407f-acd8-98599ab39c87.png)  

### Python에서의 문자열 처리
- char 타입 없음
- 텍스트 데이터의 취급방법이 통일되어 있음
- 문자열 기호
  - `'`, `"`, `'''`, `"""`
  - `+` Concatenation: 문자열 + 문자열 -  이어 붙여주는 역할
  - `*` Repeat: 문자열 * 수 - 수만큼 문자열이 반복

### 언어 별 String 처리
- C는 아스키 코드로 저장
- Java는 유니코드(UTF-16, 2byte)로 저장
- Python은 유니코드(UTF8)로 저장

### 문자열 비교
- C: strcmp() 함수
- Java: equals() 메소드
  - 문자열 비교에서 == 연산은 메모리 참조가 같은지를 묻는 것
- Python: ==, is 연산자
  - == 연산자는 내부적으로 특수 메서드 \_\_eq\_\_()를 호출

### 문자열 숫자를 정수로 변환
- C: atoi() 함수, 역함수로는 itoa()가 있다
- Java: 숫자 클래스의 parse 메서드
  - `Integer.parseInt(String)`
  - 역함수로는 toString()
- Python: 숫자와 문자변환 함수
  - `int('123'), str(123)`