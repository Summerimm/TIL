# Permutation
- 서로 다른 것들 중 몇 개를 뽑아서 한 줄로 나열하는 것
- 서로 다른 n개 중 r개를 택하는 순열 $nPr$

## 단순하게 순열을 생성하는 방법
![image](https://user-images.githubusercontent.com/108309396/227826518-d5b3157a-3fba-4880-95f4-834e8a4c6ae7.png)  
- 동일한 숫자가 포함되지 않았을 때, 각 자리 수 별로 loop 이용

## 최소 변경을 통한 방법(Minimum-exchange requirement) &rarr; Johnson-Trotter 알고리즘
![image](https://user-images.githubusercontent.com/108309396/227826756-3a4a8f4f-490c-4d54-b513-5ae9ed906d18.png)  
![image](https://user-images.githubusercontent.com/108309396/227826914-a80d0c7f-cccf-443a-a988-43f917479b6b.png)

## 재귀호출을 통한 순열 생성
![image](https://user-images.githubusercontent.com/108309396/227826971-808d589b-17cd-4d2d-b6ba-459fd195212f.png)  

## used 배열 사용
![image](https://user-images.githubusercontent.com/108309396/227828843-44a6e07a-2499-4703-91cd-97ae9f48c582.png)  
![image](https://user-images.githubusercontent.com/108309396/227828955-f45c0862-de02-404b-8f8f-51731c8dc28a.png)  
![image](https://user-images.githubusercontent.com/108309396/227829001-e18de9f9-86b8-4dda-95fa-3c110779e853.png)