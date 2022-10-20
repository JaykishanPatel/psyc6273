# stair.py  Module that defines a staircase class

# A class defines an object. It is a collection of data, along with methods for accessing
# and manipulating that data. Objects have attributes (variables)
# and methods (functions).

# Object-oriented programming is one way of using encapsulation,
# i.e., hiding unnecessary details from the user.

# Definition of a simple class Observer
class Observer:
	'''
	Class that defines an Observer object.
	It has 2 attributes: name, age, runxp, and one method time4break.
	time4break tells us when the observer should take a break based on the experiment step
	and the observer age - the older the sooner.
	'''

	# Initilisation method to initialise attributes
	def __init__(self, name, age):
		self.name = name
		self.age = age
		self.runxp = True

	# Method to indicate when the observer should take a break
	def time4break(self, step):
		if (step > (10 - self.age//10)):
			self.runxp = False
