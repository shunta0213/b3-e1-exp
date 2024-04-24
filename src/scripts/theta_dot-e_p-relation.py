import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scienceplots

plt.style.use(['science', 'ieee'])
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams["font.size"] = 18

# データをPandas DataFrameに格納
data = {
    'P': [60, 60, 60, 60, 80, 80, 80, 80, 100, 100, 100, 100],
    'e_p': [8.6, 6.8, -7.5, -9, -8.5, -5.6, 6.5, 8.7, -5.7, -4.2, 6.7, 8.9],
    'theta_dot': [7.330, 4.722, -6.898, -8.393, -7.780, -4.932, 5.013, 7.435, -4.869, -3.319, 5.246, 7.744]
}

df = pd.DataFrame(data)

# 各P値ごとにフィッティングとプロット
for p, group in df.groupby('P'):
    # データ点
    x = group['e_p']
    y = group['theta_dot']

    # 原点を通る直線のフィッティング
    slope_origin = np.sum(x * y) / np.sum(x * x)
    line_origin = slope_origin * x

    # 一次関数のフィッティング
    slope, intercept = np.polyfit(x, y, 1)
    line_fit = slope * x + intercept

    # プロット
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.scatter(x, y, color='blue')
    ax.plot(x, line_origin, 'b-', label=f'$\\dot{{\\theta}} = {slope_origin:.2f}e_p$')
    ax.plot(x, line_fit, 'r-', label=f'$\\dot{{\\theta}} = {slope:.2f}e_p + {intercept:.2f}$')

    ax.set_xlabel('$e_p$ / V')
    ax.set_ylabel('$\\dot{\\theta}$ / rad/sec')
    ax.legend()
    ax.grid(True)
    plt.savefig("../figures/theta_dot-e_p-relation/theta_dot-e_p-relation-P{}.png".format(p))
