from typing import Optional

def say_hi1(name: Optional[str] = None):
    if name is not None:
        print(f"Hola {name}")
    else:
        print("Hola mundo")
        
#? with python 3.6 or higher
#? Optional[str] is a shortcut for Union[str, None]
#? if you are using a python version below 3.10 use Union[str, None]


def say_hi2(name: str | None):
    if name is not None:
        print(f"Hola {name}")
    else:
        print("Hola mundo")
        
#? with python 3.10 or higher the import is unnecessary