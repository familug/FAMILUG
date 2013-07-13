#!usr/bin/env python2
"""Example from Full Circle Magazine 30"""
"""Demonstrate class - object """

class Cat():
	#every class has __init__(self,...)
	def __init__(self, catname, catowner, catcolor, catheight, catage, catmood):
		#setup the atrributes of our cat
		self.name = catname;
		self.owner = catowner;
		self.color = catcolor;
		self.height = catheight;
		self.age = catage;
		self.mood = catmood;
		self.hungry = False;

	#define Eat method()
	def eat(self):
		if self.hungry:
			print "Mew, yum yum.. num num"
			self.hungry = False 
		else:
			print "Mew, gru... I don't want to eat"

Dan = Cat("Dan", "HVN", "White", "10cm", "5 months", "Fun")
print "My name is %s" % Dan.name
print "My owner is %s" % Dan.owner
print "My color is %s" % Dan.color
print "My age is %s" % Dan.age
print "I'm %s" % Dan.mood

Dan.eat()
Dan.hungry = True
Dan.eat()
