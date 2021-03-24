import numpy as np

class IsingLattice:

    E = 0.0
    E2 = 0.0
    M = 0.0
    M2 = 0.0

    n_cycles = 0
    
    ignored_cyc = 225000

    def __init__(self, n_rows, n_cols):
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.lattice = np.random.choice([-1,1], size=(n_rows, n_cols))

    def energy(self):       
        energy = 0.0
        s_ilattice = self.lattice
        s_jlattice1 = np.roll(s_ilattice, 1, axis=0) #down
        s_jlattice2 = np.roll(s_ilattice, -1, axis=0) #up
        s_jlattice3 = np.roll(s_ilattice, 1, axis=1) #right
        s_jlattice4 = np.roll(s_ilattice, -1, axis=1) #left
        s_jlatticesum = s_jlattice1 + s_jlattice2 + s_jlattice3 + s_jlattice4
        energy += np.sum(np.multiply(s_ilattice, s_jlatticesum))*(-0.5)
        return energy

    def magnetisation(self):
        magnetisation = np.sum(self.lattice)
        return magnetisation

    def montecarlostep(self, T):
        # a single Monte Carlo step
        energy0 = self.energy()
        magnet0 = self.magnetisation()
        #the following two lines will select the coordinates of the random spin
        random_i = np.random.choice(range(0, self.n_rows))
        random_j = np.random.choice(range(0, self.n_cols))
        if self.lattice[random_i][random_j] == -1:
            self.lattice[random_i][random_j] += 2
        else:
            self.lattice[random_i][random_j] -= 2
        energy1 = self.energy()
        magnet1 = self.magnetisation()
        energy_d = energy1 - energy0
        #the following line will choose a random number in the range [0,1) 
        random_number = np.random.random()
        if energy_d > 0 and random_number > np.e**(-energy_d/T):
            if self.lattice[random_i][random_j] == -1:
                self.lattice[random_i][random_j] += 2
            else:
                self.lattice[random_i][random_j] -= 2
            energy1 = energy0
            magnet1 = magnet0
        if self.n_cycles > self.ignored_cyc:
            self.E += energy1
            self.E2 += energy1**2
            self.M += magnet1
            self.M2 += magnet1**2
        self.n_cycles += 1
        return energy1, magnet1
        
    def statistics(self):
        if self.n_cycles > 0:
            avg_cycles = self.n_cycles - self.ignored_cyc
            avg_e = self.E/avg_cycles
            avg_e2 = self.E2/avg_cycles
            avg_m = self.M/avg_cycles
            avg_m2 = self.M2/avg_cycles
            return avg_e, avg_e2, avg_m, avg_m2, avg_cycles
        else:
            return self.E, self.E2, self.M, self.M2, avg_cycles
       