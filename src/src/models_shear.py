
import numpy as np
R_GAS = 8.314

def eta0_arrhenius(T, eta0_ref, Q, T_ref):
    return eta0_ref * np.exp((Q / R_GAS) * (1.0/T - 1.0/T_ref))

def eta_carreau_yasuda(gammadot, T, eta_inf, lam, a, n, eta0_ref, Q, T_ref):
    gammadot = np.asarray(gammadot, dtype=float)
    eta0T = eta0_arrhenius(T, eta0_ref, Q, T_ref)
    return eta_inf + (eta0T - eta_inf) * np.power(1.0 + np.power(lam * gammadot, a), (n - 1.0) / a)
def tau_from_gammadot(gammadot, T, pars):
    eta = eta_carreau_yasuda(gammadot, T, pars['eta_inf'], pars['lambda'], pars['a'], pars['n'], pars['eta0_ref'], pars['Q'], pars['T_ref'])
    return eta * gammadot, eta
