# src/utils/grapher.py
import matplotlib.pyplot as plt

def continuous_plotter(ind_var, dep_var, title="", x_label="", y_label="", graph_label=""):
    """
    Grafica señales continuas.
    """
    plt.figure(figsize=(10, 4))
    plt.plot(ind_var, dep_var, label=graph_label, color="b", linewidth=1.5)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.grid(True, alpha=0.3)
    if graph_label:
        plt.legend()
    plt.show()


def discrete_plotter(ind_var, dep_var, title="", x_label="", y_label="", graph_label=""):
    """
    Grafica señales discretas (stem plot).
    """
    plt.figure(figsize=(10, 4))
    markerline, stemlines, baseline = plt.stem(ind_var, dep_var, linefmt="b-", markerfmt="bo", basefmt="k-")
    plt.setp(stemlines, 'linewidth', 1.2)
    plt.setp(markerline, 'markersize', 5)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.grid(True, alpha=0.3)
    if graph_label:
        plt.legend([graph_label])
    plt.show()


def plot_magnitude_spectrum(frequencies, magnitude, title="Espectro de Magnitud", x_label="Frecuencia (Hz)", y_label="Magnitud"):
    """
    Grafica el espectro de magnitudes de una señal (DFT).
    """
    plt.figure(figsize=(10, 4))
    plt.plot(frequencies, magnitude, 'r-', linewidth=1.5)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.grid(True, alpha=0.3)
    plt.show()

