# FastAPI 클라이언트 예제 (fastAPI_client.py)
# 기능 :
# - request 라이브러리를 이용해 서버로 post 요청 전송
# - 서버의 분석 결과(json) 받아 출력

import requests # http 요청 모듈이다. 통신할 때 많이 쓰입니다

# 1. 서버 주소 설정
SERVER_URL = "http://192.168.0.49:8000/analyze"

# 2. 전송할 데이터 정의
data = {
    "text": "AI 설비 예지보전 테스트 중입니다."
}

# 3. 서버로 POST 요청 전송
print("서버에 데이터 전송 중 ... ")
response = requests.post(SERVER_URL, json=data)

# 4. 서버 응답 출력
if response.status_code == 200:
    print("서버 응답 성공!")
    print("서버 응답 데이터")
    print(response.json())
else:
    print("요청 실패 :", response.status_code)
    print("응답 내용 :",response.text)