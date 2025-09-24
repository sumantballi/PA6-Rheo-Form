
Small project showing temperature- & rate-dependent **shear** (Carreau–Yasuda + Arrhenius) and **rheo-bending** (power-law + Arrhenius) for molten PA6.  
Outputs: viscosity isotherms (η–γ̇), bending isotherms (M–κ̇), Fast vs Slow M–κ, and a solver-style **material hook**.

## What to look for
- η–γ̇: shear-thinning; 260 °C curve below 230 °C below 200 °C.  
- M–κ̇: M increases with κ̇; hotter is lower.  
- Fast vs Slow (M–κ): Fast > Slow at same κ.  
- CLT vs molten: ratio ≈ 10²–10³ at 230 °C, κ̇≈0.5 s⁻¹.

## Folder map
- `src/` – code (`main.py`, models, plotting)
- `cases/` – parameters (`materials_pa6.json`)
- `data/` – optional CSVs
- `figs/` – generated plots
- `form_cases/dome/` – `material_hook.py` (solver-style call)

## Scope
Constitutive modelling + figures + a solver-ready hook.  
No full contact forming simulation.

## 🔍 Results (quick look)

**CLT vs molten:** [`figs/CLT_vs_molten_ratio.txt`](figs/CLT_vs_molten_ratio.txt)

<p align="center">
  <img src="figs/eta_overlay_200_230_260C.png" alt="η–γ̇ overlay (200/230/260 °C)" width="45%">
  <img src="figs/bending_overlay_200_230_260C_Nmm.png" alt="M–κ̇ overlay (200/230/260 °C)" width="45%">
</p>
<p align="center">
  <img src="figs/M_kappa_Fast_vs_Slow_260C_Nmm.png" alt="M–κ Fast vs Slow (260 °C)" width="45%">
</p>

**CLT vs molten (summary):** see `figs/CLT_vs_molten_ratio.txt`.


## Key Methods & Equations

**Shear (Carreau–Yasuda, with anchored Arrhenius):**  
\[
\eta(\dot\gamma,T)=\eta_\infty + \big(\eta_0(T)-\eta_\infty\big)\,\Big[1+(\lambda\,\dot\gamma)^a\Big]^{\frac{n-1}{a}},\quad
\eta_0(T)=\eta_{0,\mathrm{ref}}\exp\!\Big(\frac{Q}{R}\big(\tfrac{1}{T}-\tfrac{1}{T_\mathrm{ref}}\big)\Big)
\]

**Rheo-bending (viscous, rate- and temperature-dependent):**  
\[
M = K_b(T)\,\dot\kappa^{\,m},\qquad
K_b(T)=K_{b0}\exp\!\Big(\frac{Q_b}{R}\big(\tfrac{1}{T}-\tfrac{1}{T_\mathrm{ref}}\big)\Big),\qquad
D_\text{eq}=\frac{M}{\dot\kappa}
\]

**CLT vs molten contrast (wrinkling relevance):** compare room-T \(D_\text{room}\) to \(D_\text{eq}(T,\dot\kappa)\) at forming conditions.

**Primary references:**  
- Carreau–Yasuda model for polymer melts (shear-thinning); Arrhenius temperature dependence (anchored at \(T_\mathrm{ref}\)).  
- Brands, D. (2025). *Forming simulations for unidirectional thermoplastic composites* (PhD thesis). Focus on wrinkling sensitivity to molten bending + in-plane rheology; motivates rate/temperature-aware constitutive inputs.

## 🎯 Relevance to PhD topic
- **Constitutive**: temperature- & rate-dependent shear (Carreau–Yasuda + Arrhenius) and **rheo-bending** \(M=K_b(T)\,\dot\kappa^m\).
- **Findings**: molten bending stiffness at forming conditions is ≈ **10²–10³×** lower than room-T CLT → explains wrinkle suppression with CLT inputs.
- **Implementation**: `form_cases/dome/material_hook.py` mirrors a UMAT/VUMAT/material-plugin call (same law → solver).
