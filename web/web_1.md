# Web
- 웹 사이트란 웹 브라우저를 통해서 접속하는 웹 페이지들의 모음
- 웹 페이지는 글, 그림, 동영상 등 여러 정보를 담고 있으며, 링크를 통해 다른 웹 페이지로 이동 가능
- 즉, 링크를 통해 여러 웹 페이지를 연결한 것이 웹 사이트

### 웹 페이지 구성요소
- `HTML`: 구조(레이아웃)
- \+ `CSS`: 표현(스타일링)
- \+ `JS`: 동작(인터렉션)

# HTML
- Hyper Text Markup Language
- `Hyper Text`: 참조(하이포링크)를 통해 사용자가 한 문서에서 다른 문서로 즉시 접근할 수 있는 텍스트
- Markup Language: 태그 등을 이용하여 문서나 데이터의 구조를 명시하는 언어(ex. HTML, Markdown)
&rarr; 웹 페이지를 작성(구조화)하기 위한 언어
- `.html`

## HTML 기본 구조
- `html`: 문서의 최상위(root) 요소
- `head`: 문서 메타데이터 요소
  - 문서 제목, 인코딩, 스타일, 외부 파일 로딩 등
  - 일반적으로 브라우저에 나타나지 않는 내용
- `body`: 문서 본문 요소
  - 실제 화면 구성과 관련된 내용

### head 예시
- `<title>`: 브라우저 상단 타이틀
- `<link>`: 외부 리소스 연결 요소(CSS 파일 등)
- `<style>`: CSS 직접 작성

