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
T_{\text{tissue}} = \frac{T_{\text{rad}}}{\tau_{\text{A}}} - \frac{(1 - \tau_{\text{A}}) \cdot T_{\text{antenna}}}{\tau_{\text{A}}}
$$  

$$
T_{\text{antenna}} = V_{\text{spike}} \cdot \text{AntennaSlope} + \text{AntennaOffset}
$$

## Load + Cable

$$
T_{\text{rad}} = T_{\text{tissue}}\cdot\tau_{\text{C}} + T_{\text{cable}} \cdot (1-\tau_{\text{C}})
$$

$$
T_{\text{tissue}} = \frac{T_{\text{rad}}}{\tau_{\text{C}}} - \frac{(1 - \tau_{\text{C}}) \cdot T_{\text{cable}}}{\tau_{\text{C}}}
$$

$ \tau_{\text{C}} \sim 0.60$ , $T_{\text{cable}} \sim 25º\text{C}$

## Load + Cable + Diplexer

$$
\tau_{\text{T}} \sim \tau_{\text{D}} \cdot \tau_{\text{C}} \, \text{ , given that: } \, T_{\text{diplexer}} \sim T_{\text{cable}} 
$$

$$
T_{\text{rad}} = T_{\text{tissue}}\cdot\tau_{\text{T}} + T_{\text{cable}} \cdot (1-\tau_{\text{T}})
$$

$$
T_{\text{tissue}} = \frac{T_{\text{rad}}}{\tau_{\text{T}}} - \frac{(1 - \tau_{\text{T}}) \cdot T_{\text{cable}}}{\tau_{\text{T}}}
$$

$ \tau_{\text{D}} \sim 0.90$ , $ \tau_{\text{C}} \sim 0.60$ ,  $ \tau_{\text{T}} \sim 0.54$

## Antenna + Cable

$$
T_{\text{tissue}} = \frac{1}{\tau_{\text{A}}} \left( \frac{T_{\text{rad}} - T_{\text{cable}} \cdot (1 - \tau_{\text{C}})}{\tau_{\text{C}}} \right) - \frac{(1 - \tau_{\text{A}}) \cdot T_{\text{antenna}}}{\tau_{\text{A}}}
$$

## T_cable and tau_C

$$
T_{\text{rad}} = T_{\text{tissue}} \cdot \tau_{\text{C}} + T_{\text{cable}} \cdot (1 - \tau_{\text{C}})
$$

$$
(T_{\text{rad}}^H - T_{\text{rad}}^C) = (T_{\text{tissue}}^H - T_{\text{tissue}}^C) \cdot \tau_{\text{C}} = (T_{\text{bath}}^H - T_{\text{bath}}^C) \cdot \tau_{\text{C}}
$$

$$
\tau_{\text{C}} = \frac{T_{\text{rad}}^H - T_{\text{rad}}^C}{T_{\text{bath}}^H - T_{\text{bath}}^C} = \frac{T_{\text{rad}}^H - T_{\text{rad}}^C}{25}
$$

$$
T_{\text{cable}} = \frac{T_{\text{rad}}^H - T_{\text{bath}}^H \cdot \tau_{\text{C}}}{1 - \tau_{\text{C}}}
$$

## Diode Switch

$$
T_{\text{end\_of\_cable}} = T_{\text{hous}} \cdot \tau_{\text{C}} + T_{\text{cable}} \cdot (1 - \tau_{\text{C}})
$$

$$
T_{\text{short}} = T_{\text{end\_of\_cable}} \cdot \tau_{\text{C}} + T_{\text{cable}} \cdot (1 - \tau_{\text{C}})
$$

$$
T_{\text{short}} = T_{\text{hous}} \cdot \tau_{\text{C}}^2 + T_{\text{cable}} \cdot (1 - \tau_{\text{C}}^2)
$$

Solve for $\tau_{\text{C}}$:

$$
\tau_{\text{C}} = \pm \sqrt{\frac{T_{\text{short}} - T_{\text{cable}}}{T_{\text{hous}} - T_{\text{cable}}}}
$$

**Condition for real solutions:**

$$
\frac{T_{\text{short}} - T_{\text{cable}}}{T_{\text{hous}} - T_{\text{cable}}} \ge 0
$$

**If we do not know $T_{\text{cable}}$:**

Rename the two unknowns for easier reading: $T_{\text{cable}} = T$ and $\tau_{\text{C}} = \tau$

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
