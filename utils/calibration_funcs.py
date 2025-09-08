import numpy as np
from scipy.optimize import fsolve


def T_housing_func(V_housing, HousingSlope, HousingOffset):
    return np.array(V_housing) * HousingSlope + HousingOffset

def T_rad_func(V_rad_tot, T_housing, RadOffsetChange, RadOffset0, RadSlopeChange, RadSlope0):
    return ((2 * np.array(V_rad_tot) - 4 - RadOffset0 - RadOffsetChange * np.array(T_housing)) /
            (RadSlope0 + RadSlopeChange * np.array(T_housing))) + np.array(T_housing)

def T_antenna_func(V_spike, AntennaSlope, AntennaOffset):
    return AntennaSlope * np.array(V_spike) + AntennaOffset

def T_tissue_antenna_func(T_rad, T_antenna, tau_antenna):
    AL = 1 - tau_antenna
    return np.array(T_rad) / (1 - AL) - (AL * np.array(T_antenna)) / (1 - AL)

def T_tissue_cable_func(T_rad, T_cable, tau_cable):
    CL = 1 - tau_cable
    return np.array(T_rad) / (1 - CL) - (CL * T_cable) / (1 - CL)

def T_tissue_cable_antenna_func(T_rad, T_antenna, T_cable, tau_antenna, tau_cable):
    # Equation: T_tissue = (1/(1-AL)) * ((T_rad - T_cable*CL)/(1-CL)) - (AL*T_antenna)/(1-AL)
    CL = 1 - tau_cable
    AL = 1 - tau_antenna
    return (1/(1-AL)) * ((np.array(T_rad) - T_cable*CL)/(1-CL)) - (AL*np.array(T_antenna))/(1-AL)


# Use the quadratic equation from markdown cell 20 to solve for tau (1-CL) and T_cable
def solve_tau_and_Tcable(T_rad, T_short, T_housing, T_bath):
    """
    Solve for tau_cable (1-CL) and T_cable using the quadratic equation:
    (T_bath - T_housing) * tau^2 + (T_bath - T_rad) * tau + (T_short - T_rad) = 0
    Returns: tau_cable_1, tau_cable_2, CL_1, CL_2, T_cable_1, T_cable_2
    """
    a = T_bath - T_housing
    b = T_bath - T_rad
    c = T_short - T_rad 

    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        raise ValueError("No real solution for tau_cable (negative discriminant).")

    sqrt_disc = np.sqrt(discriminant)
    tau_cable_1 = (-b + sqrt_disc) / (2*a)
    tau_cable_2 = (-b - sqrt_disc) / (2*a)

    results = []
    for tau in [tau_cable_1, tau_cable_2]:
        if tau is not None and 0 <= tau <= 1 and tau != 1:
            T_cable = (T_rad - T_bath * tau) / (1 - tau)
            results.append({"tau_T": tau, "T_total": T_cable})

    return results

def solve_tau_pre_diode_T_pre_diode(T_short, T_hous, tauSlope, tauOffset):
    """
    Solve for tau (0<tau<1) and T_t given:
    T_short = T_hous * tau^2 + T_t * (1 - tau^2)
    tau = gamma * T_t + epsilon


    Parameters:
    T_short (float): observed T_s
    T_hous (float): T_h
    gamma (float): gamma parameter
    epsilon (float): epsilon parameter


    Returns:
    tau (float), T_t (float) if solution exists in [0,1], else (None, None)
    """
    epsilon = tauOffset
    gamma = tauSlope

    def equations(vars):
        tau, T_t = vars
        eq1 = T_hous * tau**2 + T_t * (1 - tau**2) - T_short
        eq2 = tau - (gamma * T_t + epsilon)
        return [eq1, eq2]


    # initial guesses (tau ~ 0.5, T_t ~ T_short)
    sol = fsolve(equations, [0.5, T_short])
    tau_sol, Tt_sol = sol


    # check validity
    if 0 <= tau_sol <= 1:
        return tau_sol, Tt_sol
    else:
        return None, None