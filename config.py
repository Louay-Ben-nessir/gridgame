import pygame

EMPTY_SYMBOL   = 0
starting_state = [[1,2,3],[8,6,EMPTY_SYMBOL],[7,5,4]]
final_state    = [[1,2,3],[8,0,4],[7,6,5]]
possible_moves = [[1,0],[-1,0],[0,1],[0,-1]]# up down rigth left


BLACK = (25, 25, 25)
WHITE = (225, 225, 225)
GRAY = (128, 128, 128)
GREEN = (0,128,0)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600



GRID_WINDOW_WIDTH = 300
GRID_WINDOW_HEIGHT = 300


CELL_WIDTH = GRID_WINDOW_WIDTH // 3
CELL_HEIGHT = GRID_WINDOW_HEIGHT // 3

BTN_size = (100,50)
button_configs = {"DFS" :["DFS",(200, 450, *BTN_size)] ,
                  "DFSL" : ["DFSL",(350  , 450, *BTN_size)],
                  "BFS" : ["BFS",(500  , 450, *BTN_size)],
                  "A*" : ["A*",(650  , 450, *BTN_size)],
                  "Reset" : ["Reset",(430, 125, *BTN_size)],
                  "Closed" :[ "Closed",(10, 500, *BTN_size)],
                  "All" : ["All",(10, 550,*BTN_size)]}



speeds = [0.25, 0.5, 0.75,1, 2, 4, 10, 100]
num_speeds = len(speeds)
start_speed_index = 3
speed_index = start_speed_index

slider_x, slider_y, slider_w, slider_h = 430, 250, 300, 20
slider_rect = pygame.Rect(slider_x, slider_y, slider_w, slider_h)
slider_knob_r = 10
speed_text_loaction = (430,200)

pygame.init()
main_window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Taiqun gui")
grid_window = pygame.Surface((GRID_WINDOW_WIDTH, GRID_WINDOW_HEIGHT))
font = pygame.font.SysFont(None, 50)
