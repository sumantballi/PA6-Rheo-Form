
import os, sys, json, numpy as np
BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.append(os.path.join(BASE, "src"))
from models_shear import tau_from_gammadot
from models_bending import M_from_kappa_dot
def load_params():
    with open(os.path.join(BASE, "cases", "materials_pa6.json"), "r") as f:
        return json.load(f)
def material_response(state, params=None):
    if params is None: params = load_params()
    shear_pars = params["shear"]; bend_pars = params["bending"]
    gdot = np.atleast_1d(state.get("shear_rate", 0.0))
    T = float(state.get("T", 503.15))
    kdot = np.atleast_1d(state.get("kappa_dot", 0.0))
    tau, eta = tau_from_gammadot(gdot, T, shear_pars)
    M = M_from_kappa_dot(kdot, T, bend_pars)
    return {"tau12": float(np.squeeze(tau)), "eta": float(np.squeeze(eta)), "M_per_width": float(np.squeeze(M))}
