import numpy as np
import matplotlib.pyplot as plt
from src.utils.grapher import continuous_plotter, discrete_plotter, plot_magnitude_spectrum

def dft(signal):
    N = len(signal)
    dft_result = np.zeros(N, dtype=complex)
    for k in range(N):
        for n in range(N):
            angle = -2 * np.pi * k * n / N
            dft_result[k] += signal[n] * (np.cos(angle) + 1j * np.sin(angle))
    return dft_result

def generar_senal(n, fs=256, f1=8, f2=20):
    Ts = 1 / fs
    return 3 * np.sin(2 * np.pi * f1 * n * Ts) + 5 * np.sin(2 * np.pi * f2 * n * Ts)

def anadir_ruido(signal, noise_freq, noise_amp=0.3, fs=256):
    n = np.arange(len(signal))
    noise = noise_amp * np.sin(2 * np.pi * noise_freq * n / fs)
    return signal + noise

def encontrar_picos(magnitude, frequencies, threshold_ratio=0.1):
    """Detecta picos en el espectro."""
    max_mag = np.max(magnitude)
    threshold = max_mag * threshold_ratio
    peaks_x = []
    peaks_y = []
    for i in range(1, len(magnitude)-1):
        if magnitude[i] > magnitude[i-1] and magnitude[i] > magnitude[i+1] and magnitude[i] > threshold:
            peaks_x.append(frequencies[i])
            peaks_y.append(magnitude[i])
    return peaks_x, peaks_y

def ejecutar_examen_p2():
    fs = 256.0
    duration = 6.0
    noise_freq = 40
    N = int(fs * duration)
    n = np.arange(N)

    # Señal original
    signal_original = generar_senal(n, fs=fs, f1=8, f2=20)
    dft_original = dft(signal_original)
    mag_original = np.abs(dft_original)
    freqs = np.fft.fftfreq(N, 1 / fs)
    mitad = N // 2

    discrete_plotter(
        ind_var=n[:100],
        dep_var=signal_original[:100],
        title="Señal original",
        xlabel="Muestras (n)",
        ylabel="Amplitud",
        graph_label="Señal original"
    )

    # Resaltar picos
    peaks_x, peaks_y = encontrar_picos(mag_original[:mitad], freqs[:mitad])
    plot_magnitude_spectrum(
        frequencies=freqs[:mitad],
        magnitude=mag_original[:mitad],
        title="DFT - Señal Original",
        highlight_points=(peaks_x, peaks_y)
    )

    # Señal con ruido
    signal_noise = anadir_ruido(signal_original, noise_freq)
    dft_noise = dft(signal_noise)
    mag_noise = np.abs(dft_noise)

    discrete_plotter(
        ind_var=n[:100],
        dep_var=signal_noise[:100],
        title="Señal con Ruido",
        xlabel="Muestras (n)",
        ylabel="Amplitud",
        graph_label="Señal con ruido"
    )

    peaks_x_noise, peaks_y_noise = encontrar_picos(mag_noise[:mitad], freqs[:mitad])
    plot_magnitude_spectrum(
        frequencies=freqs[:mitad],
        magnitude=mag_noise[:mitad],
        title="DFT - Señal con Ruido",
        highlight_points=(peaks_x_noise, peaks_y_noise)
    )

    # Comparación de espectros
    plt.figure(figsize=(12, 6))
    plt.plot(freqs[:mitad], mag_original[:mitad], 'g-', linewidth=1.5, label='Señal Original')
    plt.plot(freqs[:mitad], mag_noise[:mitad], 'r-', linewidth=1.5, alpha=0.7, label='Señal con Ruido')
    plt.title("Comparación de Espectros de Frecuencia")
    plt.xlabel("Frecuencia (Hz)")
    plt.ylabel("Magnitud")
    plt.grid(True, alpha=0.3)
    plt.axvline(x=8, color='red', linestyle='--', alpha=0.5, label='8 Hz')
    plt.axvline(x=20, color='green', linestyle='--', alpha=0.5, label='20 Hz')
    plt.axvline(x=noise_freq, color='orange', linestyle='--', alpha=0.5, label=f'{noise_freq} Hz (ruido)')
    plt.legend()
    plt.show()

    delta_f = fs / N
    print(f"Resolución en frecuencia: {delta_f:.4f} Hz")

def run():
    ejecutar_examen_p2()

if __name__ == "__main__":
    run()
