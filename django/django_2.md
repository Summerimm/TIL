# Design Pattern
- 각기 다른 기능을 가진 다양한 응용 소프트웨어를 개발할 때 공통적인 설계 문제가 존재
- 이를 처리하는 해결책 사이에도 공통점이 있다는 것을 발견 &rarr; 이러한 유사점을 패턴이라고 함
- 클라이언트-서버 구조도 소프트웨어 디자인 패턴 중 하나
- 자주 사용되는 소프트웨어의 구조를 일반적인 구조화를 해둔 것 &rarr; 디자인 패턴
- 커뮤니케이션의 효율성 &uarr;

## Django에서의 디자인 패턴
- `MTV Pattern` &rarr; MVC 디자인 패턴을 기반으로 조금 변형된 패턴이다.
- MVC 디자인 패턴
  - Model-View-Controller의 준말
  - 데이터 및 논리 제어를 구현하는 데 널리 사용됨
  - Model: 데이터와 관련된 로직 관리
  - View: 레이아웃과 화면을 처리
  - Controller: 명령을 model과 view부분으로 연결
  - 각 부분을 독립적으로 개발 가능 &rarr; 개발 효율성 및 유지보수 쉬워짐, 다수의 멤버로 개발하기 용이
- MTV 디자인 패턴
  - Model: 데이터 관련 로직 관리(응용 프로그램의 데이터 구조 정의 및 데이터베이스의 기록 관리)
  - Template: 레이아웃과 화면 처리 &rarr; **MVC에서의 View에 해당**
  - View: Model & Template 중간 처리 및 응답 반환(클라이언트의 요청에 대해 처리를 분기하는 역할) &rarr; **MVC에서의 Controller에 해당**  
![image](https://user-images.githubusercontent.com/108309396/225243875-ba86e172-bb44-4530-b4b3-6c932d585eea.png)
