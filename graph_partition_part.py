import networkx as nx
from collections import defaultdict
from itertools import combinations
from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
import math

gamma = 80
G = nx.gnp_random_graph(40, 0.2)

Q = defaultdict(int)

for u, v in G.edges:
    Q[(u,v)] += 1

chain_strength = gamma*len(G.nodes)

sampler = EmbeddingComposite(DWaveSampler())
response = sampler.sample_qubo(Q,
                               chain_strength=chain_strength,
                               num_reads=10,
                               label='Example - Graph Partitioning')

print(response)