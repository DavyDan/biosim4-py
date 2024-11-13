import numpy as np
import matplotlib.ticker as mat
from matplotlib.animation import FuncAnimation, PillowWriter
import matplotlib.pyplot as plt
import os


def makemovie():
    
    frame_files = sorted([f for f in os.listdir('.turtle/simframes') if f.endswith('.npy')])

    frames = [np.load(f'.turtle/simframes/{file}') for file in frame_files]

    fig, ax = plt.subplots(figsize=(20,20))
    im = ax.imshow(frames[0],cmap="bone_r")
    plt.tick_params(axis='both', left=False, top=False, right=False, bottom=False, labelleft=False, labeltop=False, labelright=False, labelbottom=False)

    def update(frame):
        im.set_data(frame)
        return [im]
        
    anim = FuncAnimation(fig,update, frames=frames, interval=33)
    video = anim.save('botspread.gif', writer=PillowWriter(fps=30),dpi=300)
    # plt.show()
makemovie()