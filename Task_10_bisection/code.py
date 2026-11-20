import numpy as np
from scipy.optimize import root_scalar
import matplotlib.pyplot as plt

# Heat-balance model: f(T) = 0 means heat gain equals heat loss
def heat_balance(T):
    return T - 25 - 10 * np.exp(-T / 20)

# ---------- Bisection Method ----------
bisect_sol = root_scalar(
    heat_balance,
    bracket=[20, 40],
    method="bisect",
    xtol=1e-10
)

# ---------- Fixed-Point Method ----------
def g(T):
    return 25 + 10 * np.exp(-T / 20)

T = 30.0
history = [T]

for i in range(100):
    T_new = g(T)
    history.append(T_new)
    if abs(T_new - T) < 1e-10:
        break
    T = T_new

print("=== Bisection Method ===")
print(f"Equilibrium temperature: {bisect_sol.root:.6f} °C")
print(f"Converged: {bisect_sol.converged}")

print("\n=== Fixed-Point Method ===")
print(f"Equilibrium temperature: {history[-1]:.6f} °C")
print(f"Iterations used: {len(history)-1}")

# Optional graph
temps = np.linspace(20, 40, 300)
plt.figure(figsize=(8, 5))
plt.plot(temps, heat_balance(temps), label="Heat-balance function")
plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(bisect_sol.root, color="red", linestyle="--", label=f"Root ≈ {bisect_sol.root:.2f}°C")
plt.xlabel("Temperature (°C)")
plt.ylabel("f(T)")
plt.title("Equilibrium Temperature (Bisection + Fixed-Point)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("Task_10_bisection/graph.png")   # saves the graph
plt.show()