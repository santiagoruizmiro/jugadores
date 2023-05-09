from config.db import conn
from fastapi import APIRouter, Response
from models.user import users
from schemas.user import User
from typing import List
from starlette.status import HTTP_204_NO_CONTENT
user=APIRouter()
@user.get(
    "/users",
    tags=["users"],
    response_model=List[User],
    description="Get a list of all users",
)
def get_users():
    result= conn.execute(users.select()).fetchall()
    return result

@user.delete("/users/{id}")
def delete_user(id:str):
    result=conn.execute(users.delete().where(users.c.id ==id))
    return Response(status_code=HTTP_204_NO_CONTENT)
@user.put("/users/{id}")
def update_user(id:str,user:User):
    conn.execute(users.update().values(name=user.name, email=user.email, password=user.password).where(users.c.id == id))
    return "updated"
@user.post("/users")
def create_user(user: User):
    new_user={"name":user.name,"email":user.email, "password":user.password}
    result=conn.execute(users.insert().values(new_user))
    return "nuevo usuario agreagado"
@user.get("/users/{id}")
def get_user_id(id:str):
    query = users.select().where(users.c.id == id)
    result = conn.execute(query).fetchone()
    print("usuario encotnrado")
