# -*- coding: utf-8 -*-
"""
@author: kevmm
"""

class CircleOne:
    
    
    def __init__(self,pie,radius):
        self.pie = pie
        self.radius = radius
        
    def calcArea(self):
        self.ans1 = self.pie * self.radius * self.radius
        
        
class CircleTwo(CircleOne):
    pass
        
    def calcCircum(self):
            self.ans2 = self.pie * self.pie * self.radius
            
answerof = CircleOne(5,2)
answerof.calcArea()
print(answerof.ans1)
answer2 = CircleTwo(3,2)
answer2.calcCircum()
print(answer2.ans2)