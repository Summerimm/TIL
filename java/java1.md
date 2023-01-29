# [Java 개발환경 Setting]
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
![IMG_4DCC696829AB-1](https://user-images.githubusercontent.com/108309396/215321533-b1fcfb93-1055-40df-81b2-7ac92612addf.jpeg)
