from reid_data import \
    (A, B, C, D, DELTA_A, DELTA_B,
     DELTA_C, DELTA_D, DELTA_HR298, DELTA_SR298)
from reid_thermodynamics import (get_Cp, calc_delta_hr, calc_delta_sr, calc_delta_gibbs, calc_equilibrium_constant)

T = 873.15

Cp = get_Cp(T, A, B, C, D)

Cp

delta_hr = calc_delta_hr(T, DELTA_HR298, DELTA_A, DELTA_B, DELTA_C, DELTA_D)

delta_hr

delta_sr = calc_delta_sr(T, DELTA_SR298, DELTA_A, DELTA_B, DELTA_C, DELTA_D)

delta_sr

delta_gibbs = calc_delta_gibbs(T, delta_hr, delta_sr, multireaction=False)

delta_gibbs

Keq = calc_equilibrium_constant(T, delta_gibbs, R = 8.314)

Keq