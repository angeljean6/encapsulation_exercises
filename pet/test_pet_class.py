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

        self.card_frame = tk.Frame(window, bg="#1F2937", bd=2, relief="solid")
        self.card_frame.pack(padx=20, pady=(0, 20), fill="both", expand=True)

        self.card_header = tk.Label(self.card_frame, text="SECURE VERIFIED ID PASSPORT", font=("Courier New", 10, "bold"), bg="#374151", fg="#00FFCC")
        self.card_header.pack(fill="x")

        self.display_name = tk.Label(self.card_frame, text="NAME: [PENDING LOG]", font=("Courier New", 11, "bold"), bg="#1F2937", fg="#F3F4F6")
        self.display_name.pack(anchor="w", padx=20, pady=(15, 4))

        self.display_type = tk.Label(self.card_frame, text="TYPE: [PENDING LOG]", font=("Courier New", 11, "bold"), bg="#1F2937", fg="#F3F4F6")
        self.display_type.pack(anchor="w", padx=20, pady=4)

        self.display_age = tk.Label(self.card_frame, text="AGE:  [PENDING LOG]", font=("Courier New", 11, "bold"), bg="#1F2937", fg="#F3F4F6")
        self.display_age.pack(anchor="w", padx=20, pady=(4, 15))

        def process_pet_data(self) -> None:
            """Collects raw visual text, updates backend data models, and updates UI using accessors."""
            raw_name = self.name_entry.get()
            raw_type = self.type_entry.get()
            raw_age_str = self.age_entry.get()

        try:
            if not raw_name.strip() or not raw_type.strip():
                raise ValueError("Fields cannot be empty space values.")
            
            raw_age = int(raw_age_str)
            if raw_age < 0:
                raise ValueError("Age cannot be structurally negative.")
            
        except ValueError:
            messagebox.showerror("System Error", "Please ensure names/types are filled and age is a positive integer entry.")
            return
        
        self.active_pet.set_name(raw_name)
        self.active_pet.set_animal_type(raw_type)
        self.active_pet.set_age(raw_age)

        self.display_name.config(text=f"NAME: {self.active_pet.get_name().upper()}")
        self.display_type.config(text=f"TYPE: {self.active_pet.get_animal_type().upper()}")
        self.display_age.config(text=f"AGE:  {self.active_pet.get_age()} YEARS OLD")

        self.card_frame.config(highlightbackground="#00FFCC", highlightcolor="#00FFCC", highlightthickness=2)
        self.card_header.config(bg="#00FFCC", fg="#0B0F19")