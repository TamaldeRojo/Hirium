from models.user import User


def userSerial(user: User) -> dict:
    serializedObj = {
        "userId": str(user["_id"]),
        "name":user["name"],
        "email":user["email"],
        "password":user["password"],
        "role": user["role"],
        "createdAt": user["createdAt"],
        "updatedAt": user["updatedAt"]
    }


    return serializedObj
def usersSerial(users: [User])-> list:
    return [userSerial(user) for user in users]