#
# board.py (Final project)
#
# A Board class for the Eight Puzzle
#

# a 2-D list that corresponds to the tiles in the goal state
GOAL_TILES = [['0', '1', '2'],
              ['3', '4', '5'],
              ['6', '7', '8']]

class Board:
    """ A class for objects that represent an Eight Puzzle board.
    """
    def __init__(self, digitstr):
        """ a constructor for a Board object whose configuration
            is specified by the input digitstr
            input: digitstr is a permutation of the digits 0-9
        """
        # check that digitstr is 9-character string
        # containing all digits from 0-9
        assert(len(digitstr) == 9)
        for x in range(9):
            assert(str(x) in digitstr)

        self.tiles = [[''] * 3 for x in range(3)]
        self.blank_r = -1
        self.blank_c = -1

        # Put your code for the rest of __init__ below.
        # Do *NOT* remove our code above.
        for r in range(3):
            for c in range(3):
                self.tiles[r][c] = digitstr[3 * r + c]
                if self.tiles[r][c] == '0':
                    self.blank_r = r
                    self.blank_c = c

    ### Add your other method definitions below. ###
    
    def __repr__(self):
        """ returns a string representation of a Board object.
        """
        output = ''
        for r in range(3):
            for c in range(3):
                if self.tiles[r][c] == '0':
                    output += '_ '
                else:
                    output = output + self.tiles[r][c] + ' '
            output += '\n'
        return output
    
    def move_blank(self, direction):
        """ takes as input a string direction that specifies the direction in 
            which the blank should move.
        """
        if direction == 'up':
            newr = self.blank_r - 1
            if newr < 0:
                return False
            else:
                self.blank_r = newr
                self.tiles[self.blank_r + 1][self.blank_c] = \
                    self.tiles[self.blank_r][self.blank_c]
                self.tiles[self.blank_r][self.blank_c] = '0'
                return True
        elif direction == 'down':
            newr = self.blank_r + 1
            if newr > 2:
                return False
            else:
                self.blank_r = newr
                self.tiles[self.blank_r - 1][self.blank_c] = \
                    self.tiles[self.blank_r][self.blank_c]
                self.tiles[self.blank_r][self.blank_c] = '0'
                return True
        elif direction == 'left':
            newc = self.blank_c - 1
            if newc < 0:
                return False
            else:
                self.blank_c = newc
                self.tiles[self.blank_r][self.blank_c + 1] = \
                    self.tiles[self.blank_r][self.blank_c]
                self.tiles[self.blank_r][self.blank_c] = '0'
                return True
        else:
            newc = self.blank_c + 1
            if newc > 2:
                return False
            else:
                self.blank_c = newc
                self.tiles[self.blank_r][self.blank_c - 1] = \
                    self.tiles[self.blank_r][self.blank_c]
                self.tiles[self.blank_r][self.blank_c] = '0'
                return True
    
    def digit_string(self):
        """ returns the string of digits that was used when creating the Board
        """
        s = ''
        for i in str(self):
            if i == '_':
                s += '0'
            elif i not in ' \n':
                s += i
        return s
    
    def copy(self):
        """ returns a newly-constructed Board object that is a deep copy of 
            the called object
        """
        return Board(self.digit_string())
    
    def num_misplaced(self):
        """ counts and returns the number of tiles in the called Board object 
            that are not where they should be in the goal state
        """
        count = 0
        for r in range(3):
            for c in range(3):
                if GOAL_TILES[r][c] != self.tiles[r][c]:
                    if self.tiles[r][c] != '0':
                        count += 1
        return count 
    
    def avgdifference(self):
        """ returns the averge index difference compared with the goal state
        """
        result = 0
        
        for r in range(3):
            for c in range(3):
                if self.tiles[r][c] != GOAL_TILES[r][c]:
                    if self.tiles[r][c] == '1':
                        result += abs(r) + abs(c - 1)
                    elif self.tiles[r][c] == '2':
                        result += abs(r) + abs(c - 2)
                    elif self.tiles[r][c] == '3':
                        result += abs(r - 1) + abs(c)
                    elif self.tiles[r][c] == '4':
                        result += abs(r - 1) + abs(c - 1)
                    elif self.tiles[r][c] == '5':
                        result += abs(r - 1) + abs(c - 2)
                    elif self.tiles[r][c] == '6':
                        result += abs(r - 2) + abs(c)
                    elif self.tiles[r][c] == '7':
                        result += abs(r - 2) + abs(c - 1)
                    elif self.tiles[r][c] == '8':
                        result += abs(r - 2) + abs(c - 2)

        return result
                    
                    
    
    def __eq__(self, other):
        """ return True if the called object (self) and the argument (other) 
            have the same values for the tiles attribute
        """
        for r in range(3):
            for c in range(3):
                if self.tiles[r][c] != other.tiles[r][c]:
                    return False
        return True






