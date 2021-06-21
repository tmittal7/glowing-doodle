from dwave.system import DWaveSampler
from dwave.system import LazyFixedEmbeddingComposite
import dwave.inspector

sampler = LazyFixedEmbeddingComposite(DWaveSampler())

Q = {(1,1):1, (2,2):0}

sample = sampler.sample_qubo(Q, num_reads = 10)

print(sample)
dwave.inspector.show(sample)