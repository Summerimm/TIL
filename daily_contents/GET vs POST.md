# GET 방식과 POST 방식의 차이

## 1. 데이터 담는 위치의 차이
- 프론트엔드에서 백엔드로 데이터 전송 시
- GET &rarr; 데이터를 **패킷의 header에 담아서 보냄**
- POST &rarr; 데이터를 **패킷의 body에 담아서 보냄**
 
## 2. 암호화 여부에 따른 차이
- GET &rarr; header에 담아서 보낼 때는 암호화 X 
- POST &rarr; 데이터를 body에 넣어 보내기 때문에 암호화해서 전달

## 3. 용량 차이
- GET &rarr; 헤더는 용량 제한이 있음 
- POST &rarr; 큰 데이터 전송 시, body에 담아서 전송