from abc import ABC, abstractmethod

from src.shared.domain.user import User


class UserRepository(ABC):
    @abstractmethod
    def save(self, user: User) -> None:
        """
        Save a user in the database
        :param user: user to save
        :type user: User
        """
        raise NotImplementedError()

    @abstractmethod
    def clear(self) -> None:
        """
        Remove all user of the database
        """
        raise NotImplementedError()
