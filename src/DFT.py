import numpy as np
from .utils.grapher import continuous_plotter, discrete_plotter

class DFTAnalyzer:
   
    def __init__(self, fm=0.5, fc=8.0, m=0.5):
        self.fm = fm  # Frecuencia de modulación
        self.fc = fc  # Frecuencia portadora
        self.m = m    # Índice de modulación
       
    def signal_function(self, t):
        envelope = 1 + self.m * np.cos(2 * np.pi * self.fm * t)
        carrier = np.sin(2 * np.pi * self.fc * t)
        return envelope * carrier
   
    def custom_dft(self, x):
        N = len(x)
        X = np.zeros(N, dtype=complex)
        for k in range(N):
            for n in range(N):
                angle = -2 * np.pi * k * n / N
                X[k] += x[n] * (np.cos(angle) + 1j * np.sin(angle))
        return X
   
    def find_peaks(self, magnitude, frequencies, threshold_ratio=0.1):
        max_mag = np.max(magnitude)
        threshold = max_mag * threshold_ratio
        peaks = []
        for i in range(1, len(magnitude) - 1):
            if (magnitude[i] > magnitude[i-1] and
                magnitude[i] > magnitude[i+1] and
                magnitude[i] > threshold):
                peaks.append({
                    'frequency': frequencies[i],
                    'magnitude': magnitude[i],
                    'amplitude_rel': magnitude[i] / max_mag
                })
        peaks.sort(key=lambda x: x['magnitude'], reverse=True)
        return peaks
   
    def analyze_signal(self, duration=4.0, fs=64.0):
        # Señal continua para visualización
        t_cont = np.linspace(0, duration, 1000)
        x_cont = self.signal_function(t_cont)
       
        # Señal muestreada
        N = int(fs * duration)
        t_discrete = np.linspace(0, duration, N)
        x_discrete = self.signal_function(t_discrete)
       
        # Resolución en frecuencia
        delta_f = fs / N
       
        # DFT personalizada
        X = self.custom_dft(x_discrete)
       
        magnitude = np.abs(X)
        frequencies = np.linspace(0, fs, N)
       
        # Primera mitad (espectro positivo)
        half_N = N // 2
        magnitude_half = magnitude[:half_N]
        frequencies_half = frequencies[:half_N]
       
        # Encontrar picos espectrales
        peaks = self.find_peaks(magnitude_half, frequencies_half)
       
        # Graficar resultados
        self.plot_results(t_cont, x_cont, t_discrete, x_discrete,
                         frequencies_half, magnitude_half, peaks)
       
        return {
            'time_cont': t_cont,
            'signal_cont': x_cont,
            'time_discrete': t_discrete,
            'signal_discrete': x_discrete,
            'frequencies': frequencies_half,
            'magnitude': magnitude_half,
            'peaks': peaks,
            'delta_f': delta_f
        }
   
    def plot_results(self, t_cont, x_cont, t_discrete, x_discrete,
                     frequencies, magnitude, peaks):
        # Señal continua
        continuous_plotter(
            t_cont, x_cont,
            title="Señal Modulada - Vista Continua",
            xlabel="Tiempo (s)",
            ylabel="Amplitud",
            grid=True
        )
       
        # Señal muestreada
        discrete_plotter(
            t_discrete, x_discrete,
            title="Señal Modulada - Muestras Discretas",
            xlabel="Tiempo (s)",
            ylabel="Amplitud",
            grid=True
        )
       
        # Espectro de frecuencias
        continuous_plotter(
            frequencies, magnitude,
            title="Espectro de Frecuencias (DFT)",
            xlabel="Frecuencia (Hz)",
            ylabel="Magnitud",
            grid=True
        )
       
        # Marcar picos principales
        if peaks:
            peak_freqs = [p['frequency'] for p in peaks[:5]]
            peak_mags = [p['magnitude'] for p in peaks[:5]]
            continuous_plotter(
                frequencies, magnitude,
                title="Espectro con Picos Identificados",
                xlabel="Frecuencia (Hz)",
                ylabel="Magnitud",
                grid=True,
                highlight_points=(peak_freqs, peak_mags)
            )


# Función principal de análisis
def run_analysis():
    analyzer = DFTAnalyzer()
    analyzer.analyze_signal()


# Función de compatibilidad para main.py
def run():
    run_analysis()


# Permitir ejecución directa de este archivo
if __name__ == "__main__":
    run()
