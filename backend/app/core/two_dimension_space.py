import numpy as np 

def get_truss_local_stiffness_matrix(area: float, elastic_modulus: float, length: float) -> np.ndarray:
    """
    Returns the stiffness matrix of a bar element.
    """
    k = area * elastic_modulus / length
    return np.array([
        [k, -k],
        [-k, k]
    ])


# def beam_stiffness_matrix(area: float, elastic_modulus: float, moment_of_inertia: float, length: float) -> np.ndarray:
#     """
#     Returns the stiffness matrix of a beam element.
#     """
#     k1 = area * elastic_modulus / length
#     k2 = 12 * elastic_modulus * moment_of_inertia / length**3
#     k3 = 6 * elastic_modulus * moment_of_inertia / length**2
#     k4 = 4 * elastic_modulus * moment_of_inertia / length
#     k5 = 2 * elastic_modulus * moment_of_inertia / length

#     return np.array([
#         [ k1,   0,    0,   -k1,   0,    0],
#         [ 0,   k2,   k3,    0,  -k2,   k3],
#         [ 0,   k3,   k4,    0,  -k3,   k5],
#         [-k1,   0,    0,    k1,   0,    0],
#         [ 0,  -k2,  -k3,    0,   k2,  -k3],
#         [ 0,   k3,   k5,    0,  -k3,   k4]
#     ])

# get_length: callable = lambda x1, y1, x2, y2: np.sqrt((x2 - x1)**2 + (y2 - y1)**2)



