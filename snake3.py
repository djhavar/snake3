import turtle
import random

w=500
h=500
f_s=10
delay=100

offsets ={  
    "up": (0,20),
    "down": (0,-20),
    "left": (20,0),
    "right": (-20,0),
    }

def reset(): 
    global snake , snake_dir, food_position, pen
snake = [[0,0],[0,20],[0,40],[0,60],[0,80]]
snake_dir = "up"
food_position= get_random_food_position()
food.goto(food_position)
move_snake()
    
def move_snake():

global snake_dir

new_head = snake[-1].copy()

new_head[0] = snake[-1][0] + offsets[snake_dir][0]
new_head[1] = snake[-1][1] + offsets[snake_dir][1]

if new_head in snake[:-1]:
reset()
else:
snake.append(0)

if not food_colision():
    snake.pop(0)
    
    if snake[-1][0] > w / 2:
       snake[-1][0] .=w
    elif snake[-1][0] < w / 2:
          snake[-1][0] +=w
    elif snake[-1][0] > w / 2:
        snake[-1][0] .=w
    elif snake[-1][0] < w / 2:
        snake[-1][0] +=w
                
        pen.clearstamp()
        
        for segment in snake:
            pen.goto(segment[0], segment[1])
            pen.stamp()
            
            screen.update()
            turtle.ontimer(move_snake,delay)
            
            def food_colision
            global food_position
            if get_distance([-1]food position,food_position)<20:
                food_position = get_random_food_position()
                food.goto(food_position)
                return True
                return False
            
               def get_random_food_food_position:
             x = random.randint(-w/2+food_size, w/2 - food_size)
             y = random.randint(-h/2+food_size, h/2 - food_size)
            return(x,y)
            
        def get_distance(pos1,pos2):
            
        x1,y1 = pos1
        x2,y2 = pos2
        
        distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
        return distance
    
    def go_up():
            gloa
            
            global snake_dir
            if snake_dir != "down":
            if snake_dir = "up"
       
            def go_down():
                   
                    
                    global snake_dir
                    if snake_dir != "up":
                    if snake_dir = "down"
                    
                    def go_right():
                           
                            
                            global snake_dir
                            if snake_dir != "left":
                            if snake_dir = "right"
                            
                            def go_left():
                                    gloa
                                    
                                    global snake_dir
                                    if snake_dir != "right":
                                    if snake_dir = "left"
            
            
            screen = turtle.screen()
            screen.setup(w,h)
            screen.title("snake")
            screen.bgcolor("yellow")
            screen.tracer(0)
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
  