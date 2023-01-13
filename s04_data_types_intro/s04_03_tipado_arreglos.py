from typing import List
def process_items1(items: List[str]):
    for e in items:
        print(e.title())
#? with python 3.6 or higher


def process_items2(items: list[str]):
    for e in items:
        print(e.title())
#? with python 3.10 or higher the import is unnecessary
