"""
Author: Alec Arcand
Breadth First Search implemented to
traverse grid represented by a string

Traverses an nxn grid represented by a single 
string to find a goal node. Possible moves are 
the value of the current node. The path of the 
start node to the end node is returned
"""

class bfs:
    def __init__(self):
        self.solution = ""
        self.frontier = []
        self.visited = []
        self.index = 0
        self.parent = {}

    def solve(self):
        """Retraces the nodes from the final
        node to the start node, then calculates
        and returns the directional moves
        """
        final_nodes = []
        final_nodes.append(self.index)
        while final_nodes[-1] != 0:
            final_nodes.append(self.parent[final_nodes[-1]])

        final_nodes.reverse() # order of start node index to end node index

        for i, j in enumerate(final_nodes[:-1]):
            col = j % 5
            row = j // 5
            next_col = final_nodes[i+1] % 5
            next_row = final_nodes[i+1] // 5
            if next_row < row:
                self.solution += "U"
            if next_row > row:
                self.solution += "D"
            if next_col < col:
                self.solution += "L"
            if next_col > col:
                self.solution += "R"
        return self.solution

    def get_moves(self, board):
        """Returns all possible moves
        of the current node
        """
        pos_m = []
        col = self.index % 5
        row = self.index // 5
        if col >= int(board[self.index]):
            pos_m.append(self.index - int(board[self.index])) # left
        if 4 - col >= int(board[self.index]):
            pos_m.append(self.index + int(board[self.index])) # right
        if row >= int(board[self.index]):
            pos_m.append(self.index - int(board[self.index]) * 5) # up
        if 4 - row >= int(board[self.index]):
            pos_m.append(self.index + int(board[self.index]) * 5) # down

        return pos_m

    def search(self, board):
        """Main function, uses breadth
        first search to visit nodes until
        the goal node is visited
        """
        if board[0] == "G":
            self.solution = "Already a solution, no moves required"
            return self.solution

        self.frontier.append(self.index)
        self.visited.append(self.index)
        while len(self.frontier) > 0:
            self.index = int(self.frontier[0])
            node = board[int(self.frontier.pop(0))] # remove next node

            if node == "G":
                self.solve()
                return self.solution

            moves = self.get_moves(board)
            for i in moves:
                if i not in self.visited:
                    self.parent[i] = self.index # save parent of node
                    self.visited.append(i)
                    self.frontier.append(i)

        self.solution = "No solution found"
        return self.solution



#b = "2322443122G22124131321422"    #  D
#b = "442111132G132214312312332"    #  RD
#b = "3211142G13211224321321242"    #  RLD
#b = "13332113112122G4223434441"    #  RRD
#b = "34G3241334411234212311341"    #  DRUL
#b = "113241211141111431333G131"    #  RRDDL
#b = "332344212G421324113131122"    #  DRDLLLUR
#b = "2132123124132G34232414241"    #  DURDDRLUD
#b = "4243133124G31334132431342"    #  RLDLDRUDRL
#b = "3233G13221222244313141432"    #  DRDLUDLUDRDULRU
#b = "33334423131313443G3334221"    #  DRUDLULURLRLDUD
#b = "41244122332212G2221234211"    #  No Solution
#b = "3211122221221134323144G31"    #  No Solution

'''
if __name__ == '__main__':
    breadth_first = bfs()
    print(breadth_first.search(b))
'''
