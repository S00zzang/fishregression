# fishregression
![image](https://github.com/user-attachments/assets/15dd2ef5-a8cd-4dda-a83f-2e4c2469a7b8)

## 작업 순서
1. 빙어 + 도미 데이터로 LinearRegression 학습
2. (1) 을 모델을 저장
3. API 화( FastAPI ) -> 도커 패키징 -> 컨테이너 RUN ( 8001 )
4. 기존의 KNeighborsClassifier API 도커 RUN ( 8002 )
5. cli 프로그램 생성 -  input 으로 길이 받기 -> (3) 호출 -> (4) 호출 -> 결과(빙어, 도미) 출력

### 작업 진행
**aws로 접속하지 않고 local을 이용하여 돌림**
LinearRegression.ipynb를 통해 pkl을 생성
(note 디렉 안에 생성되었기 때문에, model 디렉으로 복사)

main.py로 fastapi를 실행

도커에 업로드 후 컨테이너 포트를 8001로 설정 후 실행
기존에 있던 fishmlserv 도커를 컨테이너 포트 8002로 설정 후 실행

LB 디렉 생성하여 도커 업로드
컨테이너 포트 8080으로 설정 후 실행

![image](https://github.com/user-attachments/assets/dc34a382-b0b6-40e4-b6c5-636105674582)

길이로 무게 예측

![image](https://github.com/user-attachments/assets/da319371-a668-497d-8ee6-c90cc8b8292a)

길이와 무게로 생선 종류 예측

도커를 기반으로 cli.py 생성
pip install . 로 업데이트 후 
명령어 pp 입력
![image](https://github.com/user-attachments/assets/907fd821-6605-4c98-8410-2d88e9d04c05)

### ERR FIX
LB default.conf에 localhost로 입력하니, 503 오류가 발생(연결은 되나 접속이 안 됨)
- 원인
  localhost가 docker에서 사용되는 것과 컴퓨터 기본의 주소가 다르기 때문
  ![image](https://github.com/user-attachments/assets/4c09b228-15d9-4240-8068-7aca38d2c200)
- 해결법
  localhost를 172.17.0.1로 변경
