import matplotlib.pyplot as plt

def continuous_plotter(x, y, title="Gráfico Continuo", xlabel="X", ylabel="Y"):
    """
    Grafica datos continuos (líneas).
    """
    plt.figure()
    plt.plot(x, y, marker='o')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.show()


def discrete_plotter(x, y, title="Gráfico Discreto", xlabel="X", ylabel="Y"):
    """
    Grafica datos discretos (barras o puntos separados).
    """
    plt.figure()
    plt.stem(x, y, use_line_collection=True)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.show()