### Element
![1](https://user-images.githubusercontent.com/108309396/223295939-4ca44c91-b060-4f1a-b330-27646344c86e.png)  
- 여는 태그, 닫는 태그
- HTML의 요소는 태그와 내용(contents)으로 구성되어 있다.
- 열었으면, 닫아야 하고, 모든 내용은 태그로 감싸져 있다.
- 내용이 없는 태그들: br, hr, img, input, link, meta
- 요소는 중첩(nested)될 수 있음
  - 요소의 중첩을 통해 하나의 문서를 구조화
  - 여는 태그와 닫는 태그의 쌍을 잘 확인
    - 오류를 반환하는 것이 아닌 레이아웃이 깨진 상태로 출력되기 때문에, 디버깅이 힘들어질 수 있음

### Attribute
![2](https://user-images.githubusercontent.com/108309396/223295941-d697ceae-d469-4546-a5cf-e8210d88ee12.png)  
- 각 태그별로 사용할 수 있는 속성이 다르다.
- 속성은 속성명과 속성값으로 이루어져 있다.
- 속성을 통해 태그의 부가적인 정보(기능)을 설정할 수 있음
- 요소는 속성을 가질 수 있으며, 경로나 크기와 같은 추가적인 정보를 제공
- 요소의 시작 태그에 작성하며 보통 이름과 값이 하나의 쌍으로 존재
- 태그와 상관없이 사용하능한 속성(HTML Global Attribute)들도 있음

### HTML Global Attribute
- 모든 HTML 요소가 공통으로 사용할 수 있는 대표적인 속성. but 몇몇 요소에는 아무 효과가 없을 수 있음
  - `id`: 문서 전체에서 유일한 고유 식별자 지정
  - `class`: 공백으로 구분된 해당 요소의 클래스 목록(CSS, JS에서 요소 선택하거나 접근)
  - `style`: inline 스타일
  `<!-- 이것은 주석입니다. -->`: 주석
  - `<a href='https://naver.com">네이버로 이동!!</a>`: `<a></a>`-앵커, 네이버로 이동이라는 글씨를 누르면 네이버 웹사이트로 이동

## HTML 문서 구조화
- 텍스트 요소
![3](https://user-images.githubusercontent.com/108309396/223295944-71e9a239-df2b-49d4-97ea-92eaec2358bb.png)  
![4](https://user-images.githubusercontent.com/108309396/223295945-90ea3b9e-cd8a-4f24-a80c-ed8e878ef9fa.png)   
- 그룹 컨텐츠
![5](https://user-images.githubusercontent.com/108309396/223295919-f0e84fdc-cbe7-4154-a164-5ac2032beb0e.png) 
![6](https://user-images.githubusercontent.com/108309396/223295923-93dc26f7-098e-42ff-8de4-f03d6e127a4d.png)   
- `form`: `<form>`은 사용자의 정보(데이터)를 제출하기 위한 영역
  - 기본 속성
    - `action`: form을 처리할 서버의 URL
    - `method`: form을 제출할 때 사용할 HTTP 메서드(GET or POST)
- `input`: 다양한 타입을 가지는 입력 데이터 유형과 위젯이 제공됨
  - 기본 속성
    - `name`: form control에 적용되는 이름(이름/값 페어로 전송됨)
    - `value`: form control에 적용되는 값(이름/값 페어로 전송됨)
    - required, readonly, autofocus, autocomplete, disabled 등
- `input label`
  - label을 클릭하여 input 자체의 초점을 맞추거나 활성화 가능
    - 사용자는 선택할 수 있는 영역 &uarr; 편하게 사용 가능
    - label과 input 입력의 관계가 시각적 뿐만 아니라 화면 리더기에서도 label을 읽어 쉽게 내용확인 가능
  - **\<input>에 id 속성을, \<label>에는 for 속성**을 활용하여 상호연관을 시킴
- input 유형 - 일반
![7](https://user-images.githubusercontent.com/108309396/223295927-cda336d5-238e-43c2-812f-4e039c848d63.png)    
- input 유형 - 항목 중 선택
![8](https://user-images.githubusercontent.com/108309396/223295933-62a09cd0-a9b5-498c-94aa-034cc9e86131.png)  

# CSS
- Cascading Style Sheets
- 스타일을 지정하기 위한 언어
![9](https://user-images.githubusercontent.com/108309396/223295934-0c69253f-47a3-471b-8140-0bd240f98a72.png)  
- 선택자를 통해 스타일을 지정할 HTML 요소를 선택
- **중괄호 안에서는 속성과 값**, 하나의 쌍으로 이루어진 선언을 진행
- 각 쌍은 선택한 요소의 속성, 속성에 부여할 값을 의미
  - property: 어떤 스타일 기능을 변경할지
  - value: 어떻게 스타일 기능을 변경할지
- CSS 정의 방법
  - inline(인라인)
![10](https://user-images.githubusercontent.com/108309396/223295935-b57a0e81-2804-4673-9577-5a7b45855e94.png)  
  - embedding(내부 참조) - `<style>`
![11](https://user-images.githubusercontent.com/108309396/223295936-4b1ed589-87ad-4ace-bf1d-1d1a96c05c9d.png)  
  - link file(외부 참조) - 분리된 CSS 파일
![12](https://user-images.githubusercontent.com/108309396/223295938-73035f12-36c7-43ed-83bf-9a8df54ee6d8.png)  

### CSS Selectors
- Selector 유형
- 기본 선택자
  - 전체 선택자(`*`), 요소(`tag`) 선택자
  - 클래스(`.class_name`) 선택자, 아이디(`#id_name`) 선택자, 속성(`attr`) 선택자
  - id selector는 단일 사용, class selector는 다중 사용 가능
- 결합자(Combinators)
  - 자손 결합자(`.class_name > child_tag`)-자식 에게만 적용, 자식 결합자(`.class_name child_tag`)-모든 자손에 적용

### CSS 적용 우선순위(cascading order)
1. 중요도(Importance)-사용 시 주의
- `!important`: 우선순위를 모두 무시하고 우선적용
2. 우선순위(Specificity)
- `인라인 > id > class, 속성 > 요소`

### CSS 상속
- CSS는 상속을 통해 부모 요소의 속성을 자식에게 상속
  - 속성 중에는 상속이 되는 것과 되지 않는 것들이 있다.