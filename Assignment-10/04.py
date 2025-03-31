import numpy as np

def generatecartesianpoints(n):

    x = np.random.uniform(-100, 100, n)
    y = np.random.uniform(-100, 100, n)
    cartesian_points = np.column_stack((x, y))
    return cartesian_points

def cartesian_to_polar(cartesian_points):
    x, y = cartesian_points[:, 0], cartesian_points[:, 1]
    r = np.sqrt(x**2 + y**2)
    theta = np.arctan2(y, x)
    polar_points = np.column_stack((r, theta))
    return polar_points

N = 10
cartesian_points = generatecartesianpoints(N)
polar_points = cartesian_to_polar(cartesian_points)

print("Cartesian Points (x, y) = \n", cartesian_points)
print("\nPolar Points (r, θ in radians) = \n", polar_points)