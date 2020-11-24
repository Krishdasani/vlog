from pydantic import BaseModel
import json

from json import JSONEncoder
class user(BaseModel):
	name: str
	email: str
	password : str

