# 배열
- 같은 종류의 데이터를 저장하기 위한 자료구조
- **크기가 고정되어 있음** (한 번 생성된 배열은 크기를 바꿀 수 없음-배열 생성 시 메모리 상에서 연속적으로 할당하기 때문)
- 배열을 객체로 취급(참조형)
- 배열의 요소를 참조하려면 배열이름과 index라고 하는 음이 아닌 정수값을 조합하여 사용
- **index는 0부터 시작**
- **배열이름.length**를 통해 배열의 길이 조회 가능
- 크기 변경 필요 시 새로운 배열을 생성 후 내용을 옮긴다

## 배열의 선언
- 타입[] 변수 &rarr; 권장
- 타입 변수[]  
![배열](https://user-images.githubusercontent.com/108309396/216481715-c7653580-a6f3-4416-bf3f-08364f3fa98a.png)

## 배열의 생성과 초기화
- 자료형[] 배열이름 = new 자료형[길이]; // 배열 생성(자료형의 초기값으로 초기화)
- 자료형[] 배열이름 = new 자료형[] {값1, 값2, 값3, 값4}; // 배열 생성 및 값 초기화
- 자료형[] 배열이름 = {값1, 값2, 값3, 값4}; // 선언과 동시에 초기화  
![배열2](https://user-images.githubusercontent.com/108309396/216482286-d6f75f91-3c9e-44c3-9bf1-55cb86d63cc0.png)
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
![화면 캡처 2023-02-03 093744](https://user-images.githubusercontent.com/108309396/216482900-32fbab30-dba2-4e39-9524-23e9f6628e47.png)
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