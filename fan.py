class Fan:
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    def __init__(self, speed: int = SLOW, radius: float = 5.0, color: str = "blue", is_on: bool = False):
        """Constructor to initialize the fan with private attributes."""
        self.__speed = speed
        self.__radius = radius
        self.__color = color
        self.__is_on = is_on