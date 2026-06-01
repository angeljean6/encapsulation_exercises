from fan import Fan

def main():
    print("=" * 44)
    print("   🌀 FAN ELECTRICAL ENCAPSULATION TEST 🌀   ")
    print("=" * 44 + "\n")

def test_fan_program():
    first_fan = Fan()
    first_fan.set_speed(Fan.FAST)
    first_fan.set_radius(10.0)
    first_fan.set_color("yellow")
    first_fan.set_is_on(True)

    second_fan = Fan()
    second_fan.set_speed(Fan.MEDIUM)
    second_fan.set_radius(5.0)
    second_fan.set_color("blue")
    second_fan.set_is_on(False)

    print("Fan 1 Properties:")
    print("Speed:", first_fan.get_speed(), "Radius:", first_fan.get_radius(), "Color:", first_fan.get_color(), "On:", first_fan.get_is_on())
    
    print("\nFan 2 Properties:")
    print("Speed:", second_fan.get_speed(), "Radius:", second_fan.get_radius(), "Color:", second_fan.get_color(), "On:", second_fan.get_is_on())

if __name__ == "__main__":
    test_fan_program()