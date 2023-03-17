# CSS Basic
> ### [CSS 원칙]
> 1. 모든 요소는 box model, 좌측 상단에 배치  
> 2. display에 따라 크기와 배치가 달라짐  
> 3. position을 기준으로 위치의 기준을 변경  


## CSS Box model
- **모든 HTML element는 box model이다**
- 위에서 아래로, 왼쪽에서 오른쪽으로 쌓임  
![1](https://user-images.githubusercontent.com/108309396/223601980-8425cfab-0140-4552-8b84-fb9f5e7ad4a0.png)  

### Box model 구성
- 하나의 박스는 네 영역으로 이루어짐
  - content
  - padding
  - border
  - margin  
![2](https://user-images.githubusercontent.com/108309396/223601985-7c6c6c0e-cd48-42ee-ba97-76f163179bd0.png)  

### Box-sizing
- 기본적으로 모든 요소의 box-sizing은 content-box
  - padding을 제외한 순수 contents 영역만을 box로 지정
- 다만, 우리가 일반적으로 영역을 볼 때는 border까지의 너비를 지정하길 원함
  - 이 경우 box-sizing을 border-box로 설정  
![3](https://user-images.githubusercontent.com/108309396/223601989-ddba23ba-e208-4c55-8254-495da073478e.png)  

## CSS Display
- **display에 따라 크기와 배치가 달라진다.**
- `display: block`
  - 줄바꿈이 일어나는 요소(다른 element를 밀어냄)
  - 화면 크기 전체의 가로 폭을 차지
  - 블록 레벨 요소 안에 인라인 레벨 요소가 들어갈 수 있음
  - ex. div/ul, ol, li/hr/form 등
- `display: inline`
  - 줄바꿈이 일어나지 않는 행의 일부 요소
  - content를 마크업하고 있는 만큼만 가로폭을 차지
  - width, height, margin-top, margin-bottom 지정 불가
  - ex. span/a/img/input, label/b, em, i, strong 등
  - 상하 여백은 line-height로 지정
- `display: inline-block`
  - block과 inline 레벨 요소의 특징을 모두 가짐
  - inline처럼 한 줄에 표시 가능하고, block처럼 width, height, margin 속성 지정 가능
- `display: none`
  - 해당 요소를 화면에 표시하지 않고 공간조차 부여X
  - 이와 비슷한 `visibility: hidden`은 해당 요소가 공간은 차지하나 화면에 표시X

## CSS Position
- **position으로 위치의 기준을 변경할 수 있다.**
- 문서 상에서 요소의 위치를 지정(어떤 기준으로 어디에 배치시킬지)
- `position: static`
  - 모든 태그의 기본 값(기준 위치)
  - normal flow를 따르고 부모 요소 내에서 배치될 때는 부모 요소의 위치를 기준으로 배치
- `position: relative`: 상대 위치
  - 자기 자신의 static 위치를 기준으로 이동(normal flow 유지)
  - **레이아웃에서 요소가 차지하는 공간은 static일 때와 같음**
- `position: absolute`: 절대 위치
  - 요소를 normal flow에서 제거 후 레이아웃에 공간 차지X
  - static이 아닌 가장 가까운 부모/조상 element를 기준으로 이동(없는 경우 body)
- `position: fixed`: 고정 위치
  - 요소를 normal flow에서 제거 후 레이아웃에 공간 차지X
  - 부모 요소와 관계없이 **viewport를 기준으로** 이동(스크롤 시에도 항상 같은 곳에 위치)
- `position: sticky`: **스크롤에 따라** static &rarr; fixed로 변경
  - 스크롤 위치가 임계점에 이르면 `position: fixed`와 같이 박스를 화면에 고정

![hw](https://user-images.githubusercontent.com/108309396/223601991-8551d44c-33e5-4c92-98cb-a7a015d557f0.png)

