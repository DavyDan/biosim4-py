from datetime import datetime, timedelta

import Simulator


start = datetime.now()
# from moviemaker import makemovie
#hello to my self 1004
class Brain:
    def __init__(self):
        pass
    def probe():
        pass
# test multi vs single proc
  

def main():
    sim = Simulator.Simulator(
        population= 1000,
        genomelength= 4,
        arenasize= 128,
        corecount= 4,
        multiproc= False,
        stepcount= 10,
        gencount= 10 )
    
    sim.buginit(sim)
    date_times = sim.simloop()

    endtime = datetime.now() - start

    differences = [(date_times[i] - date_times[i - 1]) for i in range(1, len(date_times))]
    total_difference = sum(differences, timedelta())
    average_difference = total_difference / len(differences)

    print(f'endtime: {endtime.microseconds//1000}, time per gen: {average_difference.microseconds//1000}')


if __name__ == '__main__':
    main()
    # makemovie()
    