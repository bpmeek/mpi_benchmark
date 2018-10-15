#mpi benchmark
from mpi4py import MPI

wt = MPI.Wtime()

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

N = 100000000
n1 = N/4
n2 = 2*n1
n3 = 3*n1
if rank == 0:
    s = sum(range(n1))
    comm.send(s,dest=4,tag=11)
elif rank == 1:
    s = sum(range(n1,n2))
    comm.send(s,dest=4, tag=11)
elif rank == 2:
    s = sum(range(n2,n3))
    comm.send(s,dest=4, tag=11)    
elif rank == 3:
    s = sum(range(n3,N))
    comm.send(s,dest=4, tag=11)
elif rank == 4:
    s1 = comm.recv(source=0, tag=11)
    s2 = comm.recv(source=1, tag=11)
    s3 = comm.recv(source=2, tag=11)
    s4 = comm.recv(source=3, tag=11)
    print s1+s2+s3+s4
    print(MPI.Wtime() - wt)
