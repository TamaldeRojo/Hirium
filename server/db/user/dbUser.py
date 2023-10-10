from db.conn import database
from models.user import User
from constants.userRoles import UserRoles
from schemas.user import userSerial,usersSerial
from bson import ObjectId

collection = database.user

async def getUserInDb(userId : str) -> User:
    try:
        userMongo = await collection.find_one({'_id': ObjectId(userId)})
        user = userSerial(userMongo)
        print(f'[+] User found= {user}')
        return user
    except:
        print(f'[-] No User found with userId= {userId}')
        return

async def getUserByEmailInDb(email : str) -> User:
    try:
        userMongo = await collection.find_one({'email': email})
        user = userSerial(userMongo)
        print(f'[+] User found= {user}')
        return user
    except:
        print(f'[-] No User found with email= {email}')
        return 

async def getUsersInDb() -> list:
    try:
        usersMongo = await collection.find({}).to_list(None)
        users = usersSerial(usersMongo)
        print(f'[+] Users found= {users}')
        return users
    except:
        print(f'No Users found')
        return
 
async def getUsersByRoleInDb(role : str) -> [User]:
    try:
        usersMongo = await collection.find({'role': role}).to_list(None)
        users = usersSerial(usersMongo)

        print(f'Users found= {users}')
        return users
    except:
        print(f'No Users found with role={role}')
        return
     
async def createUserInDb(user: dict):
    try:
        userByEmail = await getUserByEmailInDb(user['email'])
        if not userByEmail:
            await collection.insert_one(user)
            user = await getUserByEmailInDb(user['email'])
            print(f'[+] User created= {user}')
            return user
        else:
            print('That email is already being used')
            return 
    except Exception as e:
        print(f'[-] Cound not create User: {e}')
        return 

async def removeUserInDb(userId: str):
    try:
        user = await getUserInDb(userId)
        await collection.delete_one({'_id': ObjectId(user["userId"])})
        
        print(f'[+] User deleted with userId={userId}')
        return True
    except Exception as e:
        print(f'[-] Cound not remove User: {e}')
        return False

async def updateUserInDb(newUser: User) -> User:
    try:
        oldUser = await getUserByEmailInDb(newUser['email'])
        print(oldUser)
        #print(f"[+] Updating user from= {oldUser} [+] to: {newUser}")
        await collection.update_one({'email':oldUser["email"]},{'$set': newUser})
        user = await getUserByEmailInDb(newUser['email'])
        print(f'[+] User updated with userId={user["userId"]}')
        return user
    except Exception as e:
        print(f'[-] Cound not update User: {e}')
        return  