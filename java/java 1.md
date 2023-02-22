# Java 개발환경 Setting
## 환경변수 설정
1. vi ~/.zshrc
```\# User configuration
JAVA_HOME=/Library/Java/JavaVirtualMachines/zulu-11.jdk/Contents/Home
PATH=$PATH:$JAVA_HOME/bin
CLASSPATH=$JAVA_HOME/lib

export JAVA_HOME
export PATH
export CLASSPATH
```
2. source ~/.zshrc
3. echo $JAVA_HOME / echo $PATH / echo $CLASSPATH 확인

### 환경변수를 설정하는 이유
- 해당 파일로 접근하기 위해서는 그 파일이 존재하는 디렉토리로 이동해야하는 불편함이 있다. 만약 어느 경로에서나 파일을 열 수 있는 방법은 없을까?

  ▶ 답은 환경변수이다. 

- 운영체제가 어떠한 명령을 받았을 때의 동작을 보자.
  1. 현재 위치한 디렉토리에 해당 명령어가 있는지 확인한다. (있는 경우 실행하고 없는 경우 2번으로 넘어간다.) 
  2. PATH라는 환경변수가 가지고 있는 모든 경로에 대해서 입력된 명령어가 존재하는지 탐색한다. 
  3. 명령어를 발견하면 실행한다. 발견하지 못하면 에러 메세지를 출력한다.

- **즉, 환경변수를 설정하는 이유는 운영체제가 어떤 경로에서든지 파일을 인식하도록 하기 위해서.**
- JDK의 /bin까지 등록하는 이유는 bin에 실행파일이 있기 때문

## IntelliJ
- project 생성 시 Project SDK로 JDK11 사용
> \> SDK란?  
> Software Development Kit 의 약자로 프로그래머들을 위해서 제공하는 개발 도구들이다. SDK 안에는 IDE(통합개발환경) 을 포함하는데, 여기에는 여러 API, 디버깅, 문서 등 여러 도구가 들어가있다.

- Project Tool Window
  - `.idea directory`: 프로젝트의 구조 정보 등의 프로젝트 관련 meta data가 존재
  - `.iml`(IntelliJ IDEA Module): Module 구성에 대해 xml 형태로 기술해놓은 파일
  - `src directory`: Class 생성하는 공간, 새로운 Class  파일을 생성하게 되어도 실제로는 .java 소스 파일이고 .class 파일은 해당 source code를 build한 뒤 생성된다.  
  <img src="https://user-images.githubusercontent.com/108309396/215321533-b1fcfb93-1055-40df-81b2-7ac92612addf.jpeg" width="50%" height="50%"/>
- `main` 입력 후 클릭 시 자동으로  `public static void main(String[] args){}` 생성
- `sout` 입력 시 자동으로 `System.out.print();` 생성
- Built Project: `cmd + F9`
- 빌드가 완료되면 out > production > [프로젝트명] > [클래스이름].class 파일이 생성됨
- Run .java: `ctrl + R` / `Shift+F10`

## JVM(Java Virtual Machine, 자바 가상머신)이란?
- 자바 바이트코드를 실행할 수 있는 주체
- 자바 바이트코드는 플랫폼에 독립적이며 모든 JVM은 자바 가상 머신 규격에 정의된대로 자바 바이트 코드를 실행
- C언어의 경우 컴파일하면 바로 기계어가 나와 머신에서 실행가능
- Java의 경우 Java 원시프로그램(.java)를 컴파일하면 자바 바이트 코드(.class)가 나오고 각 운영체제에 맞는 JVM 위에서 실행됨
- 장점: 어떤 운영체제든 컴파일을 한 번만 하면 각 운영체제 위에서 실행 가능함. 즉, 운영체제별로 컴파일할 필요가 없음
- C의 경우 목적 운영체제에 맞게 따로 컴파일을 해줘야 함  
![화면 캡처 2023-02-02 091347](https://user-images.githubusercontent.com/108309396/216198756-286d1bda-6b29-4062-96fd-d7b3fe78efce.png)
- 안드로이드 운영체제의 경우 최적화를 위해 자바 바이트 코드(.class)가 아닌 달빅 실행 파일(.dex)을 VM이 아닌 달빅 가상 머신에서 실행시킨다.

## JDK & JRE
- JDK(Java SE Developmenet Kit) = JRE + 개발에 필요한 도구(컴파일러, 디버거)
- JRE(Java Runtime Environment): 자바 실행 환경(JVM이 포함됨) 

## Hello SSAFY
```java
import java.lang.*;
public class Hello{
  public static void main(String[]args){
    System.out.println("Hello World!");
  }
}
// Hello World!
```
- Hello.java로 저장 후 C:드라이브의 Temp파일에 저장(.txt가 아닌 모든 파일로 저장)
- 터미널에서 Temp파일에 접근 후 `javac Hello.java`로 컴파일, 실행은 `java Hello`

## main method
- `public static void main(String[]args){}`
- 실행 명령인 java를 실행 시 가장 먼저 호출되는 부분
- 만약 Application에서 main() 메서드가 없다면 절대로 실행될 수 없음
- Application의 시작 &rarr; 특정 클래스의 main() 실행

## 주석(Comment)
- `//`, `/*내용*/`: 한 줄 주석, 여러 줄 주석
- `/**내용**/`: Documentation API를 위한 주석 처리

## 출력문
- print: 문자열
- println: 문자열 + "/n"
- printf
  - `%d`: 정수 
    - `%4d`: 4칸 확보 후 오른쪽 정렬 
    - `%-4d`: 4칸 확보 후 왼쪽 정렬
    - `%04d`: 4칸 확보 후 오른쪽 정렬, 빈 칸 대신 0을 채워넣음
  - `%f`: 실수(default 여섯째자리까지 표시)
    - `.2f`: 둘째 자리까지 표시
  - `%c`: 문자
  - `%s`: 문자열