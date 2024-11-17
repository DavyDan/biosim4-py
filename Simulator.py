from datetime import datetime
import random
import numpy as np
import multiprocessing
import pygame

from bug import Bug

class Simulator():
    def __init__(self,population, genomelength, arenasize, corecount, multiproc, stepcount, gencount):
        self.population = population
        self.genomelength = genomelength
        self.arenasize = arenasize
        self.stepcount = stepcount
        self.gencount = gencount

        self.corecount = corecount
        self.multiproc = multiproc

        self.metagridstates = []
        self.gridstates = []
        
        self.grid = np.zeros((arenasize,arenasize),int)
        
        self.generationtimes = []
        

    def findempty(self):
        arenasize = self.arenasize -1
        while True:
            x = random.randint(0,arenasize)
            y = random.randint(0,arenasize)
            if self.grid[(x,y)] == 0:
                break
        return (x,y)
    def update(self, loc, bugid, z = 0):
        if z == False:
            self.grid[loc] = bugid
        else:
            bugs = self.bugs
            self.grid[bugs[bugid-1].loc] = 0
            self.grid[loc] = bugid

    def buginit(self,sim):
        bugs = []
        for i in range(self.population):
            coords = self.findempty()
            bugs.append(Bug(index=i+1,loc = coords))
            self.update(coords,i)
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

    def executemove(self, frames):
        # print(f"Frame {frames}: Grid before update:\n{self.grid}")
        arenasize = self.arenasize
        if self.multiproc:
            movelist = self.setupmovesmulti()
        else:
            movelist = self.setupmoves()
        for index,direction,coords in movelist:
            x, y = coords
            if 0 <= x < arenasize and 0 <= y < arenasize:
                if self.grid[coords]==0:
                    self.update(coords,index,z=True)
                    self.bugs[index-1].loc = coords
                    self.bugs[index-1].direction = direction
        self.gridstates.append(np.copy(self.grid))
        # print(f"Frame {frames}: Grid after update:\n{self.grid}")
        
        
    def genloop(self,generation):
        for step in range(self.stepcount):
            self.executemove(generation)
    def simloop(self):
        #init the sim
        for generation in range(self.gencount):
            self.generationtimes.append(datetime.now())
            self.genloop(generation)
            self.metagridstates.append(self.gridstates)
            self.gridstates.clear
    