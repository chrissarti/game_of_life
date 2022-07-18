import numpy as np
import itertools as it
from gol_modules.params import CELL_DIMENSION as CD
import gol_modules.cells as c
import matplotlib.pyplot as plt

def main():  
  plt.ion()
  fig = plt.figure()
  
  LENGTH, HEIGHT = (CD['WIDTH'], CD['HEIGHT'])
  MATRIX = np.random.randint(2, size=(LENGTH, HEIGHT))
  GENERATION = 0
  print("Initial matrix:\n\n")
  print(MATRIX, end="\n")
  a = GENERATION
  print(f"----------- Generation: {a}\n")  

  for _ in it.repeat(None, 50):
    ax = fig.add_subplot(111)
    ax.matshow(MATRIX)
    plt.draw()
    plt.pause(0.00001)
    c.loop_matrix(MATRIX)
    print(f"----------- Generation: {GENERATION}\n")
    GENERATION += 1
  
"""
  for _ in it.repeat(None, 500):
    c.loop_matrix(MATRIX)
    print(MATRIX)
    print(f"----------- Generation: {GENERATION}\n")
    GENERATION += 1
"""

if __name__ == "__main__":
  main()

