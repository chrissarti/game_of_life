import numpy as np
import itertools as it
from gol_modules.params import CELL_DIMENSION as CD
import gol_modules.cells as c
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.style as mplstyle



def main():    
  MATRIX = np.random.randint(2, size=(CD['WIDTH'], CD['HEIGHT']))
  #MATRIX = c.gen_matrix_ones()
  """  
  # Method 1
  plt.ion()
  fig = plt.figure()
  ax = fig.add_subplot(111)
  """
  # Method 2
  fig = plt.figure( figsize=(8,6))
  plt.title(f"Cellular automata")

  mpl.rcParams['path.simplify'] = True
  mpl.rcParams['path.simplify_threshold'] = 1.0
  mplstyle.use('fast')

  np_MATRIX = np.asarray(MATRIX)

  plt.imshow(np_MATRIX)
  plt.pause(2)
  
  #for _ in it.repeat(None, 100):
  while True:
    """    
    # Method 1
    ax.matshow(np_MATRIX)
    plt.draw()
    plt.pause(0.00000000001)
    c.loop_matrix(np_MATRIX)
    print(f"----------- Generation: {GENERATION}\n")
    GENERATION += 1
    """
    # method 2
    c.loop_matrix(np_MATRIX)
    plt.pause(0.5)
    plt.imshow(np_MATRIX)
    
    
  
"""
  for _ in it.repeat(None, 500):
    c.loop_matrix(MATRIX)
    print(MATRIX)
    print(f"----------- Generation: {GENERATION}\n")
    GENERATION += 1
"""

if __name__ == "__main__":
  main()

