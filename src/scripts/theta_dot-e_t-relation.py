import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import scienceplots

plt.style.use(['science', 'ieee'])
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams["font.size"] = 18

# Data organized by D values
data_separated = {
    60: {'theta_dot': [-5.780, -4.159, 6.544, 3.319], 'et': [-2.8, -2.0, 3.4, 1.8]},
    80: {'theta_dot': [4.133, 6.212, -4.764, -5.767], 'et': [3.2, 5.3, -3.0, -3.8]},
    100: {'theta_dot': [-5.809, -4.536, 3.759, 7.018], 'et': [-6.5, -5.0, 5.3, 9.3]}
}

# Create and save plots for each D value
for D in data_separated:
    theta_dot = np.array(data_separated[D]['theta_dot']).reshape(-1, 1)
    et = np.array(data_separated[D]['et'])

    # Create figure for plotting
    fig, ax = plt.subplots(figsize=(8, 6))

    # Standard linear regression
    model_standard = LinearRegression()
    model_standard.fit(theta_dot, et)
    predicted_et_standard = model_standard.predict(theta_dot)

    # Linear regression forced through the origin
    model_origin = LinearRegression(fit_intercept=False)
    model_origin.fit(theta_dot, et)
    predicted_et_origin = model_origin.predict(theta_dot)

    # Plot the data points
    ax.scatter(theta_dot, et)

    # Plot the fit through origin
    ax.plot(theta_dot, predicted_et_origin, 'b-',
            label=f'$e_t = {model_origin.coef_[0]:.2f}\\dot{{\\theta_2}}$')
    # Plot the standard linear fit
    ax.plot(theta_dot, predicted_et_standard, 'r-',
            label=f'$e_t= {model_standard.coef_[0]:.2f}\\dot{{\\theta_2}} + {model_standard.intercept_:.2f}$')


    ax.set_xlabel('$\\dot{\\theta_2}$ / rad/s')
    ax.set_ylabel('$e_t$')
    ax.legend()
    ax.grid(True)

    # Save the plot to a file
    file_path = f'../figures/theta_dot-e_t-relation/theta_dot-e_t-relation-D{D}.png'
    plt.savefig(file_path)
    plt.close()

    print(f'Saved plot for D={D} as "{file_path}"')
