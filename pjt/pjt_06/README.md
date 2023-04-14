# 관계형 데이터베이스 설계
## 목표
- ERD(Entity-Relationship Diagram)  
![image](https://user-images.githubusercontent.com/108309396/231951316-a1daef0e-21eb-4df0-be14-4249ba34af2d.png)


## Study Point
- follow url의 조건이 username을 받아오는 것이었기 때문에 `path('<str:username>/follow/', views.follow, name='follow'),`로 구현해야 했다
- 따라서 view follow함수에서 `person = get_user_model().objects.get(username=username)`로 객체를 불러와야 했다.
- 싫어요 기능 구현 시 Movie에 해당되는 `like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')`필드를 생성해주었다.
- hates 함수 기능 시에 이미 좋아요를 누른 상태라면 좋아요 취소가 되도록, 싫어요를 누른 상태라면 싫어요 취소가 되도록 했다.
- 또 좋아요가 눌러진 상황에서 싫어요를 누를 시에 좋아요가 취소되도록 구성했다.
- `팔로잉 : {{ person.followings.count }} / 팔로워 : {{ person.followers.count }}`
- `좋아요 수: {{ movie.like_users.count }}`   
- `싫어요 수: {{ movie.hate_users.count }}`

## 느낀 점
- 클린 코드에 대해 생각해볼 수 있는 계기가 되었습니다.
- 현재는 view에서 좋아요와 싫어요를 처리해주고 있지만 hates가 기능할 때 like_user를 가져와서 remove하는 게 부자연스러울 수 있기 때문에 django의 signal 기능을 이용할 수 있다는 사실을 알게 되었습니다.