"""

"""


# FastAPI 기본 실습 예제

# 기능:
# 1. GET 요청 -> 서버 상태 확인
# 2. POST 요청 -> 사용자 데이터를 받아 처리한 후 응답

# FastAPI 프레임워크 임포트
from fastapi import FastAPI
from pydantic import BaseModel #입력데이터 유효성 검사하는 라이브러리
from  typing import Optional



# 1. FastAPI 앱 인스턴스 생성
# 서버의 중심이 되는 app 객체 만들어서 넣어야함. 모든 endpoint정보 넣어줘야 함
app = FastAPI(
    title='FastAPI example',
    description='FastAPI example',
    version='0.0.1',
)


# 2. 데이터 모델 정의
class Item(BaseModel):
    name: str #필수 아이템 이름
    price: float # 필수 가격
    description: Optional[str] = None #선택


# 3. 기본 엔드포인트 (get ) 요청
@app.get('/')
def read_root():
    return {'Hello': 'World'} # 서버 상태를 확인하고 browser나 curl 로 GET요청 시 반환


# 4. 단순 GET 요청 예제 (query parameter 사용)
@app.get('/hello')
def say_hello(name: str):
    return {'Hello': f"{name}, good morning!"}
# example - addr/hello?name=현준
# addr/docs

# 5. POST 요청 예제

@app.post('/items')
def create_item(item: Item):
    total_price = item.price * 1.1

    return {
        "name": item.name,
        "description": item.description,
        "price": item.price,
        "total_with_tax": total_price,
        "message": f"{item.name} is registered successfully!"
    }


# 6. FastAPI 실행(uvicorn)
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='192.168.0.49', port=8000)