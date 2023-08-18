'''
Created on 2023. 8. 17.

@author: 유승민
'''
class AudioTVParent:
    def __init__(self, power, volumn):
        self.power = power
        self.volumn = volumn
    
    def switch(self, onOff):
        self.power = onOff
    
    def set_volumn(self, vol):
        self.volumn = vol