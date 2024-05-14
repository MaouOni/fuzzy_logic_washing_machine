import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from mpl_toolkits.mplot3d import Axes3D

def display_wash_settings(graph_option, fabric, soil, weight, washing_duration, temperature, rpm, dry_duration, quality, result_frame):
    settings = {
        ("Seda", "Poco Sucio", "10kg <"): (0.35, "30°C", "400", "Rápido", "Buena"),
        ("Seda", "Poco Sucio", "10kg - 15kg"): (0.47, "30°C", "600", "Intermedio", "Buena"),
        ("Seda", "Poco Sucio", "15kg >"): (0.50, "40°C", "600", "Intermedio", "Excelente"),
        ("Seda", "Algo Sucio", "10kg <"): (0.50, "30°C", "400", "Largo", "Regular"),
        ("Seda", "Algo Sucio", "10kg - 15kg"): (1.18, "30°C", "800", "Rápido", "Buena"),
        ("Seda", "Algo Sucio", "15kg >"): (1.18, "40°C", "600", "Largo", "Regular"),
        ("Seda", "Muy Sucio", "10kg <"): (0.50, "30°C", "800", "Intermedio", "Buena"),
        ("Seda", "Muy Sucio", "10kg - 15kg"): (1.18, "40°C", "800", "Rápido", "Excelente"),
        ("Seda", "Muy Sucio", "15kg >"): (2.10, "40°C", "800", "Rápido", "Excelente"),
        ("Lana", "Poco Sucio", "10kg <"): (0.47, "40°C", "800", "Largo", "Regular"),
        ("Lana", "Poco Sucio", "10kg - 15kg"): (0.50, "40°C", "600", "Intermedio", "Buena"),
        ("Lana", "Poco Sucio", "15kg >"): (1.18, "40°C", "800", "Rápido", "Buena"),
        ("Lana", "Algo Sucio", "10kg <"): (0.50, "40°C", "600", "Intermedio", "Regular"),
        ("Lana", "Algo Sucio", "10kg - 15kg"): (0.50, "40°C", "600", "Intermedio", "Regular"),
        ("Lana", "Algo Sucio", "15kg >"): (1.18, "40°C", "800", "Rápido", "Excelente"),
        ("Lana", "Muy Sucio", "10kg <"): (1.18, "60°C", "800", "Rápido", "Excelente"),
        ("Lana", "Muy Sucio", "10kg - 15kg"): (1.18, "40°C", "1000", "Rápido", "Buena"),
        ("Lana", "Muy Sucio", "15kg >"): (2.10, "60°C", "1200", "Rápido", "Buena"),
        ("Algodón", "Poco Sucio", "10kg <"): (0.47, "40°C", "400", "Intermedio", "Buena"),
        ("Algodón", "Poco Sucio", "10kg - 15kg"): (0.50, "40°C", "600", "Intermedio", "Buena"),
        ("Algodón", "Poco Sucio", "15kg >"): (1.18, "40°C", "800", "Rápido", "Excelente"),
        ("Algodón", "Algo Sucio", "10kg <"): (0.50, "40°C", "600", "Intermedio", "Excelente"),
        ("Algodón", "Algo Sucio", "10kg - 15kg"): (1.18, "40°C", "800", "Rápido", "Excelente"),
        ("Algodón", "Algo Sucio", "15kg >"): (2.10, "40°C", "1000", "Rápido", "Buena"),
        ("Algodón", "Muy Sucio", "10kg <"): (1.18, "60°C", "1000", "Intermedio", "Buena"),
        ("Algodón", "Muy Sucio", "10kg - 15kg"): (1.18, "60°C", "1200", "Largo", "Excelente"),
        ("Algodón", "Muy Sucio", "15kg >"): (2.10, "60°C", "1200", "Largo", "Buena"),
        ("Mezclilla", "Poco Sucio", "10kg <"): (0.50, "30°C", "400", "Intermedio", "Buena"),
        ("Mezclilla", "Poco Sucio", "10kg - 15kg"): (0.50, "30°C", "600", "Intermedio", "Buena"),
        ("Mezclilla", "Poco Sucio", "15kg >"): (1.18, "30°C", "800", "Rápido", "Excelente"),
        ("Mezclilla", "Algo Sucio", "10kg <"): (0.50, "30°C", "600", "Intermedio", "Buena"),
        ("Mezclilla", "Algo Sucio", "10kg - 15kg"): (1.18, "30°C", "800", "Rápido", "Buena"),
        ("Mezclilla", "Algo Sucio", "15kg >"): (1.18, "40°C", "800", "Largo", "Regular"),
        ("Mezclilla", "Muy Sucio", "10kg <"): (1.18, "40°C", "800", "Intermedio", "Buena"),
        ("Mezclilla", "Muy Sucio", "10kg - 15kg"): (1.18, "40°C", "1000", "Rápido", "Excelente"),
        ("Mezclilla", "Muy Sucio", "15kg >"): (2.10, "40°C", "1000", "Rápido", "Excelente"),
        ("Delicado", "Poco Sucio", "10kg <"): (0.35, "30°C", "400", "Intermedio", "Buena"),
        ("Delicado", "Poco Sucio", "10kg - 15kg"): (0.47, "30°C", "600", "Intermedio", "Buena"),
        ("Delicado", "Poco Sucio", "15kg >"): (0.50, "30°C", "600", "Intermedio", "Excelente"),
        ("Delicado", "Algo Sucio", "10kg <"): (0.50, "30°C", "400", "Intermedio", "Regular"),
        ("Delicado", "Algo Sucio", "10kg - 15kg"): (1.18, "30°C", "800", "Rápido", "Buena"),
        ("Delicado", "Algo Sucio", "15kg >"): (1.18, "40°C", "600", "Intermedio", "Regular"),
        ("Delicado", "Muy Sucio", "10kg <"): (0.50, "30°C", "800", "Intermedio", "Buena"),
        ("Delicado", "Muy Sucio", "10kg - 15kg"): (1.18, "40°C", "800", "Rápido", "Excelente"),
        ("Delicado", "Muy Sucio", "15kg >"): (2.10, "40°C", "800", "Rápido", "Excelente"),
        ("Poliéster", "Poco Sucio", "10kg <"): (0.47, "30°C", "400", "Intermedio", "Buena"),
        ("Poliéster", "Poco Sucio", "10kg - 15kg"): (0.50, "30°C", "600", "Intermedio", "Buena"),
        ("Poliéster", "Poco Sucio", "15kg >"): (1.18, "30°C", "800", "Rápido", "Excelente"),
        ("Poliéster", "Algo Sucio", "10kg <"): (0.50, "30°C", "600", "Intermedio", "Buena"),
        ("Poliéster", "Algo Sucio", "10kg - 15kg"): (1.18, "30°C", "800", "Rápido", "Buena"),
        ("Poliéster", "Algo Sucio", "15kg >"): (1.18, "40°C", "800", "Largo", "Regular"),
        ("Poliéster", "Muy Sucio", "10kg <"): (1.18, "40°C", "800", "Intermedio", "Buena"),
        ("Poliéster", "Muy Sucio", "10kg - 15kg"): (1.18, "40°C", "1000", "Rápido", "Excelente"),
        ("Poliéster", "Muy Sucio", "15kg >"): (2.10, "40°C", "1000", "Rápido", "Excelente")
    }

    # Define categories
    fabric_type = ["Seda", "Lana", "Algodón", "Mezclilla", "Delicado", "Poliéster"]
    dirt_type = ["Poco Sucio", "Algo Sucio", "Muy Sucio"]
    weight_type = ["10kg <", "10kg - 15kg", "15kg >"]
    washing_duration_type = [0.35, 0.47, 0.50, 1.18, 2.10]
    temperature_type = ["30°C", "40°C", "60°C"]
    rpm = ["400", "600", "800", "1000", "1200"]
    dry_duration = ["Rápido", "Intermedio", "Largo"]
    quality = ["Regular", "Buena", "Excelente"]

    # Initialize lists for plotting data
    x_key = []
    y_key = []
    z_val = []

    if graph_option == "Tipo de Tela vs Nivel de Suciedad basado en Tiempo de Lavado":
        x_key = [key[0] for key in settings.keys()] #Key[0] = Tipo de Tela
        y_key = [key[1] for key in settings.keys()] #Key[1] = Suciedad
        z_val = [val[0] for val in settings.values()] #Val[0] = Duración

        fig = Figure(figsize=(8, 6), dpi=100)
        ax = fig.add_subplot(111, projection='3d')

        setup_and_plot_3d_bar(ax, x_key, y_key, z_val, 
                              fabric_type, dirt_type, weight_type, washing_duration, 
                              fabric, soil, weight)

    
    # Refresh canvas
    for widget in result_frame.winfo_children():
        widget.destroy()

    canvas = FigureCanvasTkAgg(fig, master=result_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill='both', expand=True)

def setup_and_plot_3d_bar(ax, x_key, y_key, z_val, x_type, y_type, z_type, dz_type, specific_x_type, specific_y_type, specific_z_type):
    ax.clear()  # Clear the previous plot

    # Mapping keys to their corresponding types
    x = [x_type.index(f) for f in x_key]
    y = [y_type.index(s) for s in y_key]
    z = np.zeros(len(x))

    dx = np.ones(len(x))
    dy = np.ones(len(y))
    dz = z_val

    ax.bar3d(x, y, z, dx, dy, dz, color='skyblue', alpha=0.6)

    specific_x = x_type.index(specific_x_type)
    specific_y = y_type.index(specific_y_type)
    specific_z = z_type.index(specific_z_type)
    specific_dz = dz_type

    ax.bar3d(specific_x, specific_y, specific_z, 1, 1, specific_dz, color='orange')

    # Set axis labels
    ax.set_xticks(np.arange(len(x_type)))
    ax.set_xticklabels(x_type, rotation=45, ha='right')
    ax.set_yticks(np.arange(len(y_type)))
    ax.set_yticklabels(y_type)
    ax.set_zticks(np.arange(len(z_type)))
    ax.set_zticklabels(z_type)