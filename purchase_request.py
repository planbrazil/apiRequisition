from pydantic import BaseModel

class PurchaseRequest(BaseModel):
    purchase_requisition: int
    item_requisition: int
    short_text: str
    requisition_date: str
    created_by: str
    changed_on: str
    quantity_requested: int
    unit_of_measure: str
    material_group: str
    deletion_indicator: str
    valuation_price: str
    total_value: str
    currency: str
    cost_center: str
    wbs_element: str