from Snake import Snake_class
from Apple import Apple_Class
from ConsoleUI import UI


class GameClass:
    def __init__(self,pg) -> None:
        self.pg=pg
        

    def Key_control(self):
        for event in self.pg.event.get():
           if event.type == self.pg.KEYDOWN:
              if event.key == self.pg.K_UP:
                  Snake_class.change_to = 'UP'
              if event.key == self.pg.K_DOWN:
                  Snake_class.change_to = 'DOWN'
              if event.key == self.pg.K_LEFT:
                  Snake_class.change_to= 'LEFT'
              if event.key == self.pg.K_RIGHT:
                  Snake_class.change_to = 'RIGHT' 


    def Check_move(self):
        if Snake_class.change_to == 'UP' and Snake_class.direction != 'DOWN':
            Snake_class.direction = 'UP'

        if Snake_class.change_to == 'DOWN' and Snake_class.direction  != 'UP':
            Snake_class.direction = 'DOWN'

        if Snake_class.change_to == 'LEFT' and Snake_class.direction  != 'RIGHT':
            Snake_class.direction = 'LEFT'
            
        if Snake_class.change_to == 'RIGHT' and Snake_class.direction  != 'LEFT':
            Snake_class.direction = 'RIGHT'

    def Snake_move_Dir(self):
        if Snake_class.direction == 'UP':
           Snake_class.snake_position[1] -= 10
        if Snake_class.direction == 'DOWN':
           Snake_class.snake_position[1] += 10
        if Snake_class.direction == 'LEFT':
           Snake_class.snake_position[0] -= 10
        if Snake_class.direction == 'RIGHT':
           Snake_class.snake_position[0] += 10

    def Eat_apple(self):                   
        Snake_class.snake_body.insert(0, list(Snake_class.snake_position))
        if(	Snake_class.snake_position[0] == Apple_Class.fruit_position[0] and Snake_class.snake_position[1] == Apple_Class.fruit_position[1]):
                    Snake_class.score+=10        
                    return True
        else:
            Snake_class.snake_body.pop()

    def Hit_The_Wall(self):
        if Snake_class.snake_position[0] < 0 or Snake_class.snake_position[0] > UI.window_x-10:
           return True
        if Snake_class.snake_position[1] < 20 or Snake_class.snake_position[1] > UI.window_y-10:
            return True
   
    def Touching_Snake_body(self):
    	for block in Snake_class.snake_body[1:]:
		    if Snake_class.snake_position[0] == block[0] and Snake_class.snake_position[1] == block[1]:
                        return True  