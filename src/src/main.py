import os, json
import numpy as np
from models_shear import tau_from_gammadot
from models_bending import M_from_kappa_dot, Kb_T
from fem_plate import simulate_bending_response
from plotting import (
    plot_eta_isotherms, plot_tau_isotherms,
    plot_bending_rate_temp, plot_M_kappa_curves
)

def run_all():
    here = os.path.dirname(__file__)
    ROOT = os.path.abspath(os.path.join(here, ".."))
    OUT = os.path.join(ROOT, "figs")
    os.makedirs(OUT, exist_ok=True)

    with open(os.path.join(ROOT, "cases", "materials_pa6.json"), "r") as f:
        P = json.load(f)

    shear = P["shear"]
    bend  = P["bending"]
    Droom = P.get("clt", {}).get("D_room", 1.0e-2)

    # Grids & temperatures
    gammadot = np.logspace(-2, 2, 200)
    kappa_dot = np.logspace(-3, 1, 200)
    T_list = [473.15, 503.15, 533.15]  # 200, 230, 260 °C

    # Shear isotherms
    plot_eta_isotherms(gammadot, T_list, shear, tau_from_gammadot, OUT)
    plot_tau_isotherms(gammadot, T_list, shear, tau_from_gammadot, OUT)

    # Bending isotherms (N·mm/m on Y, log X)
    plot_bending_rate_temp(kappa_dot, T_list, bend, M_from_kappa_dot, OUT)

    # Time-history bending responses
    cases = [
        ("Slow, 200°C", 2.0, 10.0, 473.15),
        ("Fast, 200°C", 2.0,  1.0, 473.15),
        ("Slow, 260°C", 2.0, 10.0, 533.15),
        ("Fast, 260°C", 2.0,  1.0, 533.15),
    ]
    for label, kappa_final, Tproc, T in cases:
        t, kappa, M = simulate_bending_response(kappa_final, Tproc, T, bend, M_from_kappa_dot, 300)
        fname = f"M_kappa_{label.replace(', ','_').replace('°','degC')}"
        plot_M_kappa_curves(kappa, M, f"PA6 Bending Response – {label}", OUT, fname)

    # CLT vs molten contrast number
    # CLT vs molten contrast at a chosen reference rate (dimensionless)
    kdot_ref = 0.5  # 1/s (pick a representative forming rate)
    Kb_230C = Kb_T(503.15, bend["Kb0"], bend["Qb"], bend["T_ref"])     # N·m·s^m/m
    D_eq = Kb_230C * (kdot_ref ** (bend["m"] - 1.0))                   # N·m/m
    ratio = Droom / max(D_eq, 1e-30)
    with open(os.path.join(OUT, "CLT_vs_molten_ratio.txt"), "w") as fh:
        fh.write(f"D_room/D_eq at 230C, kappa_dot={kdot_ref:.2f}/s  ~  {ratio:.2e}\n")
    print("All figures generated.")

if __name__ == "__main__":
    run_all()
