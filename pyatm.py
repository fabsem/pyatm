#Calcolo proprietà atmosfera standard

import numpy as np
import matplotlib as plt

#constant definition

g_e = 9.8071 #[m/s*s]
R_air = 287.05 #[J/(kg * K)]

lambda1 = -0.0065;

#stratosphere height
hstrat = 11000;

#mesosphere height
hmes = 20000;

h = int(input("select the Height: "))

def pyatm(h):
    if h <= hstrat:
        p_e = 101325;
        rho_e = 1.225;
        T_e = 15 + 273.15;

    # ISA equations for troposhpere
    p = p_e * (1 + lambda1*h/T_e)**(-g_e/(R_air*lambda1));
    rho = rho_e * (1 + lambda1*h/T_e)**(-1-g_e/(R_air*lambda1))
    T = T_e + lambda1*h

    return p,rho,T

atm = pyatm(h)
p = np.round(atm[0])
rho = np.round(atm[1])
T = np.round(atm[2])

print("\nHeight: ", h, "m")
print("Pressure: " ,p, "Pa")
print("Density: ", rho, "kg/m3")
print("Temperature: ", T, "K")
