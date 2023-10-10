from bson import ObjectId
from fastapi import APIRouter, HTTPException, Depends
from db.user.dbUser import  (getUserByEmailInDb, getUserInDb,getUsersByRoleInDb,getUsersInDb,removeUserInDb,updateUserInDb,createUserInDb)
from constants.userRoles import UserRoles 
from models.user import User, UserSingIn
from auth.jwtHandler import signJWT,decodeJWT
from auth.jwt_bearer import jwtBearer



routeApi = APIRouter() 

# routeApi.get('/api/example')
# def example():
#     return

@routeApi.get('/')
def index():
    return {'message':"Hi bb"}

# User --------------------------------->

@routeApi.get('/api/getUsers')
async def getUsers():
    users = await getUsersInDb()
    return users

@routeApi.get('/api/getUserById/{userId}')
async def getUserById(userId: str):
    user = await getUserInDb(userId)
    return user

@routeApi.get('/api/getUsersByRole/{role}')
async def getUserByRole(role: UserRoles):
    users = await getUsersByRoleInDb(role.value)
    return users

@routeApi.get('/api/getUserByEmail/{email}')
async def getUserByEmail(email: str):
    user = await getUserByEmailInDb(email)
    return user

@routeApi.post('/api/createUser')
async def createUser(user: User):
    print(f'Request: {user} from: SomeURL')
    res = await createUserInDb(dict(user))
    return signJWT(res['userId']) if res else {}

@routeApi.post('/api/updateUser', dependencies=[Depends(jwtBearer())])
async def updateUser(user: User):
    user = await updateUserInDb(dict(user))
    return user

@routeApi.post('/api/removeUser/{userId}')
async def removeUser(userId: str):
    response = await removeUserInDb(userId)
    return response

@routeApi.post('/api/signIn')
async def signIn(user: UserSingIn):
    userFound = await getUserByEmailInDb(user.email)
    return signJWT(userFound['userId']) if userFound and userFound['password'] == user.password else {}

# End User --------------------------------->