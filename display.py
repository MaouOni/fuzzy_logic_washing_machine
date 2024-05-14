import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from mpl_toolkits.mplot3d import Axes3D

def display_wash_settings(graph_option, fabric_type, soil_category, weight_category, duration, result_frame):
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

    fig = Figure(figsize=(8, 6), dpi=100)
    ax = fig.add_subplot(111, projection='3d')
    ax.clear()  # Clear the previous plot

    # Define categories
    fabric_types = ["Seda", "Lana", "Algodón", "Mezclilla", "Delicado", "Poliéster"]
    dirtiness_levels = ["Poco Sucio", "Algo Sucio", "Muy Sucio"]
    weight_categories = ["10kg <", "10kg - 15kg", "15kg >"]

    # Initialize lists for plotting data
    x_labels = []
    y_labels = []
    z_values = []

    # Populate labels and values based on the graph option
    for key, value in settings.items():
        if graph_option == "Tipo de Tela vs Nivel de Suciedad basado en Tiempo de Lavado":
            x_labels.append(key[0])
            y_labels.append(key[1])
            z_values.append(value[0])

    # Map labels to indices in their respective categories
    x = [fabric_types.index(label) for label in x_labels]
    y = [dirtiness_levels.index(label) for label in y_labels]
    z = np.zeros(len(x))  # Z always starts at 0

    dx = np.ones(len(x))
    dy = np.ones(len(y))
    dz = z_values

    ax.bar3d(x, y, z, dx, dy, dz, color='skyblue', alpha=0.6)

    # Plotting the specific selection
    specific_x = fabric_types.index(fabric_type)
    specific_y = dirtiness_levels.index(soil_category)
    specific_z = weight_categories.index(weight_category)
    specific_dz = duration
    ax.bar3d(specific_x, specific_y, specific_z, 1, 1, specific_dz, color='orange')

    # Set ticks and labels dynamically
    ax.set_xticks(np.arange(len(fabric_types)))
    ax.set_xticklabels(fabric_types, rotation=45, ha='right')
    ax.set_yticks(np.arange(len(dirtiness_levels)))
    ax.set_yticklabels(dirtiness_levels)
    ax.set_zticks(np.arange(len(weight_categories)))
    ax.set_zticklabels(weight_categories)

    # Refresh canvas
    for widget in result_frame.winfo_children():
        widget.destroy()

    canvas = FigureCanvasTkAgg(fig, master=result_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill='both', expand=True)
