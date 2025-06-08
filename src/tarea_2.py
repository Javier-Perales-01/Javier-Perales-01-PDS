# src/tarea_2.py

import numpy as np
from src.utils import grapher

def resolver_tarea_2(frecuencia):
    try:
        f = float(frecuencia)
    except ValueError:
        print("Error: la frecuencia debe ser un número válido.")
        return

    A = 1
    t = np.linspace(0, 1, 1000)
    x_t = A * np.sin(2 * np.pi * f * t)

    print(f"\n Tarea 2 - Onda senoidal con frecuencia {f} Hz")

    grapher.continuous_plotter(
        t,
        x_t,
        title=f"Onda senoidal f = {f} Hz",
        xlabel="Tiempo (s)",
        ylabel="Amplitud"
    )
