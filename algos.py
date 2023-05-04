from helper import *
from config import *

class DFS:
    def __init__(self,state):
        self.free = [state]
        self.closed = []
        self.goal = []
        self.found = False
        
        self.display = []
        self.gen_all = []
        
    def step(self):
        curr = self.free.pop(0)

        if compare_states(curr,final_state):
            self.found = True
            self.goal  = curr
            
        self.closed.append(curr)
        
        gen = all_moves(curr,possible_moves)
        gen = [s for s in gen if s not in self.closed + self.free and s ]
        
        self.gen_all.extend(gen)

        self.free = gen + self.free

        self.display = curr


    
class DFSL:
    def __init__(self,state,max_depth = 3):
        self.free = [node(state, 0)]
        self.closed = []
        self.goal = []
        self.found = False
        self.max_depth = max_depth


        self.display = []
        self.gen_all = []
        
    def step(self):
        curr = self.free.pop(0)

        if compare_states(curr.state, final_state):
            self.found = True
            self.goal = curr.state

        self.closed.append(curr)

        
        
        if curr.depth < self.max_depth:
            gen = [node(s,curr.depth+1) for s in all_moves(curr.state, possible_moves)]
            gen = [s for s in gen if s not in self.closed + self.free and s.state]
            self.gen_all.extend(gen)
            self.free = gen + self.free
        
        self.display = curr.state
        
class BFS:
    def __init__(self,state):
        self.free = [state]
        self.closed = []
        self.goal = []
        self.found = False
        
        self.display = []
        self.gen_all = []
        
    def step(self):
        curr = self.free.pop(0)

        if compare_states(curr,final_state):
            self.found = True
            self.goal  = curr
            
        self.closed.append(curr)
        
        gen = all_moves(curr,possible_moves)
        gen = [s for s in gen if s not in self.closed + self.free and s ]

        self.gen_all.extend(gen)

        self.free = self.free + gen

        self.display = curr


class AStar:
    def __init__(self, state):
        self.free = [node(state, 0, self.distance(state, final_state))]
        self.closed = []
        self.goal = []
        self.found = False

        self.display = []
        self.gen_all = []

    def distance(self,state1,state2):
        cost = 0
        for row,elem in enumerate(state1):
            for col in range(len(elem)):
                cost += int(state1[row][col]!=state2[row][col])
        return cost
    
    def step(self):
        curr = self.free.pop(0)
        self.closed.append(curr)
        
        if compare_states(curr.state,final_state):
            self.found = True
            self.goal  = curr

       

        gen = [node(s,curr.depth+1,self.distance(s,final_state)) for s in all_moves(curr.state, possible_moves)]
        gen = [s for s in gen if s not in self.closed + self.free and s.state]
        self.gen_all.extend(gen)
        
        self.free = self.free + gen
        self.free = sorted(self.free, key = lambda x : x.depth + x.distance)
        
        self.display = curr.state



