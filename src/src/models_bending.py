
import numpy as np
R_GAS = 8.314
def Kb_T(T, Kb0, Qb, T_ref):
    return Kb0 * np.exp((Qb / R_GAS) * (1.0/T - 1.0/T_ref))
def M_from_kappa_dot(kappa_dot, T, pars):
    kappa_dot = np.asarray(kappa_dot, dtype=float)
    Kb = Kb_T(T, pars['Kb0'], pars['Qb'], pars['T_ref'])
    return Kb * np.power(kappa_dot, pars['m'])
