# Day 1. 230718
## 1. GET 방식과 POST 방식의 차이
- 프론트엔드에서 백엔드로 데이터 전송 시, 데이터를 **패킷의 header에 담아서 보내느냐, body에 담아서 보내느냐**의 차이
- header에 담아서 보낼 때는 암호화하지 않음 &rarr; GET
- body에 담아서 보낼 때는 암호화함 &rarr; POST
- 헤더는 용량 제한이 있음 &rarr; 큰 데이터 전송 시, body에 담아서 전송함.

## 모범답안
- GET방식과 POST방식의 가장 큰 차이점은 프론트엔드에서 백엔드로 데이터를 전송할 때 데이터를 헤더에 담아 전달하느냐 바디에 담아 전달하느냐의 차이입니다.
- POST방식의 경우 데이터를 바디에 넣어 보내기 때문에 기본적으로 암호화해서 전달하지만 GET방식은 암호화하지 않습니다.
- 또한 POST방식은 GET방식보다 상대적으로 큰 데이터를 전송할 수 있어서 큰 데이터를 전송할 때에는 POST방식을 사용합니다.

# Day 2. 230719
## 1. 반정규화
- 데이터베이스의 **성능 향상**을 위하여, **데이터 중복을 허용**하고 **조인을 줄이는** 데이터베이스 성능 향상 방법

## 2. HTTP와 HTTPS의 차이
- http와 https의 차이는 서버와 클라이언트 사이에 전송되는 **데이터를 암호화 하느냐 그렇지 않느냐**의 차이입니다. 
https는 서버와 클라이언트 사이의 모든 데이터를 암호화 하여 전송하기 때문에 보안에 강합니다.
- 하지만 암호화하는 시간이 더 걸리기 때문에 **상대적으로 속도가 느리다**는 단점이 있습니다.

# Day 3. 230720
## 1. SPA에 대해서 설명해보세요.
- SPA는 **Single page application**으로 기존 웹페이지를 개발할 때에는 각각의 페이지마다 뷰(View)파일을 가졌다면 SPA의 구조는 **하나의 뷰(View)파일에 컴포넌트를 배치**하는 방식으로 페이지를 구성하는 개념 입니다.

# Day 4. 230723
## Cookie / Session / Token 방식의 비교
- 쿠키, 세션, 토큰 &rarr; 서버가 클라이언트 인증을 확인하는 방식

1. Cookie 인증
- 쿠키란?
  - key-value 형식의 문자열 덩어리
  - 클라이언트의 **브라우저에 설치**되는 작은 기록 정보파일
