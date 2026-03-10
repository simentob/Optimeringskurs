import pyomo.environ as pyo

produktA = {
    "konstnad_per_enhet" : 10,
    "Inntekt_per_enhet" : 20,
    "CO2_per_enhet" : 0.45,
    "Tidsbruk_maling" : 10
}
produktB = {
    "konstnad_per_enhet" : 22,
    "Inntekt_per_enhet" : 28,
    "CO2_per_enhet" : 0.12,
    "Tidsbruk_maling" : 10
}

m = pyo.ConcreteModel()

# Beslutningsvariabler
m.a = pyo.Var(domain=pyo.PositiveIntegers, initialize=0)
m.b = pyo.Var(domain=pyo.PositiveIntegers, initialize=0)

# Objektivfunkjon
def objective(model):

    inntekt_A = produktA["Inntekt_per_enhet"] - produktA["konstnad_per_enhet"]
    inntekt_B = produktB["Inntekt_per_enhet"] - produktB["konstnad_per_enhet"]

    return inntekt_A*model.a + inntekt_B*model.b

m.obj = pyo.Objective(rule=objective, sense=pyo.maximize)


# Constraints
def total_produksjons_kostnad(model):
    return produktA["konstnad_per_enhet"]*model.a + produktB["konstnad_per_enhet"]*model.b <= 10000000

def total_co2_utslipp(model):
    return produktA["CO2_per_enhet"]*model.a + produktB["CO2_per_enhet"]*model.b <= 20000

def maksimale_timer(model):
    return produktA["Tidsbruk_maling"]*model.a + produktB["Tidsbruk_maling"]*model.b <= 8750*60

m.total_produksjons_kostnad = pyo.Constraint(rule=total_produksjons_kostnad)
m.total_co2_utslipp = pyo.Constraint(rule=total_co2_utslipp)
m.maksimale_timer = pyo.Constraint(rule=maksimale_timer)

# Solve
solver = pyo.SolverFactory("glpk")
result = solver.solve(m, tee=True)

# Results
print("\nStatus:", result.solver.status)
print("Termination condition:", result.solver.termination_condition)

print(f"\n Optimal mengde produsert:")
print(f"produkt a: {pyo.value(m.a)}")
print(f"produkt b: {pyo.value(m.b)}")






