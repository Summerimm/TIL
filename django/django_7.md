### 인증과 권한 - 회원가입/회원탈퇴/회원정보 수정/비밀번호 변경
# 회원가입
- 회원가입은 User를 Create하는 것
- `UserCreationForm` built-in form을 사용

### `UserCreationForm`
- 주어진 Username과 password로 권한이 없는 새 user를 생성하는 ModelForm
- 3개의 필드를 가짐
  - username(from the user model)
  - password1
  - password2

### 1. 회원가입 페이지 작성
<img width="948" alt="image" src="https://user-images.githubusercontent.com/108309396/227785821-ee809384-10bc-4bdb-a8ae-3f8debda27ee.png">

### 2. 회원가입 링크 작성
<img width="499" alt="image" src="https://user-images.githubusercontent.com/108309396/227785900-038cf219-89bd-431a-9bf0-a30c14625e83.png">

### 3. 회원가입 로직 작성
<img width="563" alt="image" src="https://user-images.githubusercontent.com/108309396/227785934-4460fd6c-c241-4fda-8599-cffaadf5b8f6.png">

&rarr; 순서대로 진행 시 회원가입 진행 후 에러 발생: UserCreationForm이 기존 유저 모델로 작성된 클래스이기 때문

### Custom user & Built-in auth forms
- AbstractBaseUser의 모든 subclass와 호환되는 forms
1. `AuthenticationForm`
2. `SetPasswordForm`
3. `PasswordChangeForm`
4. `AdminPasswordChangeForm`  
&rarr; 기존 User 모델을 참조하는 form이 아니기 때문
- 커스텀 유저 모델을 사용하려면 다시 작성하거나 확장해야하는 forms
1. `UserCreationForm`
2. `UserChangeForm`  
&rarr; `class Meta: model = User`가 등록된 form이기 때문에 반드시 커스텀해야 함

### 4. UserCreationForm() 커스텀하기
<img width="667" alt="image" src="https://user-images.githubusercontent.com/108309396/227786210-ddb5ce89-3cf2-4a8c-b00e-ffdce5899898.png">

### `get_user_model()`
- 현재 프로젝트에서 active user model을 반환
- 직접 참조하지 않는 이유: User model을 커스텀한 상황에서는 커스텀 User 모델을 반환해주기 때문

### 5. CustomUserCreationForm()으로 대체하기
<img width="566" alt="image" src="https://user-images.githubusercontent.com/108309396/227786329-97d07bd1-95b0-4c4a-8f27-68f0e7c74c63.png">

### 6. 회원가입 후 곧바로 로그인 진행
<img width="585" alt="image" src="https://user-images.githubusercontent.com/108309396/227786374-c25596d0-dcdf-437f-9fd7-80504f470bc7.png">

# 회원탈퇴
- 회원탈퇴는 DB에서 유저를 Delete하는 것

### 1. 회원탈퇴 로직 작성
<img width="909" alt="image" src="https://user-images.githubusercontent.com/108309396/227786485-efa86567-ba8c-411f-a1cb-a66d5fbbde22.png">

### [참고] 탈퇴하면서 해당 유저의 세션 정보도 함께 지우고 싶은 경우
- 탈퇴(1) 후 로그아웃(2)의 순서가 바뀌면 안 됨
- 먼저 로그아웃해버리면 해당 요청 객체 정보가 없어지기 때문에 탈퇴에 필요한 정보 또한 없어지기 때문  
<img width="482" alt="image" src="https://user-images.githubusercontent.com/108309396/227786631-657a8d84-850f-4a72-8a98-48a0916fcc40.png">

# 회원정보 수정
- 회원정보 수정은 User를 Update하는 것
- `UserChangeForm` built-in form을 사용

### `UserChangeForm`
- 사용자의 정보 및 권한을 변경하기 위해 admin 인터페이스에서 사용되는 ModelForm
- UserChangeForm 또한 ModelForm이기 때문에 instance 인자로 기존 user data를 받는 구조 또한 동일
- 이미 앞에서 Custom 진행했기 때문에 `CustomUserChangeForm`사용

### 1. 회원정보 수정 페이지 작성
<img width="929" alt="image" src="https://user-images.githubusercontent.com/108309396/227786834-dd4ad578-b6e8-4d39-afe2-e87d155624b1.png">

### 2. 회원정보 수정 페이지 링크 작성
<img width="581" alt="image" src="https://user-images.githubusercontent.com/108309396/227787011-be0158e5-94f0-4f89-8cb1-839689fcebb8.png">

### `UserChangeForm` 사용 시 문제점
- 일반 사용자가 접근해서는 안 되는 fields들까지 모두 수정이 가능해짐
  - admin interface에서 사용되는 ModelForm이기 때문
