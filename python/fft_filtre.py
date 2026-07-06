import numpy as np
import matplotlib.pyplot as plt
import os

# ============================================
# Répertoire de travail
# ============================================
os.chdir(r'C:/Users/raiss/OneDrive/Documents/LTspice/python')

# ============================================
# Chargement des données LTspice
# ============================================
data_ideal = np.loadtxt('input_current_ideal.txt', skiprows=1)
t_ideal = data_ideal[:, 0]
i_ideal = data_ideal[:, 1]

data_real = np.loadtxt('input_current_real.txt', skiprows=1)
t_real = data_real[:, 0]
i_real = data_real[:, 1]

data_filtered = np.loadtxt(
    r'C:/Users/raiss/OneDrive/Documents/LTspice/python/input_current_filtered.txt', 
    skiprows=1)
t_filtered = data_filtered[:, 0]
i_filtered = data_filtered[:, 1]

print("Données chargées avec succès")
print(f"Nombre de points (idéal) : {len(t_ideal)}")
print(f"Nombre de points (réel) : {len(t_real)}")
print(f"Nombre de points (filtré) : {len(t_filtered)}")

# ============================================
# Rééchantillonnage sur pas de temps constant
# ============================================
fs = 100e6
dt = 1 / fs

# Circuit idéal
t_start_ideal = max(t_ideal[0], 2e-3)
t_end_ideal = t_ideal[-1]
t_uniform_ideal = np.arange(t_start_ideal, t_end_ideal, dt)
i_uniform_ideal = np.interp(t_uniform_ideal, t_ideal, i_ideal)

# Circuit réel
t_start_real = max(t_real[0], 2e-3)
t_end_real = t_real[-1]
t_uniform_real = np.arange(t_start_real, t_end_real, dt)
i_uniform_real = np.interp(t_uniform_real, t_real, i_real)

# Circuit filtré
t_start_filtered = max(t_filtered[0], 3e-3)
t_end_filtered = t_filtered[-1]
t_uniform_filtered = np.arange(t_start_filtered, t_end_filtered, dt)
i_uniform_filtered = np.interp(t_uniform_filtered, t_filtered, i_filtered)

# ============================================
# Calcul FFT
# ============================================
N_ideal = len(i_uniform_ideal)
freqs_ideal = np.fft.rfftfreq(N_ideal, d=dt)
fft_ideal = np.abs(np.fft.rfft(i_uniform_ideal)) * 2 / N_ideal

N_real = len(i_uniform_real)
freqs_real = np.fft.rfftfreq(N_real, d=dt)
fft_real = np.abs(np.fft.rfft(i_uniform_real)) * 2 / N_real

N_filtered = len(i_uniform_filtered)
freqs_filtered = np.fft.rfftfreq(N_filtered, d=dt)
fft_filtered = np.abs(np.fft.rfft(i_uniform_filtered)) * 2 / N_filtered

print("FFT calculée avec succès")
print(f"Résolution fréquentielle : {freqs_ideal[1]:.1f} Hz")
print(f"Fréquence max analysée : {freqs_ideal[-1]/1e6:.1f} MHz")

# ============================================
# Conversion courant → tension équivalente RSIL (dBµV)
# ============================================
Z_RSIL = 50

v_ideal_dBuV    = 20 * np.log10(fft_ideal * Z_RSIL * 1e6 + 1e-12)
v_real_dBuV     = 20 * np.log10(fft_real * Z_RSIL * 1e6 + 1e-12)
v_filtered_dBuV = 20 * np.log10(fft_filtered * Z_RSIL * 1e6 + 1e-12)

# ============================================
# Limite normative EN 55022/32 Class B (QP)
# ============================================
freqs_limite = np.array([150e3, 500e3, 30e6])
limite_QP    = np.array([66,    60,    60])

# ============================================
# Tracé — comparaison des trois circuits
# ============================================
plt.figure(figsize=(12, 6))

plt.semilogx(freqs_ideal, v_ideal_dBuV, 
             label='Circuit idéal', color='green', linewidth=1, alpha=0.6)
plt.semilogx(freqs_real, v_real_dBuV, 
             label='Circuit réel (sans filtre)', color='red', linewidth=1, alpha=0.6)
plt.semilogx(freqs_filtered, v_filtered_dBuV, 
             label='Circuit réel + filtre CEM', color='purple', linewidth=1.5)
plt.semilogx(freqs_limite, limite_QP, 
             label='Limite EN 55032 Class B (QP)', 
             color='blue', linestyle='--', linewidth=2)

plt.axvline(x=150e3, color='orange', linestyle='--', alpha=0.5, 
            label='150kHz (début bande réglementée)')

plt.xlim(1e3, 30e6)
plt.ylim(0, 200)
plt.xlabel('Fréquence (Hz)')
plt.ylabel('Amplitude (dBµV)')
plt.title("Spectre CEM — Idéal vs Réel vs Filtré — vs Limite EN 55032")
plt.legend()
plt.grid(True, which='both', alpha=0.3)

plt.savefig('spectrum_final_comparison.png', dpi=150)
plt.show()

print("Graphe sauvegardé : spectrum_final_comparison.png")