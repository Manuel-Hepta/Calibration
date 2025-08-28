# Manual calibration Equations

## Load

$$
T_{\text{tissue}} = T_{\text{rad}} =\left( \frac{2 \cdot V_{\text{rad-tot}} - 4 - \text{RadOffset0} - \text{RadOffsetchange} \cdot T_{\text{housing}}}{\text{Radslope0} + \text{RadSlopeChange} \cdot T_{\text{housing}}} \right) + T_{\text{housing}}
$$

$$
T_{\text{housing}} = V_{\text{housing}} \cdot \text{HousingSlope} + \text{HousingOffset}
$$

## Antenna

$$
T_{\text{tissue}} = \frac{T_{\text{rad}}}{1- \text{AL}} - \frac{\text{AL} \cdot T_{\text{antenna}}}{1- \text{AL}}
$$  

$$
T_{\text{antenna}} = V_{\text{spike}} \cdot \text{AntennaSlope} + \text{AntennaOffset}
$$

## Load + Cable

$$
T_{\text{tissue}} = \frac{T_{\text{rad}}}{1- \text{CL}} - \frac{\text{CL} \cdot T_{\text{cable}}}{1- \text{CL}}
$$

## Antenna + Cable

$$
T_{\text{tissue}} = \frac{1}{1- \text{AL}}\left(\frac{T_{\text{rad}} - T_{\text{cable}} \cdot \text{CL}}{1 - \text{CL}}\right) - \frac{\text{AL} \cdot T_{\text{antenna}}}{1- \text{AL}}
$$

## T_cable and CL

$$
T_{\text{rad}} = T_{\text{tissue}}(1 - \text{CL}) + T_{\text{cable}} \cdot \text{CL}
$$

$$
(T_{\text{rad}}^H - T_{\text{rad}}^C) = (T_{\text{tissue}}^H - T_{\text{tissue}}^C)(1 - \text{CL}) = (T_{\text{bath}}^H - T_{\text{bath}}^C)(1 - \text{CL})
$$

$$
\text{CL} = - \frac{(T_{\text{rad}}^H - T_{\text{rad}}^C) - (T_{\text{bath}}^H - T_{\text{bath}}^C)}{T_{\text{bath}}^H - T_{\text{bath}}^C} = - \frac{T_{\text{rad}}^H - T_{\text{rad}}^C - 25}{25}
$$

$$
T_{\text{cable}} = \frac{T_{\text{rad}}^H - T_{\text{bath}}^H (1 - \text{CL})}{\text{CL}}
$$

## Diode Switch

$$
\tau_{\text{cable}} = (1 - \text{CL})
$$

$$
T_{\text{end\_of\_cable}} = T_{\text{hous}} \cdot \tau_{\text{cable}} + T_{\text{cable}} \cdot (1 - \tau_{\text{cable}})
$$

$$
T_{\text{short}} = T_{\text{end\_of\_cable}} \cdot \tau_{\text{cable}} + T_{\text{cable}} \cdot (1 - \tau_{\text{cable}})
$$

$$
T_{\text{short}} = T_{\text{hous}} \cdot \tau_{\text{cable}}^2 + T_{\text{cable}} \cdot (1 - \tau_{\text{cable}}^2)
$$

Solve for $\tau_{\text{cable}}$:

$$
\tau_{\text{cable}} = \pm \sqrt{\frac{T_{\text{short}} - T_{\text{cable}}}{T_{\text{hous}} - T_{\text{cable}}}}
$$

**Condition for real solutions:**

$$
\frac{T_{\text{short}} - T_{\text{cable}}}{T_{\text{hous}} - T_{\text{cable}}} \ge 0
$$

**If we do not know $T_{\text{cable}}$:**

The equation becomes more difficult, but we can use, for example, the hot bath measurement:

Rename the two unknowns ($T_{\text{cable}} = T$ and $\tau_{\text{cable}} = \tau$)

$$
T_{\text{rad}} = T_{\text{bath}} \cdot \tau + T \cdot (1-\tau)
$$

Solve for T:

$$
T = \frac{T_{\text{rad}} - T_{\text{bath}} \cdot \tau}{1 - \tau}
$$

$$
T_{\text{short}} = T_{\text{hous}} \cdot \tau^2 + \frac{T_{\text{rad}} - T_{\text{bath}} \cdot \tau}{1 - \tau} \cdot (1 - \tau^2) \\
= T_{\text{hous}} \cdot \tau^2 + (T_{\text{rad}} - T_{\text{bath}} \cdot \tau) \cdot (1 + \tau)
$$

$$
(T_{\text{bath}} - T_{\text{hous}}) \tau^2 + (T_{\text{bath}} - T_{\text{rad}}) \tau + (T_{\text{short}} - T_{\text{rad}}) = 0
$$

Solve for $\tau$:

$$
\tau = \frac{-(T_{\text{bath}} - T_{\text{rad}}) \pm \sqrt{(T_{\text{bath}} - T_{\text{rad}})^2 - 4 (T_{\text{bath}} - T_{\text{hous}})(T_{\text{short}} - T_{\text{rad}})}}{2 (T_{\text{bath}} - T_{\text{hous}})}
$$
