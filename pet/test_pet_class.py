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

        self.title_label = tk.Label(
            window, text="🐾 PET IDENTITY CORE 🐾", 
            font=("Courier New", 16, "bold"), bg="#0B0F19", fg="#00FFCC"
        )
        self.title_label.pack(pady=15)

        self.form_frame = tk.LabelFrame(
            window, text=" Data Ingestion Fields ", font=("Arial", 10, "bold"),
            bg="#111827", fg="#9CA3AF", bd=2, relief="groove"
        )
        self.form_frame.pack(padx=20, pady=10, fill="both", expand=True)
