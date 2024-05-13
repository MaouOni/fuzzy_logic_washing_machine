import tkinter as tk
from tkinter import ttk, messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def display_wash_settings(duration, temperature, rpm, dry_time, quality):
    settings = {
        "Tiempo de lavado": duration,
        "Temperatura": temperature,
        "RPM": rpm,
        "Tiempo de secado": dry_time,
        "Calidad": quality
    }
    
    fig = Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)
    ax.barh(list(settings.keys()), list(settings.values()), color='skyblue')
    ax.set_title("Resultados de Configuración")
    ax.set_xlabel("Valor")
    
    for widget in result_frame.winfo_children():
        widget.destroy()
    
    canvas = FigureCanvasTkAgg(fig, master=result_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill='both', expand=True)

def result():
    fabric_type = fabric_var.get().lower()
    soil_category = soil_var.get().split()[0].lower()
    fabric_weight = weight_var.get()
    
    if fabric_weight < 10:
        fabric_weight_category = "below_10kg"
    elif 10 <= fabric_weight <= 15:
        fabric_weight_category = "10_to_15kg"
    else:
        fabric_weight_category = "above_15kg"
    
        settings = {
        ("seda", "poco", "below_10kg"): ("0.35 h", "30°C", "400", "Rápido", "Buena"),
        ("seda", "poco", "10_to_15kg"): ("0.47 h", "30°C", "600", "Intermedio", "Buena"),
        ("seda", "poco", "above_15kg"): ("0.50 h", "40°C", "600", "Intermedio", "Excelente"),
        ("seda", "sucio", "below_10kg"): ("0.50 h", "30°C", "400", "Largo", "Regular"),
        ("seda", "sucio", "10_to_15kg"): ("1.18 h", "30°C", "800", "Rápido", "Buena"),
        ("seda", "sucio", "above_15kg"): ("1.18 h", "40°C", "600", "Largo", "Regular"),
        ("seda", "muy", "below_10kg"): ("0.50 h", "30°C", "800", "Intermedio", "Buena"),
        ("seda", "muy", "10_to_15kg"): ("1.18 h", "40°C", "800", "Rápido", "Excelente"),
        ("seda", "muy", "above_15kg"): ("2.10 h", "40°C", "800", "Rápido", "Excelente"),
        ("lana", "poco", "below_10kg"): ("0.47 h", "40°C", "800", "Largo", "Regular"),
        ("lana", "poco", "10_to_15kg"): ("0.50 h", "40°C", "600", "Intermedio", "Buena"),
        ("lana", "poco", "above_15kg"): ("1.18 h", "40°C", "800", "Rápido", "Buena"),
        ("lana", "sucio", "below_10kg"): ("0.50 h", "40°C", "600", "Intermedio", "Regular"),
        ("lana", "sucio", "10_to_15kg"): ("0.50 h", "40°C", "600", "Intermedio", "Regular"),
        ("lana", "sucio", "above_15kg"): ("1.18 h", "40°C", "800", "Rápido", "Excelente"),
        ("lana", "muy", "below_10kg"): ("1.18 h", "60°C", "800", "Rápido", "Excelente"),
        ("lana", "muy", "10_to_15kg"): ("1.18 h", "40°C", "1000", "Rápido", "Buena"),
        ("lana", "muy", "above_15kg"): ("2.10 h", "60°C", "1200", "Rápido", "Buena"),
        ("algodón", "poco", "below_10kg"): ("0.47 h", "40°C", "400", "Intermedio", "Buena"),
        ("algodón", "poco", "10_to_15kg"): ("0.50 h", "40°C", "600", "Intermedio", "Buena"),
        ("algodón", "poco", "above_15kg"): ("1.18 h", "40°C", "800", "Rápido", "Excelente"),
        ("algodón", "sucio", "below_10kg"): ("0.50 h", "40°C", "600", "Intermedio", "Excelente"),
        ("algodón", "sucio", "10_to_15kg"): ("1.18 h", "40°C", "800", "Rápido", "Excelente"),
        ("algodón", "sucio", "above_15kg"): ("2.10 h", "40°C", "1000", "Rápido", "Buena"),
        ("algodón", "muy", "below_10kg"): ("Largo", "60°C", "1000", "Intermedio", "Buena"),
        ("algodón", "muy", "10_to_15kg"): ("1.18 h", "60°C", "1200", "Largo", "Excelente"),
        ("algodón", "muy", "above_15kg"): ("2.10 h", "60°C", "1200", "Largo", "Buena"),
        ("mezclilla", "poco", "below_10kg"): ("0.50 h", "30°C", "400", "Intermedio", "Buena"),
        ("mezclilla", "poco", "10_to_15kg"): ("0.50 h", "30°C", "600", "Intermedio", "Buena"),
        ("mezclilla", "poco", "above_15kg"): ("1.18 h", "30°C", "800", "Rápido", "Excelente"),
        ("mezclilla", "sucio", "below_10kg"): ("0.50 h", "30°C", "600", "Intermedio", "Buena"),
        ("mezclilla", "sucio", "10_to_15kg"): ("1.18 h", "30°C", "800", "Rápido", "Buena"),
        ("mezclilla", "sucio", "above_15kg"): ("1.18 h", "40°C", "800", "Largo", "Regular"),
        ("mezclilla", "muy", "below_10kg"): ("1.18 h", "40°C", "800", "Intermedio", "Buena"),
        ("mezclilla", "muy", "10_to_15kg"): ("1.18 h", "40°C", "1000", "Rápido", "Excelente"),
        ("mezclilla", "muy", "above_15kg"): ("2.10 h", "40°C", "1000", "Rápido", "Excelente"),
        ("delicado", "poco", "below_10kg"): ("0.35 h", "30°C", "400", "Intermedio", "Buena"),
        ("delicado", "poco", "10_to_15kg"): ("0.47 h", "30°C", "600", "Intermedio", "Buena"),
        ("delicado", "poco", "above_15kg"): ("0.50 h", "30°C", "600", "Intermedio", "Excelente"),
        ("delicado", "sucio", "below_10kg"): ("0.50 h", "30°C", "400", "Intermedio", "Regular"),
        ("delicado", "sucio", "10_to_15kg"): ("1.18 h", "30°C", "800", "Rápido", "Buena"),
        ("delicado", "sucio", "above_15kg"): ("1.18 h", "40°C", "600", "Intermedio", "Regular"),
        ("delicado", "muy", "below_10kg"): ("0.50 h", "30°C", "800", "Intermedio", "Buena"),
        ("delicado", "muy", "10_to_15kg"): ("1.18 h", "40°C", "800", "Rápido", "Excelente"),
        ("delicado", "muy", "above_15kg"): ("2.10 h", "40°C", "800", "Rápido", "Excelente"),
        ("poliéster", "poco", "below_10kg"): ("0.47 h", "30°C", "400", "Intermedio", "Buena"),
        ("poliéster", "poco", "10_to_15kg"): ("0.50 h", "30°C", "600", "Intermedio", "Buena"),
        ("poliéster", "poco", "above_15kg"): ("1.18 h", "30°C", "800", "Rápido", "Excelente"),
        ("poliéster", "sucio", "below_10kg"): ("0.50 h", "30°C", "600", "Intermedio", "Buena"),
        ("poliéster", "sucio", "10_to_15kg"): ("1.18 h", "30°C", "800", "Rápido", "Buena"),
        ("poliéster", "sucio", "above_15kg"): ("1.18 h", "40°C", "800", "Largo", "Regular"),
        ("poliéster", "muy", "below_10kg"): ("1.18 h", "40°C", "800", "Intermedio", "Buena"),
        ("poliéster", "muy", "10_to_15kg"): ("1.18 h", "40°C", "1000", "Rápido", "Excelente"),
        ("poliéster", "muy", "above_15kg"): ("2.10 h", "40°C", "1000", "Rápido", "Excelente")
    }
    
    key = (fabric_type, soil_category, fabric_weight_category)
    if key in settings:
        display_wash_settings(*settings[key])
    else:
        messagebox.showerror("Error", "Entrada incorrecta.")

