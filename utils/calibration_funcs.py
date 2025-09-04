import numpy as np

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

# def solve_tau_and_Tcable_v2(T_rad, T_short, T_hous, T_bath, T_diode, tau_d_minus):
#     """
#     Solve for tau_T and T_cable using the updated diode-inclusive equations.

#     Equation system:
#       L = (T_rad - T_diode * (1 - tau_d_minus)) / tau_d_minus
#       (T_hous - T_bath) * tau^2 + (L - T_bath) * tau + (L - T_short) = 0

#     Then:
#       T_cable = (L - T_bath * tau) / (1 - tau)

#     Returns only solutions with 0 <= tau <= 1.
#     """
#     # Step 1: effective measurement term
#     L = (T_rad - T_diode * (1 - tau_d_minus)) / tau_d_minus

#     # Quadratic coefficients
#     a = (T_hous - T_bath)
#     b = (L - T_bath)
#     c = (L - T_short)

#     discriminant = b**2 - 4*a*c
#     if discriminant < 0:
#         raise ValueError("No real solution for tau_T (negative discriminant).")

#     sqrt_disc = np.sqrt(discriminant)

#     # Two possible roots
#     tau1 = (-b + sqrt_disc) / (2*a) if a != 0 else None
#     tau2 = (-b - sqrt_disc) / (2*a) if a != 0 else None

#     results = []
#     for tau in [tau1, tau2]:
#         if tau is not None and 0 <= tau <= 1 and tau != 1:
#             T_cable = (L - T_bath * tau) / (1 - tau)
#             results.append({"tau_T": tau, "T_total": T_cable})

#     return results