from json import JSONDecodeError
from purchase_request import PurchaseRequest
from fastapi import FastAPI
from json_db import JsonDB
import json

app = FastAPI()

@app.get('/')
async def get_purchase_requests_endpoint():
    try:
        productDB = JsonDB(path='./data/tb_main.json')
        products = productDB.read()
        return {"purchase_requests": products}
    except (FileNotFoundError, JSONDecodeError) as e:
        return {"error": f"Failed to read new rbs data: {str(e)}"}

@app.get('/newrbs')
async def get_newrbs_requests_endpoint():
    try:  
        newrbsDB = JsonDB(path='./data/tb_newrbs.json')
        newrbsDB = newrbsDB.read()
        return {"new_rbs_data": newrbsDB}
    except (FileNotFoundError, JSONDecodeError) as e:
        return {"error": f"Failed to read new rbs data: {str(e)}"}
