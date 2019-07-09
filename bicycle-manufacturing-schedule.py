#Bicycle Manufacturing Schedule
from pulp import *

# The challenge is to maximise the profit by producing an optimum number of each type of bicycle
# A - "Mountain Bike", profit margin of $45 per unit
# B - "Street Bike", profit margin of $60 per unit
# C - "Racing Bike", profit margin of $55 per unit
# D - "Commuter bike", profit margin of $50 per unit 
#
model = LpProblem("Profit Maximising", LpMaximize)

#We can't sell half a bike, so the category for each bicycle type is an integer.
#A >= 0, B >= 0, C >= 0, D >= 0 : Input (Changing) cells
A = LpVariable('A', lowBound=0, cat='Integer')
B = LpVariable('B', lowBound=0, cat='Integer')
C = LpVariable('C', lowBound=0, cat='Integer')
D = LpVariable('D', lowBound=0, cat='Integer')

#Our objective is to maximise the profit
model += 45 * A + 60 * B + 55 * C + 50 * D, "Total Profit"

#Setup the constraints (parts available in stock)
wheels = 2 * A + 2 * B + 2 * C + 2 * D
alloy_chassis = 1 * A + 1 * C
steel_chassis = 1 * B + 1 * D
hub_gears = 1 * A + 1 * D
derailleur_gears = 1 * B + 1 * C

#Add constraints to the model
model += wheels <=180
model += alloy_chassis <= 40
model += steel_chassis <= 60
model += hub_gears <= 50
model += derailleur_gears <= 40

#Print the problem
print (model)

#Solve the problem
model.solve()
print ("Status : ", LpStatus[model.status])

#Print our changing cells
print ("Units of Mountain Bike   = ", A.varValue)
print ("Units of Street Bike     = ", B.varValue)
print ("Units of Racing Bike     = ", C.varValue)
print ("Units of Commuter Bike   = ", D.varValue)

#Print our objective function value - Result (Target) cell
print ("Total Profit             = ", value(model.objective))