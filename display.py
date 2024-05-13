import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from mpl_toolkits.mplot3d import Axes3D

def display_wash_settings(fabric_type, duration, result_frame):
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

    fabric_types = ["Seda", "Lana", "Algodón", "Mezclilla", "Delicado", "Poliéster"]
    dirtiness_levels = ["Poco Sucio", "Algo Sucio", "Muy Sucio"]

    x_labels = []
    y_labels = []
    z_values = []

    for key, value in settings.items():
        x_labels.append(key[0])
        y_labels.append(key[1])
        z_values.append(value[0])

    x = [fabric_types.index(fabric) for fabric in x_labels]
    y = [dirtiness_levels.index(dirt) for dirt in y_labels]
    z = np.zeros(len(x))

    dx = np.ones(len(x))
    dy = np.ones(len(y))
    dz = z_values

    ax.bar3d(x, y, z, dx, dy, dz, color='skyblue', alpha=0.6)

    specific_x = fabric_types.index(fabric_type)
    specific_y = dirtiness_levels.index("Poco Sucio")
    specific_z = 0
    specific_dz = duration

    ax.bar3d(specific_x, specific_y, specific_z, 1, 1, specific_dz, color='orange')

    ax.set_xlabel('Tipo de Tela', labelpad=30, loc='left')
    ax.set_ylabel('Nivel de Suciedad', labelpad=15)
    ax.set_zlabel('Duración del Lavado (h)', labelpad=15)
    ax.set_xticks(np.arange(len(fabric_types)))
    ax.set_xticklabels(fabric_types, rotation=45, ha='right')
    ax.set_yticks(np.arange(len(dirtiness_levels)))
    ax.set_yticklabels(dirtiness_levels)

    for widget in result_frame.winfo_children():
        widget.destroy()

    canvas = FigureCanvasTkAgg(fig, master=result_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill='both', expand=True)
