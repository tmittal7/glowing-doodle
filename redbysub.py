import dimod

def R_qubo(x1, x2, x3):
    '''
        The penalty function returned by this function is the same that's produced by
​
        qubo_reduction = dimod.make_quadratic({('x1', 'x2', 'x3'): 1}, 1, vartype='BINARY')
    '''
    z = x1*x2
    return z*x3 + x1*x2 -2*(x1 + x2)*z + 3*z
def R_ising(s1, s2, s3):
    '''
          Attempt to implement the penalty function for reducing a higher order ising model.
​
          Notes:
              When using make_quadratic
                v = dimod.make_quadratic({('s1', 's2', 's3'): 1}, 1, vartype='SPIN')
              this penalty model is returned (for sz=s1*s3, with an offset of 2)
                -0.5*(sz + s1 + s3) - aux + 0.5*(s1*s3 + s1*sz + s3*sz) +s1*aux + s3*aux + sz*aux
​
              _________________________________________________
              The ocean docs use the penalty function (for sz = s1s2)
                3 + s1*s2 - 2*(s1 + s2)*sz - s1 - s2 + 2*sz
​
              The ocean docs specify the BQM as
                bqm = min{ sz*s3 + M(3 + s1*s2 - 2*(s1 + s2)*sz - s1 - s2 + 2*sz) }         (M=1 in the paper)
​
          Question:
            How is the auxilliary variable (aux) calculated?
​
    '''
    sz = s1*s3
    aux = 1         # guess. Not sure how aux is calculated??

    p_model_from_make_quad = -0.5*(sz + s1 + s3) - aux + 0.5*(s1*s3 + s1*sz + s3*sz) +s1*aux + s3*aux + sz*aux
    p_model_from_docs = sz*s3 + 3 + s1 * s2 - 2 * (s1 + s2) * sz - s1 - s2 + 2 * sz
    return p_model_from_make_quad
def evaluate_qubo():
    '''
        Print the truth table for the qubo penalty model
    '''
    x1_values = [0, 0, 0, 0, 1, 1, 1, 1]
    x2_values = [0, 0, 1, 1, 0, 0, 1, 1]
    x3_values = [0, 1, 0, 1, 0, 1, 0, 1]
    print("QUBO")
    print("x1  x2   x3    z    E")
    print("--------------------")
    for i in range(8):
        z = x1_values[i]*x2_values[i]
        E = R_qubo(x1_values[i], x2_values[i], x3_values[i])
        print("{}    {}    {}    {}    {}".format(x1_values[i], x2_values[i], x3_values[i],z, E))

def evaluate_ising():
    '''
        Print the truth table for the ising penalty model
    '''
    s1_values = [-1,-1,-1,-1,1,1,1,1]
    s2_values = [-1,-1,1,1,-1,-1,1,1]
    s3_values = [-1,1,-1,1,-1,1,-1,1]

    print("\nISING")
    print("s1    s2     s3     z     E")
    print("--------------------------------")
    for i in range(8):
        z = s1_values[i] * s2_values[i]
        E = R_ising(s1_values[i], s2_values[i], s3_values[i])
        print("{}    {}    {}    {}    {}".format(s1_values[i], s2_values[i], s3_values[i], z, E))
# Print out ising model for s1*s2*s3
v = dimod.make_quadratic({('s1', 's2', 's3'): 1}, 1, vartype='SPIN')
print(v)
# Compare to truth table
evaluate_ising()