from pydantic import BaseModel

class NewrbsRequest(BaseModel):
    purchase_requisition: int
    email: str