class Card():
    def __init__(self, name: str, value: int, suit: str):
        self.name = name
        self.value = value
        self.suit = suit
    
    def __str__(self) -> str:
        return f"{self.name} of {self.suit}"
    
    def info(self) -> str:
        return f"Card: {self}\nValue: {self.value}"