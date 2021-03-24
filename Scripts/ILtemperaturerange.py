from IsingLattice import *
from matplotlib import pylab as pl
import numpy as np

n_rows = 8
n_cols = 8
il = IsingLattice(n_rows, n_cols)
il.lattice = np.ones((n_rows, n_cols))
spins = n_rows*n_cols
runtime = 350000
times = range(runtime)
temps = np.arange(0.5, 5.0, 0.05)
energies = []
magnetisations = []
energysq = []
magnetisationsq = []
for t in temps:
    for i in times:
        if i % 100 == 0:
            print(t, i)
        energy, magnetisation = il.montecarlostep(t)
    aveE, aveE2, aveM, aveM2, n_cycles = il.statistics()
    energies.append(aveE)
    energysq.append(aveE2)
    magnetisations.append(aveM)
    magnetisationsq.append(aveM2)
    #reset the IL object for the next cycle
    il.E = 0.0
    il.E2 = 0.0
    il.M = 0.0
    il.M2 = 0.0
    il.n_cycles = 0
fig = pl.figure()
enerax = fig.add_subplot(2,1,1)
enerax.set_ylabel("Energy per spin")
enerax.set_xlabel("Temperature")
enerax.set_ylim([-2.1, 2.1])
magax = fig.add_subplot(2,1,2)
magax.set_ylabel("Magnetisation per spin")
magax.set_xlabel("Temperature")
magax.set_ylim([-1.1, 1.1])
enerax.plot(temps, np.array(energies)/spins)
magax.plot(temps, np.array(magnetisations)/spins)
pl.show()

final_data = np.column_stack((temps, energies, energysq, magnetisations, magnetisationsq))
np.savetxt("8x8new.dat", final_data)
