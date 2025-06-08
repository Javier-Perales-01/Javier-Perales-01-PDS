import numpy as np
from scipy.signal import square, sawtooth
from src.utils import grapher

def resolver_tarea_1():
    print("Ejecutando tarea 1: Señales continuas y discretas")

    # Parámetros Generales
    frecuencia = 2           
    amplitud = 1
    t_ini = -1               
    t_fin = 5                
    puntos = 5000            
    t = np.linspace(t_ini, t_fin, puntos)  

    # Señales continuas
    x1 = amplitud * np.sin(2 * np.pi * frecuencia * t)                 
    u = np.where(t >= 0, 1, 0)                                          
    x2 = np.exp(-2 * t) * u                                             
    x3 = sawtooth(2 * np.pi * frecuencia * t, width=0.5)                
    x4 = square(2 * np.pi * frecuencia * t)                            

    # Muestreo y señal discreta
    Ts = 0.01                        
    n = np.arange(int((t_fin - t_ini) / Ts))  
    t_n = t_ini + n * Ts             

    # Señales muestreadas
    x1_n = amplitud * np.sin(2 * np.pi * frecuencia * t_n)
    x2_n = np.exp(-2 * t_n) * np.where(t_n >= 0, 1, 0)
    x3_n = sawtooth(2 * np.pi * frecuencia * t_n, width=0.5)
    x4_n = square(2 * np.pi * frecuencia * t_n)

    # Graficar con grapher
    grapher.continuous_plotter(t, x1, title="x₁(t) = sin(2π·f·t)", xlabel="t", ylabel="x₁(t)")
    grapher.discrete_plotter(t_n, x1_n, title="x₁[n] = sin(2π·f·nTs)", xlabel="n", ylabel="x₁[n]")

    grapher.continuous_plotter(t, x2, title="x₂(t) = e^(–2t)·u(t)", xlabel="t", ylabel="x₂(t)")
    grapher.discrete_plotter(t_n, x2_n, title="x₂[n] = e^(–2nTs)·u[n]", xlabel="n", ylabel="x₂[n]")

    grapher.continuous_plotter(t, x3, title="x₃(t) = Señal Triangular periódica", xlabel="t", ylabel="x₃(t)")
    grapher.discrete_plotter(t_n, x3_n, title="x₃[n] = Triangular discreta", xlabel="n", ylabel="x₃[n]")

    grapher.continuous_plotter(t, x4, title="x₄(t) = Señal Cuadrada periódica", xlabel="t", ylabel="x₄(t)")
    grapher.discrete_plotter(t_n, x4_n, title="x₄[n] = Cuadrada discreta", xlabel="n", ylabel="x₄[n]")

    print("Tarea 1 completada.\n")
