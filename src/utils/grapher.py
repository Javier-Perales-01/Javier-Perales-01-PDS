# src/utils/grapher.py
import matplotlib.pyplot as plt

def continuous_plotter(ind_var, dep_var, title="", xlabel="", ylabel="", graph_label="",
                       grid=False, highlight_points=None):
    """
    Grafica señales continuas.
    highlight_points: tupla (x_points, y_points) para resaltar puntos específicos
    grid: mostrar cuadrícula
    """
    plt.figure(figsize=(10, 4))
    plt.plot(ind_var, dep_var, label=graph_label, color="b", linewidth=1.5)
    
    # Resaltar puntos si se proporciona
    if highlight_points:
        x_points, y_points = highlight_points
        plt.plot(x_points, y_points, 'ro', markersize=6, label="Picos")
        for x, y in zip(x_points, y_points):
            plt.text(x, y, f"{x:.2f} Hz", ha='center', va='bottom', fontsize=8)
    
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if grid:
        plt.grid(True, alpha=0.3)
    if graph_label or highlight_points:
        plt.legend()
    plt.show()


def discrete_plotter(ind_var, dep_var, title="", xlabel="", ylabel="", graph_label="",
                     grid=False, highlight_points=None):
    """
    Grafica señales discretas (stem plot).
    highlight_points: tupla (x_points, y_points) para resaltar puntos específicos
    grid: mostrar cuadrícula
    """
    plt.figure(figsize=(10, 4))
    markerline, stemlines, baseline = plt.stem(ind_var, dep_var, linefmt="b-", markerfmt="bo", basefmt="k-")
    plt.setp(stemlines, 'linewidth', 1.2)
    plt.setp(markerline, 'markersize', 5)
    
    # Resaltar puntos si se proporciona
    if highlight_points:
        x_points, y_points = highlight_points
        plt.plot(x_points, y_points, 'ro', markersize=6, label="Picos")
        for x, y in zip(x_points, y_points):
            plt.text(x, y, f"{x:.2f} Hz", ha='center', va='bottom', fontsize=8)
    
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if grid:
        plt.grid(True, alpha=0.3)
    if graph_label or highlight_points:
        plt.legend()
    plt.show()


def plot_magnitude_spectrum(frequencies, magnitude, title="Espectro de Magnitud",
                            xlabel="Frecuencia (Hz)", ylabel="Magnitud",
                            highlight_points=None, grid=False):
    """
    Grafica el espectro de magnitudes de una señal (DFT).
    highlight_points: tupla (x_points, y_points) para resaltar puntos específicos
    grid: mostrar cuadrícula
    """
    plt.figure(figsize=(10, 4))
    plt.plot(frequencies, magnitude, 'r-', linewidth=1.5)
    
    if highlight_points:
        x_points, y_points = highlight_points
        plt.plot(x_points, y_points, 'bo', markersize=6, label="Picos")
        for x, y in zip(x_points, y_points):
            plt.text(x, y, f"{x:.2f} Hz", ha='center', va='bottom', fontsize=8)
    
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if grid:
        plt.grid(True, alpha=0.3)
    if highlight_points:
        plt.legend()
    plt.show()
