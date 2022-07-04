import pygame
import gol_modules.gol_params as p

WIN = pygame.display.set_mode((p.WIDTH, p.HEIGHT))
pygame.display.set_caption('Demo - Game of life')

# Check if quit event exists
def handle_event_quit(pygame):
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return True
      else:
        False

def draw_window():
  WIN.fill(p.COLOR['WHITE'])
  pygame.display.update()
  
def main():
  clock = pygame.time.Clock()
  while not handle_event_quit(pygame):
    clock.tick() # make sure execution doesn't go over FPS(60)
    draw_window()
    
  print(f"quit? {quit}")
  pygame.quit()

if __name__ == "__main__":
  main()

