import numpy as np
from src.utils import grapher

def resolver_tarea_4(num_bits):
    """
    Ejecuta la simulación de un DAC para un número específico de bits.
    """
    VFS = 5.0  # Voltaje de escala completa (5V)
    N = int(num_bits)

    niveles = 2 ** N
    paso = VFS / (niveles - 1)
    resolucion = (paso / VFS) * 100

    print(f"\n Tarea 4 - DAC de {N} bits")
    print(f"Niveles posibles: {niveles}")
    print(f"Tamaño del paso: {paso:.6f} V")
    print(f"Resolución porcentual: {resolucion:.4f} %")

    # Crear vector de entrada digital y salida analógica
    entrada_digital = np.arange(niveles)
    salida_analogica = entrada_digital * paso

    # Graficar la salida analógica del DAC
    grapher.discrete_plotter(
        entrada_digital,
        salida_analogica,
        title=f"Salida del DAC para N = {N} bits",
        xlabel="Entrada digital",
        ylabel="Voltaje analógico (V)"
    )
