# 프로젝트 환경설정 
## 1-1 프로젝트 생성
- `start.spring.io`: spring initializr &rarr; 초기 설정을 다 만들어줌
- Project: `Gradle-Groovy`, Language: `Java`
- Spring Boot &rarr; SNAPSHOT: 만드는 중 / M1, M2: 정식 릴리즈 전
- Project Metadata
  - Group: 보통 회사의 도메인명을 적음 `hello`
  - Artifact: 빌드되어 나올 때의 결과물 `hello-spring`, 프로젝트명
- Dependencies
  - 어떤 라이브러리를 사용할 것인지
  - Spring Web: `WEB` 
  - Thymeleaf: `Template Engines`, HTML을 만들어주는 템플릿 엔진
- GENERATE(`cmd + enter`)
- IntelliJ &rarr; `Open or Import` &rarr; `build.gradle` 파일을 `Open as Project`

## 프로젝트의 구조
  - `.idea`: 인텔리제이가 사용하는 설정 파일
- `gradle`: gradle이 사용하는 폴더
- `src`
  - `main`: java(패키지와 소스파일), resources(xml, properties, html 등 자바 파일을 제외한 설정파일)
  - `test`: testcode와 관련된 소스 &rarr; 요즘 개발 트렌드에서는 testcode가 굉장히 중요
- `build.gradle`
  - `plugins`: spring initializr에서 입력한 값
  - `group`, `version`: spring initializr에서 입력한 값
  - `sourceCompatibility`: Java버전이 명시
  - `repositories`: 라이브러리들을 다운받는 곳(여기서는 `mavenCentral()`)
  - `dependencies`: spring initializr에서 선택한 라이브러리

### 동작 확인
- 기본 메인 클래스 실행
- 스프링 부트 메인 실행 후 에러페이지로 간단하게 동작 확인(`http://localhost:8080`)

### IntelliJ Gradle 대신에 자바 직접 실행
- 최근 IntelliJ 버전은 Gradle을 통해서 실행 하는 것이 기본 설정이다. 이렇게 하면 실행속도가 느리다.
- 다음과 같이 변경하면 자바로 바로 실행해서 실행속도가 더 빠르다.
- Preferences &rarr; Build, Execution, Deployment &rarr; Build Tools &rarr; Gradle 
  - Build and run using: Gradle &rarr; IntelliJ IDEA
  - Run tests using: Gradle &rarr; IntelliJ IDEA

# 1-2 라이브러리 살펴보기
- Gradle은 의존관계가 있는 라이브러리를 함께 다운로드함
1. **스프링 부트 라이브러리**
   - spring-boot-starter-web 
     - spring-boot-starter-tomcat: 톰캣 (웹서버) 
     - spring-webmvc: 스프링 웹 MVC
   - spring-boot-starter-thymeleaf: 타임리프 템플릿 엔진(View) 
   - spring-boot-starter(공통): 스프링 부트 + 스프링 코어 + 로깅
     - spring-boot 
       - spring-core
   - spring-boot-starter-logging 
     - logback, slf4j
     - 현업에서는 System.in.print로 출력하면 안 된다.
     - 로그로 남겨야 심각한 에러들은 따로 모아볼 수 있고, 로그 파일들이 관리가 됨
2. **테스트 라이브러리**
   - spring-boot-starter-test
   - junit5: 테스트 프레임워크(핵심)
   - mockito: 목 라이브러리
   - assertj: 테스트 코드를 좀 더 편하게 작성하게 도와주는 라이브러리 
   - spring-test: 스프링 통합 테스트 지원


# 1-3 View 환경설정
### Welcome Page 만들기
- 스프링 부트가 제공하는 Welcome Page 기능
- 도메인으로 들어왔을 때 첫 화면
- `src/resources/static/index.html`을 올려두면 Welcome page 기능을 제공
- (https://docs.spring.io/spring-boot/docs/2.3.1.RELEASE/reference/html/spring-boot-features.html#boot-features-spring-mvc-welcome-page)


### Thymeleaf 템플릿 엔진
- Thymeleaf 공식 사이트: https://www.thymeleaf.org/
- 스프링 공식 튜토리얼: https://spring.io/guides/gs/serving-web-content/
- 스프링부트 메뉴얼: https://docs.spring.io/spring-boot/docs/2.3.1.RELEASE/reference/html/spring-boot-features.html#boot-features-spring-mvc-template-engines


### Controller
- 웹에서 첫 번째 진입점이 controller
- `main/java/hello.hellospring.controller/HelloController.class`
```java
@Controller
  public class HelloController {

      @GetMapping("hello")
      public String hello(Model model) {
          model.addAttribute("data", "hello!!");
          return "hello";
      }
}
```

### Templates
- `main/resources/templates/hello.html`
```html
<!DOCTYPE HTML>
  <!-- thymeleaf 엔진 사용 가능하게 해줌 -->
  <html xmlns:th="http://www.thymeleaf.org">
  <head>
      <title>Hello</title>
      <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
  </head>
<body>
<!-- {data}는 model의 속성으로 넣었던 키 값으로 hello!!를 받아온다. -->
<p th:text="'안녕하세요. ' + ${data}" >안녕하세요. 손님</p>
  </body>
  </html>
```

### Thymeleaf 템플릿엔진 동작 확인 
- 실행: http://localhost:8080/hello

## 동작 환경 그림
<img width="785" alt="image" src="https://user-images.githubusercontent.com/108309396/230116820-158a35e2-78ad-42ef-ac93-4b6d3d4f3d1d.png">  

- 컨트롤러에서 리턴 값으로 문자를 반환하면 뷰 리졸버(`viewResolver`)가 화면을 찾아서 처리
- 스프링 부트 템플릿엔진 기본 viewName 매핑
- `resources:templates/` + `{ViewName}` + `.html`

### [참고] 서버 재시작 없이 View 파일 변경 방법
- spring-boot-devtools 라이브러리를 추가하면, html 파일을 컴파일만 해주면 서버 재시작 없이 View 파일 변경이 가능하다.
- 인텔리J 컴파일 방법: 메뉴 build &rarr; Recompile


# 1-4 빌드하고 실행하기
- 터미널로 이동
1. `./gradlew build`
2. `cd build/libs`
3. `java -jar hello-spring-0.0.1-SNAPSHOT.jar`
4. 실행확인
5. ./gradlew clean &rarr; 빌드 파일 삭제됨