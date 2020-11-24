from typing import Optional
from fastapi import FastAPI, status
from db import users
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from model import user_model
import json
app = FastAPI()

@app.post("/register")
def user(body: user_model.user):
	user = users.User.objects.create(
		name=body.name,
		email=body.email,
		password=body.password,
	)

	user.save()
	return JSONResponse(content='Successfully Created', status_code=status.HTTP_200_OK)

@app.get("/login",response_model=user_model.user)
	
def login(email : str, password:str):
		user_detail = users.User.objects(email=email).first()
		# response = user_model.user(
	 # 	name=user_detail.name,
	 # 	email=user_detail.email,
	 # 	password=user_detail.password,
 	# ).dict()
		# return JSONResponse(content=response)
		if email == "admin@admin.com" and password == "password":
			return JSONResponse(content="Admin");
		elif email == user_detail.email and password == user_detail.password:
			return JSONResponse(content="Logged in");
		else :
			return JSONResponse(content="Invalid details");

