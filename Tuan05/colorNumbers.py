"""
Restricted license - for non-production use only - expires 2023-10-25
Gurobi Optimizer version 9.5.2 build v9.5.2rc0 (win64)
Thread count: 6 physical cores, 12 logical processors, using up to 12 threads
Optimize a model with 0 rows, 0 columns and 0 nonzeros
Model fingerprint: 0xf9715da1
Coefficient statistics:
  Matrix range     [0e+00, 0e+00]
  Objective range  [0e+00, 0e+00]
  Bounds range     [0e+00, 0e+00]
  RHS range        [0e+00, 0e+00]
Presolve time: 0.01s
Presolve: All rows and columns removed
Iteration    Objective       Primal Inf.    Dual Inf.      Time
       0    0.0000000e+00   0.000000e+00   0.000000e+00      0s

Solved in 0 iterations and 0.01 seconds (0.00 work units)      
Optimal objective  0.000000000e+00
"""

# import
import gurobipy as gp
from gurobipy import GRB

model = gp.Model("color_8_2")

# lb, up, vtype, name
# nhi phan, nguyen, lien tuc(thuc)
x1 = model.addVar(vtype = GRB.BINARY)
x2 = model.addVar(vtype = GRB.BINARY)
x3 = model.addVar(vtype = GRB.BINARY)
x4 = model.addVar(vtype = GRB.BINARY)
x5 = model.addVar(vtype = GRB.BINARY)
x6 = model.addVar(vtype = GRB.BINARY)
x7 = model.addVar(vtype = GRB.BINARY)
x8 = model.addVar(vtype = GRB.BINARY)

model.addConstr(x1 + x2 + x3 <=2)
model.addConstr(x1 + x2 + x3 >=1)

model.addConstr(x1 + x3 + x4 <=2)
model.addConstr(x1 + x3 + x4 >=1)

model.addConstr(x1 + x4 + x5 <=2)
model.addConstr(x1 + x4 + x5 >=1)

model.addConstr(x1 + x5 + x6 <=2)
model.addConstr(x1 + x5 + x6 >=1)

model.addConstr(x1 + x6 + x7 <=2)
model.addConstr(x1 + x6 + x7 >=1)

model.addConstr(x1 + x7 + x8 <=2)
model.addConstr(x1 + x7 + x8 >=1)

model.addConstr(x2 + x3 + x5 <=2)
model.addConstr(x2 + x3 + x5 >=1)

model.addConstr(x2 + x4 + x6 <=2)
model.addConstr(x2 + x4 + x6 >=1)

model.addConstr(x2 + x5 + x7 <=2)
model.addConstr(x2 + x5 + x7 >=1)

model.addConstr(x2 + x6 + x8 <=2)
model.addConstr(x2 + x6 + x8 >=1)

model.addConstr(x3 + x4 + x7 <=2)
model.addConstr(x3 + x4 + x7 >=1)

model.addConstr(x3 + x5 + x8 <=2)
model.addConstr(x3 + x5 + x8 >=1)

model.setObjective(0, sense = GRB.MAXIMIZE)

model = gp.Model()
model.optimize()