# [Toy Project] Spring Boot를 이용한 게시판 CRUD
- OS: MacOS M1(ARM 64-bit)
- 개발언어: Java(JDK 11)
- 프레임워크: Spring Boot
- IDE: IntelliJ Ultimate
- DB: MariaDB
- Template Engine: Thymeleaf  
\+ JPA(Java Persistence API)

# 순서
1. 개발 환경 세팅
   - IntelliJ Ultimate
   - MariaDB
   - MySQL Workbench
2. 프로젝트 생성
   - Spring Boot 프로젝트 생성
   - MariaDB Database(스키마) 생성
3. Create: 게시글 작성
   - MariaDB Database에 'Board' 테이블 생성
   - 게시글 작성 폼 생성
   - 게시글 작성 처리
4. Read: 게시글 전체조회(list), 상세조회(detail)
   - 게시글 리스트 페이지 생성
   - 게시글 리스트 페이지에 DB에 저장된 게시글 출력
5. Delete: 게시글 삭제
   - 게시글 삭제 버튼 생성
   - 게시글 삭제 처리
6. Update: 게시글 수정
   - 게시글 수정 페이지 생성
   - 게시글 수정 처리

# 1. 개발 환경 세팅
1. IntelliJ Ultimate
   - JetBrains Toolbox를 통해 설치
2. MariaDB 재설치 과정
   - Homebrew 사용
   - **이슈**: 삭제 후 재설치 해도 `brew services start mariadb`시 MariaDB 서버가 stopped 상태임
   - **원인**: uninstall 후에도 잔존파일이 남아있음
   - 해결방법
     - `brew services stop mariadb`
     - `brew unlink mariadb`
     - `brew uninstall mariadb`
     - `brew cleanup`
     - `/opt/homebrew/etc` 위치에 있는 `my.cnf*`파일들을 모두 삭제(`rm -rf my.cnf*`)
     - `/opt/homebrew/var` 위치에 있는 `mysql` 삭제(`rm -rf mysql`) &rarr; 이후 재부팅함
     - 이후 mariadb 재설치(`brew install mariadb`)
     - `brew services start mariadb` &rarr; `brew services list`로 started 표시 확인
3. MySQL Workbench 설치
   - MariaDB 11.0.2 버전 이용 시 호환성 문제 경고 뜨나 무시하고 진행

# 2. 프로젝트 생성
1. Spring Boot 프로젝트 생성
   1. Spring Initializr: `start.spring.io`에 접속
      - Project: Gradle-Groovy
      - Language: Java
      - Spring Boot: 2.7.13 &rarr; 버전 3.0이상의 경우 JDK 17 이상 필요
      - Java: 11(JDK 11)
      - Dependencies: Spring Web, Spring Data JPA, MariaDB Driver, Thymeleaf, Lombok
   2. Generate 후 IntelliJ project open 실행(`build.gradle`)
      - settings에서 Build Tools에 Build and run이 모두 IntelliJ IDEA에서 실행되도록 변경
   3. JPA 사용 시 기본적으로 DB와 연동되어 있어야 함
      - `main/resources/application.properties`에 설정 추가
        ```
        spring.datasource.driver-class-name=org.mariadb.jdbc.Driver
        spring.datasource.username=root
        spring.datasource.password=123456
        spring.datasource.url=jdbc:mariadb://localhost:3306/board
        ```
2. MariaDB Database(스키마) 생성
   - 통모양 버튼 클릭 후 'board' 이름으로 생성 &rarr; Apply
   - 8080 포트를 이미 사용 시, 위 코드에 `server.port=8090` 추가
3. DB에 테이블 생성
   - id INT(PK, NN(Not Null), AI(Auto Increment)), title VARCHAR(45)(NN), content TEXT(NN)