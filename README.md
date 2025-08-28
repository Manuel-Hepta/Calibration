# Manual calibration Equations

## Load

$$
T_{tissue} = T_{rad} =\left( \frac{2 \cdot V_{rad-tot}-4 - RadOffset0 - RadOffsetchange \cdot T_{housing}}{Radslope0 + RadSlopeChange \cdot T_{housing}} \right) + T_{housing} 
$$

$$
 T_{housing} = \ V_{housing} \cdot HousingSlope + HousingOffset 
$$

## Antenna

$$ 
T_{tissue} = \frac{T_{rad}}{1- AL} - \frac{AL \cdot T_{antenna}}{1- AL} 
$$  

$$
T_{antenna} = \ V_{spike} \cdot AntennaSlope + AntennaOffset 
$$

## Load + Cable

$$ 
T_{tissue} = \frac{T_{rad}}{1- CL} - \frac{CL \cdot T_{cable}}{1- CL} 
$$ 

## Antenna + Cable

$$
T_{tissue} = \frac{1}{1- AL}\left(\frac{T_{rad} - T_{cable}\cdot CL}{1 - CL}\right) - \frac{AL \cdot T_{antenna}}{1- AL} 
$$


## T_cable and CL 

$$
T_{rad} = T_{tissue}(1 - CL) +  T_{cable}\cdot CL
$$

$$
(T_{rad}^H - T_{rad}^C) = (T_{tissue}^H - T_{tissue}^C)(1 - CL) = (T_{bath}^H - T_{bath}^C)(1 - CL)
$$

$$
CL = - \frac{(T_{rad}^H - T_{rad}^C) - (T_{bath}^H - T_{bath}^C)}{T_{bath}^H - T_{bath}^C} = - \frac{T_{rad}^H - T_{rad}^C - 25}{25}
$$

$$
T_{cable} = \frac{T_{rad}^H-T_{bath}^H(1-CL)}{CL}
$$

