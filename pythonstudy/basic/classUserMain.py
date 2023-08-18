'''
Created on 2023. 8. 17.

@author: 유승민
'''
from basic.classAudio import Audio
from basic.classTV import TV

obj01 = Audio(True, 15)
obj02 = TV(False, 12, 40)

obj01.set_volumn(10)
obj01.tune()

obj02.switch(True)
obj02.watch()