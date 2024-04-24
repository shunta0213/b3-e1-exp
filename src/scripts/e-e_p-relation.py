import matplotlib.pyplot as plt
import numpy as np
import scienceplots

plt.style.use(['science', 'ieee'])
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams["font.size"] = 18

# Data from the LaTeX table
data = {
    60: [(0.9, 8.6), (0.6, 6.8), (-1.0, -7.5), (-1.2, -9.0)],
    80: [(-0.8, -8.5), (-0.6, -5.6), (0.4, 6.5), (0.65, 8.7)],
    100: [(-0.034, -5.7), (-0.0275, -4.2), (0.0238, 6.7), (0.034, 8.9)]
}

for p, values in data.items():
    fig, ax = plt.subplots(figsize=(8, 6))
    e_values, ep_values = zip(*values)
    e_values = np.array(e_values)
    ep_values = np.array(ep_values)

    # Scatter plot
    ax.scatter(e_values, ep_values)

    # Fit and plot line (not through the origin)
    coefficients = np.polyfit(e_values, ep_values, 1)
    polynomial = np.poly1d(coefficients)
    x_fit = np.linspace(min(e_values), max(e_values), 100)
    y_fit = polynomial(x_fit)
    ax.plot(x_fit, y_fit, 'b-', label=f'$e_p = {coefficients[0]:.2f} e + {coefficients[1]:.2f}$')

    # Perform linear regression through the origin
    A = e_values[:, np.newaxis]
    m, _, _, _ = np.linalg.lstsq(A, ep_values, rcond=None)
    y_fit_origin = m[0] * x_fit
    ax.plot(x_fit, y_fit_origin, 'r-', label=f'$e_p = {m[0]:.2f} e$')

    ax.set_xlabel('$e$')
    ax.set_ylabel('$e_p$')
    ax.legend()  # Show the legend with the equations
    ax.grid(True)

    # Save the figure
    filename = f'e-e_p-relation-{p}.png'
    plt.savefig(f"../figures/e-e_p-relation/{filename}")
    plt.close(fig)
