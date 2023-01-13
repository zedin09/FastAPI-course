from typing import Union
def process_item(item: Union[int,str]):
    print(item)
#? with python 3.6 or higher
    
    
def process_item(item: int | str):
    print(item)
#? with python 3.10 or higher the import is unnecessary
