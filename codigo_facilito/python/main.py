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