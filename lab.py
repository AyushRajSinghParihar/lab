bund phati programs- https://chatgpt.com/share/6775838b-5a40-8001-9f46-eaca754ee6a4

program 1: water jug

import queue
import time
import random

dfsq = queue.Queue()

class node:
    def __init__(self, data):
        self.x = 0
        self.y = 0
        self.parent = data

    def printnode(self):
        print("(", self.x, ",", self.y, ")")

def generateAllSuccessors(cnode):
    list1 = []
    list_rule = []
    while len(list_rule) < 8:
        rule_no = random.randint(1, 8)
        if rule_no not in list_rule:
            list_rule.append(rule_no)
            nextnode = operation(cnode, rule_no)
            if nextnode is not None and not IsNodeInlist(nextnode, visitednodelist):
                list1.append(nextnode)
    return list1

def operation(cnode, rule):
    x = cnode.x
    y = cnode.y

    if rule == 1:
        if x < maxjug1:
            x = maxjug1
        else:
            return None
    elif rule == 2:
        if y < maxjug2:
            y = maxjug2
        else:
            return None
    elif rule == 3:
        if x > 0:
            x = 0
        else:
            return None
    elif rule == 4:
        if y > 0:
            y = 0
        else:
            return None
    elif rule == 5:
        if x + y >= maxjug1:
            y = y - (maxjug1 - x)
            x = maxjug1
        else:
            return None
    elif rule == 6:
        if x + y >= maxjug2:
            x = x - (maxjug2 - y)
            y = maxjug2
        else:
            return None
    elif rule == 7:
        if x + y < maxjug1:
            x = x + y
            y = 0
        else:
            return None
    elif rule == 8:
        if x + y < maxjug2:
            x = 0
            y = x + y
        else:
            return None

    if x == cnode.x and y == cnode.y:
        return None

    nextnode = node(cnode)
    nextnode.x = x
    nextnode.y = y
    nextnode.parent = cnode
    return nextnode

def pushlist(list1):
    for m in list1:
        dfsq.put(m)

def popnode():
    if dfsq.empty():
        return None
    else:
        return dfsq.get()

def isGoalNode(cnode, gnode):
    if cnode.x == gnode.x and cnode.y == gnode.y:
        return True
    return False

visitednodelist = []

def dfsMain(initialNode, GoalNode):
    dfsq.put(initialNode)
    while not dfsq.empty():
        visited_node = popnode()
        print("Pop node:")
        visited_node.printnode()
        if isGoalNode(visited_node, GoalNode):
            return visited_node
        successor_nodes = generateAllSuccessors(visited_node)
        pushlist(successor_nodes)
    return None

def IsNodeInlist(node, list1):
    for m in list1:
        if node.x == m.x and node.y == m.y:
            return True
    return False

def printpath(cnode):
    temp = cnode
    list2 = []
    while temp is not None:
        list2.append(temp)
        temp = temp.parent
    list2.reverse()
    for i in list2:
        i.printnode()
    print("Path Cost:", len(list2))

if __name__ == '__main__':
    list2 = []
    maxjug1 = int(input("Enter value of maxjug1:"))
    maxjug2 = int(input("Enter value of maxjug2:"))
    initialNode = node(None)
    initialNode.x = 0
    initialNode.y = 0
    initialNode.parent = None
    GoalNode = node(None)
    GoalNode.x = int(input("Enter value of Goal in jug1:"))
    GoalNode.y = 0
    GoalNode.parent = None

    start_time = time.time()
    solutionNode = dfsMain(initialNode, GoalNode)
    end_time = time.time()

    if solutionNode is not None:
        print("Solution can Found:")
        printpath(solutionNode)
    else:
        print("Solution can't be found.")

    diff = end_time - start_time
    print("Execution Time:", diff * 1000, "ms")


program 2: cannibals and missionaries


import copy

# The problem starts with 3 Missionaries (M) and 3 Cannibals (C) in the left side of a river
# trying to cross with a boat (B) going to the right side (rightCoast) with the restriction
# that the number of Cannibals will never outnumber the Missionaries on either side.

class CoastState:
    def __init__(self, c, m):
        self.cannibals = c
        self.missionaries = m

    # Check if the state of the coast is valid
    def valid_coast(self):
        if self.missionaries >= self.cannibals or self.missionaries == 0:
            return True
        else:
            return False

    # Check if the goal state has been reached
    def goal_coast(self):
        if self.cannibals == 3 and self.missionaries == 3:
            return True
        else:
            return False

