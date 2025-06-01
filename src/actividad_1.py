import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import square, sawtooth

# Parámetros generales
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

# Graficado
plt.figure(figsize=(12, 10))
plt.subplots_adjust(hspace=0.5)

# Señal Senoidal
plt.subplot(4, 1, 1)
plt.plot(t, x1, 'r', label='x₁(t) continua')
plt.stem(t_n, x1_n, 'r', markerfmt='ro', linefmt='r--', basefmt=" ", label='x₁[n] discreta')
plt.title('x₁(t) = sin(2π·f·t)')
plt.grid()
plt.legend()

# Señal Exponencial con escalón
plt.subplot(4, 1, 2)
plt.plot(t, x2, 'g', label='x₂(t) continua')
plt.stem(t_n, x2_n, 'g', markerfmt='go', linefmt='g--', basefmt=" ", label='x₂[n] discreta')
plt.title('x₂(t) = e^(–2t)·u(t)')
plt.grid()
plt.legend()

# Señal Triangular
plt.subplot(4, 1, 3)
plt.plot(t, x3, 'b', label='x₃(t) continua')
plt.stem(t_n, x3_n, 'b', markerfmt='bo', linefmt='b--', basefmt=" ", label='x₃[n] discreta')
plt.title('x₃(t) = Señal Triangular periódica')
plt.grid()
plt.legend()

# Señal Cuadrada
plt.subplot(4, 1, 4)
plt.plot(t, x4, 'm', label='x₄(t) continua')
plt.stem(t_n, x4_n, 'm', markerfmt='mo', linefmt='m--', basefmt=" ", label='x₄[n] discreta')
plt.title('x₄(t) = Señal Cuadrada periódica')
plt.grid()
plt.legend()

plt.show()