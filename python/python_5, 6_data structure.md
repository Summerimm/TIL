# Data Structure
## 데이터구조 / 자료구조
- 여러 데이터를 효과적으로 사용, 관리하기 위한 구조
- 파이썬에는 대표적으로 List, Tuple, Dict, Set 등이 있음  
![image7](https://user-images.githubusercontent.com/108309396/214465652-70ff274d-5f06-41e8-b9ba-f43824a673cb.png)
- 데이터 구조를 활용하기 위해서는 method 사용
  - 메서드는 클래스 내부에 정의한 함수
  - 쉽게 설명하자면 객체의 기능
  - **데이터구조.메서드()** 형태로 활용!

# 순서가 있는 데이터 구조
## String
- 모든 문자는 str 타입(immutable)
- 문자열은 작음따옴표(')나 큰 따옴표(")를 활용하여 표기 &rarr; 소스코드 내에서 하나의 문장부호를 유지 권장
- 문자열 조회/탐색 및 검증 메서드  
![image8](https://user-images.githubusercontent.com/108309396/214722293-6dcb55b3-2ee4-4943-a731-4f7ea16cb8ec.png)
    - `.find(x)`: x가 존재하지 않을 때 **-1 반환**  
    - `.index(x)`: x가 존재하지 않을 때 **오류 발생**

- 문자열 변경 메서드  
![image9](https://user-images.githubusercontent.com/108309396/214722686-b5493ef8-6c37-4cad-aa68-1a0d42c6882f.png)
    - `.replace(old, new[, count])`: count를 지정하면, 해당 개수만큼만 시행
    - strip(양쪽 제거), lstrip(왼쪽 제거), rstrip(오른쪽 제거)
    - `'separator'.join([iterable])`
      ```python
      print('!'.join('Hello')) # 'H!e!l!l!o'
      ```

## List
- 여러 개의 값을 **순서가 있는 구조**로 저장하고 싶을 때 사용
- **mutable**
- 어떠한 자료형도 저장 가능
- 순서가 있는 시퀀스로 인덱스를 통해 접근 가능  
![image12](https://user-images.githubusercontent.com/108309396/214730101-331486a0-4810-4991-9e7c-32bdfeaafe7a.png)

## Tuple
- 여러 개의 값을 **순서가 있는 구조**로 저장하고 싶을 때 사용
- **immutable**
- 항상 소괄호 형태로 사용
- 값에 영향을 미치지 않는 메서드만을 지원
- 리스트 메서드와 대부분 동일
- 단일 항목의 경우 반드시 값 뒤에 **쉼표**를 붙여야 함
- 복수 항목의 경우 마지막 항목에 쉼표는 없어도 되지만, 넣는 것을 권장(Trailing comma)

## Operator
1. Membership Operator
   - `in` / `not in`
2. Sequence Type Operator
   - 산술연산자(+): 시퀀스 간의 concatenation
   - 반복연산자(*): 시퀀스 반복



# 순서가 없는 데이터 구조
## Set
- **중복되는 요소가 없이**, 순서에 상관없는 데이터 묶음
  - 중복되는 원소가 있다면 하나만 저장
  - 순서가 없기 때문에 index를 이용한 접근이 불가능
- 수학에서의 집합과 동일
  - 집합 연산이 가능(여집합을 표현하는 연산자는 별도로 존재X)
- mutable 
 
![image10](https://user-images.githubusercontent.com/108309396/214724172-6f2c7512-fd6e-4c41-9290-f93d4053f10f.png)

## Dictionary
- Key-value 쌍으로 이뤄진 자료형(3.7부터는 ordered, 이하 버전은 unordered)
- key
  - key는 immutable한 데이터만 활용 가능
- values
  - 어떠한 형태는 상관없음  

![image11](https://user-images.githubusercontent.com/108309396/214725505-a1139de2-d1cb-45fa-b671-a790676f5490.png)


# 얕은 복사와 깊은 복사(Shallow Copy & Deep Copy)
### 복사 방법
- 할당(Assignment)
  - 대입 연산자(=): 해당 객체에 대한 객체 참조를 복사
  - 해당 주소의 일부 값을 변경하는 경우 이를 참조하는 모든 변수에 영향
## 1. 얕은 복사(Shallow copy)
![image15](https://user-images.githubusercontent.com/108309396/214735332-37c800d4-68e7-4d59-bc2a-fcc58d551d4f.png)
  - slice 연산자 활용하여 같은 원소를 가진 리스트지만 연산된 결과를 복사(다른 주소)
  - 복사하는 리스트의 원소가 주소를 참조하는 경우  
## 2. 깊은 복사(Deep copy)
![image14](https://user-images.githubusercontent.com/108309396/214735062-52957be6-ca88-4adb-af24-61752b4377de.png)