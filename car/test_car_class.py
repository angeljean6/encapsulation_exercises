import tkinter as tk
from car import Car

class CarDashboardGUI:
    def __init__(self, window: tk.Tk):
        self.window = window
        self.window.title("Nitro Telemetry Matrix")
        self.window.geometry("450x350")
        self.window.configure(bg="#121212")
        
        self.my_car = Car(2026, "Nissan GT-R Ultra")