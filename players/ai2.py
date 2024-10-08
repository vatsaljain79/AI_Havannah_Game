


import time
import math
import random
import numpy as np
from helper import *

class Node:
    def __init__(self, state, parent=None):
        self.state = state  
        self.parent = parent
        self.children = []
        self.wins = 0
        self.visits = 0
        self.player = None
        self.move=None
        self.children_left={}

class AIPlayer:

    def __init__(self, player_number: int, timer):
        """
        Intitialize the AIPlayer Agent

        # Parameters
        `player_number (int)`: Current player number, num==1 starts the game
        
        `timer: Timer`
            - a Timer object that can be used to fetch the remaining time for any player
            - Run `fetch_remaining_time(timer, player_number)` to fetch remaining time of a player
        """
        self.player_number = player_number
        self.type = 'ai'
        self.player_string = 'Player {}: ai'.format(player_number)
        self.timer = timer
    
    def find_winning_position(self, state: np.array, player_number: int) -> Tuple[int, int]:
        valid_actions= get_valid_actions(state, player_number)
        for action in valid_actions:
            new_state = state.copy()
            new_state[action] = player_number
            if check_win(new_state, action, player_number)[0]:
                # print(new_state,action)
                return action
        return None
    
    def evaluate_double_moves(self, state, player_number, moves):
        new_state=state.copy()
        for move in moves:
            new_state[move[0]][move[1]]=player_number
            moves.remove(move)
            no_of_wins=0
            for move2 in moves:
                new_state[move2[0]][move2[1]]=player_number
                if check_win(new_state, move2, player_number)[0]:
                    no_of_wins+=1
                    if no_of_wins==2:
                        return move
                new_state[move2[0]][move2[1]]=0 
            new_state[move[0]][move[1]]=0
            moves.add(move)
            
        return None
    
    def evaluate_triple_moves(self,state, player_number, moves, no_of_random=50):
        dc = {(10**6, 10**6): 0}
        # print(type(moves))
        # print(moves)
        moves_random1 = random.sample(moves, min(no_of_random, len(moves)))
        new_state = state.copy()
        for move in moves_random1:
            new_state[move[0]][move[1]] = player_number

            # Check for second layer
            moves_random2 = random.sample(moves, min(no_of_random, len(moves)))
            if move in moves_random2:
                moves_random2.remove(move)

            for move2 in moves_random2:
                new_state[move2[0]][move2[1]] = player_number

                # Check for third layer
                moves_random3 = random.sample(moves, min(no_of_random, len(moves)))
                if move in moves_random3:
                    moves_random3.remove(move)
                if move2 in moves_random3:
                    moves_random3.remove(move2)

                for move3 in moves_random3:
                    new_state[move3[0]][move3[1]] = player_number

                    # Check if the move results in a win
                    if check_win(new_state, move3, player_number)[0]:
                        if move not in dc:
                            dc[move] = 0
                        dc[move] += 1

                    new_state[move3[0]][move3[1]] = 0

                new_state[move2[0]][move2[1]] = 0

            new_state[move[0]][move[1]] = 0

        # Find the best move
        max_value = -1
        max_key = (10**6, 10**6)
        for i in dc:
            if dc[i] > max_value:
                max_value = dc[i]
                max_key = i

        for i in dc:
            if dc[i] == max_value and max_value > 4:
                return max_key

        return None  # If no move is found
    
    def evaluate_moves_4_layers(self,state, player_number, mov, no_of_random):
        # Set of available moves
        if len(mov)>25:
            return None
        dc = {(10**6, 10**6): 0}
        new_state = state.copy()
        # Random sampling for the first layer of moves
        moves_random1 = random.sample(mov, min(no_of_random, len(mov)))
        for move in moves_random1:
            new_state[move[0]][move[1]] = player_number
            
            # Second layer of moves
            moves_random2 = random.sample(mov, min(no_of_random, len(mov)))
            if move in moves_random2:
                moves_random2.remove(move)
            for move2 in moves_random2:
                new_state[move2[0]][move2[1]] = player_number

                # Third layer of moves
                moves_random3 = random.sample(mov, min(no_of_random, len(mov)))
                if move in moves_random3:
                    moves_random3.remove(move)
                if move2 in moves_random3:
                    moves_random3.remove(move2)
                for move3 in moves_random3:
                    new_state[move3[0]][move3[1]] = player_number

                    # Fourth layer of moves
                    moves_random4 = random.sample(mov, min(no_of_random, len(mov)))
                    if move in moves_random4:
                        moves_random4.remove(move)
                    if move2 in moves_random4:
                        moves_random4.remove(move2)
                    if move3 in moves_random4:
                        moves_random4.remove(move3)
                    for move4 in moves_random4:
                        new_state[move4[0]][move4[1]] = player_number

                        # Check if winning condition is met for the player
                        if check_win(new_state, move4, player_number)[0]:
                            if move not in dc:
                                dc[move] = 0
                            dc[move] += 1

                        # Undo fourth layer move
                        new_state[move4[0]][move4[1]] = 0

                    # Undo third layer move
                    new_state[move3[0]][move3[1]] = 0
                
                # Undo second layer move
                new_state[move2[0]][move2[1]] = 0

            # Undo first layer move
            new_state[move[0]][move[1]] = 0

        # Find the move with the maximum value
        max_val = -1
        max_key = (10**6, 10**6)
        for i in dc:
            if dc[i] > max_val:
                max_val = dc[i]
                max_key = i
        
        # Return the best move if it satisfies the winning condition
        for i in dc:
            if dc[i] == max_val and max_val > 10:
                return max_key
        return None



    def get_move(self, state: np.array,should:bool=False) -> Tuple[int, int]:
        # print(get_neighbours(len(state), (3, 3)))
        """
        Given the current state of the board, return the next move

        # Parameters
        `state: Tuple[np.array]`
            - a numpy array containing the state of the board using the following encoding:
            - the board maintains its same two dimensions
            - spaces that are unoccupied are marked as 0
            - spaces that are blocked are marked as 3
            - spaces that are occupied by player 1 have a 1 in them
            - spaces that are occupied by player 2 have a 2 in them

        # Returns
        Tuple[int, int]: action (coordinates of a board cell)
        """
        # print(state)
        
        opponent_number = 3-self.player_number
        copy_state = state.copy()
        
        valid_actions= get_valid_actions(copy_state, self.player_number)
        winning_position = self.find_winning_position(copy_state, self.player_number)
        if winning_position:
            # print('Winning Position: ', winning_position)
            return winning_position
        
        opp_winning_position = self.find_winning_position(state, opponent_number)
        if opp_winning_position:
            # print('Opponent Winning Position: ', opp_winning_position)
            return opp_winning_position
        
        root=Node(state)
        root.player=self.player_number
        for i in get_valid_actions(state):
            root.children_left[i]=[0,0]
    
        moves=set(root.children_left.copy())
        
        check1=self.evaluate_double_moves(state, self.player_number, moves)
        check2=self.evaluate_double_moves(state, 3-self.player_number, moves)
        if check1:
            return check1
        if check2:
            return check2
        
        no_of_random=50
        check3=self.evaluate_triple_moves(state, self.player_number, moves, no_of_random)
        check4=self.evaluate_triple_moves(state, 3-self.player_number, moves, no_of_random)
        if check3:
            return check3
        if check4:
            return check4
        
        check5=self.evaluate_moves_4_layers(state, self.player_number, moves, no_of_random)
        check6=self.evaluate_moves_4_layers(state, 3-self.player_number, moves, no_of_random)
        if check5:
            return check5
        if check6:
            return check6
                            
        for i in range(325):
            node=root
            while len(node.children_left)==0 and node.children :
                node=self.select(node)
            node=self.expand(node)
            if not node:
                continue
            win=0
            for j in range(3):
                winner=self.rollout(node)
                if(winner==self.player_number):
                    win+=1
            loss=3-win
            tot_win=win-loss
            self.backpropagate(node, winner,tot_win)
                
        best_node=None
        best_val=-float('inf')
        for i in root.children:
                if i.visits>best_val:
                    best_val=i.visits
                    best_node=i
                elif i.visits==best_val:
                    if i.wins>best_node.wins:
                        best_node=i
        return best_node.move
                    
    def is_alkene_like(self, move1, move2, board):     
        n1=get_neighbours(len(board),move1)
        n2=get_neighbours(len(board),move2)
        common_neighbours=set(n1).intersection(n2)
        if len(common_neighbours)==2:
            if board[common_neighbours.pop()[0]][common_neighbours.pop()[1]]==0:
                if board[common_neighbours.pop()[0]][common_neighbours.pop()[1]]==0:
                    return True
                
        return False

    def expand(self,node):
        # Expand the current node by generating a new child for an unexplored move.
        available_moves = node.children_left
        if available_moves:
            move=random.choice(list(available_moves.keys()))
            new_state = node.state.copy()
            new_state[move[0]][move[1]]=node.player
            child_node = Node(state=new_state, parent=node)
            child_node.player = 3-node.player
            child_node.move=move
            child_node.children_left=available_moves
            node.children.append(child_node)
            return child_node
        return None
    
    def select(self,node):   
        # Select the best node based on UCB1.
        return max(node.children, key=lambda child: self.ucb1(child))

    def rollout(self, node):  
        # Simulate a random game starting from the current node's state.
        current_state = node.state.copy()
        current_player = node.player
        moves = set(get_valid_actions(current_state))
        
        while moves:
            move=random.choice(list(moves))
            current_state[move[0]][move[1]] = current_player
            if check_win(current_state, move, current_player)[0]:
                return current_player  # Return winner if found
            current_player = 3 - current_player  # Alternate player turns
            moves.remove(move)

        return 0  # Return draw or no winner if moves are exhausted
    def backpropagate(self, node, winner,tot_win):
        """
        Propagate the result of the simulation up to the root node.
        """
        while node is not None:
            node.visits += 3
            node.wins += tot_win
            node = node.parent

            
    def ucb1(self, child, exploration_factor=1.75):
        """
        Calculate the UCB1 value for a node, with additional scoring if an alkene-like pattern is formed.
        """
        if child.visits == 0:
            return float('inf')  
        win_rate = child.wins / child.visits
        exploration_term = exploration_factor * np.sqrt(np.log(child.parent.visits) / child.visits)
        
        # Add bonuses for board position (corner, edge)
        if get_corner(child.move, len(child.state)) != -1:
           win_rate+=(abs(win_rate))*(0.8 if win_rate<0 else 0.3)
        if get_edge(child.move, len(child.state)) != -1:
            win_rate+=(abs(win_rate))*(0.2 if win_rate<0 else 0.1)
        
        # Add bonus for adjacent to player's or opponent's moves
        if self.is_adjacent(child.move, 3 - child.player, child.state):
            win_rate += win_rate * 0.1
        if self.is_adjacent(child.move, child.player, child.state):
            win_rate += win_rate * 0.1

        # Check for alkene-like formation and boost score
        for move in get_valid_actions(child.state):
            if self.is_alkene_like(child.move, move):
                win_rate += win_rate * 0.8  # Boost for alkene-like patterns

        return win_rate + exploration_term
 
    def is_adjacent(self,move,pnum,board):
        neighbours=get_neighbours(len(board),move)
        h=[]
        for i in neighbours:
            if board[i[0]][i[1]]==pnum:
                return True
        return False
