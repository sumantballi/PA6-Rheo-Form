
def compare_clt_vs_molten(D_room, Kb_T_value):
    return D_room / max(Kb_T_value, 1e-30)
