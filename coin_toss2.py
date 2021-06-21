from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
from minorminer import find_embedding
import matplotlib.pyplot as plt
import pandas as pd

coins = 10

h = {68:0,69:0}

# sampler = DWaveSampler(solver = 'DW_2000Q_6')
sampler = DWaveSampler()
# target = sampler.nodelist
# print(target)
# print(h)

# embedding = find_embedding(h, target)

# sampler = EmbeddingComposite(sampler)
sample = sampler.sample_ising(h,{}, num_reads = 10000)

print(sample.record)

count = [0]*coins
tot = 0
for s in sample:
    # print(s)
    tot+=1
print(tot)
for s in sample.record:
    for i in range(coins):
        if s[0][i] > 0:
            count[i] += (1*s[2])

print(count)

plt.figure(figsize=(15, 4))
pd.Series(count).hist(bins=50)
plt.title('Figure 1: distribution of number of occurences of 1 for each spins.')
plt.xlim(0, 10000)
plt.savefig('dist_adv')