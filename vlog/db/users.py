from mongoengine import Document
from mongoengine import fields

class User(Document):
	name = fields.StringField()
	email = fields.EmailField(unique=True, required=True)
	password = fields.StringField()
