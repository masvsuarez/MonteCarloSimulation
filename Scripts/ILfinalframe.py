from IsingLattice import *
from matplotlib import pylab as pl
import numpy as np

n_rows = 16
n_cols = 16
temperature = 4.0
runtime = 150000
il = IsingLattice(n_rows, n_cols)
spins = n_rows*n_cols
times = range(runtime)
E = []
M = []
for i in times:
    if i % 100 == 0:
        print("Step ", i)
    energy, magnetisation = il.montecarlostep(temperature)
    E.append(energy)
    M.append(magnetisation)
fig = pl.figure()
matax = fig.add_subplot(3,1,1)
matax.matshow(il.lattice)
enerax = fig.add_subplot(3,1,2)
enerax.set_ylabel("Energy per spin")
enerax.set_xlabel("Monte Carlo Steps")
enerax.set_ylim([-2.1, 2.1])
magax = fig.add_subplot(3,1,3)
magax.set_ylabel("Magnetisation per spin")
magax.set_xlabel("Monte Carlo Steps")
magax.set_ylim([-1.1, 1.1])
enerax.plot(times, np.array(E)/spins)
magax.plot(times, np.array(M)/spins)
pl.show()
#np.savetxt("8x8.dat")