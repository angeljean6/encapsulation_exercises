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

    def get_speed(self) -> int:
        return self.__speed

    def set_speed(self, speed: int) -> None:
        if speed in [Fan.SLOW, Fan.MEDIUM, Fan.FAST]:
            self.__speed = speed
        else:
            print("[-] Invalid speed level! Please choose SLOW (1), MEDIUM (2), or FAST (3).")

    def get_radius(self) -> float:
        return self.__radius

    def set_radius(self, radius: float) -> None:
        if radius > 0:
            self.__radius = radius
        else:
            print("[-] Radius must be a positive value.")

    def get_color(self) -> str:
        return self.__color

    def set_color(self, color: str) -> None:
        if color.strip():
            self.__color = color
        else:
            print("[-] Color cannot be empty.")

    def get_is_on(self) -> bool:
        return self.__is_on

    def set_is_on(self, is_on: bool) -> None:
        self.__is_on = is_on

    def display_properties(self, fan_name: str) -> None:
        """Displays the fan properties in a visually appealing terminal box."""
        speed_label = {1: "SLOW", 2: "MEDIUM", 3: "FAST"}.get(self.__speed, "UNKNOWN")
        status_label = "⚡ ON" if self.__is_on else "❌ OFF"    

        border = "═" * 40
        
        print(f"╔{border}╗")
        print(f"║ {fan_name.upper().center(38)} ║")
        print(f"╠{border}╣")
        print(f"║  • Status  : {status_label:<27} ║")
        print(f"║  • Speed   : {speed_label} ({self.__speed})?<19 ║" if self.__is_on else f"║  • Speed   : {speed_label} (Idle) : Fan is OFF     ║")
        print(f"║  • Radius  : {self.__radius:<27} ║")
        print(f"║  • Color   : {self.__color.capitalize():<27} ║")
        print(f"╚{border}╝\n")