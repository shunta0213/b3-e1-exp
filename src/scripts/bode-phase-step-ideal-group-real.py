import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lti, step
import scienceplots

plt.style.use(['science', 'ieee'])
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams["font.size"] = 16

# 各組の (omega, zeta) ペアの設定
parameters = [
    [(5.0, 1.0), (5.9, 0.87), (25, 0.20)],
    [(5.0, 1.4), (5.9, 1.2), (25, 0.29)],
    [(5.0, 1.6), (5.9, 1.4), (25, 0.33)],
    [(5.0, 2.1), (5.9, 1.8), (25, 0.43)]
]

# 周波数範囲
frequency = np.logspace(-1, 2, 1000)

# 各組み合わせについてのプロット
for index, param_set in enumerate(parameters):
    plt.figure(figsize=(12, 12))

    for omega_n, zeta in param_set:
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
        plt.semilogx(frequency, mag, label=f'$\\omega={omega_n}$, $\\zeta={zeta}$')
        plt.ylabel('Magnitude / dB')
        plt.grid(True)

        # 位相のプロット
        plt.subplot(3, 1, 2)
        plt.semilogx(frequency, phase, label=f'$\\omega={omega_n}$, $\\zeta={zeta}$')
        plt.ylabel('Phase / deg')
        plt.xlabel('Frequency / rad/sec')
        plt.grid(True)

        # ステップ応答の計算とプロット
        t, y = step(system)
        plt.subplot(3, 1, 3)
        plt.plot(t, y, label=f'$\\omega={omega_n}$, $\\zeta={zeta}$')
        plt.ylabel('Output')
        plt.xlabel('Time / seconds')
        plt.grid(True)

    plt.subplot(3, 1, 1)
    plt.legend(loc='lower left')
    plt.subplot(3, 1, 2)
    plt.legend(loc='upper right')
    plt.subplot(3, 1, 3)
    plt.legend(loc='upper right')

    plt.savefig(f"../figures/bode-phase-step-ideal-group-real/bode-phase-step-ideal-group-real-{index + 1}.png")
    plt.close()
