import numpy as np
import matplotlib.pyplot as plt

#def continuous_sin():
frecuency = 1
amplitude = 1
start_time = 0
end_time = 5
points = 5000
t = np.linspace(start_time, end_time, points)
x_t = amplitude * np.sin( 2 * np.pi * frecuency * t )


#def discrete_sin():
#frecuency = 1
#amplitude = 1
fs = 20
ts = 1 / fs
samples = 100
n = np.arange(samples)
x_n = amplitude * np.sin( 2 * np.pi * frecuency * n * ts )

#########
samples1 = 6
n1 = np.arange(samples1)
x_n1 = amplitude * np.sin( 2 * np.pi * frecuency * n1 * ts )

#GRAFICAS
plt.figure()
plt.subplots_adjust(hspace=0.5)

plt.subplot(3,1,1)
plt.plot( t, x_t, 'r' )
plt.title('Continue Function')
plt.grid()

plt.subplot(3,1,2)
plt.stem( n, x_n, 'b' )
plt.title('Discrete Function')
plt.grid()

plt.subplot(3,1,3)
plt.plot( t, x_t, 'g' )
plt.stem( n1, x_n1, 'b' ) 
plt.title('Continue & Discrete Function')
plt.grid()


#continuous_sin()
#discrete_sin()


plt.show()