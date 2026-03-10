import pyomo.environ as pyo
import pandas as pd

materials = pd.read_csv("materials.csv", index_col="rm_id")
orders    = pd.read_csv("orders.csv",   index_col="order_id")

MAT      = materials.index.tolist()
ELEMENTS = ["Si", "Fe", "Mg"]

# DEL 1 Produksjonsplan for 1 charge (20 tonn)


target_weight = 20_000  # kg

kjemikrav = {
    "Si": (6.5, 7.5),
    "Fe": (0.0, 0.5),
    "Mg": (0.3, 0.45),
}

m = pyo.ConcreteModel()

# Beslutningsvariabler
m.x = pyo.Var(MAT, domain=pyo.NonNegativeReals)

# Objektivfunksjon: 
def objective(model):
    return sum(materials.loc[i, "value"] * model.x[i] for i in MAT)

m.obj = pyo.Objective(rule=objective, sense=pyo.minimize)

# Constraint: summen av alle materialer = ønsket vekt
def total_vekt(model):
    return sum(model.x[i] for i in MAT) == target_weight

m.total_vekt = pyo.Constraint(rule=total_vekt)

# Constraints: kjemisk sammensetning
def kjemi_min(model, element):
    lo = kjemikrav[element][0]
    return sum(materials.loc[i, f"{element}_perc"] / 100 * model.x[i] for i in MAT) >= lo / 100 * target_weight

def kjemi_max(model, element):
    hi = kjemikrav[element][1]
    return sum(materials.loc[i, f"{element}_perc"] / 100 * model.x[i] for i in MAT) <= hi / 100 * target_weight

m.kjemi_min = pyo.Constraint(ELEMENTS, rule=kjemi_min)
m.kjemi_max = pyo.Constraint(ELEMENTS, rule=kjemi_max)

# Ny constraint, lager tilgjengelighet
def tilgjengelighet(model, i):
    return model.x[i] <= materials.loc[i, "stock"] * 1000  # tonn → kg

m.tilgjengelighet = pyo.Constraint(MAT, rule=tilgjengelighet)

# Solve
solver = pyo.SolverFactory("glpk")
result = solver.solve(m)

# Results Del 1
print("DEL 1 – Produksjonsplan for 1 charge (20 tonn)")
print(f"Status: {result.solver.status} | {result.solver.termination_condition}")
print(f"Total kostnad: {pyo.value(m.obj):,.2f} kr")

print("\nMaterialer brukt:")
print(f"{'rm_id':>8}  {'kg brukt':>12}  {'kostnad':>12}")
for i in MAT:
    kg = pyo.value(m.x[i])
    if kg > 0.01:
        kost = materials.loc[i, "value"] * kg
        print(f"{i:>8}  {kg:>12.2f}  {kost:>12.2f}")

total_kg = sum(pyo.value(m.x[i]) for i in MAT)
print("\nKjemisk sammensetning:")
for element in ELEMENTS:
    andel = sum(materials.loc[i, f"{element}_perc"] / 100 * pyo.value(m.x[i]) for i in MAT) / total_kg * 100
    lo, hi = kjemikrav[element]
    print(f"  {element}: {andel:.3f}%  (krav: {lo}% – {hi}%)")


# DEL 2 Produksjonsplan for alle ordre i orders.csv

ORDERS = orders.index.tolist()

m2 = pyo.ConcreteModel()

# Beslutningsvariabler, kg av hvert materiale per ordre
m2.x = pyo.Var(ORDERS, MAT, domain=pyo.NonNegativeReals)

# Objektivfunksjon: minimer total materialkostnad over alle ordre
def objective2(model):
    return sum(
        materials.loc[i, "value"] * model.x[o, i]
        for o in ORDERS for i in MAT
    )

m2.obj = pyo.Objective(rule=objective2, sense=pyo.minimize)

# Constraint total vekt per ordre = bestilt mengdem
def total_vekt2(model, o):
    return sum(model.x[o, i] for i in MAT) == orders.loc[o, "weight"] * 1000 #tonn gjort opp til kg

m2.total_vekt = pyo.Constraint(ORDERS, rule=total_vekt2)

# Constraint, kjemisk sammensetning per ordre
def kjemi_min2(model, o, element):
    lo = orders.loc[o, f"{element}_min"]
    vekt_kg = orders.loc[o, "weight"] * 1000
    return sum(materials.loc[i, f"{element}_perc"] / 100 * model.x[o, i] for i in MAT) >= lo / 100 * vekt_kg

def kjemi_max2(model, o, element):
    hi = orders.loc[o, f"{element}_max"]
    vekt_kg = orders.loc[o, "weight"] * 1000
    return sum(materials.loc[i, f"{element}_perc"] / 100 * model.x[o, i] for i in MAT) <= hi / 100 * vekt_kg

m2.kjemi_min = pyo.Constraint(ORDERS, ELEMENTS, rule=kjemi_min2)
m2.kjemi_max = pyo.Constraint(ORDERS, ELEMENTS, rule=kjemi_max2)

# Constraint, samlet bruk av hvert materiale på tvers av alle ordre må være mindre enn lageret
def tilgjengelighet2(model, i):
    return sum(model.x[o, i] for o in ORDERS) <= materials.loc[i, "stock"] * 1000

m2.tilgjengelighet = pyo.Constraint(MAT, rule=tilgjengelighet2)

# Solve
result2 = solver.solve(m2)

# Results Del 2
print("\nDEL 2 – Produksjonsplan for alle ordre")
print(f"Status: {result2.solver.status} | {result2.solver.termination_condition}")
print(f"Total kostnad alle ordre: {pyo.value(m2.obj):,.2f} kr")

for o in ORDERS:
    vekt_kg = orders.loc[o, "weight"] * 1000
    ordrekost = sum(materials.loc[i, "value"] * pyo.value(m2.x[o, i]) for i in MAT)
    print(f"\nOrdre {o}  ({orders.loc[o, 'weight']} tonn)  kostnad: {ordrekost:,.2f} kr")
    print(f"  {'rm_id':>8}  {'kg brukt':>12}")
    for i in MAT:
        kg = pyo.value(m2.x[o, i])
        if kg > 0.01:
            print(f"  {i:>8}  {kg:>12.2f}")
    print("  Kjemisk sammensetning:")
    for element in ELEMENTS:
        andel = sum(materials.loc[i, f"{element}_perc"] / 100 * pyo.value(m2.x[o, i]) for i in MAT) / vekt_kg * 100
        lo = orders.loc[o, f"{element}_min"]
        hi = orders.loc[o, f"{element}_max"]
        print(f"    {element}: {andel:.3f}%  (krav: {lo}% – {hi}%)")
