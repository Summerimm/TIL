# Bootstrap
## CDN
- Content Delivery(Distribuition) Network
  - 컨텐츠(CSS, JS, Image, Text 등)를 효율적으로 전달하기 위해 여러 노드를 가진 네트워크에서 데이터를 제공하는 시스템
  - 개별 end-user의 가까운 서버를 통해 빠르게 전달 가능(지리적 이점)
  - 외부 서버를 활용함으로써 본인 서버의 부하 &darr;

### Spacing
![image](https://user-images.githubusercontent.com/108309396/224209085-418bdcf8-fd29-4bad-8388-c9b9ecd7c8c0.png)
![image](https://user-images.githubusercontent.com/108309396/224210143-22f8ce42-8d07-4e83-a2b7-6c2f8c4e2648.png)  
- 단위
  - `px`
  - `%`
  - `vw`: view port &rarr; 50vw = 50%
  - `rem`: HTML 폰트 사이즈 비례(default 16px) &rarr; 10rem = 160px

### Color
![image](https://user-images.githubusercontent.com/108309396/224209279-6b017529-b464-455a-a2e6-1b3d9612cc21.png)  
![image](https://user-images.githubusercontent.com/108309396/224210316-ec985732-8999-4a00-a070-19c8954e26c3.png)  

### Text
![image](https://user-images.githubusercontent.com/108309396/224210366-b7238019-90e1-4752-8787-da2e7efd1139.png)  
```css
@font-face {
  font-family: '짱이쁜 폰트';
  src: url();
}
```

### Display
![image](https://user-images.githubusercontent.com/108309396/224210447-78a8b728-8fee-4453-8202-f13308537656.png)  
![image](https://user-images.githubusercontent.com/108309396/224210455-cf0548d7-8c7b-4dd3-8795-81a644db3054.png)  

### Flexbox
![image](https://user-images.githubusercontent.com/108309396/224210496-8b9e6e4b-2b20-4b41-8510-a960477bdcb5.png)

## 반응형 웹(Responsive Web)
- 같은 컨텐츠를 보는 각기 다른 디바이스

## Bootstrap Grid System
- CSS가 아닌 편집 디자인에서 나온 개념으로 구성 요소를 잘 배치해서 시각적을 좋은 결과물을 만들기 위함
- 기본적으로 안쪽에 있는 요소들의 오와 열을 맞추는 것에서 기인
- 정보 구조와 배열을 체계적으로 작성하여 정보의 질서를 부여하는 시스템
- 기본 요소
  - Column: 실제 컨텐츠를 포함하는 부분 &rarr; 12개(약수가 많기 때문)
  - Gutter: 칼럼과 칼럼 사이의 공간(사이 간격)
  - Container: Column들을 담고 있는 공간
- Bootstrap Grid system은 flexbox로 제작됨
- container, rows, column으로 컨텐츠를 배치하고 정렬
- 12개의 column, 6개의 grid breakpoints  
![image](https://user-images.githubusercontent.com/108309396/224259527-eca700bb-3982-4d19-96bd-da31c00d0478.png)  
![image](https://user-images.githubusercontent.com/108309396/224259599-8911878d-f427-4b99-9a4a-86b49b8cd1d9.png)  