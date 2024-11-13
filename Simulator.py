from datetime import datetime
import random
import numpy as np
import multiprocessing
from numba import njit

from Bug import Bug


class Simulator():
    def __init__(self,population, genomelength, arenasize, corecount, multiproc, stepcount, gencount):
        self.population = population
        self.genomelength = genomelength
        self.arenasize = arenasize
        self.stepcount = stepcount
        self.gencount = gencount

        self.corecount = corecount
        self.multiproc = multiproc

        self.grid = np.zeros((arenasize,arenasize),int)
        
    def simloop(self):
        #init the sim
        gencount = self.gencount
        stepcount = self.stepcount
        #sim loop
        generationtime = []
        for generation in range(gencount):
            # print(f'beggining generation: {generation}')
            generationtime.append(datetime.now())
        #generation loop
            for step in range(stepcount):
                self.executemove()
        print(f'simulation complete')
        return generationtime
    def findempty(self):
        arenasize = self.arenasize -1
        while True:
            x = random.randint(0,arenasize)
            y = random.randint(0,arenasize)
            if self.grid[(x,y)] == 0:
                break
        return (x,y)
    def update(self, loc, bugid, z = 0):
        bugs = self.bugs
        if z == False:
            self.grid[loc] = bugid
        else:
            self.grid[bugs[bugid-1].loc] = 0
            self.grid[loc] = bugid

    def buginit(self,sim):
        bugs = []
        for i in range(self.population):
            coords = self.findempty()
            bugs.append(Bug(id=i+1,loc = coords))
        self.bugs = bugs
    
    def setupmoves(self):
        movelist = []
        for bug in self.bugs:
            movelist.append(bug.move())
        return movelist
    @staticmethod
    def worker(bug):
        return bug.move()  # Call the move method and return the result
    # @staticmethod
    def setupmovesmulti(self):
        corecount = self.corecount
        with multiprocessing.Pool(processes=corecount) as pool:
            # Map the worker function to the bugs
            results = pool.map(self.worker, self.bugs)
        return results

    def executemove(self):
        arenasize = self.arenasize
        if self.multiproc:
            movelist = self.setupmovesmulti()
        else:
            movelist = self.setupmoves()
        for id,direction,coords in movelist:
            x, y = coords
            if 0 <= x < arenasize and 0 <= y < arenasize:
                if self.grid[coords]==0:
                    self.update(coords,id,z=True)
                    self.bugs[id-1].loc = coords
                    self.bugs[id-1].direction = direction