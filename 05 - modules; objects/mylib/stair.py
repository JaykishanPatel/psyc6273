# stair.py  Module that defines a staircase class

# An object is a collection of data, along with methods for accessing
# and manipulating that data. Objects have attributes (variables)
# and methods (functions).

# Object-oriented programming is one way of using encapsulation,
# i.e., hiding unnecessary details from the user.

import random

# define a staircase class
class Stair:
    
    # the constructor is a special method called __init__, which
    # initializes the object
    def __init__(self, up=1, down=3, levels=[ i for i in range(10) ]):
        self.countLimits = [up, down]
        self.levels = levels
        self.count = [0, 0]
        self.stimk = round(len(levels)/2)
    
    # get the current stimulus level
    def stim(self):
        return self.levels[self.stimk]
    
    # report the result of a trial with the current stimulus level
    def response(self, correct):
        
        # increment the number of correct or incorrect trials
        self.count[correct] += 1
        
        # if too many incorrect trials, increase the stimulus level
        if self.count[0] >= self.countLimits[0]:
            self.stimk = min( self.stimk+1, len(self.levels)-1 )
            self.count = [0, 0]
            
        # if too many correct trials, decrease the stimulus level
        elif self.count[1] >= self.countLimits[1]:
            self.stimk = max( self.stimk-1, 0 )
            self.count = [0, 0]
    
    # __repr__ is a special function that is called whenever we print
    # the object; it should return a string that represents the current
    # state of the object
    def __repr__(self):
        return f'Stair(countlimits={self.countLimits}, levels={self.levels}, count={self.count}, stimk={self.stimk})'

