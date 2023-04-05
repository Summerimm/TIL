# 스프링 웹 개발 기초
## 2-1 정적 컨텐츠
- 파일을 그대로 웹 브라우저에 전달해주는 것
- `resources/static/hello-static.html`  
<img width="786" alt="image" src="https://user-images.githubusercontent.com/108309396/230120882-20abc241-ec52-4dc6-8e89-3d0ea47326fe.png">


## 2-2 MVC와 템플릿 엔진
- 서버에서 변형을 해서 웹 브라우저에 전달해주는 방식
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