import numpy as np
import matplotlib.pyplot as plt

# =========================================================
# RANDOM NUMBER GENERATION (NumPy style)
# =========================================================

# NumPy uses a "random number generator" object.
# Think of this as a *stateful probability space*.
#
# - rng is NOT a random number
# - rng is an OBJECT that *produces* random numbers
#
# Why this exists:
#   • reproducibility (fixed seeds)
#   • better statistical properties
#   • faster vectorized generation
#
rng = np.random.default_rng(42)   # 42 is just a seed


# =========================================================
# MONTE CARLO ESTIMATOR
# =========================================================
def monte_carlo_pi(N, rng):
    """
    N   : number of samples
    rng : random number generator object
    """

    # -----------------------------------------------------
    # X and Y are NumPy ARRAYS (not Python lists)
    #
    # X[i] ~ Uniform[-1,1], independently for each i
    #
    # Type of X: numpy.ndarray
    # Shape of X: (N,)
    #
    X = rng.uniform(-1.0, 1.0, size=N)
    Y = rng.uniform(-1.0, 1.0, size=N)

    # -----------------------------------------------------
    # This line is crucial:
    #
    # X**2        -> elementwise squaring
    # X**2 + Y**2 -> elementwise addition
    #
    # The comparison <= 1.0 is also elementwise
    #
    # Result:
    # inside[i] = True  if X[i]^2 + Y[i]^2 <= 1
    #           = False otherwise
    #
    # Type of inside: numpy.ndarray of dtype=bool
    #
    inside = (X**2 + Y**2) <= 1.0

    # -----------------------------------------------------
    # np.mean on a boolean array works like this:
    #
    # True  -> 1
    # False -> 0
    #
    # So np.mean(inside) =
    #   (# of points inside disk) / N
    #
    pi_hat = 4.0 * np.mean(inside)

    return pi_hat


# =========================================================
# VISUALIZATION OF THE RANDOM POINTS
# =========================================================

N_vis = 10_000

X = rng.uniform(-1.0, 1.0, size=N_vis)
Y = rng.uniform(-1.0, 1.0, size=N_vis)

inside = (X**2 + Y**2) <= 1.0   # boolean NumPy array

plt.figure()

# X[inside] means:
#   "select only those entries of X where inside == True"
#
# This is called BOOLEAN INDEXING (very important in NumPy)
#
plt.scatter(X[~inside], Y[~inside], s=1)  # outside disk
plt.scatter(X[inside],  Y[inside],  s=1)  # inside disk

plt.gca().set_aspect("equal")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Monte Carlo sampling of the unit disk")
plt.show()


# =========================================================
# ERROR ANALYSIS
# =========================================================

# Python list (you know this already)
errors = []

# NumPy array of sample sizes
Ns = np.array([10**2, 10**3, 10**4, 10**5, 10**6])

for N in Ns:
    pi_hat = monte_carlo_pi(N, rng)

    # abs(...) is scalar here
    error = abs(pi_hat - np.pi)

    # append to a Python list
    errors.append(error)

# Convert list -> NumPy array
# This allows vectorized math later
errors = np.array(errors)


# =========================================================
# LOG-LOG PLOT
# =========================================================

plt.figure()

# loglog applies log scale to BOTH axes
plt.loglog(Ns, errors, marker='o')

plt.xlabel("Number of samples N")
plt.ylabel("Absolute error |π̂ − π|")
plt.title("Monte Carlo error decay")
plt.show()


# =========================================================
# FIT A POWER LAW
# =========================================================

# Take logs explicitly
logN = np.log(Ns)
logE = np.log(errors)

# Fit: log(error) ≈ a * log(N) + b
a, b = np.polyfit(logN, logE, 1)

print("Estimated slope:", a)
