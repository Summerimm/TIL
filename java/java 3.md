# 조건문 Conditional Statement
## if 문
```java
if 조건식{
  실행할 문장1;
  실행할 문장2;
}
```
- 실행할 문장이 하나라면 중괄호 생략 가능
## if-else문
```java
if 조건식{
  실행할 문장1;
  실행할 문장2;
}
else{
  실행할 문장a;
}
```
## 중첩 if문
```java
if (조건식A){
  if (조건식B){
    조건식 A, B 모두 참일 경우 수행할 문장;
  }
  else{
    조건식 A는 참, B는 거짓일 경우 수행할 문장;
  }
}
else{
  조건식 A가 거짓일 경우 수행할 문장;
}
```
- 중첩의 횟수에는 제한이 없음

## if-else if-else문
```java
if (조건식){
  실행할 문장1;
}
else if(조건식){
  실행할 문장a;
}
else{
  실행할 문장A;
}
```
## switch문
- 인자로 선택변수를 받아 변수의 값에 따라서 실행문이 결정
- break가 있는지 없는지가 중요
- default &rarr; else의 역할과 동일
```java
switch(수식){
  case 값1:
    실행문 A;
    break;
  case 값2:
    실행문 B;
    break;
  default:
    실행문 C;
}
```

# 반복문(Loop)
## for문
```java
for(초기화식; 조건식; 증감식){
    반복수행할 문장;
  }
```
- 초기하는 반복문이 시작될 때 한 번 실행
- 조건식이 false면 반복문 종료
- 증감식은 반복문의 반복이 끝나면 실행
- 초시화식, 증감식은 `,`를 사용하여 둘 이상을 작성할 수 있음
- 필요하지 않은 부분은 생략할 수 있음 &rarr; `for(;;)` 무한루프
- 반복횟수를 알고 있을 때 유용

## 중첩 for문
```java
for(초기화식; 조건식; 증감식){
  for(초기화식; 조건식; 증감식){
    반복수행할 문장;
  }
}
```
- 실습
```java
public class Main {
    public static void main(String[] args) {
        outer: for(int i=0; i<3; i++){
            for (int j=0; j<3; j++){
                if(i==1) continue outer;
                System.out.println((i+","+j));
            }
        }
    }
}
// 0,0 0,1 0,2 2,0 2,1 2,2
// outer는 라벨
```

## while문
```java
while(조건식){
    반복수행할 문장;
}
```
- 조건식이 true일 경우 계속해서 반복
- 조건식 생략 불가능
- 실습
```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // 1을 입력 받으면 계속 반복
        // 그 외의 값이면 종료(반복X)
        int num = sc.nextInt();
        while(num == 1){
            System.out.println("블록을 실행합니다.");
            num = sc.nextInt();
        }
    }
}
```

## do while문
```java
do{
  반복 수행할 문장
}
while(조건식);
```
- 블록 내용을 먼저 수행 후 조건식 판단(최소 한 번은 수행)
- 조건식이 true일 경우 계속해서 반복
- 조건식 생략 불가능
```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // 1을 입력 받으면 계속 반복
        // 그 외의 값이면 종료(반복X)
        int num = sc.nextInt();
        do{
            System.out.println("블록을 실행합니다.");
            num = sc.nextInt();
        }while(num == 1);
    }
}
```

## break & continue
1. break
  - switch, while, do-while, for문의 블록에서 빠져나오기 위해 사용
  - 반복문에 라벨을 붙여 한 번에 빠져 나올 수 있음
```java
public class Main {
    public static void main(String[] args) {
        for(int i=0; i<10; i++){
            if(i==3) break;
            System.out.println(i);
        }
    }
}
// 0 1 2
```

2. continue
  - 반복문의 특정지점에서 제어를 반복문의 처음으로 보냄
  - 반복문에 라벨을 붙여 제어할 수 있음
```java
public class Main {
    public static void main(String[] args) {
        for(int i=0; i<10; i++){
            if(i==3) continue;
            System.out.println(i);
        }
    }
}
```