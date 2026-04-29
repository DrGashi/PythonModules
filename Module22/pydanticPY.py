from pydantic import BaseModel, conint, constr
from typing import Optional

class User(BaseModel):
    id: int
    name: str
    age: int
    email: str

user = User(id=1, name="Dren", age=17, email="dren@gmail.com")
print(user)

class User(BaseModel):
    id: int
    name: str
    age: int = 0
    email: str = "example@domain.com"

user = User(id=2, name="Dren")
print(user)