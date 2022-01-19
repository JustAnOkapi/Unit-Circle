from sympy import *
from prettytable import PrettyTable, ALL

circle = PrettyTable(["Degree", "Radian", "sin()", "cos()"]) 
circle.hrules = ALL
for deg in [0,30,45,60,90,120,135,150,180,210,225,240,300,315,330]:
    rad = Rational(deg, 180) * pi
    circle.add_row([deg, pretty(rad), pretty(sin(rad)), pretty(cos(rad))]) 
    
pprint(circle)
# idk how this took 2 hours to do