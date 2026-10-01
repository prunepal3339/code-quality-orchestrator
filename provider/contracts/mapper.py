from typing import Protocol

class Mapper(Protocol):
    def map(self, args: dict) -> dict:
        ...