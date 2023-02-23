# Array 배열
- 같은 종류의 데이터를 저장하기 위한 자료구조
- **크기가 고정되어 있음** (한 번 생성된 배열은 크기를 바꿀 수 없음-배열 생성 시 메모리 상에서 연속적으로 할당하기 때문)
- 배열을 객체로 취급(참조형)
- 배열의 요소를 참조하려면 배열이름과 index라고 하는 음이 아닌 정수값을 조합하여 사용
- **index는 0부터 시작**
- **배열이름.length**를 통해 배열의 길이 조회 가능
  - `.`: 멤버 연산자
- 크기 변경 필요 시 새로운 배열을 생성 후 내용을 옮긴다

## 배열의 선언
- 타입[] 변수 &rarr; 권장
- 타입 변수[]  
<img width="711" alt="image" src="https://user-images.githubusercontent.com/108309396/220562404-c4e53e81-6b90-4356-998b-af1c44dfef0e.png">


## 배열의 생성과 초기화
- 자료형[] 배열이름 = new 자료형[길이]; // 배열 생성(자료형의 초기값으로 초기화)
- 자료형[] 배열이름 = new 자료형[] {값1, 값2, 값3, 값4}; // 배열 생성 및 값 초기화
- 자료형[] 배열이름 = {값1, 값2, 값3, 값4}; // 선언과 동시에 초기화  
<img width="675" alt="image" src="https://user-images.githubusercontent.com/108309396/220562264-342bb586-0201-4332-818b-eaa2588ebd41.png">
```java
public class Main {
    public static void main(String[] args) {
        boolean[] bArr = new boolean[5];
        char[] cArr = new char[5];
        float[] fArr = new float[5];
        double[] dArr = new double[5];
        String[] sArr = new String[5];

        System.out.println(bArr[0]); // false
        System.out.println(cArr[0]); // 공백문자 \u0000
        System.out.println(fArr[0]); // 0.0
        System.out.println(dArr[0]); // 0.0
        System.out.println(sArr[0]); // null
    }
}
```
## 배열의 메모리 생성과정
<img width="754" alt="스크린샷 2023-02-22 오후 5 15 43" src="https://user-images.githubusercontent.com/108309396/220562011-595f3ac8-555d-43a0-9aad-72c5d1195e5a.png">

```java
public class Main {
    public static void main(String[] args) {
        // 배열 변수(주소값을 담을 수 있는)의 선언
        int[] arr;
        int[] arr2; // 권장하지 않음

        int[] arr3 = new int[5]; // int형의 경우 0으로 초기화, 나눠쓸 수 있음
        int[] arr4 = new int[] {1, 2, 3, 4, 5}; // 원하는 값으로 초기화할 때, 나눠쓸 수 있음
        int[] arr5 = {1, 3, 5, 7, 9}; // 반드시 한 줄에 써줘야 함. 나눠서 쓰면 에러

        int[] arr6;
        arr6 = new int[7];
        // arr6 = {1, 2, 3, 4, 5}; // 에러 발생
        arr6 = new int[] {1, 2, 3, 4, 5};
    }
}
```
### for-each
- 가독성이 개선된 반복문으로, 배열 및 Collections에서 사용
- index 대신 직접 요소(elements)에 접근하는 변수를 제공
- naturally ready only(copied value)
- 전체 순회할 때 유용
```java
int intArray [] = {1, 3, 5, 7, 9};
for(intx : intArray){
  System.out.println(x);
}
```
- 전통적인 for문: index를 통해 부분적으로 접근 가능, 역순으로도 접근가능하다는 장점
```java
for(int i=0; i<intArray.length; i++){
  int x  = intArray[i];
  System.out.println(x)
}
```

