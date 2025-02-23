from pydantic import BaseModel

class CreateTable(BaseModel):
    place_id: str
    name: str
    comment: str

class Table(CreateTable):
    id: int

