import numpy as np

statenames, populations, electoral_votes = np.loadtxt('state_info.csv', delimiter=',', unpack=True, dtype='string', skiprows=1, usecols=(0, 1, 2))

populations = np.array(populations, dtype='int')
electoral_votes = np.array(electoral_votes, dtype='int')

avg_evs_per_person = 538.0 / np.sum(populations)
norm_evs_per_person = ((1.0*electoral_votes) / populations) / avg_evs_per_person

args = np.argsort(norm_evs_per_person)

for i in range(len(statenames)):
    print statenames[args[i]], norm_evs_per_person[args[i]]