class GameState:
    def __init__(self, data):
        self.data = data
        self.parent = None

    # Creating the Search Tree
    def building_tree(self):
        children = []
        coast = ""
        across_coast = ""
        temp = copy.deepcopy(self.data)

        if self.data["boat"] == "left":
            coast = "left"
            across_coast = "right"
        elif self.data["boat"] == "right":
            coast = "right"
            across_coast = "left"

        # MOVING 2 CANNIBALS (CC)
        if temp[coast].cannibals >= 2:
            temp[coast].cannibals -= 2
            temp[across_coast].cannibals += 2
            temp["boat"] = across_coast
            if temp[coast].valid_coast() and temp[across_coast].valid_coast():
                child = GameState(temp)
                child.parent = self
                children.append(child)

        temp = copy.deepcopy(self.data)
        # MOVING 2 MISSIONARIES (MM)
        if temp[coast].missionaries >= 2:
            temp[coast].missionaries -= 2
            temp[across_coast].missionaries += 2
            temp["boat"] = across_coast
            if temp[coast].valid_coast() and temp[across_coast].valid_coast():
                child = GameState(temp)
                child.parent = self
                children.append(child)

        temp = copy.deepcopy(self.data)
        # MOVING 1 CANNIBAL (C)
        if temp[coast].cannibals >= 1:
            temp[coast].cannibals -= 1
            temp[across_coast].cannibals += 1
            temp["boat"] = across_coast
            if temp[coast].valid_coast() and temp[across_coast].valid_coast():
                child = GameState(temp)
                child.parent = self
                children.append(child)

        temp = copy.deepcopy(self.data)
        # MOVING 1 MISSIONARY (M)
        if temp[coast].missionaries >= 1:
            temp[coast].missionaries -= 1
            temp[across_coast].missionaries += 1
            temp["boat"] = across_coast
            if temp[coast].valid_coast() and temp[across_coast].valid_coast():
                child = GameState(temp)
                child.parent = self
                children.append(child)

        temp = copy.deepcopy(self.data)
        # MOVING 1 CANNIBAL AND 1 MISSIONARY (CM)
        if temp[coast].missionaries >= 1 and temp[coast].cannibals >= 1:
            temp[coast].missionaries -= 1
            temp[across_coast].missionaries += 1
            temp[coast].cannibals -= 1
            temp[across_coast].cannibals += 1
            temp["boat"] = across_coast
            if temp[coast].valid_coast() and temp[across_coast].valid_coast():
                child = GameState(temp)
                child.parent = self
                children.append(child)

        return children

def breadth_first_search():
    left = CoastState(3, 3)
    right = CoastState(0, 0)
    root_data = {"left": left, "right": right, "boat": "left"}

    explored = []
    nodes = []
    path = []
    nodes.append(GameState(root_data))

    while len(nodes) > 0:
        g = nodes.pop(0)
        explored.append(g)
        if g.data["right"].goal_coast():
            path.append(g)
            return g
        else:
            next_children = g.building_tree()
            for x in next_children:
                if (x not in nodes) or (x not in explored):
                    nodes.append(x)
    return None

def print_path(g):
    path = [g]
    while g.parent:
        g = g.parent
        path.append(g)

    print("                 " + "Left Side" + "                      " + "Right Side" + "                   " + "Boat")
    print(
        "          Cannibals" + "     Missionaries" + "       " + "Cannibals" + "       Missionaries" + "    Boat Position")
    counter = 0
    for p in reversed(path):
        print("State " + str(counter) + "    Left C: " + str(p.data["left"].cannibals) + ".    Left M: "
              + str(p.data["left"].missionaries) + ".     |   Right C: " + str(
            p.data["right"].cannibals) + ".     Right M: " + str(p.data["right"].missionaries) + ".     | Boat: " + str(
            p.data["boat"]))
        counter += 1
    print("End of Path!")

def main():
    solution = breadth_first_search()
    print("Missionaries and Cannibals AI Problem Solution using Breadth-First Search:")
    print_path(solution)

if __name__ == "__main__":
    main()


program 3: 8 queens

print("Enter the number of queens")
N = int(input())
board = [[0] * N for _ in range(N)]

def is_attack(i, j):
    for k in range(0, N):
        if board[i][k] == 1 or board[k][j] == 1:
            return True
    for k in range(0, N):
        for l in range(0, N):
            if (k + l == i + j) or (k - l == i - j):
                if board[k][l] == 1:
                    return True
    return False

