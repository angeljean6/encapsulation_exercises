class Pet:
    def __init__(self):
        """Constructor initializing private fields for encapsulation."""
        self.__name = ""
        self.__animal_type = ""
        self.__age = 0
    
    def set_name(self, name: str) -> None:
        self.__name = name if name.strip() else "Unknown"

    def set_animal_type(self, animal_type: str) -> None:
        self.__animal_type = animal_type if animal_type.strip() else "Unknown"

    def set_age(self, age: int) -> None:
        self.__age = age if age >= 0 else 0