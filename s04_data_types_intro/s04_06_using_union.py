from typing import Union
def process_item1(item: Union[int,str]):
    print(item)
#? with python 3.6 or higher
    
    
def process_item2(item: int | str):
    print(item)
#? with python 3.10 or higher the import is unnecessary
