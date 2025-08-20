import numpy as np
import matplotlib.pyplot as plt
from src.utils.grapher import continuous_plotter, discrete_plotter

def dft(x):
    """Implementación manual de la Transformada de Fourier Discreta"""
    N = len(x)
    X = []
    for k in range(N):
        s = 0
        for n in range(N):
            s += x[n] * np.exp(-2j * np.pi * k * n / N)
        X.append(s)
    return np.array(X)

def run():
    fm = 0.5   
    fc = 8     
    m = 0.5
    fs = 32    
    T = 4      
    t = np.arange(0, T, 1/fs)

    x_t = (1 + m * np.cos(2*np.pi*fm*t)) * np.sin(2*np.pi*fc*t)

    N = len(t)
    x_n = x_t

    X_k = dft(x_n)
    freqs = np.arange(N) * (fs / N)

    continuous_plotter(t, x_t, "Señal continua x(t)")
    discrete_plotter(freqs, np.abs(X_k), "Espectro |X[k]|")

    delta_f = fs / N
    print(f"Resolución en frecuencia Δf = {delta_f:.3f} Hz")
