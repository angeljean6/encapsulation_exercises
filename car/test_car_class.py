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