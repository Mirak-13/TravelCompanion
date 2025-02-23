from pydantic import BaseModel

class CreateTable(BaseModel):
    place_id: str
    user_name: str
    comment: str

class Table(CreateTable):
    id: int

    class Config:
        from_attributes = True
