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