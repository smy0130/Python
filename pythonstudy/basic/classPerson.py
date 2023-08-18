'''
Created on 2023. 8. 17.

@author: 유승민
'''
class Person:
    # 생성자
    def __init__(self, name):
        self.name = name
    
    # 함수- 메서드    
    def say_hello(self):
        print("Hi!", self.name)