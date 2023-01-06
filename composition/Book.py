from typing import *

class Book:
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    def __str__(self) -> str:
        return f"{self.name} by {self.author}"

