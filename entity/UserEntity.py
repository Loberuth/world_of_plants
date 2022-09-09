from config.DBConfig import base
from sqlalchemy import Column, Integer, String

class UserEntity(base):

    __tablename__ = "users"

    id = Column("ID", Integer, primary_key = True)
    firstName = Column("First name", String, nullable=False)
    lastName = Column("Last name", String, nullable=False)
    username = Column("Username", String, nullable=False, unique=True)
    password = Column("Password", String, nullable=False, unique=True)
    position = Column("Position", String, nullable=False)

    def __repr__(self):
        return f"User ID: {self.id} - First and last name: {self.firstName} {self.lastName}\n" \
               f"Username and password: {self.username} - {self.password} - Position - {self.position}"
