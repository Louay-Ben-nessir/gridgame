from config import *
import random
def find_empty(state : list) -> type :
    """
    finds and returns the postion of the empty symbol
    """
    for i , row in enumerate(state):
        for j , elem in enumerate(row):
            if elem == EMPTY_SYMBOL:
                return (i,j)
    raise Exception(f"The state is missign an empty state{EMPTY_SYMBOL}")

def copy_array(arr: list) -> list:
    return [[i for i in row] for row in arr]


def get_elem(state : list, x : int, y: int) -> int: # -numero(t, x, y)
    """
    return the number of the pice on postion x,y
    """
    return state[y][x]

def get_diff(state1 : list,state2: list) -> list:
    """
    Find and return the postion of the diffrent elemts bettween two game states.
    """
    diff = []
    for i in range(3):
        for j in range(3):
            if state1[i][j]!=state2[i][j]:
                diff.append((i,j))
    return diff

def permutate(state: list, pos1 : list, pos2 : list) -> list :
    """
    Swap pices on the board
    """
    temp_state = copy_array(state)
    old_y , old_x = pos1
    new_y , new_x = pos2
    temp_state[new_y][new_x],temp_state[old_y][old_x] = temp_state[old_y][old_x],temp_state[new_y][new_x]
    return temp_state

def make_move(state : list, move : list) -> list:
    """
    check for the legality of the move and make it.
    return [] if the move is illigale else the new state
    """
    temp_state  = []
    bsy,bsx     = len(state), len(state[0]) #board size y and x 
    y_emp,x_emp = find_empty(state)
    off_y , off_x = move
    new_y , new_x = off_y + y_emp, off_x + x_emp
    if bsy > new_y >= 0 and bsx > new_x >= 0: #make sure that the move is with in the bound of the board
        temp_state = permutate(state, [new_y , new_x] , [y_emp,x_emp])
    return temp_state

def compare_states(state1 : list, state2 : list):
    return state1 == state2
def all_moves(state : list , moves : list) -> list:
    """
    Generate and return a list of all possible legal moves for a given board
    return an array of states
    """
    all_perm = []
    for move in moves:
        new_board = make_move(state,move)

        if new_board not in all_perm:
            all_perm.append(new_board)
    
    return all_perm

def gen_random_state():
    """
    Generates and new random valid board state
    Used for the rest btn
    """
    l = [EMPTY_SYMBOL] + list(range(1,9))
    random.shuffle(l)

    state = []
    for i in range(3):
        row = []
        for j in range(3):
            row.append(l[i * 3 + j])
        state.append(row)
    return state

def valid_state(state):
    """
    Checks if a state has all of the numbers and an emmpty symbol
    """
    flatten = set(i for i in state)
    correct = set([EMPTY_SYMBOL] + list(range(1,9)))
    return flatten == correct

class node:
    def __init__(self, state, depth, distance = None):
        self.state = state
        self.depth = depth
        self.distance = distance
    def __eq__(self, other):
        """
        two board states are considered equal if the numbers match, regardless of depth
        """
        return compare_states(self.state, other.state)
