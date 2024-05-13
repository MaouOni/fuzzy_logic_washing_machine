import customtkinter as ctk
from ui import create_ui

if __name__ == "__main__":
    ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
    ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

    root = ctk.CTk()
    create_ui(root)
    root.mainloop()
