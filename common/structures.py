from dataclasses import dataclass 

@dataclass 
class vector2:
    x: float = 0
    y: float = 0

@dataclass 
class colour:
    r: float = 0
    g: float = 0
    b: float = 0

@dataclass 
class character:
    colour: colour = colour()
    char: str = "A"
    invert: bool = False 

@dataclass 
class tRange:
    start: vector2
    stop: vector2
