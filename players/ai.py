


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
        # self.rave_wins=0
        # self.rave_visits=0
        self.player = None
        self.move=None
        # self.children_left=set()
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
    
    def get_opponent_number(self):
        return 1 if self.player_number == 2 else 2
    
    def find_winning_position(self, state: np.array, player_number: int) -> Tuple[int, int]:
        valid_actions= get_valid_actions(state, player_number)
        for action in valid_actions:
            new_state = state.copy()
            new_state[action] = player_number
            if check_win(new_state, action, player_number)[0]:
                # print(new_state,action)
                return action
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
        # Do the rest of your implementation here
        opponent_number = self.get_opponent_number()
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
            
        new_state=state.copy()
        moves=set(root.children_left.copy())
        mapp=0
        for move in root.children_left:
            new_state[move[0]][move[1]]=self.player_number
            moves.remove(move)
            f=0
            for move2 in moves:
                new_state[move2[0]][move2[1]]=self.player_number
                if check_win(new_state, move2, self.player_number)[0]:
                    f+=1
                    mapp=max(mapp,f)
                    if f==2:
                        
                        # print('hi')
                        print('move from Double move1', move)
                        # print(move)
                        return move
                new_state[move2[0]][move2[1]]=0 
            new_state[move[0]][move[1]]=0
            moves.add(move)
            
        
            
        for move in root.children_left:
            new_state[move[0]][move[1]]=3-self.player_number
            moves.remove(move)
            f=0
            for move2 in moves:
                new_state[move2[0]][move2[1]]=3-self.player_number
                if check_win(new_state, move2, 3-self.player_number)[0]:
                    f+=1
                    mapp=max(mapp,f)
                    if f==2:
                        # print('bye')
                        print('move from Double move2', move)
                        return move
                new_state[move2[0]][move2[1]]=0 
            new_state[move[0]][move[1]]=0
            moves.add(move)
        print(mapp)
        dc1={(10**6,10**6):0}
        no_of_random=50
        mov=set()
        for i in moves:
            if self.is_adjacent(i,self.player_number,state):
                mov.add(i)
            if self.is_adjacent(i,3-self.player_number,state):
                mov.add(i)
        mov=set(moves)
        moves_random1=random.sample(mov, min(no_of_random,len(mov)))
        for move in moves_random1:
            new_state[move[0]][move[1]] = self.player_number
            # moves.remove(move)
            # Check for second layer
            moves_random2=random.sample(mov, min(no_of_random,len(mov)))
            if move in moves_random2:
                moves_random2.remove(move)
            for move2 in moves_random2:
                new_state[move2[0]][move2[1]] = self.player_number
                # moves.remove(move2)
                moves_random3=random.sample(mov, min(no_of_random,len(mov)))
                # Check for third layer
                if move in moves_random3:
                    moves_random3.remove(move)
                if move2 in moves_random3:
                    moves_random3.remove(move2)
                for move3 in moves_random3:
                    new_state[move3[0]][move3[1]] = self.player_number
                    if check_win(new_state, move3, self.player_number)[0]:
                        if move not in dc1:
                            dc1[move]=0
                        dc1[move]+=1
                            
                    new_state[move3[0]][move3[1]] = 0
                
                new_state[move2[0]][move2[1]] = 0
                # moves.add(move2)
           
            new_state[move[0]][move[1]] = 0
            # moves.add(move)
            
        max_value=-1
        max_key=(10**6,10**6)   
        for i in dc1:
            if dc1[i]>max_value:
                max_value=dc1[i]
                max_key=i
        print('max_values in dc1', max_value, max_key)
        for i in dc1:
            if dc1[i]==max_value and max_value>4:
                # print('ALL Moves Available',dc1[i])
                # print('FINAL HERO from triple1',max_key)
                return max_key
            
        # Mirror the same logic for the opponent's moves
        dc={(10**6,10**6):0}
        moves_random1=random.sample(mov, min(no_of_random,len(mov)))
        for move in moves_random1:
            new_state[move[0]][move[1]] = 3-self.player_number
            # moves.remove(move)
            # Check for second layer
            moves_random2=random.sample(mov, min(no_of_random,len(mov)))
            if move in moves_random2:
                moves_random2.remove(move)
            for move2 in moves_random2:
                new_state[move2[0]][move2[1]] = 3-self.player_number
                # moves.remove(move2)
                moves_random3=random.sample(mov, min(no_of_random,len(mov)))
                # Check for third layer
                if move in moves_random3:
                    moves_random3.remove(move)
                if move2 in moves_random3:
                    moves_random3.remove(move2)
                for move3 in moves_random3:
                    new_state[move3[0]][move3[1]] = 3-self.player_number
                    if check_win(new_state, move3, 3-self.player_number)[0]:
                        if move not in dc:
                            dc[move]=0
                        dc[move]+=1
                            
                    new_state[move3[0]][move3[1]] = 0
                
                new_state[move2[0]][move2[1]] = 0
                # moves.add(move2)
           
            new_state[move[0]][move[1]] = 0
            # moves.add(move)
            
        max_val=-1
        max_key=(10**6,10**6)
        for i in dc:
            if dc[i]>max_val:
                max_val=dc[i]
                max_key=i
        print('max_val in dc', max_val, max_key)
        for i in dc:
            if dc[i]==max_val and max_val>4:
                # print('ALL Moves Available',dc[i])
                # print('FINAL HERO from triple2',max_key)
                return max_key
        print('len(mov):',len(mov))
        if len(mov)<25: 
            print("Playing Randommmom")
            dc={(10**6,10**6):0}
            moves_random1=random.sample(mov, min(no_of_random,len(mov)))
            for move in moves_random1:
                new_state[move[0]][move[1]] = self.player_number
                # moves.remove(move)
                # Check for second layer
                moves_random2=random.sample(mov, min(no_of_random,len(mov)))
                if move in moves_random2:
                    moves_random2.remove(move)
                for move2 in moves_random2:
                    new_state[move2[0]][move2[1]] = self.player_number
                    # moves.remove(move2)
                    moves_random3=random.sample(mov, min(no_of_random,len(mov)))
                    # Check for third layer
                    if move in moves_random3:
                        moves_random3.remove(move)
                    if move2 in moves_random3:
                        moves_random3.remove(move2)
                    for move3 in moves_random3:
                        new_state[move3[0]][move3[1]] = self.player_number
                        moves_random4=random.sample(mov, min(no_of_random,len(mov)))
                        # Check for third layer
                        if move in moves_random4:
                            moves_random4.remove(move)
                        if move2 in moves_random4:
                            moves_random4.remove(move2)
                        if move3 in moves_random4:
                            moves_random4.remove(move3)
                        for move4 in moves_random4:
                            new_state[move4[0]][move4[1]] = self.player_number
                            if check_win(new_state, move4, self.player_number)[0]:
                                if move not in dc:
                                    dc[move]=0
                                dc[move]+=1
                            new_state[move4[0]][move4[1]] = 0
                                    
                        new_state[move3[0]][move3[1]] = 0
                    
                    new_state[move2[0]][move2[1]] = 0
                    # moves.add(move2)
            
                new_state[move[0]][move[1]] = 0
                # moves.add(move)
                
            max_val=-1
            max_key=(10**6,10**6)
            for i in dc:
                if dc[i]>max_val:
                    max_val=dc[i]
                    max_key=i
            print('max_val in dc3', max_val, max_key)
            for i in dc:
                if dc[i]==max_val and max_val>10:
                    # print('ALL Moves Available',dc[i])
                    # print('FINAL HERO from triple2',max_key)
                    return max_key
                
            # Mirror the same logic for the opponent's moves
            dc={(10**6,10**6):0}
            moves_random1=random.sample(mov, min(no_of_random,len(mov)))
            for move in moves_random1:
                new_state[move[0]][move[1]] = 3-self.player_number
                # moves.remove(move)
                # Check for second layer
                moves_random2=random.sample(mov, min(no_of_random,len(mov)))
                if move in moves_random2:
                    moves_random2.remove(move)
                for move2 in moves_random2:
                    new_state[move2[0]][move2[1]] = 3-self.player_number
                    # moves.remove(move2)
                    moves_random3=random.sample(mov, min(no_of_random,len(mov)))
                    # Check for third layer
                    if move in moves_random3:
                        moves_random3.remove(move)
                    if move2 in moves_random3:
                        moves_random3.remove(move2)
                    for move3 in moves_random3:
                        new_state[move3[0]][move3[1]] = 3-self.player_number
                        moves_random4=random.sample(mov, min(no_of_random,len(mov)))
                        # Check for third layer
                        if move in moves_random4:
                            moves_random4.remove(move)
                        if move2 in moves_random4:
                            moves_random4.remove(move2)
                        if move3 in moves_random4:
                            moves_random4.remove(move3)
                        for move4 in moves_random4:
                            new_state[move4[0]][move4[1]] = 3-self.player_number
                            if check_win(new_state, move4, 3-self.player_number)[0]:
                                if move not in dc:
                                    dc[move]=0
                                dc[move]+=1
                            new_state[move4[0]][move4[1]] = 0
                                    
                        new_state[move3[0]][move3[1]] = 0
                    
                    new_state[move2[0]][move2[1]] = 0
                    # moves.add(move2)
            
                new_state[move[0]][move[1]] = 0
                # moves.add(move)
                
            max_val=-1
            max_key=(10**6,10**6)
            for i in dc:
                if dc[i]>max_val:
                    max_val=dc[i]
                    max_key=i
            print('max_val in dc4', max_val, max_key)
            for i in dc:
                if dc[i]==max_val and max_val>10:
                    # print('ALL Moves Available',dc[i])
                    # print('FINAL HERO from triple2',max_key)
                    return max_key
                    
        # Evaluate each valid move using the heuristic
        # best_move = None
        # best_score = -float('inf')

        # for move in valid_actions:
        #     score = self.calculate_heuristic(state, self.player_number, move)
        #     if score > best_score:
        #         best_score = score
        #         best_move = move

        # return best_move  
        
        # for i in range(325):
        #     node=root
        #     while len(node.children_left)==0 :
        #         node=self.select(node)
        #     node=self.expand(node)
        #     if not node:
        #         continue
        #     for _ in range(3):
        #         winner=self.rollout(node)
        #         self.backpropagate(node, winner)
        
        for i in range(325):
            node=root
            while len(node.children_left)==0 and node.children :
                node=self.select(node)
            # print(node.state)
            node=self.expand(node)
            if not node:
                continue
            # print(node.state)
            win=0
            for j in range(3):
                winner=self.rollout(node)
                if(winner==self.player_number):
                    win+=1
                # print(winner)
            loss=3-win
            tot_win=win-loss
            self.backpropagate(node, winner,tot_win)
                
        best_node=None
        best_val=-float('inf')
        g=[]
        gg=[]
        for i in root.children:
                g.append(i)
                gg.append(i.move)
                if i.visits>best_val:
                    best_val=i.visits
                    best_node=i
                elif i.visits==best_val:
                    if i.wins>best_node.wins:
                        best_node=i
        
        # print('FINAL HERO',best_node.move)
        print("Playing MCTS")
        return best_node.move
                    
        # action = random.choice(valid_actions)
        # return int(action[0]), int(action[1])
        # Additional helper to check if the move is in an "alkene-like" connection
    # def is_alkene_like(self, move1, move2):
    #     """
    #     Check if two moves are in a straight line and 2 steps apart (resembling an alkene-like bond).
    #     """
    #     if abs(move1[0] - move2[0]) == 2 and move1[1] == move2[1]:
    #         return True  # Vertical alignment, two steps apart
    #     if abs(move1[1] - move2[1]) == 2 and move1[0] == move2[0]:
    #         return True  # Horizontal alignment, two steps apart
    #     return False
    
    
    def is_alkene_like(self, move1, move2, board):
        """
        Check if two moves are in a straight line, two steps apart, with an empty cell in between (resembling an alkene-like bond).
        
        Parameters:
        - move1: Tuple[int, int] - The first move coordinates
        - move2: Tuple[int, int] - The second move coordinates
        - board: np.array - The game board to check for empty cells
        
        Returns:
        - bool: True if the moves form an "alkene-like" bond with empty cells between them, False otherwise.
        """
        
        n1=get_neighbours(len(board),move1)
        n2=get_neighbours(len(board),move2)
        common_neighbours=set(n1).intersection(n2)
        if len(common_neighbours)==2:
            if board[common_neighbours.pop()[0]][common_neighbours.pop()[1]]==0:
                if board[common_neighbours.pop()[0]][common_neighbours.pop()[1]]==0:
                    return True
                
        return False


    def expand(self,node):
        """
        Expand the current node by generating a new child for an unexplored move.
        """
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
        """
        Select the best node based on UCB1.
        """
        return max(node.children, key=lambda child: self.ucb1(child))

    
    def rollout(self, node):
        """
        Simulate a random game starting from the current node's state.
        """
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
    
    # def calculate_heuristic(self, state, player_number, move):
    #     score = 0
        
    #     # Winning move heuristic
    #     if check_win(state, move, player_number)[0]:
    #         score += 100000  # High score for a direct win
        
    #     # Block opponent's winning move heuristic
    #     opponent_number = self.get_opponent_number()
    #     temp_state = state.copy()
    #     temp_state[move[0]][move[1]] = opponent_number
    #     if check_win(temp_state, move, opponent_number)[0]:
    #         score += 100000  # High score for blocking opponent's win
        
    #     # Create multiple winning opportunities
    #     if self.creates_multiple_wins(state, move, player_number):
    #         score += 1000  # Reward for creating multiple winning paths
        
    #     # Central and corner control bonus
    #     if self.is_central(move, state):
    #         score += 100  # Central control is often strategically better
    #     elif self.is_corner(move, state):
    #         score += 300   # Corner control can be valuable
        
    #     # Adjacent friendly pieces heuristic
    #     adjacent_count = self.count_adjacent(state, move, player_number)
    #     score += adjacent_count * 10  # Reward for clustering pieces

    #     # Alkene-like connection heuristic
    #     alkene_like_score = self.count_alkene_like(state, move, player_number)
    #     score += alkene_like_score * 20  # Add higher weight for alkene-like moves
        
        
    #     return score
    
    def count_alkene_like(self, state, move, player_number):
        """
        Count how many alkene-like connections (two steps apart but linearly aligned)
        are present around the current move.
        """
        count = 0
        directions = [(2, 0), (-2, 0), (0, 2), (0, -2)]  # Two-step horizontal or vertical directions

        for d in directions:
            new_x, new_y = move[0] + d[0], move[1] + d[1]
            if 0 <= new_x < state.shape[0] and 0 <= new_y < state.shape[1]:  # Stay within bounds
                if state[new_x][new_y] == player_number:
                    count += 1

        return count


    # def creates_multiple_wins(self, state, move, player_number):
    #     # Simulate placing the move and count potential win lines
    #     new_state = state.copy()
    #     new_state[move[0]][move[1]] = player_number
    #     win_count = 0
    #     for next_move in get_valid_actions(new_state, player_number):
    #         if check_win(new_state, next_move, player_number)[0]:
    #             win_count += 1
    #     return win_count > 1  # Return true if it creates multiple win lines

    # def is_central(self, move,state):
    #     # Assuming a square board, check if the move is in the center
    #     center = (state.shape[1]) // 2, state.shape[1] // 2
    #     return move == center

    # def is_corner(self, move,state):
    #     rows, cols = state.shape
    #     return move in [(0, 0), (0, cols - 1), (rows - 1, 0), (rows - 1, cols - 1)]

    # def count_adjacent(self, state, move, player_number):
    #     # Count friendly pieces adjacent to the current move
    #     adjacent_positions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
    #     count = 0
    #     for dx, dy in adjacent_positions:
    #         new_x, new_y = move[0] + dx, move[1] + dy
    #         if 0 <= new_x < state.shape[0] and 0 <= new_y < state.shape[1]:
    #             if state[new_x][new_y] == player_number:
    #                 count += 1
    #     return count
    
    # # Additional helper function to get adjacent moves (can be used for scoring)
    # def get_adjacent_moves(self, move, state):
    #     """
    #     Get all adjacent moves (direct neighbors) to a given move.
    #     """
    #     adj_moves = []
    #     for dx in [-1, 0, 1]:
    #         for dy in [-1, 0, 1]:
    #             if dx == 0 and dy == 0:
    #                 continue  # Skip the original move itself
    #             new_x, new_y = move[0] + dx, move[1] + dy
    #             if 0 <= new_x < state.shape[0] and 0 <= new_y < state.shape[1]:
    #                 adj_moves.append((new_x, new_y))
    #     return adj_moves


# print('hi')
