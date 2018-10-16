#Standard Atmosphere Properties Calculator

##################################################
## Given the height, evaluate atm properties
##################################################
## GPL License
##################################################
## Author: Francesco Fabio Semeraro
## Copyright: Copyright 2018, pyrocket
## Credits: US atmosphere 1976
## License: GPL
## Version: 0.1
## 
## Email: semerarofabio@gmail.com
##
##################################################


import numpy as np
import matplotlib as plt

#constant definition

g_e = 9.80665 #[m/s*s]
#value at latitude 45.5° h = 0.

#value at latitude 45.5° h = 0.

r_e = 6356766 #[m]
R_air = 287.05 #[J/(kg * K)]
gamma = 1.4

#gradients of the linearly segmented T-h profile
lambda0 = -0.0065 #[K/m]
lambda1 = 0.0
lambda2 = 1.0
lambda3 = 2.8
lambda4 = 0.0
lambda5 = -2.8
lambda6 = -2.0
#lambda7 = 

#stratosphere height and reference values
hstrat = 11000
pstrat = 22632
rhostrat = 0.3639
Tstrat = 216.65

#mesosphere height
hmes = 20000;


h = int(input("select the Height: "))

#g equation
#TO DO, implement Lambert equation
#r_e depends on latitude
g = g_e * (r_e /(r_e + h))**2


def pyatm(h):
    if h <= hstrat:
        p_e = 101325;
        rho_e = 1.225;
        T_e = 15 + 273.15;

    # ISA equations for troposhpere
        p = p_e * (1 + lambda0*h/T_e)**(-g_e/(R_air*lambda0));
        rho = rho_e * (1 + lambda0*h/T_e)**(-1-g_e/(R_air*lambda0))
        T = T_e + lambda0*h
    
    if h <= hmes:
    #stratosphere equations
        p = pstrat * np.exp(-g_e/(R_air * Tstrat) * (h - hstrat))
        rho = rhostrat * np.exp(-g_e/(R_air * Tstrat) * (h - hstrat))
        T = Tstrat

    return p,rho,T

atm = pyatm(h)
p = atm[0]
rho = atm[1]
T = atm[2]

#speed of sound calculation
a = np.sqrt(gamma * R_air * T)


print("\nHeight: ", h, "m")
print("Pressure: " ,np.round(p,2), "Pa")
print("Density: ", np.round(rho,5), "kg/m3")
print("Temperature: ", np.round(T, 2), "K")
print("Gravity constant: ", np.round(g, 5), "m/s^2")
print("Speed of sound: ", np.round(a, 5), "m/s")