- 따라서 `CustomUserChangeForm`에서 접근 가능한 필드를 조정해야 함

### 3. `CustomUserChangeForm` fields overriding  
<img width="396" alt="image" src="https://user-images.githubusercontent.com/108309396/227787293-7b665b08-82c1-4ef1-8269-e0526116e889.png">

### 4. 회원정보 수정 로직 작성
<img width="657" alt="image" src="https://user-images.githubusercontent.com/108309396/227787342-8fe5a7c3-86a2-46a6-bbb7-c241ab395a43.png">

# 비밀번호 변경
- `PasswordChangeForm` 사용

### `PasswordChangeForm`
- 사용자가 비밀번호를 변경할 수 있도록 하는 Form
- 이전 비밀번호를 입력하여 비밀번호를 변경할 수 있도록 함
- 이전 비밀번호를 입력하지 않고 비밀번호를 설정하는 `SetPasswordForm`을 상속받는 서브 클래스

### 1. 비밀번호 변경 페이지 작성
<img width="950" alt="image" src="https://user-images.githubusercontent.com/108309396/227787485-c92d4e50-20c2-49af-bdc2-bbe190b1e2ad.png">

### 2. 비밀번호 변경 로직 작성
<img width="587" alt="image" src="https://user-images.githubusercontent.com/108309396/227787534-f850b1a9-21c5-4377-bf31-b12abe816068.png">
- 변경 후 로그인 상태가 지속되지 못하는 문제 발생

### 암호 변경 시 세션 무효화 방지
- 비밀번호가 변경되면 기존 세션과의 회원 인증 정보가 일치하지 않아 로그인 상태가 유지되지 못함
- `update_session_auth_hash(request, user)`
  - 현재 요청과 새 session data가 파생될 업데이트 된 사용자 객체를 가져오고, session data를 적절히 업데이트해줌
  - 암호가 변경되어도 로그아웃 되지 않도록 새로운 password의 session data로 session을 업데이트

### 3. `update_session_auth_hash()` 작성
<img width="630" alt="image" src="https://user-images.githubusercontent.com/108309396/227787720-741ac3eb-0b07-4ff3-8f6b-c44b7d1039be.png">

# View decorators
### Decorator
- 기존 함수에 기능을 추가하고 싶을 때, 해당 함수를 수정하지 않고 기능을 추가해주는 함수

### Allowed HTTP methods
- `django.views.decorators.http`의 데코레이터를 사용하여 요청 메서드를 기반으로 접근 제한 가능
- 일치하지 않는 메서드 요청이라면 405 Method Not Allowed를 반환 &rarr; 요청 방법이 서버에게 전달되었으나 사용 불가능한 상태
- `required_http_methods(), require_POST(), require_safe()`
<img width="658" alt="image" src="https://user-images.githubusercontent.com/108309396/227787925-dc57f465-8584-4de0-a1f8-751d10aabb7f.png">  
<img width="793" alt="image" src="https://user-images.githubusercontent.com/108309396/227787948-2b07ba32-3427-4b47-a9ad-75d4031d182f.png">  
<img width="853" alt="image" src="https://user-images.githubusercontent.com/108309396/227787989-9df4ad2d-fab0-48f7-931b-77229d4b1bcb.png">  

# Limiting access to logged-in users
- 로그인 사용자에 대한 접근 제한하기
- `is_authenticated`
  - 모든 User 인스턴스에 대해 항상 True인 읽기 전용 속성
  - AnonymousUser에 대해서는 항상 False
  - `request.user.is_authenticated`
  - 권한과는 관련이 없으며, 사용자가 활성화 상태거나 유효한 세션을 가지고 있는지도 확인X

### 1. 로그인/비로그인 상태에서 다르게 링크 출력하기
<img width="588" alt="image" src="https://user-images.githubusercontent.com/108309396/227788155-d84f2f38-20eb-4ad7-92f7-e6bb21ad0fa5.png">

### 2. 인증된 사용자만 게시글 작성 링크를 볼 수 있도록 처리하기
<img width="697" alt="image" src="https://user-images.githubusercontent.com/108309396/227788210-07814a62-ccec-4c9b-b2a9-f61e34365f53.png">  

- 하지만 비로그인 상태로도 URL을 직접 입력하면 게시글 작성 페이지로 갈 수 있음

### 3. 인증된 사용자라면 로그인 로직을 수행할 수 없도록 처리
<img width="498" alt="image" src="https://user-images.githubusercontent.com/108309396/227788265-5996cb95-8dbe-4eb5-aebe-3517e2329309.png">
