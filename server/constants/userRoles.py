from enum import Enum 

class UserRoles(str, Enum):
    admin = 'ADMIN'
    owner = 'OWNER'
    client = 'CLIENT'
    