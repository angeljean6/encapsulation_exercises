class Car:
    def __init__(self, year_model: int, make: str):
        """Constructor to initialize the car with private attributes."""
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0
    
    def accelerate(self) -> None:
        """Adds 5 to the speed data attribute."""
        self.__speed += 5

    def brake(self) -> None:
        """Subtracts 5 from the speed data attribute safely."""
        if self.__speed >= 5:
            self.__speed -= 5
        else:
            self.__speed = 0
    
    def get_speed(self) -> int:
        return self.__speed

    def get_year_model(self) -> int:
        return self.__year_model

    def get_make(self) -> str:
        return self.__make