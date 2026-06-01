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

        tk.Label(self.form_frame, text="Pet Identity Name:", font=("Arial", 10), bg="#111827", fg="#F3F4F6").pack(anchor="w", padx=15, pady=(10, 2))
        self.name_entry = tk.Entry(self.form_frame, font=("Arial", 11), bg="#1F2937", fg="#FFFFFF", insertbackground="white", bd=1)
        self.name_entry.pack(fill="x", padx=15, ipady=4)

        tk.Label(self.form_frame, text="Animal Classification (e.g., Dog, Cat):", font=("Arial", 10), bg="#111827", fg="#F3F4F6").pack(anchor="w", padx=15, pady=(10, 2))
        self.type_entry = tk.Entry(self.form_frame, font=("Arial", 11), bg="#1F2937", fg="#FFFFFF", insertbackground="white", bd=1)
        self.type_entry.pack(fill="x", padx=15, ipady=4)

        tk.Label(self.form_frame, text="Standard Matrix Age:", font=("Arial", 10), bg="#111827", fg="#F3F4F6").pack(anchor="w", padx=15, pady=(10, 2))
        self.age_entry = tk.Entry(self.form_frame, font=("Arial", 11), bg="#1F2937", fg="#FFFFFF", insertbackground="white", bd=1)
        self.age_entry.pack(fill="x", padx=15, ipady=4)
        
        self.submit_btn = tk.Button(
            window, text="⚡ GENERATE PASSPORT ⚡", font=("Arial", 11, "bold"),
            bg="#00FFCC", fg="#0B0F19", activebackground="#00CCAA", activeforeground="#0B0F19",
            bd=0, cursor="hand2", command=self.process_pet_data
        )
        self.submit_btn.pack(fill="x", padx=20, pady=15, ipady=8)