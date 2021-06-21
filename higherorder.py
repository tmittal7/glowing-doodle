import dimod

J = {('a','b','c'): 1}

bqm = dimod.make_quadratic(J, strength= 1, vartype= dimod.SPIN)

print(bqm)