def N_queen(n):
    if n == 0:
        return True
    for i in range(0, N):
        for j in range(0, N):
            if (not is_attack(i, j)) and (board[i][j] != 1):
                board[i][j] = 1
                if N_queen(n - 1) == True:
                    return True
                board[i][j] = 0
    return False

N_queen(N)
for i in board:
    print(i)


program 4: tsp using heuristic approach


import math

maxsize = float('inf')

def copyToFinal(curr_path):
    final_path[:N + 1] = curr_path[:]
    final_path[N] = curr_path[0]

def firstMin(adj, i):
    min = maxsize
    for k in range(N):
        if adj[i][k] < min and i != k:
            min = adj[i][k]
    return min

def secondMin(adj, i):
    first, second = maxsize, maxsize
    for j in range(N):
        if i == j:
            continue
        if adj[i][j] <= first:
            second = first
            first = adj[i][j]
        elif adj[i][j] <= second and adj[i][j] != first:
            second = adj[i][j]
    return second

def TSPRec(adj, curr_bound, curr_weight, level, curr_path, visited):
    global final_res

    if level == N:
        if adj[curr_path[level - 1]][curr_path[0]] != 0:
            curr_res = curr_weight + adj[curr_path[level - 1]][curr_path[0]]
            if curr_res < final_res:
                copyToFinal(curr_path)
                final_res = curr_res
        return

    for i in range(N):
        if adj[curr_path[level - 1]][i] != 0 and not visited[i]:
            temp = curr_bound
            curr_weight += adj[curr_path[level - 1]][i]
            if level == 1:
                curr_bound -= ((firstMin(adj, curr_path[level - 1]) + firstMin(adj, i)) / 2)
            else:
                curr_bound -= ((secondMin(adj, curr_path[level - 1]) + firstMin(adj, i)) / 2)

            if curr_bound + curr_weight < final_res:
                curr_path[level] = i
                visited[i] = True
                TSPRec(adj, curr_bound, curr_weight, level + 1, curr_path, visited)

            curr_weight -= adj[curr_path[level - 1]][i]
            curr_bound = temp
            visited = [False] * len(visited)
            for j in range(level):
                if curr_path[j] != -1:
                    visited[curr_path[j]] = True

def TSP(adj):
    curr_bound = 0
    curr_path = [-1] * (N + 1)
    visited = [False] * N

    for i in range(N):
        curr_bound += (firstMin(adj, i) + secondMin(adj, i))
    curr_bound = math.ceil(curr_bound / 2)
    visited[0] = True
    curr_path[0] = 0
    TSPRec(adj, curr_bound, 0, 1, curr_path, visited)

adj = [[0, 4, 12, 7],
       [5, 0, 0, 18],
       [11, 0, 0, 6],
       [10, 2, 3, 0]]
N = 4
final_path = [None] * (N + 1)
visited = [False] * N
final_res = maxsize
TSP(adj)

print("Minimum cost :", final_res)
print("Path Taken : ", end=' ')
for i in range(N + 1):
    print(final_path[i], end=' ')


program 5: tic tac toe


import numpy as np
import random
from time import sleep

def create_board():
    return np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])

def possibilities(board):
    l = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                l.append((i, j))
    return l

def random_place(board, player):
    selection = possibilities(board)
    current_loc = random.choice(selection)
    board[current_loc] = player
    return board

def row_win(board, player):
    for x in range(len(board)):
        win = True
        for y in range(len(board)):
            if board[x, y] != player:
                win = False
                continue
        if win:
            return win
    return win

def col_win(board, player):
    for x in range(len(board)):
        win = True
        for y in range(len(board)):
            if board[y][x] != player:
                win = False
                continue
        if win:
            return win
    return win

def diag_win(board, player):
    win = True
    for x in range(len(board)):
        if board[x, x] != player:
            win = False
    if win:
        return win
    win = True
    for x in range(len(board)):
        y = len(board) - 1 - x
        if board[x, y] != player:
            win = False
    return win

def evaluate(board):
    winner = 0
    for player in [1, 2]:
        if row_win(board, player) or col_win(board, player) or diag_win(board, player):
            winner = player
    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner

def play_game():
    board, winner, counter = create_board(), 0, 1
    print(board)
    sleep(2)
    while winner == 0:
        for player in [1, 2]:
            board = random_place(board, player)
            print("Board after " + str(counter) + " move")
            print(board)
            sleep(2)
            counter += 1
            winner = evaluate(board)
            if winner != 0:
                break
    return winner

print("Winner is: " + str(play_game()))


