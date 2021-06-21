import dimod
from dwave.system import DWaveSampler, EmbeddingComposite
from minorminer import find_embedding
from dwave.embedding import embed_qubo, unembed_sampleset
from dwave.embedding.chain_strength import uniform_torque_compensation
import dwave.inspector

# Create sampler and record it's graph structure
solver = EmbeddingComposite(DWaveSampler(solver = "Advantage_system1.1"))
# _,target_edgelist,target_adjacency = solver.structure

#State the problem
Hdict={1: 100.0, 2: 0.0, 3: 0.0, 4: 0.0, 5: -100.0}
Jdict={(1, 2): -100.0, (1, 3): 0.0, (1, 4): 0.0, 
        (1, 5): 0.0, (2, 1): 0.0, (2, 3): -100.0, 
        (2, 4): 0.0, (2, 5): 0.0, (3, 1): 0.0, (3, 2): 0.0, 
        (3, 4): -100.0, (3, 5): 0.0, (4, 1): 0.0, (4, 2): 0.0, 
        (4, 3): 0.0, (4, 5): -100.0, (5, 1): 0.0, (5, 2): 0.0, 
        (5, 3): 0.0, (5, 4): 0.0}
bqm = dimod.BQM.from_ising(Hdict, Jdict)
chain_st = uniform_torque_compensation(bqm)
print(chain_st)

# Find an embedding to map logical problem onto QPU
# emb = find_embedding(Q,target_edgelist)
# print(emb)
# embedded_qubo = embed_qubo(Q,emb,target_adjacency)
# print(embedded_qubo)

#Sample the embedded problem
# sample2 = solver.sample(bqm, chain_strength= chain_st, num_reads = 1000)
# print(sample2)
sampler_exact = dimod.ExactSolver()
response = sampler_exact.sample_ising(Hdict,Jdict)
# print(response)


# dwave.inspector.show(sample2)

#Unembed the solution
# unembedded = unembed_sampleset(sample2, emb, bqm)