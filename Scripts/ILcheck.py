import numpy as np
import pylab as pl
import IsingLattice as il


lattice_size = 4

fig = pl.figure()
left_figure = fig.add_subplot(1,3,1)
middle_figure = fig.add_subplot(1,3,2)
right_figure = fig.add_subplot(1,3,3)

#plot the low energy state in the left figure
lattice = il.IsingLattice(lattice_size, lattice_size)
lattice.lattice = np.ones((lattice_size,lattice_size))
left_figure.matshow(lattice.lattice)
left_figure.set_title("Energy Minimum")
left_figure.xaxis.set_ticks([])
left_figure.yaxis.set_ticks([])

target_energy = -2.0*lattice_size*lattice_size
actual_energy = lattice.energy()
target_magnetisation = 1.0*lattice_size*lattice_size
actual_magnetisation = lattice.magnetisation()
left_figure.text(0, 4, "Expected E = {}".format(target_energy))
left_figure.text(0, 4.4, "Actual E = {}".format(actual_energy))
left_figure.text(0, 4.8, "Expected M = {}".format(target_magnetisation))
left_figure.text(0, 5.2, "Actual M = {}".format(actual_magnetisation))

#plot the "perfectly disordered", high energy, state in the right figure
high_energy_latticerow1 = [1, -1]*int(lattice_size/2)
high_energy_latticerow2 = [-1, 1]*int(lattice_size/2)
lattice.lattice = np.array([high_energy_latticerow1, high_energy_latticerow2]*int(lattice_size/2))
right_figure.matshow(lattice.lattice)
right_figure.set_title("Energy Maximum")
right_figure.xaxis.set_ticks([])
right_figure.yaxis.set_ticks([])
target_energy = 2.0*lattice_size*lattice_size
actual_energy = lattice.energy()
target_magnetisation = 0.0
actual_magnetisation = lattice.magnetisation()
right_figure.text(0, 4, "Expected E = {}".format(target_energy))
right_figure.text(0, 4.4, "Actual E = {}".format(actual_energy))
right_figure.text(0, 4.8, "Expected M = {}".format(target_magnetisation))
right_figure.text(0, 5.2, "Actual M = {}".format(actual_magnetisation))

#plot a random configuration in the middle figure
lattice.lattice = np.random.choice([1,-1], (lattice_size,lattice_size))
#lattice.lattice = np.ones((lattice_size, lattice_size))
middle_figure.matshow(lattice.lattice)
middle_figure.set_title("Random Configuration")
middle_figure.xaxis.set_ticks([])
middle_figure.yaxis.set_ticks([])
target_energy = -1.0*np.sum(np.multiply(lattice.lattice, np.roll(lattice.lattice, 1, 0)))
target_energy -= 1.0*np.sum(np.multiply(lattice.lattice, np.roll(lattice.lattice, 1, 1)))
actual_energy = lattice.energy()
target_magnetisation = 1.0*np.sum(lattice.lattice)
actual_magnetisation = lattice.magnetisation()
middle_figure.text(0, 4, "Expected E = {}".format(target_energy))
middle_figure.text(0, 4.4, "Actual E = {}".format(actual_energy))
middle_figure.text(0, 4.8, "Expected M = {}".format(target_magnetisation))
middle_figure.text(0, 5.2, "Actual M = {}".format(actual_magnetisation))

#draw the whole figure on the screen
pl.show()
