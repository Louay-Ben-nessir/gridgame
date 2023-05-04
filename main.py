import pygame
import time
import math
from utils import *
from algos import *
from config import *
make_grid(starting_state,grid_window)




speed = speeds[speed_index]


last_up  = time.perf_counter()
grid_values = starting_state
selected_cell = None
solveing = False
algo = None
diff = []
dragging = False

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN and slider_rect.collidepoint(event.pos):
            dragging = True
        elif event.type == pygame.MOUSEMOTION and dragging:
            slider_knob_x = event.pos[0]
            if slider_knob_x < slider_x:
                slider_knob_x = slider_x
            elif slider_knob_x > slider_x + slider_w:
                slider_knob_x = slider_x + slider_w
            speed_index = int((slider_knob_x - slider_x) / slider_w * num_speeds)
            if speed_index < 0:
                speed_index = 0
            elif speed_index >= num_speeds:
                speed_index = num_speeds - 1
            speed = speeds[speed_index]
            
        elif event.type == pygame.MOUSEBUTTONUP:
            selected_cell = None
            dragging = False
            if not solveing:
                if buttons["DFS"].collidepoint(event.pos):
                    solveing = True
                    algo = DFS(grid_values)
                    selected_btn = buttons["DFS"]
                elif buttons["DFSL"].collidepoint(event.pos):
                    solveing = True
                    algo = DFSL(grid_values)
                    selected_btn = buttons["DFSL"]
                elif buttons["BFS"].collidepoint(event.pos):
                    solveing = True
                    algo = BFS(grid_values)
                    selected_btn = buttons["BFS"]
                elif buttons["A*"].collidepoint(event.pos):
                    solveing = True
                    algo = AStar(grid_values)
                    selected_btn = buttons["A*"]
 
            if buttons["Reset"].collidepoint(event.pos):
                grid_values = starting_state#gen_random_state()
                algo = None
                selected_btn = None
                diff = []
                solveing = False
                

            else:
                x, y = event.pos
                if 50 <= x < 350 and 50 <= y < 350:
                    i, j = (y - 50) // CELL_HEIGHT, (x - 50) // CELL_WIDTH
                    selected_cell = (i, j)
                else:
                    selected_cell = None
        elif event.type == pygame.KEYDOWN:
            if selected_cell is not None and event.unicode.isdigit() and not solveing:
                i, j = selected_cell
                grid_values[i][j] = int(event.unicode)
    


    main_window.fill(WHITE)
    main_window.blit(grid_window, (50, 50))
    update_btns(buttons)
    draw_slider(speed)

    
    
   
    if time.perf_counter()-last_up > 1/speed and solveing: #only redraw every x seconds
            last_up = time.perf_counter()
            algo.step() 
            diff = get_diff(grid_values, algo.display )
            grid_values = algo.display
            solveing = not algo.found and algo.free
            last_up = time.perf_counter()
            
    if not solveing and algo is not None:
        draw_results(algo,selected_btn)


    make_grid(grid_values,grid_window,selected_cell,diff)
    

    pygame.display.update()
    
