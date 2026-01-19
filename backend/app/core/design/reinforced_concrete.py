import numpy as np 
# import backend.appcore.mathematics import solve

def equilibrium(neutral_axis_depth: float, 
                concrete_compression_strength: float, 
                width: float, 
                tension_steel_depth: float,
                compression_steel_depth: float, 
                tension_steel_area: float, 
                compression_steel_area: float, 
                steel_yield_stress: float): 
    
    fy: float = steel_yield_stress

    c: float = neutral_axis_depth
    fc: float = concrete_compression_strength
    b: float = width 

    As: float = tension_steel_area
    d: float = tension_steel_depth

    As_prime: float = compression_steel_area
    d_prime: float = compression_steel_depth

    a: float = get_beta1(concrete_compression_strength=fc) * c
    Cc: float = 0.85 * fc * a * b

    compression_steel_strain: float = 0.0021 / (d - c) * (c - d_prime)
    Cs: float = As_prime * get_steel_stress(strain=compression_steel_strain, yield_stress=fy)

    Ts: float = As * fy  # Assume steel yields in tension

    axial_load: float = Cc + Cs + Ts
    moment = Cc * (d - a/2) + Cs * (d - d_prime) 

    return axial_load, moment

def stability(lateral_bracing_spacing: float): 
    pass 

def get_minimum_depth(support_condition: str, length: float) -> float: 
    if support_condition == "simply supported":
        return length / 16.00
    elif support_condition == "one end continuous":
        return length / 18.50
    elif support_condition == "both ends continuous":
        return length / 21.00
    elif support_condition == "cantilever":
        return length / 8.00
    else:
        raise ValueError("Invalid support condition")
    

## DESIGN
def get_strength_reduction_factor() -> float: 
    return 0.90

def get_beta1(concrete_compression_strength: float) -> float: 
    if concrete_compression_strength <= 16.99: 
        raise ValueError("Concrete compression strength must be at least 17 MPa")

    elif concrete_compression_strength <= 28: 
        beta_1: float = 0.85
    
    elif concrete_compression_strength >= 55: 
        beta_1: float = 0.65 
    
    else: 
        beta_1: float = 0.85 - 0.20/27 * (concrete_compression_strength - 28)
    
    return beta_1


def get_minimum_flexural_reinforcement_ratio(
        concrete_compression_strength: float,
        steel_yield_strength: float) -> float: 
    
    fc: float = concrete_compression_strength
    fy: float = steel_yield_strength

    reinforcement_ratio: float = max(0.25 * np.sqrt(fc), 1.4) / fy

    return reinforcement_ratio

def get_minimum_shear_reinforcement(
        concrete_compression_strength: float, 
        steel_yield_strength: float, 
        width: float) -> float: 
    fc: float = concrete_compression_strength
    fyt: float = steel_yield_strength
    b: float = width

    return max(0.062 * np.sqrt(fc) * b / fyt, 0.35 * b / fyt)


def get_steel_stress(strain:float, yield_stress: float) -> float: 
    young_modulus: float = 200_000.0  # MPa

    if abs(strain) * young_modulus >= yield_stress: 
        return yield_stress * np.sign(strain)  # return sign of strain times fy
    else: 
        return young_modulus * strain
    
def get_nominal_moment(
        concrete_compression_strength: float, 
        steel_yield_strength: float,
        width: float, 
        height: float,
        tension_steel_area: float,
        tension_steel_depth: float,
        compression_steel_area: float, 
        compression_steel_depth: float): 
    
    fc: float = concrete_compression_strength
    fy: float = steel_yield_strength
    beta1: float = get_beta1(concrete_compression_strength=fc)

    b: float = width

    d: float = tension_steel_depth
    d_prime: float = compression_steel_depth

    As: float = tension_steel_area
    As_prime: float = compression_steel_area


    MAX_ITER: int = 100
    iteration: int = 0
    balance: float = 2.0
    before_balance: float = 2.00
    c = height / 2 # initial guess for neutral axis depth
    step = height/4

    Cc: float = 0.0
    Cs: float = 0.0 
    Ts: float = 0.0
    a: float = 0.0

    while (iteration < MAX_ITER) and (abs(balance) > 1e-3): 
        iteration += 1

        theta: float = 0.0021 / (d - c)

        a: float = beta1 * c
        Cc: float = 0.85 * fc * a * b

        compression_steel_strain: float = theta * (c - d_prime)
        Cs: float = As_prime * get_steel_stress(strain=compression_steel_strain, yield_stress=fy)

        tension_steel_strain: float = -theta * (d - c)
        Ts: float = As * get_steel_stress(strain=tension_steel_strain, yield_stress=fy)

        before_balance = balance
        balance = Cc + Cs + Ts

        if np.sign(balance) != np.sign(before_balance):
            step: float = step / 2

        if balance > 0: # Compression greater than Tension
            c = c - step
            # print(f"decreasing c, steop {step}")
        
        if balance < 0: # Tension greater than Compression
            c = c + step
            # print(f"increasing c, step {step}")

        # print(f"{iteration},{Cc:.2f}, {Cs:.2f}, {Ts:.2f}, {balance:.2f}, {c:.2f}, {step:.2f}")

    nominal_moment: float = Cc * (d - a/2) + Cs * (d - d_prime)
    return nominal_moment

def get_concrete_nominal_shear(
        concrete_compression_strength: float,
        width: float,
        gross_area: float,
        tension_steel_depth: float, 
        axial_load: float) -> float:
    
    b: float = width
    fc: float = concrete_compression_strength
    d: float = tension_steel_depth
    N: float = axial_load
    Ag: float = gross_area

    Vc1: float = 0.17 * np.sqrt(fc) + min(0.05 * fc, N / ( 6 * Ag )) 
    Vc2: float = 0.42 * np.sqrt(fc) * b * d
    Vc: float = min(Vc1, Vc2)

    return Vc

def get_stirrups_nominal_shear(
        leg_area: float, 
        number_of_legs: int,
        steel_yield_stress: float,
        tension_steel_depth: float,
        spacing: float
) -> float: 
    
    fyt: float = steel_yield_stress
    d: float = tension_steel_depth
    Av: float = leg_area * number_of_legs
    s: float = spacing

    Vs: float = Av * fyt * d / s
    return Vs 

def get_nominal_shear(
    concrete_compression_strength: float, 
    width: float, 
    gross_area: float, 
    tension_steel_depth: float, 
    axial_load: float, 
    leg_area: float, 
    number_of_legs: int, 
    steel_yield_stress: float, 
    spacing: float
) -> float:

    Vc: float = get_concrete_nominal_shear(
        concrete_compression_strength=concrete_compression_strength,
        width=width,
        gross_area=gross_area,
        tension_steel_depth=tension_steel_depth,
        axial_load=axial_load
    )

    Vs: float = get_stirrups_nominal_shear(
        leg_area=leg_area,
        number_of_legs=number_of_legs,
        steel_yield_stress=steel_yield_stress,
        tension_steel_depth=tension_steel_depth,
        spacing=spacing
    )

    return Vc + Vs
if __name__ == "__main__":  
    print(get_steel_stress(-0.002, 420.0))

    print(get_beta1(28))
    
    print(get_nominal_moment(
        concrete_compression_strength=21.0,
        steel_yield_strength=420.0,
        width=300.0,
        height=600.0,
        tension_steel_area=570.0,
        tension_steel_depth=600.0-53.0,
        compression_steel_area=0.0,
        compression_steel_depth=50.0
    ))