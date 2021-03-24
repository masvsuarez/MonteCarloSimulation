import time
import IsingLattice as il

#using a relatively big lattice of 25x25 so that we get more accurate timing data
n_rows = 25
n_cols = 25

lattice = il.IsingLattice(n_rows, n_cols)
#record the time at which we start running
start_time = time.clock()
#do 2000 monte carlo steps
for i in range(2000):
    lattice.montecarlostep(1.0)
#record the time at which we stop running
end_time = time.clock()

#work out how many seconds the loop took, and print it
elapsed_time = end_time - start_time
print("Took {}s".format(elapsed_time))
