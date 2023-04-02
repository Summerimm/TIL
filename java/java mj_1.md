# Java 기본 문법1
## Variable이란?
- 자료를 저장하기 위한 메모리 공간으로 **타입에 따라 크기가 달라짐**
- 메모리 공간에 value를 assign 후 사용

## Type이란?
- 데이터의 종류
  - `primitive type(기본형)`: 미리 정해진 크기의 데이터 표현, 변수 자체에 값 저장
  - `reference type(참조형)`: 크기가 미리 정해질 수 없는 데이터의 표현, 변수에는 실제 값을 참조할 수 있는 주소만 저장  
![image](https://user-images.githubusercontent.com/108309396/228397020-6068e77c-af60-448c-bcf1-8089e91ddb58.png)

### Integer Overflow
- 정수 계산 시 overflow 주의
- 필요한 수의 크기를 고려해서 int 또는 long 등 타입 선택
```java
public static void main(String[] args){
  int i1 = Integer.MAX_VALUE;
  int i2 = i1 + 1;
  System.out.println(i2);
  // -2147483648
  // 10000000000000..(2)
}
```

### Float, Double의 특징
- 실수의 연산은 부정확함
- 유효 자리수를 이용한 반올림 처리
```java
public static void main(String[] args){
  float f1 = 2.0f;
  float f2 = 1.1f;
  System.out.println(f1 - f2);  // 0.9

  double d1 = 2.0;
  double d2 = 1.1;
  System.out.println(d1 - d2);  // 0.89999999..

  // 1. 100곱하고 100.0으로 나누기
  System.out.println(( (int)(d1*100)- (int)(d2*100) )/100.0);
  // 2. BigDecimal class 사용
  BigDecimal b1 = new BigDecimal("2.0");
  BigDecimal b2 = new BigDecimal("1.1");
  System.out.println(b1.subtract(b2));
}
```

## Type casting(형 변환)
- 변수의 타입을 다른 타입으로 변환하는 것
- primitive는 primitive끼리, reference는 reference끼리 형 변환 가능
- 기본형과 참조형의 형 변환을 위해선 Wrapper 클래스 사용
  - (int), (float)...
- 형 변환 연산자(괄호) 사용
```java
double d = 100.5;
int result = (int) d; // 100
```

### 기본형의 형 변환 진행
- 작은 집 &rarr; 큰 집: 값 손실X(묵시적 형 변환)
- 큰 집 &rarr; 작은 집: 값 손실O(명시적 형 변환)
- 값의 크기, 타입의 크기가 아닌 **타입의 표현 범위가 커지는 방향**으로 할당할 경우는 묵시적 형 변환 발생
- 묵시적 형 변환은 자료의 손실 걱정이 없으므로 JVM이 서비스 해줌.
- char는 sign비트가 없어 양수로 표현할 때는 short보다 많이 표현 가능하지만 음수 표현시에는 short가 더 많이 표현 가능
  - 따라서 같은 16비트임에도 서로 호환 불가

## 연산자란?
- 어떤 기능을 수행하는 기호(+, -, *, /...)
- 산술 이항 연산자는 연산 전에 피연산자의 타입을 일치시킨다.
- 피연산자의 크기가 4byte(int) 미만이면 int로 변경한 후 연산 진행
- 두 개의 피연산자 중 큰 타입으로 형 변환 후 연산 진행
- short circuit 연산자(`||`): a || b를 연산할 경우 a가 true이면 굳이 b를 연산하지 않는다

# java 기본 문법2
## 조건문(Conditional Statement)
- `if (_____)`: 논리형, 비교식, Method Call
- `switch (_____)`: 정수호환, Enum, Class Object, Method Call

## 반복문(Loop)
- `for ( __; __; __)`
- 초기값, 조건식, 증감식의 위치가 명확
- 반복의 회수가 명확한 경우
- index의 증감 활용  
![image](https://user-images.githubusercontent.com/108309396/228401674-df93f9b5-2fa6-4f60-895b-6ff32549f135.png)    
- `while(___)`  
- 반복의 회수가 불명확
- index보다는 break, continue 활용  
![image](https://user-images.githubusercontent.com/108309396/228401757-1e40675a-39cc-4b33-ac70-c4161570fad4.png)  