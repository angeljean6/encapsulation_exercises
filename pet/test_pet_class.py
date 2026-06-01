import tkinter as tk
from tkinter import messagebox
from pet import Pet

class PetRegistryGUI:
    def __init__(self, window: tk.Tk):
        self.window = window
        self.window.title("Nexus Pet Registry System")
        self.window.geometry("480x560")
        self.window.configure(bg="#0B0F19")  

        self.active_pet = Pet()