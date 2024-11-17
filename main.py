from datetime import datetime, timedelta

from simulator import Simulator
from animation import Animation
start = datetime.now()

  

def main():
    print(f'sim start {datetime.now()}')
#init sim
    
    sim = Simulator(
        population= 1000,
        genomelength= 4,
        arenasize= 128,
        corecount= 4,
        multiproc= False,
        stepcount= 300,
        gencount= 10 )
#init bugs and then run sim
    sim.buginit(sim)
    sim.simloop()
#animate sim
    anim = Animation(
            sim.arenasize,
            screen_size=800,
            cell_size= 40)
    anim.create_gif_from_grids(sim.metagridstates)
#time sim
    generationtimes = sim.generationtimes
    endtime = datetime.now() - start
    # differences = [(date_times[i] - date_times[i - 1]) for i in range(1, len(date_times))]
    # total_difference = sum(differences, timedelta())
    # average_difference = total_difference / len(differences)

    print(f'sim complete {datetime.now} \n endtime: {endtime}')
  

if __name__ == '__main__':
    main()
    
    # makemovie()
    