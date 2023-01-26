# [Function application]

## 1. 함수 응용
> ### 내장 함수(Built-in Functions)  
![image6](https://user-images.githubusercontent.com/108309396/213324974-01eafa64-c27d-4334-82b5-2260cb43bdf0.png)

> ### map(function, iterable)
- 순회 가능한 데이터구조(iterable)의 모든 요소에 함수(function) 적용하고, 그 결과를 **map object**로 반환
  - 리스트 형변환 등을 통해 결과를 직접 확인 가능

> ### filter(function, iterable)
- 순회 가능한 데이터구조(iterable)의 모든 요소에 함수(function) 적용하고, 그 결과가 **True**인 것들을 **filter object**로 반환
  - 리스트 형변환 등을 통해 결과를 직접 확인 가능


> ### zip(*iterables)
- 복수의 iterable을 모아 튜플을 원소로 하는 zip object를 반환
  - 리스트 형변환 등을 통해 결과를 직접 확인 가능


> ### lambda[parameter]: 표현식
- 표현식을 계산한 결괏값을 반환하는 함수로, 이름이 없는 함수여서 익명 함수라고도 불림
- 특징
  - return문을 가질 수 없음
  - 간편 조건문 외 조건문이나 반복문을 가질 수 없음
- 장점
  - 함수를 정의해서 사용하는 것보다 간결하게 사용 가능
  - def를 사용할 수 없는 곳에서도 사용 가능

> ### 재귀 함수(recursive function)
- 자기 자신을 호출하는 함수
- 변수의 사용이 줄어들며, 코드의 가독성이 높아짐
- 1개 이상의 base case(종료되는 상황)가 존재하고, 수렴하도록 작성
> Factorial   
```python
def fac(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fac(n - 1)

fac(5)
```

> ### 재귀함수 주의사항
- base case 필수
- 메모리 스택이 넘치게 되면(stack overflow) 프로그램이 동작X
- 파이썬에서는 maximum recursion depth가 1,000번으로 호출 횟수가 이를 넘어가면 Recursion Error 발생


## 2. 함수 가변 입력 (패킹/언패킹)
> ### Packing/Unpacking Operator
- 모든 시퀀스형은 패킹/언패킹 연산자 *를 사용하여 객체의 패킹 또는 언패킹이 가능

> ### Packing
```python
x, *y = i, j, k... # x = i, y = j, k, .. 
```
- 대입문의 좌변 변수에 위치
- 우변의 객체 수가 좌변의 변수 수보다 많을 경우 객체를 순서대로 대입
- 나머지 항목들은 모두 별 기호 표시된 변수에 리스트로 대입 

> ### Unpacking
- argument 이름이 *로 시작하는 경우, unpacking
  - \* packing의 경우, 리트스토 대입
  - \* unpacking의 경우, 튜플 형태로 대입

> 가변 인자(*args)
- 여러 개의 Positional argument를 하나의 필수 parameter로 받아서 사용
- 몇 개의 Positional argument를 받을지 모르는 함수를 정의할 때 유용

> 가변 키워드 인자(**kwargs)
- 몇 개의 키워드 인자를 받을지 모르는 함수를 정의할 때 유용
- \**kwargs는 **딕셔너리**로 묶여 처리되며, parameter에 \**를 붙여 표현

## 3. 모듈과 패키지
- 다양한 기능을 하나의 파일(.py)로 &rarr; **module**
- 다양한 파일(모듈)을 하나의 폴더로 &rarr; **package**
- 다양한 패키지를 하나의 묶음으로 &rarr; **library**

&rarr; 이를 관리하는 관리자: pip  
&rarr; 패키지의 활용 공간: 가상환경

> 파이썬 패키지 관리자(pip) 명령어
- 패키지 삭제: `$pip uninstall Somepackage`
- 패키지 목록: `$pip list`
- 특정 패키지 정보: `$pip show SomePackage`
- 패키지 관리하기  
  - `$pip freeze > requirements.txt`  
  - `$pip install -r requirements.txt`

> 패키지
- 패키지는 여러 모듈/하위 패키지로 구조화
  - package.module
- 모든 폴더에는 \_\_init__.py를 만들어 패키지로 인식

## 4. 가상환경
- 파이썬 표준 라이브러리가 아닌 외부 패키지와 모듈을 사용하는 경우 모두 pip를 통해 설치
- 다수의 프로젝트를 진행하는 경우 버전이 상이할 수 있음 &rarr; 가상환경을 만들어 프로젝트 별로 독립적인 패키지 관리 가능
- 특정 디렉토리에 가상 환경을 만들고 고유한 파이썬 패키지 집합을 가질 수 있음
  - 실행환경(Git bash 등)에서 가상환경을 활성화시켜 해당 폴더에 있는 패키지를 관리/사용
- 가상환경을 생성하면, 해당 디렉토리에 별도의 파이썬 패키지가 설치됨 `$ python -m venv venv`
- 활성화 
  - `<venv>`는 가상환경을 포함하는 디렉토리의 경로  
![111](https://user-images.githubusercontent.com/108309396/214743248-2c8a8e2e-02a1-43b0-bd04-61cf49d6161a.png)
- 비활성화는 `$ deactivate`