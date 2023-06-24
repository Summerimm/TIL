# 스프링 웹 개발 기초
## 2-1 정적 컨텐츠
- 파일을 그대로 웹 브라우저에 전달해주는 것
- `resources/static/hello-static.html`  
<img width="786" alt="image" src="https://user-images.githubusercontent.com/108309396/230120882-20abc241-ec52-4dc6-8e89-3d0ea47326fe.png">


## 2-2 MVC와 템플릿 엔진
- 서버에서 HTML파일을 렌더링해서 웹 브라우저에 전달해주는 방식
- MVC: Model, View, Controller
- 과거에는 Controller와 View가 분리되어 있지 않았음(model-one 방식)
- View는 화면을 그리는 것에 집중
- Controller 비즈니스 로직, 서버 뒷단과 관련된, 내부적인 것을 처리하는 데 집중
- 즉, 코드 유지보수에 용이

### Controller
```java
@Controller
  public class HelloController {
      @GetMapping("hello-mvc")
      public String helloMvc(@RequestParam("name") String name, Model model) {
          model.addAttribute("name", name);
          return "hello-template";
      }
}
```

### View
- `resources/templates/hello-template.html`
```html
<html xmlns:th="http://www.thymeleaf.org">
<body>
<p th:text="'hello ' + ${name}">hello! empty</p>
</body>
</html>
```

### [참고] Thymeleaf 장점
- HTML을 기본적으로 그대로 쓰고 서버 없이 열어도 확인이 가능함(HTML Markup으로 활용가능)
- 템플릿 엔진으로 동작하면 안의 내용으로 치환됨

### 실행
http://localhost:8080/hello-mvc?name=spring

### 동작
<img width="784" alt="image" src="https://user-images.githubusercontent.com/108309396/230124012-17a2e8e2-c301-43eb-8ab5-95ba8b9fdaf3.png">



## 2-3 API
- JSON 데이터 구조 포맷으로 클라이언트에게 전달하는 방식
- Vue.js, React.. &rarr; API 방식으로 데이터만 보내면 화면은 클라이언트가 그림
- 서버끼리 통신할 때는 HTML이 아닌 API 방식으로 통신
- `@ResponseBody`: HTTP에서 Response Body부에 이 데이터를 직접 넣어주겠다는 의미
- View같은 것 없이 문자가 그대로 내려감

### @ResponseBody 문자 반환
```java
@Controller
public class HelloController {
    @GetMapping("hello-string")
        @ResponseBody
        public String helloString(@RequestParam("name") String name) {
            return "hello " + name;
        }
}
```  
![image](https://user-images.githubusercontent.com/108309396/230242470-cc1088c4-59b5-4b7f-9c2c-d940d1a1f5a3.png)  
- 페이지 소스보기를 눌러도 HTML 형식이 아닌 데이터를 그대로 보내주는 API 형식이 활용된 것을 알 수 있다.
- `@ResponseBody`를 사용하면 `viewResolver`를 사용하지 않음
- 대신에 HTTP의 BODY에 문자 내용을 직접 반환(HTML BODY TAG 아님)'
- 실행: http://localhost:8080/hello-api?name=spring


### @ResponseBody 객체 반환
```java
@GetMapping("hello-api")
    @ResponseBody
    public Hello helloApi(@RequestParam("name") String name) {
        Hello hello = new Hello();
        hello.setName(name);
        return hello;
    }

    static class Hello {
        private String name;

        public String getName() {
            return name;
        }

        public void setName(String name) {
            this.name = name;
        }
    }
```
![image](https://user-images.githubusercontent.com/108309396/230243352-c1a3cd2a-dcf8-43ac-bab4-f499c3760330.png)  
- [참고] Mac `cmd + shift + enter`, Windows `ctrl + shift + enter`로 자동완성 기능
- [참고] getter, setter MacOS `cmd + N`, Windows `alt + insert` &rarr; 자바 빈 표준 규약, property 접근 방식
- `@ResponseBody`를 사용하고, 객체를 반환하면 객체가 JSON으로 변환됨
- JSON: key-value로 이루어진 구조
- 실행: http://localhost:8080/hello-api?name=spring

### @ResponseBody 사용 원리  
![image](https://user-images.githubusercontent.com/108309396/230243879-d0148a34-821c-4c33-aca2-252d48125138.png)
- @ResponseBody 를 사용
  - HTTP의 BODY에 문자 내용을 직접 반환
  - `viewResolver` 대신에 `HttpMessageConverter` 가 동작
  - 기본 문자처리: `StringHttpMessageConverter`
  - 기본 객체처리: `MappingJackson2HttpMessageConverter`
  - byte 처리 등등 기타 여러 `HttpMessageConverter`가 기본으로 등록되어 있음
- [참고]: 클라이언트의 HTTP Accept 해더와 서버의 컨트롤러 반환 타입 정보 둘을 조합해서 `HttpMessageConverter` 가 선택됨