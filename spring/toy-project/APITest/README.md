# [Toy Project] API Response Test using Spring Boot
- OS: MacOS M1(ARM 64-bit)
- Language: Java(JDK 11)
- Framework: Spring Boot
- IDE: IntelliJ Ultimate

## API Test Application
1. Controller 추가
```java
@Controller
public class ApiController {

    // GET request -> JSON 직접 만드는 방법
    @GetMapping("/api/test")
    @ResponseBody
    public String getApiTest() {

        return "{\"result\":\"ok\"}";
    }

    @PostMapping("/api/test2")
    @ResponseBody
    public String getApiTest2() {

        return "{\"result2\":\"ok\"}";
    }
    
    // 정석
    @GetMapping("/data")
    @ResponseBody
    public Map<String, Object> getData() {
        Map<String, Object> data = new HashMap<>();
        data.put("message", "Hello, World!");
        data.put("timestamp", new Date());
        return data;
    }
}
```
2. GET, POST 요청 및 응답 확인

## Learning Point
1. `@Controller`
2. `@Get/PostMapping("URL")`
3. `@ResponseStatus(value = HttpStatus.OK)`로 Status 지정
4. `@ResponseBody`
5. `Map<String, Object> data = new HashMap<>();`을 통해 JSON 구현