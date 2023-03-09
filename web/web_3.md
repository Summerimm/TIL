# CSS Layout
# Float
- 박스를 왼쪽 혹은 오른쪽으로 이동시켜 텍스트를 포함 인라인요소들이 주변을 wrapping하도록 함
- 요소가 normal flow를 벗어나도록 함
- 최근 Flexbox, Grid 등장과 함께 사용도가 낮아짐
- `none`: 기본값
- `left`: 요소를 왼쪽으로 띄움
- `right`: 요소를 오른쪽으로 띄움

# Flexbox
![1](https://user-images.githubusercontent.com/108309396/223898603-898950ef-6e30-4c09-b8ab-6f6e3877cb23.png)  
- 행과 열 형태로 아이템들을 배치하는 1차원 레이아웃 모델
- 축
  - **Main axis(메인 축)**
  - **Cross axis(교차 축)**
- 구성 요소
  - Flex Container(부모 요소)
    - flexbox 레이아웃을 형성하는 가장 기본적인 모델
    - Flex Item들이 놓여있는 영역
    - display 속성을 flex 혹은 inline-flex로 지정
  - Flex Item(자식 요소)  
    - 컨테이너에 속해있는 컨텐츠(박스)
---
## Flex 속성
- 배치 설정
  - `flex-dirrection`
  - `flex-wrap`
- 공간 나누기
  - `justify-content` (main axis)
  - `align-content` (cross axis)
- 정렬
  - `align-items` (모든 아이템을 cross axis 기준으로)
  - `align-self` (개별 아이템)
- 기타 속성
  - `flex-grow`: 남은 영역을 아이템에 분배
  - `order`: 배치 순서  
![8](https://user-images.githubusercontent.com/108309396/223902001-ed9f2095-f276-4854-81cd-a9f785780335.png)  

---
## 배치 설정
1. `flex-direction`
- Main axis 기준으로 방향 설정
- 역방향의 경우 HTML 태그 선언 순서와 시각적으로 다르니 주의  
![2](https://user-images.githubusercontent.com/108309396/223901991-9f22e9f9-4a7e-406d-bbbe-b143caa66b41.png)  
2. `flex-wrap`
- 아이템이 컨테이너를 벗어나는 경우 해당 영역 내에 배치되도록 설정
- 즉, 기본적으로 컨테이너 영역을 벗어나지 않도록 함  
![3](https://user-images.githubusercontent.com/108309396/223901992-a82ec949-8ba6-4fc0-85df-a8231b77ca80.png)
3. 정리
- `flex-direction`: Main axis의 방향을 설정
- `flex-wrap`: 요소들이 강제로 한 줄에 배치되게 할 것인지 설정
  - `nowrap`(기본값): 한 줄에 배치
  - `wrap`: 넘치면 그 다음 줄로 배치
- `flex-flow`
  - flex-direction과 flex-wrap의 shorthand, 설정값을 차례로 작성
  - ex) flex-flow: row nowrap;
---
## 공간 나누기
1. `justify-content`
- Main axis 기준으로 공간 배분  
![4](https://user-images.githubusercontent.com/108309396/223901993-e9b84a32-5fb7-4429-b6be-0623a6bd7e28.png)  
2. `align-content`
- Cross axis를 기준으로 공간 배분(아이템이 한 줄로 배치되는 경우 확인 불가)  
![5](https://user-images.githubusercontent.com/108309396/223901994-459e4b04-c0de-48dc-818a-e54baf728e73.png)  
3. 정리
- `flex-start`: 아이템들을 axis 시작점으로
- `flex-end`: 아이템들을 axis 끝 쪽으로
- `center`: 아이템들을 axis 중앙으로
- `space-between`: 아이템 사이의 간격을 균일하게 분배
- `space-around`: 아이템을 둘러싼 영역을 균일하게 분배(가질 수 있는 영역을 반으로 나눠서 양쪽에)
- `space-evenly`: 전체 영역에서 아이템 간 간격을 균일하게 분배
---
## 정렬
1. `align-items`
- 모든 아이템을 Cross axis를 기준으로 정렬  
![6](https://user-images.githubusercontent.com/108309396/223901997-b800e231-94b3-453e-aeb1-e56b1ec70d64.png)
2. `align-self`
- 개별 아이템을 Cross axis 기준으로 정렬
- 해당 속성은 컨테이너에 적용X, **개별 아이템에 적용**  
![7](https://user-images.githubusercontent.com/108309396/223902000-77331ee8-57a9-4edc-9d46-7ffee497b522.png)  
