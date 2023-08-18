'''
Created on 2023. 8. 17.

@author: 유승민
'''
from basic.AudioTVParent import AudioTVParent

# 상속 표현: class 자식클래스(부모클래스)
class Audio(AudioTVParent):
    def __init__(self, power, volumn):
        # super() 생성자
        super().__init__(power, volumn)
        
    def tune(self):
        str01 = "ha ha ha..." if self.power else "turn it on"
        # if self.power:
        #     str01 = "ha ha ha..."
        # else:
        #   str01 = "turn it on"
        print(str01)
        
        
        
    