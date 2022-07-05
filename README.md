# game_of_life
Little version of the game of life. Just for fun


## Cells rules

- If a cell is ON and has fewer than two neighbors that are ON, it turns OFF
- If a cell is ON and has either two or three neighbors that are ON, it remains ON.
- If a cell is ON and has more than three neighbors that are ON, it turns OFF.
- If a cell is OFF and has exactly three neighbors that are ON, it turns ON.

  ### Simplified
  if CELL is ALIVE
  	if neighbors < 2
  		CELL DIES
  	if neighbors == 2 or neighbors == 3
  		no change	
  	if neighbors > 3
  		CELL DIES
  
  if CELL is DEAD
  	if neighbors == 3
  	CELL is ALIVE   