from enum import Enum
from typing import List

from pydantic import BaseModel


class Department(Enum):
    SALES = "SALES"
    PRICING = "PRICING"

    @classmethod
    def get_values(cls) -> List[str]:
        return [department.value for department in cls]


class CustomerRequest(BaseModel):
    department: Department
    question: str
