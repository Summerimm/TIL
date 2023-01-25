# [Function]

## 1. Intro
> ### 함수를 왜 사용할까?
  - **Decomposition** (분해): 기능을 분해해 재사용 가능하게 만듦
  - **Abstraction** (추상화): 복잡한 내용을 모르더라도 사용할 수 있도록 &rarr; 재사용성과 가독성, 생산성

## 2. 함수 기초  
> ### 함수의 종류  
1. 내장 함수(built-in function)  
    - 파이썬에 기본적으로 포함된 함수
2. 외장 함수(라이브러리)
    - import문을 통해 사용하며, 외부 라이브러리에서 제공하는 함수
3. 사용자 정의 함수(user-defined function)
    - 직접 사용자가 만드는 함수
4. 람다 함수(lambda function)  
    - anonymous fuction, 1회용으로 한 줄에 정의하여 사용하는 함수   

> ### 함수의 정의   
- 특정한 기능을 하는 코드의 묶음  
- 특정 코드를 매번 다시 작성하지 않고, 필요시에만 호출해 간편히 사용    
![image1](https://user-images.githubusercontent.com/108309396/213062735-05b09c33-35ad-4fff-80a9-e28bccd92b1c.png) 

> ### 함수 기본 구조
- Define & call  
- Input
- Docstring
  - 함수 body 앞에 선택적으로 작성 가능
  - 작성 시에는 반드시 첫 번째 문장에 문자열 """
- Scope
- Output  

![image2](https://user-images.githubusercontent.com/108309396/213062793-20c3abf7-b09b-4d88-874e-8532ca0d6614.png)
## 3. 함수의 결과값(Output)
> ### Output 값에 따른 함수의 종류
1. Void function
      - 명시적인 return 값이 없는 경우 &rarr; None을 반환하고 종료
      - ex) print: 값을 출력하지만, 반환하지는 않음
  1. Value returning function
      - 함수 실행 후 return문을 통해 값 반환
      - return을 하게 되면, 값 반환 후 **함수가 바로 종료**

> ### 두 개 이상의 값 반환
- 튜플(혹은 리스트와 같은 컨테이너)을 활용하여 두 개 이상의 값 반환  
![image3](https://user-images.githubusercontent.com/108309396/213062796-72d4d8ff-abb1-43b1-933b-db2c20e807f1.png)

## 4. 함수의 입력(Input)
> ### Parameter와 Argument
- **Parameter**: 함수를 **정의**할 때, 함수 내부에서 사용되는 변수 (매개변수) 
- **Argument**: 함수를 **호출**할 때, 넣어주는 값 (인자)
  - 필수 argument: 반드시 전달되어야 함  
  - 선택 argument: 값을 전달하지 않아도 되는 경우는 기본값 전달 (ex. range() 기본값은 1씩 증가)
  - Positional Arguments: 각 위치에 자동 배정  
  - Keyword Arguments: 직접 변수의 이름으로 특정 argument를 전달
    - **Keyword argument 다음에 Positional argument를 활용할 수 없음**
![image5](https://user-images.githubusercontent.com/108309396/213062798-7bfc484d-404f-46e5-ac7f-3590ca028495.png)
  - Default Arguments Values  
    - 기본값을 지정하여 함수 호출 시 argument 값을 설정하지 않도록 함  
    - 정의된 것보다 더 적은 개수의 argument들로 호출 가능  
![image4](https://user-images.githubusercontent.com/108309396/213062797-81f6b86f-b63f-4081-95f9-af736d493dd0.png) 

### 5. 함수의 범위(Scope)  
> ### Scope
- 함수는 코드 내부에 local scope 생성 / 그 외의 공간은 global scope로 구분
  - global scope: 코드 어디에서든 참조할 수 있는 공간
  - local scope: 함수가 만든 scope. 함수 내부에서만 참조 가능

> ### Variable
  - global variable: global scope에 정의된 변수
  - local variable: local scope에 정의된 변수

> ### 변수 수명주기(lifecycle)
- 변수는 각자의 수명주기가 존재
  - built-in scope
    - 파이썬이 실행된 이후부터 영원히 유지
  - global scope
    - 모듈이 호출된 시점 이후 혹은 인터프리터가 끝날 때까지 유지
  - local scope
    - 함수가 호출될 때 생성되고, 함수가 종료될 때까지 유지

> ### Namespace
> - 식별자들을 기억하는 공간  
> - 같은 이름이 가능하다
1. **Built-in namespace**: 내장된 namespace (return, id, list, dict...)
2. **Global namespace**: 하나의 작성된 파이썬 프로그램 내에서 실행되면서 생성되는 namespace
3. **Enclosing namespace**: 함수 안쪽에 함수를 중첩 가능 &rarr; 안쪽 함수 기준으로 바깥쪽 함수의 namespace가 Enclosing namespace
4. **Local namespace**: 함수 실행 시 함수 안쪽에 생성되는 name space
- locals(), globals(): dictionary 형식으로 local namespace 안의 변수와 값들을 보여줌

> ### 이름 검색 규칙(Name Resolution)
- LEGB Rule
  - Local scope: 지역 범위(현재 작업 중인 범위)
  - Enclosed scope: 지역 범위 한 단계 위 범위
  - Global scope: 최상단에 위치한 범위
  - Built-in scope: 모든 것을 담고 있는 범위(ex. print())
- 함수 내에서는 바깥 scope의 변수에 접근 가능하나 수정은 할 수 없음

> ### global x
- 현재 코드 블록 전체에 적용, 나열된 식별자가 global variable
  - global에 나열된 이름은 같은 코드 블록에서 global 앞에 나올 수 없음
  - global에 나열된 이름은 parameter, for loop 대상, 클래스/함수 정의 등으로 정의되지 않아야 함
- 선언된 적 없는 변수도 활용 가능

> ### nonlocal x
- global을 제외하고 가장 가까운(둘러싸고 있는) scope의 변수를 연결하도록 함
  - nonlocal에 나열된 이름은 같은 코드 블록에서 nonlocal 앞에 나올 수 없음
  - nonlocal에 나열된 이름은 parameter, for loop 대상, 클래스/함수 정의 등으로 정의되지 않아야 함
- global과 달리 이미 존재하는 이름과의 연결만 가능

> ### 함수의 범위 주의
- 기본적으로 함수에서 선언된 변수는 Local scope에 생성되고, **함수 종료 시 사라짐**
- 해당 scope에 변수가 없는 경우 LEGB rule에 의해 이름을 검색
  - 변수에 접근 가능 but 수정 불가능
  - 값을 할당하는 경우 해당 scope의 namespace에 새롭게 생성되기 때문
  - **단, 함수 내에서 필요한 상위 scope 변수는 argument로 넘겨서 활용할 것**
- 상위 scope에 있는 변수를 수정하고 싶다면 global, nonlocal 키워드 활용 가능
  - 단, 코드가 복잡해지면서 변수의 변경을 추적하기 어렵고, 예기치 못한 오류 발생 가능
  - 가급적 사용X, **함수로 값을 바꾸고자 한다면 항상 argument로 넘기고 return값을 사용하는 것을 추천**