from Snake import Snake_class
import time

class UI: 
    window_x = 720
    window_y = 480 

    def __init__(self,pg) -> None:
        self.pg=pg
        self.black = self.pg.Color(0, 0, 0)
        self.white = self.pg.Color(255, 255, 255)
        self.red = self.pg.Color(255, 0, 0)
        self.green = self.pg.Color(0, 255, 0)
        self.blue = self.pg.Color(0, 0, 255)
        pg.init()
        self.pg.display.set_caption('Snakes Game')
        UI.game_window = self.pg.display.set_mode((UI.window_x, UI.window_y)) 
        pg.init()

    def game_over_show(self):
        my_font = self.pg.font.SysFont('times new roman', 50)
        game_over_surface = my_font.render('Your Score is : ' + str(Snake_class.score), True, self.red)
        game_over_rect = game_over_surface.get_rect()
        game_over_rect.midtop = (UI.window_x/2, UI.window_y/4)
        UI.game_window.blit(game_over_surface, game_over_rect)
        self.pg.display.flip()
        time.sleep(2)
        self.pg.quit()
        quit()
        
    def show_score( self,color, font, size):
        score_font = self.pg.font.SysFont(font, size)
        score_surface = score_font.render('Score : ' + str(Snake_class.score), True, color)
        score_rect = score_surface.get_rect()
        self.game_window.blit(score_surface, score_rect)
        self.pg.display.flip()

    def Black_Screen(self):
        UI.game_window.fill(self.black)
    
    def Draw_snake(self):
        for pos in Snake_class.snake_body:
            self.pg.draw.rect(UI.game_window, self.red, self.pg.Rect(
            pos[0], pos[1], 10, 10))
            self.pg.display.flip()
 
    def Draw_Apple(self,fruit_pos):
        self.pg.draw.rect(UI.game_window, self.blue, self.pg.Rect(fruit_pos[0],fruit_pos[1], 10, 10))

    def Print_Line(self):
        self.pg.draw.line(UI.game_window, self.green, (0, 20), (720, 20))
        self.pg.display.flip()

