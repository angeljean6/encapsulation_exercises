import tkinter as tk
from car import Car

class CarDashboardGUI:
    def __init__(self, window: tk.Tk):
        self.window = window
        self.window.title("Nitro Telemetry Matrix")
        self.window.geometry("450x350")
        self.window.configure(bg="#121212")
        
        self.my_car = Car(2026, "Nissan GT-R Ultra")

        self.header_label = tk.Label(
            window, 
            text=f"⚡ {self.my_car.get_year_model()} {self.my_car.get_make().upper()} ⚡", 
            font=("Courier New", 14, "bold"), 
            bg="#121212", 
            fg="#00FF66"
        )
        self.header_label.pack(pady=20)

        self.speed_frame = tk.Frame(window, bg="#1a1a1a", bd=2, relief="ridge")
        self.speed_frame.pack(pady=10, ipadx=40, ipady=10)

        self.speed_display = tk.Label(
            self.speed_frame, 
            text="000", 
            font=("Helvetica", 48, "bold"), 
            bg="#1a1a1a", 
            fg="#00E5FF"
        )
        self.speed_display.pack()

        self.unit_label = tk.Label(self.speed_frame, text="KM / H", font=("Arial", 10, "bold"), bg="#1a1a1a", fg="#777777")
        self.unit_label.pack()

        self.button_frame = tk.Frame(window, bg="#121212")
        self.button_frame.pack(pady=30)

        self.accel_btn = tk.Button(
            self.button_frame, 
            text="LAUNCH ACCEL", 
            font=("Arial", 10, "bold"),
            bg="#00FF66", 
            fg="#000000", 
            activebackground="#00CC52",
            width=15, 
            height=2,
            command=self.trigger_acceleration
        )
        self.accel_btn.grid(row=0, column=0, padx=10)

        self.brake_btn = tk.Button(
            self.button_frame, 
            text="BREMBO BRAKE", 
            font=("Arial", 10, "bold"),
            bg="#FF3333", 
            fg="#FFFFFF", 
            activebackground="#CC2424",
            width=15, 
            height=2,
            command=self.trigger_braking
        )
        self.brake_btn.grid(row=0, column=1, padx=10)

        def trigger_acceleration(self) -> None:
        """Mutates data via accelerate method and updates UI via getter."""
        self.my_car.accelerate()
        current_speed = self.my_car.get_speed()
        self.speed_display.config(text=f"{current_speed:03d}")

        def trigger_braking(self) -> None:
        """Mutates data via brake method and updates UI via getter."""
        self.my_car.brake()
        current_speed = self.my_car.get_speed()
        self.speed_display.config(text=f"{current_speed:03d}")

