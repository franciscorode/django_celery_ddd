import uuid

from faker import Faker
from src.shared.domain.user import User

fake = Faker()


class UserMother:
    @staticmethod
    def random() -> User:
        return User(
            public_id=uuid.uuid4(),
            name=fake.user_name(),
            email=fake.email(),
            phone_number=fake.phone_number(),
            origin="website",
        )