### 배열의 출력
- 반복문을 통해서 출력
- `Arrays.toString(배열)`: 배열 안의 요소를 [값1, 값2,...] 형태로 출력
```java
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] scores = new int[5];
        for (int i = 0; i < 5; i++) {
            scores[i] = sc.nextInt();
        }

        // 전통적인 방식
        for (int i = 0; i < 5; i++) {
            System.out.println(i + "번째 점수는: " + scores[i]);
        }

        // for-each
        for (int num : scores) {
            System.out.println("점수는: " + num);
        }

        // Arrays.toString을 이용한 배열 출력
        System.out.println(Arrays.toString(scores));

        // 평균
        int sum = 0;
        for(int num : scores){
            sum += num;
        }
        System.out.println(sum /5);
    }
}
```

### 배열의 복사
-  배열은 생성하면 길이를 변경할 수 없기 때문에 더 많은 저장공간이 필요하다면 큰 배열을 생성하고 이전 배열의 값을 복사해야함
-  새로운 배열 = Arrays.copyOf(복사하고 싶은 배열, 새로운 배열의 크기)
```java
public class Main {
    public static void main(String[] args) {
        int[] scores = new int[] {29, 45, 67, 84, 92};
        // scores[5] = 44; -> ArrayIndexOutOfBoundsException
        // 기본적인 방법
        int[] newScores = new int[10];
        for(int i=0; i<5; i++){
            newScores[i] = scores[i];
        }
        System.out.println(Arrays.toString(newScores));
        // Arrays.copyOf 사용
        int[] newScores2 = Arrays.copyOf(scores, scores.length * 2);
        System.out.println(Arrays.toString(newScores2));
    }
}
```

## 배열 실습 문제
### 배열의 최댓값, 최솟값 찾기 문제
```java
public class Main {
    public static void main(String[] args) {
        int[] intArray = { 3, 27, 13, 8, 235, 7, 22, 9, 435, 31, 54 };

        int min = Integer.MAX_VALUE; // 21억
        int max = Integer.MIN_VALUE; // -21억

        for(int num : intArray){
            min = Math.min(min, num);
            max = Math.max(max, num);
        }
        System.out.printf("min: %d, max: %d%n", min, max);
    }
}
```

### 배열 빈도수 구하기
```java
public class Main {
    public static void main(String[] args) {
        int[] intArray = {3, 7, 2, 5, 7, 7, 9, 2, 8, 1, 1, 5, 3};
        int[] count = new int[10]; // using Counting array

        for(int num : intArray){
            count[num]++;
        }
        System.out.println(Arrays.toString(count));
    }
}
```

# Multidimensional Array 다차원 배열
- 2차원 이상의 배열을 의미
- 배열 요소로 또 다른 배열을 가지는 배열
- 2차원 배열은 배열 요소로 1차원 배열의 참조를 가지는 배열
- 3차원 배열은 배열 요소로 2차원 배열의 참조를 가지는 배열

### 2차원 배열 선언
- `int[][] iArr` &rarr; 권장
- `int iArr[][]`
- `int[] iArr[]`

### 2차원 배열 생성
- `배열의 이름 = new 배열유형[1차원 배열개수][1차원 배열의 크기];`
- `배열의 이름 = new 배열유형[1차원 배열개수][];`
```java
int [][] scores = {{90, 95, 84, 90},{100, 80, 75, 60}, {100, 90, 80, 95}};
```
![배열](https://user-images.githubusercontent.com/108309396/216528999-f9ff4288-a611-47e4-a7ed-8e564df2e9dc.png)
```java
public class Main {
    public static void main(String[] args) {
        int[][] arr = new int[3][4];
        int[][] raggedArr = new int[3][];
        raggedArr[0] = new int[4];
        raggedArr[1] = new int[3];
        raggedArr[2] = new int[5];

        // new int[행][열]
        // 행: 2차원 배열의 크기
        // 열: 1차원 배열의 크기
        // arr.length: 3
        // arr[0].length : 4
        // arr.length * arr[0].length : 12
        for(int r=0; r<3; r++){
            for(int c=0; c<4; c++){
                System.out.printf("%4d", arr[r][c]);
            }
            System.out.println();
        }
    }
```

### 실습문제) 모래시계
```java
public class Main {
    public static void main(String[] args) {
        int[][] iArr = new int[6][6];

    }
}
/*
1 2 3 4 5
  6 7 8
    9
  10 11 12
13 14 15 16 17
 */
```