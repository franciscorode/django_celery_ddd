from enum import Enum

from pydantic import BaseModel


class Department(Enum):
    SALES = "SALES"
    PRICING = "PRICING"


class CustomerRequest(BaseModel):
    department: Department
    question: str
