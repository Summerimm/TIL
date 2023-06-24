# 스프링 빈과 의존관계
### 스프링 빈을 등록하는 2가지 방법
1. 컴포넌트 스캔과 자동 의존관계 설정
2. 자바 코드로 직접 스프링 빈 등록하기


## 4-1 컴포넌트 스캔과 자동 의존관계 설정 
- 회원 컨트롤러가 회원서비스와 회원 리포지토리를 사용할 수 있게 의존관계를 준비

###  회원 컨트롤러에 의존관계 추가
```java
package hello.hellospring.controller;

import hello.hellospring.service.MemberService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;

@Controller
public class MemberController {

    private final MemberService memberService;

    @Autowired
    public MemberController(MemberService memberService) {
        this.memberService = memberService;
    }
}
```
- 생성자에 `@Autowired`가 있으면 스프링이 연관된 객체를 스프링 컨테이너에서 찾아서 넣어준다.
- 이렇게 객체 의존관계를 외부에서 넣어주는 것을 DI(Dependency Injection), 의존성 주입이라 함

## 컴포넌트 스캔 원리
- `@Component` annotation이 있으면 스프링 빈으로 자동 등록됨
- `@Component` 컨트롤러가 스프링 빈으로 자동 등록된 이유도 컴포넌트 스캔 때문
- `@Component`을 포함하는 다음 annotation도 스프링 빈으로 자동 등록됨
  - `@Controller`, `@Service`, `@Repository`

### 회원 서비스 스프링 빈 등록
```java
@Service
public class MemberService {

    private final MemberRepository memberRepository;

    @Autowired
    public MemberService(MemberRepository memberRepository) {
        this.memberRepository = memberRepository;
    }
}
```
- 생성자에 `@Autowired`를 사용하면 객체 생성 시점에 스프링 컨테이너에서 해당 스프링 빈을 찾아서 주입합
- 생성자가 1개만 있으면 `@Autowired`는 생략할 수 있음

### 회원 리포지토리 스프링 빈 등록
```java
@Repository
public class MemoryMemberRepository implements MemberRepository{}
```

### 스프링 빈 등록 이미지
![image](https://user-images.githubusercontent.com/108309396/231661011-06831ca0-6613-438b-92f4-1dd7229b0b37.png)  
- memberService와 memberRepository가 스프링 컨테이너에 스프링 빈으로 등록되었다.
- [참고] 스프링은 스프링 컨테이너에 스프링 빈을 등록할 때, 기본으로 **싱글톤**으로 등록함(유일하게 하나만 등록해서 공유)
- 따라서 같은 스프링 빈이면 모두 같은 인스턴스.


## 4-2 자바 코드로 직접 스프링 빈 등록하기
- 회원 서비스와 회원 리포지토리의 @Service, @Repository, @Autowired 애노테이션을 제거하고 진행
```java
package hello.hellospring;
import hello.hellospring.repository.MemberRepository;
import hello.hellospring.repository.MemoryMemberRepository;
import hello.hellospring.service.MemberService;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class SpringConfig {
  @Bean
  public MemberService memberService() {
    return new MemberService(memberRepository());
  }

  @Bean
  public MemberRepository memberRepository() {
    return new MemoryMemberRepository();
  }
}
```

> 참고: DI에는 필드 주입, setter 주입, 생성자 주입 이렇게 3가지 방법이 있다. 의존관계가 실행중에 동적으로 변하는 경우는 거의 없으므로 생성자 주입을 권장한다.
> - 필드 주입은 중간에 수정이 힘들다.
> - setter 주입은 셋팅 후 수정할 상황이 만들어지지 않아야 하는데 수정할 수 있게 끔 public하게 노출된다

> 참고: 실무에서는 주로 정형화된 컨트롤러, 서비스, 리포지토리 같은 코드는 컴포넌트 스캔을 사용한다.
정형화 되지 않거나, 상황에 따라 구현 클래스를 변경해야 하면 설정을 통해 스프링 빈으로 등록한다.

> 주의: `@Autowired` 를 통한 DI는 helloController , memberService 등과 같이 스프링이 관리하는 객체에서만 동작한다. 스프링 빈으로 등록하지 않고 내가 직접 생성한 객체에서는 동작하지 않는다.