- 쿠키 인증 방식
  - ![image](https://github.com/Haaarimmm/TIL/assets/108309396/30cf95e3-e2c9-493c-9738-3321219dddaf)
  - 1. 브라우저(클라이언트)가 서버에 요청(접속)을 보낸다.
  - 2. 서버는 클라이언트의 요청에 대한 응답을 작성할 때, 클라이언트 측에 저장하고 싶은 정보를 응답 헤더의 Set-Cookie에 담는다.
  - 3. 이후 해당 클라이언트는 요청을 보낼 때마다, 매번 저장된 쿠키를 요청 헤더의 Cookie에 담아 보낸다.
  - 4. 서버는 쿠키에 담긴 정보를 바탕으로 해당 요청의 클라이언트가 누군지 식별하거나 정보를 바탕으로 추천 광고를 띄우거나 한다.
- 쿠키 방식의 단점
  - 요청 시 쿠키의 값을 그대로 보내기 때문에 **보안에 취약**함
  - **용량 제한**이 있어 쿠키에는 많은 정보를 담지 못함
  - **브라우저 간 공유 불가능**
  - 쿠키의 사이즈가 커질수록 **네트워크 부하**&uarr;

2. Session 인증
- 세션은 클라이언트의 민감한 인증정보를 브라우저가 아닌 **서버 측에 저장하고 관리**
  - 서버의 메모리, 로컬 파일, DB 등에 저장
- 세션 인증 방식
  - ![image](https://github.com/Haaarimmm/TIL/assets/108309396/ad32ed7e-3e15-47e3-a330-ee0f5fc67cdc)
  - 1. 유저가 웹사이트에서 로그인하면 세션이 서버 메모리(혹은 데이터베이스) 상에 저장된다. 이때, 세션을 식별하기 위한 Session Id를 기준으로 정보를 저장한다.
  - 2. 서버에서 브라우저에 쿠키에다가 Session Id를 저장한다.
  - 3. 쿠키에 정보가 담겨있기 때문에 브라우저는 해당 사이트에 대한 모든 Request에 Session Id를 쿠키에 담아 전송한다.
  - 4. 서버는 클라이언트가 보낸 Session Id 와 서버 메모리로 관리하고 있는 Session Id를 비교하여 인증을 수행한다.
- 세션 방식의 단점
  - 해커가 세션ID 자체를 탈취하면 클라이언트인 척 위장할 수 있다는 한계 존재
    - 서버에서 IP특정을 통해 해결 가능
    - 서버에서 세션 저장소를 사용하므로 요청이 많아지면 서버에 부하가 심해짐

3. Token 인증
- 서버가 클라이언트에게 유일한 토큰을 부여한다.
- 토큰은 세션과는 달리 클라이언트에 저장되기 때문에 서버의 부담을 덜 수 있다.
- 토큰 인증 방식
  - ![image](https://github.com/Haaarimmm/TIL/assets/108309396/3f157e72-e06c-4993-80f1-e74e280fb325)
  - 1. 사용자가 아이디와 비밀번호로 로그인을 한다.
  - 2. 서버 측에서 사용자(클라이언트)에게 유일한 토큰을 발급한다.
  - 3. 클라이언트는 서버 측에서 전달받은 토큰을 쿠키나 스토리지에 저장해 두고, 서버에 요청을 할 때마다 해당 토큰을 HTTP 요청 헤더에 포함시켜 전달한다.
  - 4. 서버는 전달받은 토큰을 검증하고 요청에 응답한다.
  - 5. 토큰에는 요청한 사람의 정보가 담겨있기에 서버는 DB를 조회하지 않고 누가 요청하는지 알 수 있다.
- 토큰 방식의 단점
  - 토큰 자체의 데이터 길이가 길어 인증 요청이 많아질수록 네트워크 부하&uarr;
  - payload 자체는 암호화되지 않아 중요한 정보는 담지 못함
  - 토큰을 탈취당하면 대처하기 어려움 &rarr; 사용 기간 제한을 설정하는 식으로 해결 가능

4. 세션 vs 토큰
- 세션의 경우 서버측에서 인증정보를 관리하다보니 클라이언트로부터 요청을 받으면 클라이언트의 상태를 유지해놓고 사용(stateful)
- 사용자 증가 시 성능의 문제 일으킬 수 있으며, 확장성이 어렵다
- 토큰의 경우 로그인이 필요한 작업일 경우 헤더에 토큰을 함께 보내 인증받은 사용자인지 확인
- 상태를 유지하지 않으므로 stateless

# Day 4. 230724
## Redis란?
![image](https://github.com/Haaarimmm/TIL/assets/108309396/e8852873-e79a-41c1-9cbd-9bbc62348201)
- Key, value 형태의 비정형 데이터를 저장하고 관리하기 위한 DBMS
- DB, cache, 메모리 브로커로 사용되며 **인메모리 데이터 구조**를 가짐

### Cache server?
- DB는 데이터를 물리 디스크에 직접 쓰기 때문에 서버세 문제가 발생하더라도 데이터 손실X
- But, 매번 디스크에 접근해야 하기 때문에 사용자가 많아질수록 부하&uarr;
- Redis는 cache server의 대표적인 예

### Redis의 특징
- Key, Value 구조이기 때문에 쿼리 사용할 필요X
- 메모리에서 데이터를 처리하기 때문에 속도 빠름
- String, Lists, Sets, Sorted sets, Hashs 자료 구조 지원
- Singled Threaded: 한 번에 하나의 명령만 처리 가능

### Redis 사용 주의사항
- 서버에 장애 발생 시, 데이터 유실 가능성 있음
- Singled Threaded의 특성 상, 한 번에 하나의 명령만 처리 가능하기 때문에 처리하는 데 시간이 오래 걸리는 요청, 명령은 피해야 함

### Redis 심화
- Master-Slave 형식의 데이터 이중화 구조: Redis Replication
- 분산처리: Redis cluster
- 장애 복구 시스템: Redis Sentinel, Redis Topology, Redis Sharding, Redis Failover

### MacOS Redis 사용법
1. MacOS Redis 설치
   - `brew install redis`: 설치
   - `redis-server --version`: 버전 확인
   - `brew uninstall redis`: 삭제
2. MacOS Redis 실행
  - 2-1. Foreground로 실행하기(정상 설치 확인 용도): `redis-server`
  - 2-2. Background로 실행하기(실제 Redis 사용 시)
    - `brew services start redis`: 실행
    - `brew services restart redis`: 재실행
    - `brew services stop redis`: 중지
3. Redis 실행 상태 확인
   - `brew services info redis`
4. Redis CLI 사용
   - `redis-cli`: redis-cli 사용
   - `set {key} {value}`: redis 데이터 생성, 수정(같은 key값 존재 시, 데이터만 업데이트)
   - `get {key}`: 데이터 조회
   - `keys *`: key 목록 조회
   - `rename {key} {key2}`: key 수정
   - `dbsize`: key 개수 조회
   - `del {key}`: key(데이터) 삭제
   - `flushall`: 전체 데이터 삭제
   - `HGETALL {key}`: Hash 형태의 데이터 조회

# Day 5. 230725
## ORM이란?
- (ORM은 Object Relational Mapping의 약자로) **기존에는 SQL문을 사용하여 데이터베이스를 제어**했다면 
- ORM은 **객체를 데이터베이스와 직접 맵핑하여 제어**하는 개념

# Day 6. 230726
## 1. Framework란?
- 소프트웨어의 전체적인 구조를 재사용과 확장, 유지보수가 용이하도록 미리 설계해둔 것.

## 2. openVidu
### WebRTC(Web Real-Time Communication)
- 웹 브라우저가 서로 통신할 수 있또록 설계된 API
- 웹 브라우저 상에서 음성채팅, 화상채팅, 데이터 교환 가능
- P2P(Peer-to-Peer) 통신에 최적화

### 시그널링(Signaling)
- Signaling Server를 통해 데이터를 주고 받는 프로세스
- 서로 다른 두 peer간 미디어 통신을 하기 위해 서로 상대방의 정보를 파악하는 과정

### Signaling Server
- 시그널링 서버는 단지 웹 브라우저를 특정하기 위한 시그널링 과정으로만 쓰임
- 시그널링을 마친 뒤 실제 데이터는 P2P 혹은 중개 서버를 통해 주고 받음
- 서버는 Websocket(TCP) 사용(cf. WebRTC는 UDP)
- ![image](https://github.com/Haaarimmm/TIL/assets/108309396/98bf1d8c-054f-41b3-b11e-3138dcf72f81)

### STUN(Session Traversal Utilities fro NAT) Server
- Publice IP를 알려주는 서버
- NAT 환경(사설망)에 놓인 클라이언트는 자신의 public IP를 알지 못함
- STUN 서버는 peer 자신의 Public IP를 알려주는 서버

### TURN(Traversal Using Relays around NAT) Server
- 중개서버
- TURN 서버는 Public 망에 존재하기 때문에 각 peer들이 접속 가능
- 두 peer가 같은 NAT환경에 있거나 방화벽 등의 이유로 P2P 통신 불가능 할 시 TURN 서버를 경유하여 통신

### WebRTC에서 데이터 교환이 일어나는 과정
![image](https://github.com/Haaarimmm/TIL/assets/108309396/7b9c2e57-c983-4d2a-b243-c921531d3d7f)

### openVidu란?
- 웹 또는 앱에서 화상 통화를 쉽게 추가할 수 있는 플랫폼
- Kurento 기반의 중개 서버를 쉽게 추가할 수 있도록 완전한 기술스택 제공
  - Kurento: WebRTC 미디어 서버 역할을 함과 동시에 애플리케이션을 돕는 클라이언트 API 세트
  - ![image](https://github.com/Haaarimmm/TIL/assets/108309396/2f5c5ef4-5bc9-4d94-b75c-cd0c40c88fd3)

# Day 7. 230727
## MVC 패턴이란?
- MVC 패턴이란 애플리케이션의 구조를 Model, View, Controller로 나누어 설계하는 방법을 말합니다. 
- Model은 데이터를 처리하는 영역이며, 
- View는 사용자에게 보여질 화면을 처리하는 영역이고,
- Controller는 사용자의 요청을 처리하는 영역을 말합니다.

# Day 8. 230729
## RabbitMQ
- 15672번 포트는 관리자 콘솔, 5672가 AMQP 포트라서 5672로 설정하는 것이 맞음
- admin, admin으로 사용자 추가는 해놨는데 권한 설정이 안 되어있었음 
- administrator 태그건다고 권한 주어지는 게 아니라 따로 권한 설정해주어야 함

# Day 9. 230801
## REST란?
- Representational State Transfer의 약자로 자원을 이름으로 구분하여 해당 자원의 상태를 주고 받는 것
- HTTP URI를 통해 자원을 명시하고 HTTP Method를 통해 해당 자원에 대한 상태를 주고 받는 방식을 말함

# Day 10. 230802