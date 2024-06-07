username: str = "David"
altura: float = 1.70
edad:int = 20

print(username, altura, edad)

# LISTAS, TUPLAS Y DICCIONARIOS

from typing import Tuple, List, Dict

numbers: List[int] = [1, 2, 3]
name: Tuple[str, str] = ("Oscar", "David")
scores: Dict[str, int] = {"user1": 100, "User2":70}

# FUCTIONS

def average(numbers: List[int]) -> float :
    return sum(numbers) / len(numbers)

scores: List[int] = [10,10,8,8,8,7]
result: float =average(scores)
print(f"The average is {result}")


#UNION

from typing import Union, List

def average(numbers: List[int]) -> Union[None, float]:
    
    if len (numbers) == 0:
        return None
    
    return sum(numbers) / len(numbers)

numbers = [1, 2, 3, 4]
result: Union[None, float] = average(numbers)

print(result)

# CLASES

class User:
    def __init__(self, username: str, email: str):
        self.username = username
        self.email = email
        
def make_user (username: str, email:str ):
    return User(username, email)

david: User = make_user("DavidBC", "davidbocanegrac@gmail.com")
print(david.username)
print(david.email)

#Tipos NamedTuple
from typing import NamedTuple

class DataBaseSettings(NamedTuple):
    username: str
    password: str
    part: int
    database: str
    
data_base_config_1 = DataBaseSettings(
    'root',
    'password1234',
    8080,
    'superoot'
)