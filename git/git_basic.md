# Git Basic
## [ Initialization ]
- `git init`
	- Create Git repository
	- git으로 관리된다는 의미(working directory)
- `.gitignore` => **git init**하자마자 생성
  - secret.txt 등 commit하면 안 되는 것은 `.gitignore` 메모장에 복사+붙여넣기
  - gitignore.io에서 운영체제, 언어, 에디터 선택 후 생성
  - `git push`를 몇 번 한 상태에서 `git init`을 하게 되면 이전에 올라가있는 ignore되어야 할 파일들은 여전히 삭제해도 git 관리가 됨
    - git repository를 새로 팔 수 밖에 없을 듯  
![image](https://user-images.githubusercontent.com/108309396/230531827-9e05b781-d569-4e5d-9e57-8ec4175376ed.png)

---
## [ Add & Commit ]
- `git add {파일 이름}`
	- staging area에 추가
	- `git add .` 사용 시 전체를 add
- `git commit -m '{message}'`
	- 커밋(기록) 남기기
---
## [ Log ]
- `git status`
	- 상태 확인
- `git log`
	- 커밋 확인
	- `git log --oneline` => 한 커밋 당 한 줄로 출력
  - `git log --oneline -3` => 가장 최근 3줄만 출력
  - `git log --oneline --graph` => 그래프 형식으로 branch까지 보여줌
---
## [ Push ]
- `git remote add origin {url}`
	- 원격 연결(origin = url)
- `git push origin master`
	- 업로드
	- `git push -u origin master` => configure default (git push만 해도 동작)
---
## [ Configuration ]
- `git config --global user.name {name}`
- `git config --global user.email {email}`  
---
## [ Clone & Pull ]
- **`git clone {url} .`**
  - 깃허브에 있는 깃 새로 가져오기 => 해당 위치에 바로 clone
  - .생략 시 레포이름으로 clone 하위 폴더가 생성 
- `git pull origin master`
  - 이미 연결된 상태에서 당겨오기
  - `git pull -u origin master` => configure default (git pull만 해도 동작)
- `git commit --amend`
  - 커밋 수정
  - vim 에디터가 나옴
    - i => 에디터 모드
    - esc => 모드 나가기
    - :wq => 저장 후 나가기
    - :q! => 강제종료
---
## [ Merging ]
- "`github`" / "`git_all/git_home`" / "`git_all/git_cafe`" 동시에 수정하는 상황
  1. home에는 home1.txt, cafe에는 cafe1.txt 저장 후 각각 push   
  => vim editor가 뜨면서 Merge branch로 automerging됨
  1. home과 cafe 두 곳에서 abc.txt를 각각 수정 후 `git push`   
  => 동일한 파일에 접근했기 때문에 **![rejected]** 발생   
	=> `git pull` => **Conflict** 발생   
	=> VScode를 열어서 abc.txt를 merging(Conflict fixing)
	=> 저장 후 add, commit, push

---
## [ etc ]
- `git reset --hard`
  - 깃 커밋 되돌리기
    - 스켈레톤 코드 사용할 경우만 사용하기
  - --hard: 폴더, staging, commit 모두 reset
  - --mixed: staging, commit만 reset
  - --soft: commit만 reset
  - reset 이후엔 clone/pull
- `revert`: 없었던 것으로 commit 남김 
- `git reflog`
  - 로컬에서 깃 커밋 변경이력 모두 보여줌 
- `git pull` 받은 상태에서 파일을 잘라내기하게 되면 변경이력이 생김. 웬만하면 복사 붙여넣기 해야함
  - 이럴 경우 `git restore`하게 되면 `git pull`같은 상태로 복구 가능(잘라내기한 파일도 남아있음)