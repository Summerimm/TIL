## [ Ch 01-1. C언어 기반의 C++ 1 : printf와 scanf를 대신하는 입출력 방식 ]
# C++ 버전의 Hello World 출력 프로그램
- 헤더파일의 선언 `include <iostream>`
- 출력의 기본구성 `std::cout<<'출력대상1'<<'출력대상2<<'출력대상3';`
- 개행의 진행 `std::endl`을 출력하면 개행이 이뤄짐
```cpp
#include <iostream>

int main(void)
{
  int num=20;
  std::cout<<"Hello World!"<<std::endl;
  std::cout<<"Hello "<<"World!"<<std::endl;
  std::cout<<num<<' '<<'A';
  std::cout<<' '<<3.14<<std::endl;
  return 0;
}
```
- 출력결과
```
Hello World!
Hello World!
20 A 3.14
```

# scanf를 대신하는 데이터의 입력
- 입력의 기본구성 `std::cin>>'변수'`
- 변수의 선언위치: 함수의 중간부분에서도 변수의 선언이 가능
```cpp
#include <iostream>

int main(void)
{
  int val1;
  std::cout<<"첫 번째 숫자 입력: ";
  std::cin>>val1;
  int val2; // 변수의 선언 위치에 제한X
  std::cout<<"두 번쨰 숫자 입력: ";
  std::cin>>val2;
  int result=val1+val2;
  std::cout<<"덧셈 결과: "<<result<<std::endl;
  return 0;
}
```
- 출력결과
```
첫 번째 숫자 입력: 3
두 번째 숫자 입력: 5
덧셈 결과: 8
```
- 출력에서와 마찬가지로 입력에서도 별도의 서식 지정이 불필요

# C++의 Local variable 선언
```cpp
#include <iostream>

int main(void)
{
	int val1, val2;
	int result=0;
	std::cout<<"두 개의 숫자입력: ";
	std::cin>>val1>>val2;

	if(val1<val2)
	{
		for(int i=val1+1; i<val2; i++)
			result+=i;
	}
	else
	{
		for(int i=val2+1; i<val1; i++)
			result+=i;
	}

	std::cout<<"두 수 사이의 정수 합: "<<result<<std::endl;
	return 0;
}
```
- 출력결과
```
두 개의 숫자입력: 3 7
두 수 사이의 정수 합: 15
```
- `std::cin`을 통해서 입력되는 데이터의 구분은 스페이스 바, 엔터, 탭과 같은 공백을 통해서 이뤄짐

# 배열 기반의 문자열 입출력
```cpp
#include <iostream>

int main(void)
{
	char name[100];
	char lang[200];

	std::cout<<"이름은 무엇입니까? ";
	std::cin>>name;

	std::cout<<"좋아하는 프로그래밍 언어는 무엇인가요? ";
	std::cin>>lang;

	std::cout<<"내 이름은 "<<name<<"입니다.\n";
	std::cout<<"제일 좋아하는 언어는 "<<lang<<"입니다."<<std::endl;
	return 0;
}
```
- 출력결과
```
이름은 무엇입니까? Yoon
좋아하는 프로그래밍 언어는 무엇인가요? C++
내 이름은 Yoon입니다.
제일 좋아하는 언어는 C++입니다.
```