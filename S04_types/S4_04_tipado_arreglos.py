from typing import List
def process_items(items: List[str]):
    for e in items:
        print(e.title())
#? with python 3.6 or higher


def process_items(items: list[str]):
    for e in items:
        print(e.title())
#? with python 3.10 or higher the import is unnecessary
