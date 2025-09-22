
import numpy as np
def impose_curvature_history(t, kappa_final, T_total):
    return (t / T_total) * kappa_final
def simulate_bending_response(kappa_final=2.0, T_process=1.0, T=503.15, bending_pars=None, bending_model=None, n_steps=200):
    t = np.linspace(0.0, T_process, n_steps)
    kappa = impose_curvature_history(t, kappa_final, T_process)
    dt = t[1] - t[0] if n_steps > 1 else T_process
    kappa_dot = np.gradient(kappa, dt)
    M = bending_model(kappa_dot, T, bending_pars)
    return t, kappa, M
