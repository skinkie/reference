import highspy
import numpy as np

inf = highspy.kHighsInf
h = highspy.Highs()
h.setOptionValue('output_flag', False)
h.addVars(2, np.array([-inf, -inf]), np.array([inf, inf]))
h.changeColsCost(2, np.array([0, 1]), np.array([0, 1], dtype=np.double))
num_cons = 2
lower = np.array([2, 0], dtype=np.double)
upper = np.array([inf, inf], dtype=np.double)
num_new_nz = 4
starts = np.array([0, 2])
indices = np.array([0, 1, 0, 1])
values = np.array([-1, 1, 1, 1], dtype=np.double)
h.addRows(num_cons, lower, upper, num_new_nz, starts, indices, values)

"""
h = highspy.Highs()

x0 = h.addVar(0, 4)
x1 = h.addVar(1, 7)

h.addConstr(5 <=   x0 + 2*x1 <= 15)
h.addConstr(6 <= 3*x0 + 2*x1)

h.minimize(x0 + x1)

# x0 = h.addVar(lb = 0, ub = 1)
# x1 = h.addVar(lb=0, ub=1)
# x2 = h.addVar(lb=0, ub=1)
# x3 = h.addVar(lb=0, ub=1)

# h.addConstr(x0 == 1)
# h.addConstr(x1 == 1)
# h.addConstr(x2 == 1)
# h.addConstr(x3 == 1)

# h.minimize(x0 + x1 + x2 + x3)

# h.minimize(x0)

h.run()

solution = h.getSolution()
basis = h.getBasis()
info = h.getInfo()
model_status = h.getModelStatus()
print('Model status = ', h.modelStatusToString(model_status))
print()
print('Optimal objective = ', info.objective_function_value)
print('Iteration count = ', info.simplex_iteration_count)
print('Primal solution status = ', h.solutionStatusToString(info.primal_solution_status))
print('Dual solution status = ', h.solutionStatusToString(info.dual_solution_status))
print('Basis validity = ', h.basisValidityToString(info.basis_validity))
"""