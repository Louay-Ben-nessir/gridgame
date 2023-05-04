import pygame
import time
import random
from helper import *
from config import *
def make_grid(grid_values,grid_window,selected = None,moved=[]):
    grid_window.fill(WHITE)
    for i in range(1, 3):
        pygame.draw.line(grid_window, BLACK, (0, i * CELL_HEIGHT), (GRID_WINDOW_WIDTH, i * CELL_HEIGHT), 2)
        pygame.draw.line(grid_window, BLACK, (i * CELL_WIDTH, 0), (i * CELL_WIDTH, GRID_WINDOW_HEIGHT), 2)
 
    for i in range(3):
        for j in range(3):
                color = BLACK
                if (i,j) == selected :
                    color = GRAY
                if (i,j) in moved:
                    color = GREEN
                text = font.render(str(grid_values[i][j]), True, color)
                text_rect = text.get_rect(center=((j + 0.5) * CELL_WIDTH, (i + 0.5) * CELL_HEIGHT))
                grid_window.blit(text, text_rect)



def update_btns(btn_list : dict):
    for name,btn in btn_list.items():
        btn.draw()

class make_text:
    def __init__(self, filed_name, location):
        self.btn  = pygame.Rect(*location)
        self.text = font.render(filed_name, True, BLACK)
        self.text_rect = self.text.get_rect(center=self.btn.center)
        
        self.border = filed_name in ["Reset", "DFS","DFSL", "A*","BFS"]
        

    def draw(self):
        if self.border:
            color = GRAY if self.btn.collidepoint(pygame.mouse.get_pos()) else BLACK 
            pygame.draw.rect(main_window, color, self.btn, 2)
            
        main_window.blit(self.text, self.text_rect)
        
    def collidepoint(self,pos):
        return self.btn.collidepoint(pos)
         
def draw_results(algo,btn_class):
    closed_loc = (btn_class.btn.topleft[0],button_configs["Closed"][1][1],*BTN_size)
    closed_text = str(len(algo.closed))
   
    all_loc = (btn_class.btn.topleft[0],button_configs["All"][1][1],*BTN_size)
    all_text = str(len(algo.gen_all))

    make_text(closed_text,closed_loc).draw()
    make_text(all_text,all_loc).draw()
    
    
def draw_slider(speed):
    speed_index = speeds.index(speed)
    pygame.draw.rect(main_window, BLACK, slider_rect)
    slider_knob_x = slider_x + int((speed_index + 0.5) * slider_w / num_speeds)
    pygame.draw.circle(main_window, GRAY, (slider_knob_x, slider_y + slider_h // 2), slider_knob_r)
    
    # Draw the speed text
    speed_text = font.render(f"Speed: {speed}", True, BLACK)
    main_window.blit(speed_text, speed_text_loaction)
    
buttons = {btn_name : make_text(*properties) for (btn_name,properties) in button_configs.items()}

