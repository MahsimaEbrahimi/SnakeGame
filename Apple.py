import random
from ConsoleUI import UI

class Apple_Class:
    fruit_position=[]


    fruit_spawn=True

    def GetApplePosition(self):

        Apple_Class.fruit_position = [random.randrange(1, (UI.window_x//10)) * 10,
				random.randrange(20,((UI.window_y)//10)) * 10]