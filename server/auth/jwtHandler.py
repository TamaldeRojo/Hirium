# This file is responsible for signing, encoding, decoding, and returning JWTs.

import time
import jwt
from decouple import config

JWT_SECRET = config("SECRETKEY")
JSWT_ALGORITHM = config("ALGORITHM")

#This fn returns generated Tokens (JWTs)
def tokenReponse(token: str):
    return {
        "AccessToken" : token
    }
    
# This fn is used for signing the JWT string
def signJWT(userId: str):
    payload = {
        "userId": userId,
        "expiry": time.time() + 600
    }
    token = jwt.encode(payload, JWT_SECRET,algorithm=JSWT_ALGORITHM)
    return tokenReponse(token)

def decodeJWT(token:str):
    try:
        decode_token = jwt.decode(token, JWT_SECRET, algorithms=JSWT_ALGORITHM)
        return decode_token if decode_token['expires'] >= time.time() else None
    except:
        return {}