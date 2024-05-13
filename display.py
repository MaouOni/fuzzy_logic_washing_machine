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
    ax.clear()

    fabric_types = ["Seda", "Lana", "Algodón", "Mezclilla", "Delicado", "Poliéster"]
    dirtiness_levels = ["Poco Sucio", "Algo Sucio", "Muy Sucio"]
    weight_categories = ["10kg <", "10kg - 15kg", "15kg >"]
    temperature_levels = sorted(set(int(value[1].replace("°C", "")) for value in settings.values()))
    rpm_levels = sorted(set(value[2] for value in settings.values()))

    x_labels = []
    y_labels = []
    z_values = []

    for key, value in settings.items():
        if graph_option == "Tipo de Tela vs Nivel de Suciedad basado en Tiempo de Lavado":
            x_labels.append(key[0])
            y_labels.append(key[1])
            z_values.append(value[0])
        elif graph_option == "Tipo de Tela vs Temperatura basado en Nivel de Suciedad":
            x_labels.append(key[0])
            y_labels.append(int(value[1].replace("°C", "")))
            z_values.append(key[1])
        elif graph_option == "Temperatura vs Nivel de Suciedad basado en la Carga":
            x_labels.append(int(value[1].replace("°C", "")))
            y_labels.append(key[1])
            z_values.append(key[2])
        elif graph_option == "Temperatura vs Tipo de Tela basado en la Carga":
            x_labels.append(int(value[1].replace("°C", "")))
            y_labels.append(key[0])
            z_values.append(key[2])
        elif graph_option == "RPM vs Tipo de Tela basado en Nivel de Suciedad":
            x_labels.append(value[2])
            y_labels.append(key[0])
            z_values.append(key[1])
        elif graph_option == "RPM vs Tipo de Tela basado en la Carga":
            x_labels.append(value[2])
            y_labels.append(key[0])
            z_values.append(key[2])
        elif graph_option == "Carga vs Nivel de Suciedad basado en RPM":
            x_labels.append(key[2])
            y_labels.append(key[1])
            z_values.append(value[2])
        elif graph_option == "Carga vs Nivel de Suciedad basado en Tiempo de Secado":
            x_labels.append(key[2])
            y_labels.append(key[1])
            z_values.append(value[3])
        elif graph_option == "Tiempo de Secado vs Tipo de Tela basado en Nivel de Suciedad":
            x_labels.append(value[3])
            y_labels.append(key[0])
            z_values.append(key[1])
        elif graph_option == "Tiempo de Secado vs Tipo de Tela basado en la Carga":
            x_labels.append(value[3])
            y_labels.append(key[0])
            z_values.append(key[2])
        elif graph_option == "Calidad de Lavado vs Tipo de Tela basado en la Carga":
            x_labels.append(value[4])
            y_labels.append(key[0])
            z_values.append(key[2])
        elif graph_option == "Calidad de Lavado vs Nivel de Suciedad basado en la Carga":
            x_labels.append(value[4])
            y_labels.append(key[1])
            z_values.append(key[2])

    axis_categories = {
        'x': fabric_types,
        'y': dirtiness_levels,
        'z': weight_categories
    }

    x = [axis_categories['x'].index(label) for label in x_labels]
    y = [axis_categories['y'].index(label) for label in y_labels]
    z = np.zeros(len(x))

    dx = np.ones(len(x))
    dy = np.ones(len(y))
    dz = z_values

    ax.bar3d(x, y, z, dx, dy, dz, color='skyblue', alpha=0.6)
    if graph_option == "Tipo de Tela vs Nivel de Suciedad basado en Tiempo de Lavado":
        ax.set_xlabel('Tipo de Tela', labelpad=30, loc='left')
        ax.set_ylabel('Nivel de Suciedad', labelpad=15)
        ax.set_zlabel('Duración del Lavado (h)', labelpad=15)
    elif graph_option == "Tipo de Tela vs Temperatura basado en Nivel de Suciedad":
        ax.set_xlabel('Tipo de Tela', labelpad=30, loc='left')
        ax.set_ylabel('Temperatura (°C)', labelpad=15)
        ax.set_zlabel('Nivel de Suciedad', labelpad=15)
    elif graph_option == "Temperatura vs Nivel de Suciedad basado en la Carga":
        ax.set_xlabel('Temperatura (°C)', labelpad=30, loc='left')
        ax.set_ylabel('Nivel de Suciedad', labelpad=15)
        ax.set_zlabel('Carga (kg)', labelpad=15)
    elif graph_option == "Temperatura vs Tipo de Tela basado en la Carga":
        ax.set_xlabel('Temperatura (°C)', labelpad=30, loc='left')
        ax.set_ylabel('Tipo de Tela', labelpad=15)
        ax.set_zlabel('Carga (kg)', labelpad=15)
    elif graph_option == "RPM vs Tipo de Tela basado en Nivel de Suciedad":
        ax.set_xlabel('RPM', labelpad=30, loc='left')
        ax.set_ylabel('Tipo de Tela', labelpad=15)
        ax.set_zlabel('Nivel de Suciedad', labelpad=15)
    elif graph_option == "RPM vs Tipo de Tela basado en la Carga":
        ax.set_xlabel('RPM', labelpad=30, loc='left')
        ax.set_ylabel('Tipo de Tela', labelpad=15)
        ax.set_zlabel('Carga (kg)', labelpad=15)
    elif graph_option == "Carga vs Nivel de Suciedad basado en RPM":
        ax.set_xlabel('Carga (kg)', labelpad=30, loc='left')
        ax.set_ylabel('Nivel de Suciedad', labelpad=15)
        ax.set_zlabel('RPM', labelpad=15)
    elif graph_option == "Carga vs Nivel de Suciedad basado en Tiempo de Secado":
        ax.set_xlabel('Carga (kg)', labelpad=30, loc='left')
        ax.set_ylabel('Nivel de Suciedad', labelpad=15)
        ax.set_zlabel('Tiempo de Secado (h)', labelpad=15)
    elif graph_option == "Tiempo de Secado vs Tipo de Tela basado en Nivel de Suciedad":
        ax.set_xlabel('Tiempo de Secado (h)', labelpad=30, loc='left')
        ax.set_ylabel('Tipo de Tela', labelpad=15)
        ax.set_zlabel('Nivel de Suciedad', labelpad=15)
    elif graph_option == "Tiempo de Secado vs Tipo de Tela basado en la Carga":
        ax.set_xlabel('Tiempo de Secado (h)', labelpad=30, loc='left')
        ax.set_ylabel('Tipo de Tela', labelpad=15)
        ax.set_zlabel('Carga (kg)', labelpad=15)
    elif graph_option == "Calidad de Lavado vs Tipo de Tela basado en la Carga":
        ax.set_xlabel('Calidad de Lavado', labelpad=30, loc='left')
        ax.set_ylabel('Tipo de Tela', labelpad=15)
        ax.set_zlabel('Carga (kg)', labelpad=15)
    elif graph_option == "Calidad de Lavado vs Nivel de Suciedad basado en la Carga":
        ax.set_xlabel('Calidad de Lavado', labelpad=30, loc='left')
        ax.set_ylabel('Nivel de Suciedad', labelpad=15)
        ax.set_zlabel('Carga (kg)', labelpad=15)

    specific_x = fabric_types.index(fabric_type)
    specific_y = dirtiness_levels.index(soil_category)
    specific_z = weight_categories.index(weight_category)
    specific_dz = duration
    ax.bar3d(specific_x, specific_y, specific_z, 1, 1, specific_dz, color='orange')

    ax.set_xticks(np.arange(len(axis_categories['x'])))
    ax.set_xticklabels(axis_categories['x'], rotation=45, ha='right')
    ax.set_yticks(np.arange(len(axis_categories['y'])))
    ax.set_yticklabels(axis_categories['y'])
    ax.set_zticks(np.arange(len(axis_categories['z'])))
    ax.set_zticklabels(axis_categories['z'])

    for widget in result_frame.winfo_children():
        widget.destroy()

    canvas = FigureCanvasTkAgg(fig, master=result_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill='both', expand=True)
