from purchase_request import PurchaseRequest
from pydantic import BaseModel
import json


class JsonDB(BaseModel):
    path: str
    
    def read(self):
        f = open(self.path)
        data = json.loads(f.read())
        f.close()
        return data
    