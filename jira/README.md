# Jira 및 JQL 활용
## Jira의 목적
1. Issue Tracking
2. Project Management
3. Agile: Scrum vs Kanban
4. DevOps
   - 반복적인 작업들을 Tool을 이용해서 자동화
   - 팀원 모두가 알고 있는 하나의 공유된 지표가 필요
   - 장애나 이슈가 있을 때 혼자만 알지 말고 팀원들과 공유 필요 
5. SRE(Site Reliability Engineering)

## Jira SaaS 버전
1. Create Issue
2. Issue Type
   - Task: General(애매한 것)
   - Story: User story
   - Bug
   - Epic: 모든 일을 묶은 큰 개념
3. Component: 조직, 모듈 - 리더 지정 시 담당자로 지정되고 담당자가 분배 가능
4. Reporter: 이슈를 제기한 사람
5. Linked Issues: 연관되는 이슈
6. Fix versions: 이슈를 해결할 버전
7. Affects versions: 지금 이 버그가 어떤 버전에서 발생했는지
8. Assignee: 담당자
9. Priority: 해당 이슈의 우선순위
10. Labels: 해시태그, 대소문자가 다르면 다른 라벨로 인식됨
11. Epic Link: 어떤 에픽에 해당되는지
12. Sprint 지정가능

## JQL
- Jira Query Language
- Jira Issue를 구조적으로 검색하기 위해 제공하는 언어
- 쌓인 Issue들을 재가공해 유의미한 데이터를 도출해내는데 활용(Gadget, Agile Board 등)

## JQL Operators
- `=, !=, >, >=`
- `in, not in`
- `~(contains), !~(not contains)`
- `is empty, is not empty, is null, is not null`

## JQL Keywords
- `AND, OR, NOT, EMPTY, NULL, ORDER BY`

## JQL Dates
- Relative Dates
- Past: `-2w, -1w, -6d, ...-1d`
- Future: `1d, 2d, ...6d, 1w, 2w..`

## JQL Functions
- `endOfDay(), startOfDay()`
- `endOfWeek() (Saturday), startOfWeek() (Sunday)`
- `endOfMonth(), startOfMonth(), endOfYear(), startOfYear()`
- `currentUser()`

## Workflow
- Ticket이 생성되고 완료될 때까지의 상태 변화
- 프로젝트 진행상황을 한 눈에 파악 가능
- 불필요한 커뮤니케이션 감소
- ![image](https://github.com/Haaarimmm/TIL/assets/108309396/1b4b44b9-64fa-4925-b2a3-69d5b879c9be)
- 프로젝트 설정 - 워크플로 - 텍스트 클릭 시 확인 가능
  - 팀에 일괄 반영이 됨

## Component
- 팀장 권한으로 등록 시 같은 태그 사용 가능
  - 담당자(PL)

## 스윔레인
- 담당자 기준으로 해놓으면 편함

## 릴리스
- 빌드에 대한 버전 컨트롤
- 백로그에서 드래그를 통해 설정 가능

## Jira Convention
1. 매주 월요일 오전 스크럼 회의 이후 각자의 이슈 티켓을 생성한다.
2. 이슈 생성 시 확인해야 할 부분
    - **컴포넌트**가 지정되어 있는지 (FE, BE, 공통 중 택1)
    - **Epic Link**가 지정되어 있는지 (설계, FE개발, BE개발, 회의, 학습)
    - 스프린트의 **총 Story Points가 40 이상**인지
3. 이슈 티켓 이름은 **[말머리] 구체적인 기능** 으로 적는다.
    - 개발 에픽에서 **[말머리]**는 기능 명세서의 대분류를 따른다.