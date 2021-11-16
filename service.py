from model import User
from repository import UserRepository

class UserService:
    repository: UserRepository

    def __init__(self, repository: UserRepository) -> None:
        self.repository = repository

    def login(self, username: str, password: str) -> User:
        return self.repository.findByIdentifier(username, password)

    def create(self, user: User):
        self.repository.create(user)