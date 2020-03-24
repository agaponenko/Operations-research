from pulp import *
x11 = pulp.LpVariable("x11", lowBound=0)
x21 = pulp.LpVariable("x21", lowBound=0)
x31 = pulp.LpVariable("x31", lowBound=0)
x41 = pulp.LpVariable("x41", lowBound=0)
x12 = pulp.LpVariable("x12", lowBound=0.7)
x22 = pulp.LpVariable("x22", lowBound=0.1)
x32 = pulp.LpVariable("x32", lowBound=0, upBound=0.2)
x42 = pulp.LpVariable("x42", lowBound=0.04)
x13 = pulp.LpVariable("x13", lowBound=0.5)
x23 = pulp.LpVariable("x23", lowBound=0)
x33 = pulp.LpVariable("x33", lowBound=0, upBound=0.3)
x43 = pulp.LpVariable("x4", lowBound=0.06)
problem = pulp.LpProblem('0',pulp.LpMaximize)
problem += (2 - 0.8*x11 -0.6*x21 - 0.4*x31 - x41) + (3 - 0.8*x12 -0.6*x22 - 0.4*x32 - x42) + (4 - 0.8*x13 -0.6*x23 - 0.4*x33 - x43), "Функция цели"
problem += x11 + x21 +x31 + x41 == 1, "1"
problem += x12 + x22 +x32 + x42 == 1, "2"
problem += x13 + x23 +x33 + x43 == 1, "3"
problem.solve()
print ("Результат:")
for variable in problem.variables():
    print (variable.name, "=", variable.varValue)
print ("Значение целевой функции:", value(problem.objective))