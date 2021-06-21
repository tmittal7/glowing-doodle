import dimod
from dwave.system import DWaveSampler, EmbeddingComposite
import dwave.inspector

# Modifiable parameters
num_qubits = 5                        # Number of qubits in our chain
fm_qubit_bias = [1, 0, 0, 0, -1]      # List of biases to apply to each qubit in our chain
fm_coupler_strength = -1               # The coupling we want to apply to two adjacent qubits
num_reads = 1000                         # The number of times the QPU is sampled

h = fm_qubit_bias
J = {} 


for i in range(num_qubits-1):
    J[(i, i+1)] = fm_coupler_strength

print(J)

# Submit the problem to the QPU
# sampler = EmbeddingComposite(DWaveSampler(solver={'qpu': True}))
# response = sampler.sample_ising(h, J, num_reads=num_reads)

#exact solver
sampler_exact = dimod.ExactSolver()
response = sampler_exact.sample_ising(h,J)

print(response)

# dwave.inspector.show(response)