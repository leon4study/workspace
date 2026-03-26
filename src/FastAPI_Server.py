# Fast API 서버 예제 (server_fastapi.py)

# 기능:
# - 클라이언트가 post로 텍스트 데이터를 보내면
# - 서버가 분석(문자 길이 계산) 후 결과를 반환함

from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn


# 1. 데이터 모델 정의
class TextData(BaseModel):
    text: str

# 2. Fast API 인스턴스 생성
app = FastAPI(
    title='FastAPI Server Test',
    description='클라이언트와 데이터 송수신하는 예제',
    version='1.0.0',
)

# 3. 기본 확인용 get 엔드포인트
@app.get('/')
def home():
    return {'message': 'fast api 서버가 정상적으로 실행 중입니다'}

# 4. post 요청 처리( 텍스트 분석)
@app.post('/analyze')
def analyze_text(data: TextData):
    """
    클라이언트로부터 텍스트를 받아 길이 분석 결과를 반환 요청
    """
    text = data.text
    lenght = len(text)
    word_count = len(text.split()) #단어 기준으로 구분

    result = {
        "original_text": text,
        "char_length": lenght,
        "word_count": word_count,
        "messagge" : f"문자 수 {lenght}개, 단어 수 {word_count}개 분석 완료"
    }

    return result


# 5. fastAPI  서버 실행
if __name__ == '__main__':
    uvicorn.run(app, host='192.168.0.49', port=8000)