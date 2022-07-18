import numpy as np
import itertools as it
import pygame
from gol_modules.params import CELL_DIMENSION as CD
import gol_modules.cells as c

#pygame.display.set_caption('Demo - Game of life')
#WIN = pygame.display.set_mode((p.WIDTH, p.HEIGHT))

# Check if quit event exists
def handle_event_quit(pygame):
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return True
      else:
        False

def draw_window():
  WIN.fill(p.COLOR['WHITE'])
  draw_grid()
  pygame.display.update()

def draw_grid():
  rect = pygame.Rect(100, 100, 20, 30)
  pygame.draw.rect(WIN, p.COLOR["BLACK"], rect)
  
"""  
def main():
  clock = pygame.time.Clock()
  MATRIX = c.create_binary_matrix(p.CELL_DIMENSION)
  Original = MATRIX
  GENERATION = 0
  print(f"Generation {GENERATION}")
  print(f"{MATRIX}\n")
  
  while not handle_event_quit(pygame):
    clock.tick() # make sure execution doesn't go over FPS(60)
    #draw_window()

    c.loop_matrix(MATRIX)
    GENERATION += 1
    print(f"Generation {GENERATION}")
    print(f"{MATRIX}\n")
    
  pygame.quit()

  print(f"{Original}\n")
"""

def main():  
  LENGTH, HEIGHT = (CD['WIDTH'], CD['HEIGHT'])
  MATRIX = np.random.randint(2, size=(LENGTH, HEIGHT))
  GENERATION = 0
  print("Initial matrix:\n\n")
  print(MATRIX, end="\n")
  a = GENERATION
  print(f"----------- Generation: {a}\n")  

  for _ in it.repeat(None, 20):
    c.loop_matrix(MATRIX)
    print(MATRIX)
    print(f"----------- Generation: {GENERATION}\n")
    GENERATION += 1

if __name__ == "__main__":
  main()

