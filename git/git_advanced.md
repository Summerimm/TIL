# Git undoing
- Git 작업 되돌리기
  - Working Directory 작업 단계
  - Staging Area 작업 단계
    - Staging Area에 반영된 파일을 Working Directory로 되돌리기
    - `git rm --cached`
    - `git restore --staged`
  - Repository 작업 단계
    - 커밋을 완료한 파일을 Staging Area로 되돌리기
    - `git commit --amend` 


## Working Directory 작업 단계 되돌리기
![image](https://user-images.githubusercontent.com/108309396/230521830-ce6aee33-b53a-4874-abc9-ae10ba3c046b.png)  
![image](https://user-images.githubusercontent.com/108309396/230521855-30f82e5c-6f8f-484b-bdff-2ea242c7b56d.png)
- Working Directory에서 수정한 파일 내용을 이전 커밋 상태로 되돌리기
    - `git restore {파일 이름}`
    - `git restore`를 통해 되돌리면 해당 내용 복원 불가

## Staging Area 작업 단계 되돌리기
- Staging Area에 반영된 파일을 Working Directory로 되돌리기(== Unstage)
- root-commit이 없는 경우: `git rm --cached {파일 이름}`
  - Git 저장소가 만들어지고 한 번도 커밋을 안 한 경우
![image](https://user-images.githubusercontent.com/108309396/230522145-da36036e-0231-47ba-a31e-b5e59653eceb.png)    
![image](https://user-images.githubusercontent.com/108309396/230522165-64bf5167-e608-4da8-bf44-2e1438a51c9e.png)

- root-commit이 있는 경우: `git restore --staged {파일 이름}`
  - Git 저장소에 한 개 이상의 커밋이 있는 경우
![image](https://user-images.githubusercontent.com/108309396/230522294-b45641f5-09c3-4cd4-8fcc-d6453e4e0037.png)  
![image](https://user-images.githubusercontent.com/108309396/230522311-f662a5d2-6d5e-44ab-8d99-18355a05b70b.png)

## Repository 작업 단계 되돌리기
- 커밋 완료한 파일을 Staging Area로 되돌리기
  1. Staging Area에 새로 올라온 내용이 없다면, **직전 커밋의 메시지만 수정**
![image](https://user-images.githubusercontent.com/108309396/230522570-d22123c2-9ca6-4b81-af90-1c4d4e476091.png)  
![image](https://user-images.githubusercontent.com/108309396/230522590-f2213e89-1874-4288-bf56-78276a66d990.png)  
![image](https://user-images.githubusercontent.com/108309396/230522635-8f09883d-0b95-4230-ae70-62991ddbd949.png)

  2. Staging Area에 새로 올라온 내용이 있다면, **직전 커밋을 덮어쓰기**
![image](https://user-images.githubusercontent.com/108309396/230522677-fb9e8928-cee3-4f46-b870-1fd564f594f5.png)  
![image](https://user-images.githubusercontent.com/108309396/230522689-780dbb71-d6e9-43c4-ae76-7aef1c4208a8.png)  
![image](https://user-images.githubusercontent.com/108309396/230522733-29ab6628-5fc8-430b-aa24-14409dc952ea.png)
- amend(수정하다) 즉, 이전 커밋을 수정해서 새 커밋으로 남김
- 커밋 내용을 수정하거나 수정 사항을 새로 커밋에 추가하고 싶을 때 사용
- 수정 사항을 반영하기 위해 새로운 커밋을 생성하지 않아도 됨

# Git reset
![image](https://user-images.githubusercontent.com/108309396/230523461-e9292e2d-3e3f-49ad-ad3e-31a28142ffe6.png)  
- 프로젝트를 특정 커밋(버전) 상태로 되돌림
- 특정 커밋으로 되돌아 갔을 때, **해당 커밋 이후로 쌓았던 커밋들은 전부 사라짐**
- `git reset [옵션] {커밋 ID}`
  - 옵션은 `soft, mixed, hard` 중 하나를 작성
  - 커밋 ID는 되돌아가고 싶은 시점의 커밋ID를 작성

## `git reset`의 옵션
![image](https://user-images.githubusercontent.com/108309396/230523098-2ac841f5-b2c4-447a-b397-0a3d6c25a531.png)  
- `--soft`
  - 해당 커밋으로 되돌아가고 되돌아간 커밋 이후의 파일들은 Staging Area로 돌려놓음
- `--mixed`
  - 해당 커밋으로 되돌아가고 되돌아간 커밋 이후의 파일들은 Working Directory로 돌려놓음
  - git reset 옵션의 기본값
- `--hard`
  - 해당 커밋으로 되돌아가고 되돌아간 커밋 이후의 파일들을 모두 Working Directory에서 삭제
  - 따라서 사용 시 주의
  - 기존의 Untracked 파일은 사라지지 않고 Untracked로 남아있음

## [참고] `git reflog`
- git reset의 hard 옵션은 Working Directory 내용까지 삭제하므로 위험할 수 있음
- `git reflog` 명령어 사용 시 reset 하기 전의 커밋 내역을 모두 조회 가능
- 이후 해당 커밋으로 reset하면 hard 옵션으로 삭제된 파일도 복구 가능

# Git revert
![image](https://user-images.githubusercontent.com/108309396/230523414-06e12517-8ea0-45b5-8eb0-ddafdbebe904.png)  
- 과거를 없었던 일로 만드는 행위, 이전 커밋을 취소한다는 새로운 커밋을 생성함
- `git revert {커밋 ID}`
  - 커밋 ID는 취소하고 싶은 커밋 ID를 작성

## `git reset`과의 차이점
- 개념적 차이
  - `reset`은 커밋 내역을 삭제하는 반면, `revert`는 새로운 커밋을 생성함
- 문법적 차이
  - `git reset 5sd2f42`라고 작성하면 5sd2f42라는 커밋으로 되돌린다는 뜻
  - `git rever 5sd2f42`라고 작성하면 5sd2f42라는 커밋 한 개를 취소한다는 뜻(커밋이 취소되었다는 내용의 새로운 커밋을 생성함)

# Git branch
- 브랜치(Branch)는 나뭇가지라는 뜻으로, 여러 갈래로 작업 공간을 나누어 **독립적으로 작업**할 수 있도록 도와주는 Git의 도구  
![image](https://user-images.githubusercontent.com/108309396/230515267-7807e5f9-96e7-4a37-ad97-e713e058fa30.png)
- 장점
  - 브랜치는 **독립 공간을 형성**하기 때문에 원본(master)에 대해 안전함
  - 하나의 작업은 하나의 브랜치로 나누어 진행되므로 **체계적인 개발이 가능**함
  - Git은 브랜치를 만드는 속도가 굉장히 빠르고, 적은 용량을 소모함

## Git branch 명령어
### `git branch`
- 조회
  - `git branch`: 로컬 저장소의 브랜치 목록 확인
  - `git branch -r`: 원격 저장소의 브랜치 목록 확인
- 생성
  - `git branch {branch 이름}`: 새로운 브랜치 생성
  - `git branch {branch 이름} {commit ID}`: 특정 커밋 기준으로 브랜치 생성
- 삭제
  - `git branch -d {branch 이름}`: 병합된 브랜치만 삭제 가능
  - `git branch -D {branch 이름}`: 강제 삭제

### `git log`
- `git log --al`l
	- 모든 브랜치의 깃 로그 확인
- `git log --graph`
	- 깃 로그를 그림으로 확인
- `git log --oneline --all --graph`
	- 모든 브랜치의 깃 로그를 / 한줄로 / 그림으로 확인(명령어들의 조합)

### `git switch`
- 이동
  - `git switch {branch 이름}`: 다른 브랜치로 이동
  - `git switch -c {branch 이름}`: 브랜치를 만들면서 이동
	- `git switch -c {branch 이름} {commit ID}`: 특정 커밋 기준으로 브랜치 생성 및 이동
- **switch하기 전에, 해당 브랜치의 변경 사항을 반드시 커밋 해야함을 주의할 것**
  - 다른 브랜치에서 파일을 만들고 커밋하지 않은 상태에서 switch를 하면 브랜치를 이동했음에도 불구하고 해당 파일이 그대로 남아있음

# Git merge
- 분기된 브랜치들을 하나로 합치는 명령어
- master 브랜치가 상용이므로, 주로 master 브랜치에 병합
- `git merge {합칠 브랜치 이름}`
  - 병합하기 전에 브랜치를 합치려고 하는, 즉 메인 브랜치로 switch해야함

## 1. Fast-Forward
- 빨리감기처럼 브랜치가 가리키는 커밋을 앞으로 이동시키는 방법  
![image](https://user-images.githubusercontent.com/108309396/230530430-d877b3a5-16fc-4aa4-9a04-d55b05155e71.png)  
![image](https://user-images.githubusercontent.com/108309396/230530701-d9ae3971-5ca1-48a5-9362-a139391bd8d3.png)

## 2. 3-way Merge
- 각 브랜치의 커밋 두 개와 공통 조상 하나를 사용하여 병합하는 방법  
![image](https://user-images.githubusercontent.com/108309396/230530822-eede8869-6a18-40bc-8c4e-5a17d47e9724.png)  
![image](https://user-images.githubusercontent.com/108309396/230530861-3f822e62-48a6-4851-9988-18ce40557d1a.png)  

## 3. Merge Conflict
- 두 브랜치에서 같은 부분을 수정한 경우, Git이 어느 브랜치의 내용으로 작성해야 하는지 판단하지 못 하기 때문에 Conflict 발생
- 보통 **같은 파일의 같은 부분**을 수정했을 때 자주 발생    
![image](https://user-images.githubusercontent.com/108309396/230531295-e5345e9b-e4f5-4054-895c-6590bc4b3e0f.png)
- 충돌이 발생한 부분은 작성자가 직접 해결
![image](https://user-images.githubusercontent.com/108309396/230531142-34f66333-5233-4731-8bc2-0154a9dfa4d8.png)
- 충돌 해결 후, 병합된 내용을 기록한 Merge Commit 생성  
![image](https://user-images.githubusercontent.com/108309396/230531214-880203b5-01fe-424c-ab5e-9c22c00b134d.png)  
- 서로 다른 파일을 수정 후 병합하는 경우 &rarr; automerging  
![image](https://user-images.githubusercontent.com/108309396/230531249-548e7310-4736-415d-ac0d-61eaa95f340a.png)

# Git Workflow
- Branch와 원격 저장소를 이용해 협업을 하는 두 가지 방법
  - 원격 저장소 소유권O &rarr; Shared repository model
  - 원격 저장소 소유권X &rarr; Fork & Pull model

## Shared repository model
- 원격 저장소가 자신의 소유이거나 Collaborator로 등록되어 있는 경우
- master 브랜치에 직접 개발하는 것이 아니라, 기능 별로 브랜치를 따로 만들어 개발
- `Pull Request`를 사용하여 팀원 간 변경 내용에 대한 소통 진행

### 실습
1. 소유권이 있는 원격 저장소를 로컬 저장소로 clone 받기
2. 사용자는 자신이 작업할 기능에 대한 브랜치를 생성하고, 그 안에서 기능을 구현
3. 기능 구현이 완료되면, 원격 저장소에 해당 브랜치를 Push(`git push origin {브랜치 이름}`)
4. 원격 저장소에 각 기능의 브랜치가 반영됨
5. Pull Request를 통해 브랜치를 master에 반영해달라는 요청을 보냄
6. 병합이 필요한 브랜치는 원격 저장소에서 삭제
7. 원격 저장소에서 병합이 완료되면, 사용자는 로컬에서 master 브랜치로 switch
8. 병합으로 인해 변경된 원격 저장소의 master 내용을 로컬에 pull
9. 원격 저장소 master의 내용을 받았으므로, 기존 로컬 브랜치 삭제