def on_submit():
    result()

root = tk.Tk()
root.title("Configuración de Lavado")
root.attributes('-fullscreen', True)

main_frame = tk.Frame(root, padx=20, pady=20)
main_frame.pack(expand=True, fill='both', side='left')

result_frame = tk.Frame(root, padx=20, pady=20)
result_frame.pack(expand=True, fill='both', side='right')

# App name and logo
logo_label = tk.Label(main_frame, text="LavadoApp", font=("Arial", 24, "bold"))
logo_label.grid(row=0, columnspan=2, pady=10)

# Fabric type dropdown
tk.Label(main_frame, text="Tipo de Tela:", font=("Arial", 14)).grid(row=1, column=0, padx=10, pady=10, sticky="w")
fabric_var = tk.StringVar()
fabric_options = ["Seda", "Lana", "Algodón", "Mezclilla", "Delicado", "Poliéster"]
fabric_menu = ttk.Combobox(main_frame, textvariable=fabric_var, values=fabric_options, state="readonly", font=("Arial", 14))
fabric_menu.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

# Soil category dropdown with examples
tk.Label(main_frame, text="Suciedad:", font=("Arial", 14)).grid(row=2, column=0, padx=10, pady=10, sticky="w")
soil_var = tk.StringVar()
soil_options = [
    "Poco sucio (ej., tierra, sudor)",
    "Sucio (ej., pasto, manchas de comida)",
    "Muy sucio (ej., lodo, aceite, vino)"
]
soil_menu = ttk.Combobox(main_frame, textvariable=soil_var, values=soil_options, state="readonly", font=("Arial", 14))
soil_menu.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

# Fabric weight slider
tk.Label(main_frame, text="Carga (kg):", font=("Arial", 14)).grid(row=3, column=0, padx=10, pady=10, sticky="w")
weight_var = tk.IntVar()
weight_slider = tk.Scale(main_frame, from_=1, to=30, orient="horizontal", length=300, tickinterval=5, variable=weight_var, font=("Arial", 14))
weight_slider.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

# Submit button
submit_button = tk.Button(main_frame, text="Iniciar", command=on_submit, font=("Arial", 14))
submit_button.grid(row=4, columnspan=2, pady=20)

root.mainloop()
