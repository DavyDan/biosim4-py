import random
import struct
from numba import njit

class Bug:
    def __init__(self, id = int, loc = tuple, genome = bytes, genomelength = int, direction = None, nnet = None):
        self.id = id
        self.alive = True
        self.loc = loc
        self.age = 0
        self.genome = genome
        self.genomelength = genomelength
        self.nnet = nnet
        self.direction = direction
    def nnetinit():
        pass
    def genomeinit(self, genomelength):
        def geneinit():
            r = random.randint
            sourcetype = r(0,1)  
            sourceid = r(0,127)
            source = (sourcetype << 7) | sourceid
            desttype = r(0,1)
            destid = r(0,127)
            dest = (desttype << 7) | destid
            weight = r(0,255)
            reserved = 0
            gene = struct.pack('BBBB',source,dest,weight,reserved) #gene
            return gene
        genome = b''.join([geneinit() for _ in range(genomelength)])
        self.genome = genome
    @njit
    def cpu_intensive_task(self, n=int):
        if n <= 1:
            return n
        else:
            return self.cpu_intensive_task(n - 1) + self.cpu_intensive_task(n - 2)


    def move(self,dir = None):
        self.cpu_intensive_task(n=15)
        dir = random.randint(0,7)
        match dir:
            case 0:  # move S
                newcoord = (self.loc[0] - 1, self.loc[1])  # Move south
            case 1:  # move N
                newcoord = (self.loc[0] + 1, self.loc[1])  # Move north
            case 2:  # move NE
                newcoord = (self.loc[0] + 1, self.loc[1] + 1)  # Move northeast
            case 3:  # move NW
                newcoord = (self.loc[0] + 1, self.loc[1] - 1)  # Move northwest
            case 4:  # move E
                newcoord = (self.loc[0], self.loc[1] + 1)  # Move east
            case 5:  # move W
                newcoord = (self.loc[0], self.loc[1] - 1)  # Move west
            case 6:  # move SE
                newcoord = (self.loc[0] - 1, self.loc[1] + 1)  # Move southeast
            case 7:  # move SW
                newcoord = (self.loc[0] - 1, self.loc[1] - 1)  # Move southwest
            case _:  # If dir is 8 or invalid, do not move
                newcoord = self.loc  # Stay in place
        return((self.id,dir,newcoord))