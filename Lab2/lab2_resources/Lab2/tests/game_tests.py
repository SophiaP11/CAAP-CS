# importing package to be able to run the tests
from nose.tools import *
# Here you should import all the modules/classes you want to test
from game.scores import Score
import game.game
from game.map import Map

# define a function like these for each class/module you test.
# e.g. assert 2+2 == 4
def test_map():
    testMap = Map('central_corridor')
    assert(testMap.opening_scene(),'central_corridor')

def test_scores():
	pass
    #raise ValueError ('todo')

# etc...