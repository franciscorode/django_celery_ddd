from random import choice

from faker import Faker
from src.customer_assistance.domain.customer_request import CustomerRequest, Department

fake = Faker()


class CustomerRequestMother:
    @staticmethod
    def sales_request() -> CustomerRequest:
        return CustomerRequest(department=Department.SALES, question=fake.text())

    @staticmethod
    def pricing_request() -> CustomerRequest:
        return CustomerRequest(department=Department.PRICING, question=fake.text())

    @staticmethod
    def random() -> CustomerRequest:
        return choice(
            [
                CustomerRequestMother.sales_request(),
                CustomerRequestMother.pricing_request(),
            ]
        )
