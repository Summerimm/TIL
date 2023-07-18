# Day 1.
## 1. GET 방식과 POST 방식의 차이
- 프론트엔드에서 백엔드로 데이터 전송 시, 데이터를 패킷의 헤더에 담아서 보내느냐, body에 담아서 보내느냐의 차이
- 헤더에 담아서 보낼 때는 암호화하지 않음 &rarr; GET
- 헤더는 용량 제한이 있음 &rarr; 큰 데이터 전송 시, body에 담아서 전송함.
- body에 담아서 보낼 때는 암호화함 &rarr; POST

### 모범답안
Q. GET방식과 POST방식의 차이에 대하여 설명하세요.
- GET방식과 POST방식의 가장 큰 차이점은 프론트엔드에서 백엔드로 데이터를 전송할 때 데이터를 헤더에 담아 전달하느냐 바디에 담아 전달하느냐의 차이입니다.
- POST방식의 경우 데이터를 바디에 넣어 보내기 때문에 기본적으로 암호화해서 전달하지만 GET방식은 암호화하지 않습니다.
- 또한 POST방식은 GET방식보다 상대적으로 큰 데이터를 전송할 수 있어서 큰 데이터를 전송할 때에는 POST방식을 사용합니다.