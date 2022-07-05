import pygame
import gol_modules.params as p
import gol_modules.cells as c

pygame.display.set_caption('Demo - Game of life')
WIN = pygame.display.set_mode((p.WIDTH, p.HEIGHT))

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

if __name__ == "__main__":
  main()

