from json import JSONDecodeError
from purchase_request import PurchaseRequest
from fastapi import FastAPI
from json_db import JsonDB
import uvicorn
import json

app = FastAPI()


        # productDB = JsonDB(path='./data/tb_main.json')
        # products = productDB.read()
        


@app.get('/main')
def get_purchase_requests_endpoint():
    try:
        productDB = JsonDB(path='./data/tb_main.json')
        products = productDB.read()
        return {"purchase_requests": products}
    except (FileNotFoundError, JSONDecodeError) as e:
        return {"error": f"Failed to read new rbs data: {str(e)}"}

@app.get('/newrbs')
def get_newrbs_requests_endpoint():
    try:  
        newrbsDB = JsonDB(path='./data/tb_newrbs.json')
        newrbsDB = newrbsDB.read()
        return {"new_rbs_data": newrbsDB}
    except (FileNotFoundError, JSONDecodeError) as e:
        return {"error": f"Failed to read new rbs data: {str(e)}"}


if __name__ == "__main__":
    uvicorn.run(app, port=8000)