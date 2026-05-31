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