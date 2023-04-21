# DB 설계를 활용한 REST API 설계
## 목표
- DRF(Django Rest Framework)를 활용한 API Server 제작
- DB 1:N에 대한 이해
- DB M:N에 대한 이해

## 제공사항
- 주어진 fixture 파일은 movies앱 내에 위치시키고, loaddata는 **반드시 모델 정의 및 migrate 후 가능**
- 하지만 ERD와 동일하게 DB를 만들지 않으면 의미상 문제가 생기지 않더라도 loaddata 진행 불가.
- 완전히 ERD와 table명이 동일하도록 만들어줌

## ERD(Entity-Relationship Diagram)  
![image](https://user-images.githubusercontent.com/108309396/233547276-2ed42729-12d6-43e8-85c1-a070d23fc10d.png)

## View  
![image](https://user-images.githubusercontent.com/108309396/233547490-453c01a3-ea66-41b9-8744-b461dfeb0088.png)

### 사전준비
- `settings.py`에 `rest_framework`를 등록해주어야 함(pip install 된 상황에서)
- `mypjt`의 `urls.py`에 `'api/v1/'`을 추가해 movies앱의 urls와 연결해준다.
- Model을 먼저 생성해주는데, 이 때 ERD에서 보듯이 Django에서 자동으로 생성해주는 중개테이블이 `movies_movie_actors`이므로 `Movie` 모델에  `ManyToManyField`로 `actors`를 추가한다.
- `Review` 모델의 경우 `Movie`와 1:N의 관계를 가지므로 Foreign Key로 `Movie`를 받아온다.


## 응답
### A. 배우 전체 조회
- GET api/v1/actors/
- ActorSerializer에서 모든 필드 사용
- views에서는 actors에 Actor모델의 모든 객체를 담아 ActorSerializer로 넘겨준다.(인스턴스가 여러 개 이므로 many=True)

### B. 배우 상세 조회
- GET api/v1/actors/1
- ActorDetailSerializer를 사용
- movie라는 이름으로 배우가 출연한 영화의 title을 받아와야 하므로 MovieTitleSerializer를 생성한다.
- MovieTitleSerializer는 fields로 title만 가진다.
- `to_representation()`을 overriding하여 movie가 아닌 movies로 표현이 되도록 변경한다.
  - `rep = super().to_representation(instance)`에는 딕셔너리 형식으로 해당 actor의 id, movie, name 정보가 저장되어 있다.
  - `rep['movies'] = rep.pop('movie', [])`를 통해 movie 안에 담겨있는 정보를 모두 pop시켜 새로운 키인 movies에 저장한다.
  - 이렇게 하면 보이는 movie key만 movies key로 변경가능하다.
- views에서는 Actor 모델에서 actor_pk를 이용해 actor 인스턴스를 생성해 ActorDetailSerializer로 넘겨준다.

### C. 영화 전체 조회
- GET api/v1/movies/
- 배우 전체 조회와 거의 유사하나, title과 overview 필드만 보이게 하기 위해 fields를 '\_\_all\_\_'이 아닌 ('title', 'overview',)로 수정한다.

### D. 영화 상세 조회
- GET api/v1/movies/1/
- 배우 상세 조회와 거의 유사하고 MovieDetailSerializer에서 ActorSerializer와 ReviewSerializer를 각각 actors와 review_set에 넣는다.
- Movie의 모든 필드는 추가하고, actors의 id는 제외하기 위해서 다음과 같은 코드를 추가했다.
```python
def to_representation(self, instance):
        rep = super().to_representation(instance)
        for actor in rep['actors']:
            del(actor['id'])
        return rep
```

### E. 리뷰 전체 조회
- GET api/v1/reviews/
- ReviewSerializer 사용
- ReviewSerializer에서 fields는 title과 content만 사용한다.

### F. 리뷰 상세 조회
- GET api/v1/reviews/1/
- ReviewDetailSerializer 사용
- movie의 title만 가져오기 위해 MovieTitleSerializer를 사용했다.

### G. 리뷰 수정
- PUT api/v1/reviews/1/
- review_detail 함수에서 method로 PUT이 들어오는 기준으로 분기점 생성
- ReviewDetailSerializer에 review 객체와 data로 request.data를 받았다.
- 유효성 검사를 진행 후 저장해 넘겨줬다.

### H. 리뷰 삭제
- DELETE api/v1/reviews/1/
- review_detail 함수에서 method로 DELETE이 들어오는 기준으로 분기점 생성
- review.delete() 진행 후 status=status.HTTP_204_NO_CONTENT로 확인

### I. 리뷰 추가
- POST api/v1/movies/1/
- 리뷰를 작성할 영화의 pk가 필요하므로 movie_detail 함수에 추가했다.
- method가 POST로 들어오면 serializer에 ReviewSerializer(data=request.data)를 넣어주고 유효하다면 `serializer.save()`의 옵션으로 `(movie=movie)`를 추가해 movie_id를 넣어준다.
- 성공 시 status=status.HTTP_201_CREATED로 확인

