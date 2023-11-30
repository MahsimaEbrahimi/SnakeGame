from Snake import Snake_class
from Apple import Apple_Class
from Game import GameClass
from ConsoleUI import UI
import pygame as pg

if __name__=="__main__":

    fps = pg.time.Clock()

    Snake_obj=Snake_class()
    Apple_obj=Apple_Class()
    Game_obj=GameClass(pg)
    UI_Obj=UI(pg)        

    Apple_obj.GetApplePosition()        

    while True:
        
        UI_Obj.Print_Line()
        UI_Obj.show_score(UI_Obj.white, 'times new roman', 20)
        UI_Obj.Draw_snake()

        Game_obj.Check_move()      
        Game_obj.Key_control()
        Game_obj.Eat_apple
        Game_obj.Snake_move_Dir()
        UI_Obj.Black_Screen()

        UI_Obj.Draw_Apple(Apple_obj.fruit_position)
            
        if(Game_obj.Eat_apple()==True):  
            UI_Obj.Black_Screen()
            Apple_obj.GetApplePosition()        
            UI_Obj.Draw_Apple(Apple_obj.fruit_position)


        if(Game_obj.Hit_The_Wall()==True):
            UI_Obj.game_over_show()

        if(Game_obj.Touching_Snake_body()==True):
            UI_Obj.game_over_show()

            
        fps.tick(Snake_class.snake_speed)

