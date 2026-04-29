from pydantic import BaseModel, field_validator, conint, constr
from pydantic_core.core_schema import FieldValidationInfo

class User(BaseModel):
    id: int
    name: str
    age: int

    @field_validator('age')
    def age_must_be_positive(cls, v, info: FieldValidationInfo):
        if v <= 0:
            raise ValueError('Age must be a positive integer')
        return v
try:
    user = User(id=1, name="Dren", age=1)
    print(user)
except ValueError as e:
    print(e)

class Adress(BaseModel):
    id: int
    city: str
    street: str

    @field_validator('id')
    def int_must_be_positive(cls, v, info: FieldValidationInfo):
        if v <= 0:
            raise ValueError('ID must be a positive integer')
        return v
    @field_validator('street')
    def char_length(cls, v, info: FieldValidationInfo):
        if len(v) < 2 or len(v) > 50:
            raise ValueError('Street name must be between 2 and 50 characters')
        return v
try:
    adress = Adress(id=2, city="Prizren", street="Alpet Shqipetare")
    print(adress)
except ValueError as e:
    print(e)