# AOP
## 1. AOP가 필요한 상황
- 모든 메서드의 호출 시간을 측정하고 싶다면? &rarr; 모든 메서드에 시간 측정 로직을 작성해야 함..
- 공통 관심 사항(cross-cutting concern) vs 핵심 관심 사항(core concern)
- 시간 측정 로직
```java
long start = System.currentTimeMillis();
try {
  validateDuplicateMember(member); //중복 회원 검증
  memberRepository.save(member);
  return member.getId();
} finally {
  long finish = System.currentTimeMillis();
  long timeMs = finish - start;
  System.out.println("join " + timeMs + "ms");
}
```

### 문제점
- 회원가입, 회원 조회에 시간을 측정하는 기능은 핵심 관심 사항이 아님 &rarr; 둘이 섞이면 유지보수 어려움
- 시간을 측정하는 로직은 **공통 관심 사항**
- 시간을 측정하는 로직을 변경할 때 모든 로직을 찾아가면서 변경해야 한다.

## 2. AOP 적용
- AOP: Aspect Oriented Programming
- 공통 관심 사항 vs 핵심 관심 사항 분리  
<img width="804" alt="image" src="https://user-images.githubusercontent.com/108309396/234590122-664510df-6fb5-45f7-a20d-e7fc29d69c18.png">

### 시간 측정 AOP 등록
```java
package hello.hellospring.aop;

import org.aspectj.lang.ProceedingJoinPoint;
import org.aspectj.lang.annotation.Around;
import org.aspectj.lang.annotation.Aspect;
import org.springframework.stereotype.Component;

@Component
@Aspect
public class TimeTraceAop {
    @Around("execution(* hello.hellospring..*(..))")
    public Object execute(ProceedingJoinPoint joinPoint) throws Throwable {

        long start = System.currentTimeMillis();

        System.out.println("START: " + joinPoint.toString());

        try {
            return joinPoint.proceed();
        } finally {
            long finish = System.currentTimeMillis();
            long timeMs = finish - start;

            System.out.println("END: " + joinPoint.toString()+ " " + timeMs + "ms"); 
        }
    }
}
```
- 회원가입, 회원 조회 등 핵심 관심사항과 시간을 측정하는 공통 관심 사항을 분리
- 핵심 관심 사항을 깔끔하게 유지할 수 있다.
- 변경이 필요하면 이 로직만 변경하면 된다.
- 원하는 적용 대상을 선택할 수 있다.

### AOP 적용 전 의존관계 및 전체그림
<img width="693" alt="image" src="https://user-images.githubusercontent.com/108309396/234591809-b1a0ab5b-97bb-4b74-9619-fcb92d381975.png">  
<img width="693" alt="image" src="https://user-images.githubusercontent.com/108309396/234592107-e847a457-df21-4d99-a6ce-6c7b039a39bf.png">

### AOP 적용 후 의존관계 및 전체그림
<img width="694" alt="image" src="https://user-images.githubusercontent.com/108309396/234591968-ed75b405-228f-420b-a7bf-1aa9cdbdc2f9.png">  
<img width="693" alt="image" src="https://user-images.githubusercontent.com/108309396/234592212-6a11e8b9-4cda-4b79-aa8e-d9a855bdc193.png">