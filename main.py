import numpy as np
import itertools as it
from gol_modules.params import CELL_DIMENSION as CD
import gol_modules.cells as c
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.style as mplstyle
import matplotlib.animation as animation

def main():    
  MATRIX = np.random.randint(2, size=(CD['WIDTH'], CD['HEIGHT']))
  #MATRIX = c.gen_matrix_ones()
  np_MATRIX = np.asarray(MATRIX)

  plt.rcParams["figure.figsize"] = [6.00, 3.50]
  plt.rcParams["figure.autolayout"] = True
  fig, ax = plt.subplots()
  
  def update(i):
    c.loop_matrix(np_MATRIX)
    #MATRIX = np.random.randint(2, size=(CD['WIDTH'], CD['HEIGHT']))
    ax.imshow(MATRIX)
    ax.set_axis_off()

  mpl.rcParams['path.simplify'] = True
  mpl.rcParams['path.simplify_threshold'] = 1.0
  mplstyle.use('fast')

  ani = animation.FuncAnimation(fig, update, interval=500, frames=len(MATRIX)-1) #, frames=1)
  plt.draw()
  plt.show()


if __name__ == "__main__":
  main()