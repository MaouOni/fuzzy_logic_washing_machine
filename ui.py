import customtkinter as ctk
from tkinter import messagebox
from display import display_wash_settings
from settings import get_wash_settings
from tkinter import ttk

def show_help():
    help_text = (
        "Esta aplicación te ayuda a configurar tu lavadora basándose en el tipo de tela que ingresas, "
        "nivel de suciedad, y la carga. Simplemente seleccione de las diversas opciones y dele a la opción "
        "de 'Iniciar' para visualizar los resultados de la configuración."
    )
    messagebox.showinfo("Ayuda", help_text)

def on_submit(fabric_var, soil_var, weight_var, graph_var, result_frame, table):
    fabric_type = fabric_var.get().capitalize()
    soil_category = soil_var.get().split()[0].capitalize() + " Sucio"
    fabric_weight = weight_var.get()

    if fabric_weight < 10:
        fabric_weight_category = "10kg <"
    elif 10 <= fabric_weight <= 15:
        fabric_weight_category = "10kg - 15kg"
    else:
        fabric_weight_category = "15kg >"

    settings = get_wash_settings(fabric_type, soil_category, fabric_weight_category)
    if settings:
        duration = settings[0]  # Assuming the first item in settings is the duration
        display_wash_settings(graph_var.get(), fabric_type, soil_category, fabric_weight_category, duration, result_frame)
        update_table(table, fabric_type, soil_category, fabric_weight_category, settings)
    else:
        messagebox.showerror("Error", "Entrada incorrecta.")

def update_table(table, fabric_type, soil_category, fabric_weight_category, settings):
    for i in table.get_children():
        table.delete(i)
    
    table.insert("", "end", values=(fabric_type, soil_category, fabric_weight_category, *settings))

def update_weight_label(weight_var, weight_label):
    weight_label.configure(text=f"Carga: {weight_var.get()} kg")

def create_ui(root):
    root.title("Configuración de Lavado")
    root.geometry("1200x700")
    root.resizable(True, True)

    main_frame = ctk.CTkFrame(root)
    main_frame.pack(expand=True, fill='both', side='left', padx=20, pady=20)

    result_frame = ctk.CTkFrame(root)
    result_frame.pack(expand=True, fill='both', side='right', padx=20, pady=20)

    logo_label = ctk.CTkLabel(main_frame, text="Fuzzy Wash", font=("Arial", 24, "bold"))
    logo_label.grid(row=0, columnspan=2, pady=10)

    ctk.CTkLabel(main_frame, text="Tipo de Tela:", font=("Arial", 14)).grid(row=1, column=0, padx=10, pady=10, sticky="w")
    fabric_var = ctk.StringVar()
    fabric_options = ["Seda", "Lana", "Algodón", "Mezclilla", "Delicado", "Poliéster"]
    fabric_menu = ctk.CTkComboBox(main_frame, variable=fabric_var, values=fabric_options, font=("Arial", 14))
    fabric_menu.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

    ctk.CTkLabel(main_frame, text="Suciedad:", font=("Arial", 14)).grid(row=2, column=0, padx=10, pady=10, sticky="w")
    soil_var = ctk.StringVar()
    soil_options = [
        "Poco Sucio (ej., Tierra, Sudor)",
        "Algo Sucio (ej., Pasto, Manchas de Comida)",
        "Muy Sucio (ej., Lodo, Aceite, Vino)"
    ]
    soil_menu = ctk.CTkComboBox(main_frame, variable=soil_var, values=soil_options, font=("Arial", 14))
    soil_menu.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

    weight_var = ctk.IntVar()
    weight_slider = ctk.CTkSlider(main_frame, from_=1, to=30, number_of_steps=29, variable=weight_var, command=lambda val: update_weight_label(weight_var, weight_label))
    weight_slider.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

    ctk.CTkLabel(main_frame, text="Carga (kg):", font=("Arial", 14)).grid(row=3, column=0, padx=10, pady=10, sticky="w")
    weight_label = ctk.CTkLabel(main_frame, text="Carga: 1 kg", font=("Arial", 14))
    weight_label.grid(row=4, column=1, padx=10, pady=10, sticky="w")

    ctk.CTkLabel(main_frame, text="Opciones de Gráfico:", font=("Arial", 14)).grid(row=5, column=0, padx=10, pady=10, sticky="w")
    graph_var = ctk.StringVar()
    graph_options = [
        "Tipo de Tela vs Nivel de Suciedad basado en Tiempo de Lavado",
        "Tipo de Tela vs Temperatura basado en Nivel de Suciedad",
        # Add more graph options as needed
    ]
    graph_menu = ctk.CTkComboBox(main_frame, variable=graph_var, values=graph_options, font=("Arial", 14))
    graph_menu.grid(row=5, column=1, padx=10, pady=10, sticky="ew")

    columns = ("Tiempo de Lavado", "Temperatura", "RPM", "Tiempo de Secado", "Calidad de Lavado")
    table = ttk.Treeview(main_frame, columns=columns, show="headings", height=1, style="Custom.Treeview")
    for col in columns:
        table.heading(col, text=col)
        table.column(col, anchor="center")
    table.grid(row=6, columnspan=2, pady=10)

    submit_button = ctk.CTkButton(main_frame, text="Iniciar", command=lambda: on_submit(fabric_var, soil_var, weight_var, graph_var, result_frame, table), font=("Arial", 14))
    submit_button.grid(row=7, columnspan=2, pady=20)

    help_button = ctk.CTkButton(main_frame, text="Ayuda", command=show_help, font=("Arial", 14))
    help_button.grid(row=8, columnspan=2, pady=10)

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Custom.Treeview", background="#2e2e2e", foreground="white", fieldbackground="#2e2e2e", rowheight=25)
    style.configure("Custom.Treeview.Heading", background="#1f1f1f", foreground="white")

