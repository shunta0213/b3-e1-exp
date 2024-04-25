import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lti, step
import scienceplots

plt.style.use(['science', 'ieee'])
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams["font.size"] = 16

# 角周波数と減衰係数の設定
omegas = [5, 6, 25]
zetas = [0.2, 0.5, 1.0, 1.5, 2.0]

# 周波数範囲
frequency = np.logspace(-1, 2, 1000)

# 各角周波数についてのプロット
for omega_n in omegas:
    plt.figure(figsize=(12, 12))
    for zeta in zetas:
        # 伝達関数を定義
        num = [omega_n**2]
        den = [1, 2*zeta*omega_n, omega_n**2]
        system = lti(num, den)

        # 振幅ゲインの計算
        mag = 20 * np.log10(1 / np.sqrt((1 - frequency**2 / omega_n**2)**2 + (2 * zeta * frequency / omega_n)**2))
        # 位相の計算
        phase = np.arctan2(2 * zeta * omega_n * frequency, omega_n**2 - frequency**2) * 180 / np.pi - 180

        # 振幅ゲインのプロット
        plt.subplot(3, 1, 1)
        plt.semilogx(frequency, mag, label=f'$\\zeta={zeta}$')
        plt.ylabel('Magnitude (dB)')
        plt.grid(True)

        # 位相のプロット
        plt.subplot(3, 1, 2)
        plt.semilogx(frequency, phase, label=f'$\\zeta={zeta}$')
        plt.ylabel('Phase / deg')
        plt.xlabel('Frequency / rad/sec')
        plt.grid(True)

        # ステップ応答の計算とプロット
        t, y = step(system)
        plt.subplot(3, 1, 3)
        plt.plot(t, y, label=f'$\\zeta={zeta}$')
        plt.xlabel('Time / s')
        plt.grid(True)

    plt.subplot(3, 1, 1)
    plt.legend(loc='upper right')
    plt.subplot(3, 1, 2)
    plt.legend(loc='lower right')
    plt.subplot(3, 1, 3)
    plt.legend(loc='upper right')

    plt.savefig(f"../figures/bode-phase-step-ideal-group-omega/bode-phase-step-ideal-group-omega-{omega_n}.png")
    plt.close()
