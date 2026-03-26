# FastAPI + MongoDB 연동 예제

# 기능
# 1. 클라이언트가 POST로 데이터를 보내면 MongoDB에 저장
# 3. GET 요청으로 저장된 데이터를 조회

from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from pydantic import BaseModel
from typing import List, Optional
from bson import ObjectId
import json


# 1. MongoDB 연결 설정
mongo_url = "mongodb://localhost:27017"
db_name = "fastapi_db"
collection_name = "items"

# mongo_client 생성
client = MongoClient(mongo_url)
db = client[db_name]
collection = db[collection_name]

# 2. FastAPI 앱 생성
app = FastAPI(
    title="FastAPI mongodb",
    version="0.0.1",
    description="클라이언트 요청을 mongodb에 자동 저장하고 조회"
)


# 3. 데이터 모델 정의
class Item(BaseModel):
    item_name: str
    item_price: int
    item_quantity: int
    item_description: Optional[str]=None


# 5. POST 요청 : MongoDB에 데이터 저장
@app.post("/insert_item")
def insert_item(item: Item):

    """
    item_dict = {
        "item_name": item.item_name,
        "item_price": item.item_price,
        "item_quantity": item.item_quantity,
        "item_description": item.item_description
    }
    """
    item_dict = item.model_dump()
    db.get_collection(collection_name).insert_one(item_dict)
    return {"message" : "Item inserted successfully" }

# 6. get 요청 : MongoDB 데이터 조회
@app.get("/show_items")
def show_items():
    items  = []
    for students_csv in collection.find():
        students_csv["_id"] = str(students_csv["_id"])  # ObjectId → 문자열 변환
        items.append(students_csv)

    return items

# 7. fast api 서버 실행
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='192.168.0.49', port=8000)