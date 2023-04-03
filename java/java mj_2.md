# 배열
## 배열이란? 
- **동일한 타입의 데이터 0개 이상**을 하나의 **연속된 메모리 공간**에서 관리하는 것
- 요소에 접근하는 속도가 매우 빠르다
- 한 번 생성하면 크기 변경 불가

## 배열의 생성과 초기화
- 타입[] 변수명;
  - `int[] points; String[] names;` &rarr; reference 타입 변수
- 생성
  - new keyword와 함께 저장하려는 데이터 타입 및 길이 지정: new data_type[length]
- 배열 요소의 초기화
  - 배열의 생성과 동시에 저장 대상 자료형에 대한 기본값으로 default 초기화 진행  
<img width="443" alt="image" src="https://user-images.githubusercontent.com/108309396/229297203-56bef705-15c1-4063-8104-c66852ca4799.png">  
- 생성과 동시에 할당한 값으로 초기화
  - `int[] b = new int[] {1, 3, 4};`
  - `int[] c = {1, 3, 4};`
- 선언과 생성을 따로 처리할 경우 초기화 주의
  - `int[] points;`
  - `points = new int[]{1, 3, 5};`

## 배열의 사용
- 배열은 index 번호를 가지고 각 요소에 접근 가능
  - index 번호는 0부터 시작
  - 배열의 길이: `배열이름.length`로 배열의 크기 조회 가능
- [참고] Array 출력을 편리하게 &rarr; for문을 통한 출력 대신 `Arrays.toString()`

## [예제] char[]를 이용해 String "SSAFY"의 각 문자를 저장하고 출력하는 코드 작성
```java
String org = "SSAFY";
char[] chars = new char[org.length()];

for (int i=0; i<chars.length; i++){
  chars[i] = org.charAt();
}

for (int i=0; i<chars.length; i++){
  System.out.print(chars[i])
}

// API의 활용
chars = org.toCharArray();
for (int i=0; i<chars.length(); i++){
  System.out.print(chars[i])
}

```

## 배열의 생성과 메모리 사용 과정
<img width="935" alt="image" src="https://user-images.githubusercontent.com/108309396/229298048-5225718e-2814-448a-9d09-1e5b80a96e6a.png">

## for-each with Array
- 가독성이 개선된 반복문으로, 배열 및 Collections에서 사용
- index 대신 직접 요소(element)에 접근하는 변수를 제공
  - naturally read only(copied value)  
<img width="302" alt="image" src="https://user-images.githubusercontent.com/108309396/229298119-278ce102-ebe8-4274-8f5e-babe167eb7c4.png">

## Array is Immutable
- 배열은 최초 메모리 할당 이후, 크기 변경 불가
- 개별 요소는 다른 값으로 변경 가능하나, 요소를 추가하거나 삭제 불가
- API 제공하는 배열 복사 method
  - <img width="761" alt="image" src="https://user-images.githubusercontent.com/108309396/229298739-abf794ad-daa2-45e2-9542-84fb320cf66b.png">

## [참고] Random 
```java
Random rand = new Random();
int[] arr = new int[5];

for (int i=0; i<arr.length; i++){
  arr[i] = rand.nextInt(6) + 1;
}
```

# 다차원 배열
## 2차원 배열 만들기(1)
- 선언: `int[][] intArray;`
- 생성: `intArray = new int[4][3];`
- 값 할당: `intArray[0][2] = 3;`
- 선언, 생성, 할당 동시에 `int[][] intArray = {{0, 1, 2}, {0, 1, 2}};`

## 2차원 배열 만들기(2)
- 1차 생성: `int[][] intArray = new int[4][];
- 1차 배열만 생성 후, 필요에 따라 2차 배열을 생성: `intArray[0] = new int[3]; intArray[1] = new int[2];`

## 2차원 배열의 메모리 사용 단계
![image](https://user-images.githubusercontent.com/108309396/229529245-4c19796b-1e77-4052-8ec2-712bcdbe721a.png)