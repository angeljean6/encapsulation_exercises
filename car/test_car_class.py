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