import numpy as np
import itertools as it
from gol_modules.params import CELL_STATE as CS
from gol_modules.params import CELL_DIMENSION as CD
import matplotlib.pyplot as plt

# border of 1s, center of 0s
def gen_matrix_ones():
  W = CD['WIDTH']; H = CD['HEIGHT']
  
  x = np.ones( (W, H) )
  #x[2:-2, 2:-2] = 0
  #x[6:-6, 6:-6] = 0
  x[20:-12, 20:-12] = 0
  return x

def gen_bin_matrix_rand():
  W = CD['WIDTH']; H = CD['HEIGHT']
  x = np.random.randint(2, size=(W, H) )
  x[2:-2, 2:-2] = 0
  return x

def kill_cell(matrix, r, c):
  if matrix[r][c] == CS['ALIVE']:
    matrix[r][c] = CS['DEAD']

def revive_cell(matrix, r, c):
  if matrix[r][c] == CS['DEAD']:
    matrix[r][c] = CS['ALIVE']

def cell_is_alive(matrix, r, c):
  """True: is alive | False: is dead"""
  return matrix[r][c] == CS['ALIVE']

def row_is_within_bounds(row):
  return row >= 0 and row < CD['WIDTH']

def col_is_within_bounds(col):
  return col >= 0 and col < CD['HEIGHT']

def count_neighbors(matrix, r,c):
  total_neighbors = 0
  n_idx = [
    (-1,-1), (-1,0), (-1,1),
    (0,-1),          (0,1),
    (1,-1),  (1,0),  (1,1)]  
  #print(f"cell[{r}][{c}]:{matrix[r][c]}:")
  for idx in n_idx:
    i = r+idx[0]; j = c+idx[1]
    #print(f"\tTRYING idx[{i}][{j}]...")
    if row_is_within_bounds(i) and col_is_within_bounds(j):
      #print(f"\t\tFoundneighbor[{i}][{j}]")
      total_neighbors += matrix[i][j]
      
  return total_neighbors

def evaluate_cell(matrix,r,c):
  neighbors_count = count_neighbors(matrix,r,c)
  if not cell_is_alive(matrix, r,c):
    if neighbors_count == 3:
      revive_cell(matrix,r,c)
      #print(f"\tREVIVED CELL[{r}][{c}]:{matrix[r][c]}")
  elif cell_is_alive(matrix,r,c):
    if neighbors_count < 2 or neighbors_count > 3:
      kill_cell(matrix,r,c)
      #print(f"\tKILLED CELL[{r}][{c}]:{matrix[r][c]}")

def loop_matrix(matrix):
  for id_r,row in enumerate(matrix):
    for id_c, _ in enumerate(row):
      evaluate_cell(matrix, id_r,id_c)

def create_binary_matrix(d):
  return np.random.randint(2, size=(d['WIDTH'], d['HEIGHT']))

def cellular_plot(matrix):
  loop_matrix(matrix)
  