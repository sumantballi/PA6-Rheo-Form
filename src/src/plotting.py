
import matplotlib.pyplot as plt
import numpy as np
import os
def plot_eta_isotherms(gammadot_grid, T_list, shear_pars, tau_eta_fn, outpath):
    for T in T_list:
        T_C = T - 273.15
        tau, eta = tau_eta_fn(gammadot_grid, T, shear_pars)
        plt.figure(); plt.loglog(gammadot_grid, eta)
        plt.xlabel("Shear rate $\\dot{\\gamma}$ [1/s]"); plt.ylabel("Viscosity $\\eta$ [Pa·s]")
        plt.title(f"PA6 Melt Viscosity vs Shear Rate (T={T_C:.0f} °C)")
        plt.grid(True, which="both"); plt.savefig(os.path.join(outpath, f"eta_isotherm_{int(T)}K.png"), dpi=200, bbox_inches="tight"); plt.close()
def plot_tau_isotherms(gammadot_grid, T_list, shear_pars, tau_eta_fn, outpath):
    for T in T_list:
        T_C = T - 273.15
        tau, eta = tau_eta_fn(gammadot_grid, T, shear_pars)
        plt.figure(); plt.loglog(gammadot_grid, tau)
        plt.xlabel("Shear rate $\\dot{\\gamma}$ [1/s]"); plt.ylabel("Shear stress $\\tau$ [Pa]")
        plt.title(f"PA6 Shear Stress vs Shear Rate (T={T_C:.0f} °C)")
        plt.grid(True, which="both"); plt.savefig(os.path.join(outpath, f"tau_isotherm_{int(T)}K.png"), dpi=200, bbox_inches="tight"); plt.close()
def plot_bending_rate_temp(kappa_dot_grid, T_list, bending_pars, M_fn, outpath):
    for T in T_list:
        T_C = T - 273.15
        M = M_fn(kappa_dot_grid, T, bending_pars); M_Nmm = 1e3 * M
        plt.figure(); plt.semilogx(kappa_dot_grid, M_Nmm)
        ax = plt.gca(); ax.ticklabel_format(axis='y', style='plain', useOffset=False)
        plt.xlabel("Curvature rate $\\dot{\\kappa}$ [1/s]"); plt.ylabel("Moment per width $M$ [N·mm/m]")
        plt.title(f"Rheo-Bending: M vs $\\dot{{\\kappa}}$ (T={T_C:.0f} °C)")
        plt.grid(True, which="both", axis='both'); plt.savefig(os.path.join(outpath, f"bending_isotherm_{int(T)}K_Nmm.png"), dpi=200, bbox_inches="tight"); plt.close()
def plot_M_kappa_curves(kappa, M, label, outpath, fname):
    M_Nmm = 1e3 * M; import os
    plt.figure(); plt.plot(kappa, M_Nmm); ax = plt.gca(); ax.ticklabel_format(axis='y', style='plain', useOffset=False)
    plt.xlabel("Curvature $\\kappa$ [1/m]"); plt.ylabel("Moment per width $M$ [N·mm/m]"); plt.title(label + " (N·mm/m)")
    plt.grid(True); plt.savefig(os.path.join(outpath, f"{fname}_Nmm.png"), dpi=200, bbox_inches="tight"); plt.close()
