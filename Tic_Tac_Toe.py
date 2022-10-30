import turtle
import time




screen = turtle.Screen()

screen.title('Tic Tac Toe')
screen.setup(800, 800)
def quit():
    turtle.bye()
def restarted():
    coordinates_x = [[-266],[0],[266]]
    coordinates_y = [[266],[0],[-266]]
    x1 = 0
    x2 = 0
    x3 = 0
    x4 = 0
    x5 = 0
    x6 = 0
    x7 = 0
    x8 = 0
    x9 = 0
    turtle.goto(0, 0)
    turtle.penup()
    positions = [[x1], [x2], [x3], [x4], [x5], [x6], [x7], [x8], [x9]]
    steps = [[0], [1], [0], [1], [0], [1], [0], [1], [0], [1]]
    a = positions[0]
    class figures():
        def x_figure(coordinates_x, coordinates_y):
            
            x_figure = turtle.Turtle()
            x_figure.hideturtle()
            x_figure.pen(speed=10)
            x_figure.color('black')
            x_figure.shape('square')
            x_figure.penup()
            x_figure.goto(coordinates_x, coordinates_y)
            x_figure.shapesize(stretch_len=2,stretch_wid=12.25)
            x_figure.tilt(45)
            x_figure.showturtle()
            x_figure = x_figure.clone()
            x_figure.hideturtle()

            x_figure.tilt(-90)
            x_figure.penup()
            x_figure.showturtle()
        def o_figure(coordinates_x, coordinates_y):
            o_figure = turtle.Turtle()
            o_figure.speed(10)
            o_figure.hideturtle()
            o_figure.color('black')
            o_figure.penup()
            o_figure.goto(coordinates_x, coordinates_y)
            o_figure.pendown()
            o_figure.dot(250)
            o_figure.showturtle()
    class processing():
        def list_to_int_x(i):        
            aboba = str(coordinates_x[i])
            aboba = aboba.replace('[','')
            aboba = aboba.replace(']','')
            return int(aboba)
        def list_to_int_y(i):        
            aboba = str(coordinates_y[i])
            aboba = aboba.replace('[','')
            aboba = aboba.replace(']','')
            return int(aboba)










    turtle.bgpic("img\TABLE.png")

    turtle.hideturtle()

    #Для обозначения позиции processing.list_to_int_x(0), processing.list_to_int_y(0)





        




 
    iterat = 0
    checker = True
    while checker:
        
        if steps[iterat] == a:
            figure = 'x'
            
        else:
            figure = 'o'
        turtle.penup()
        turtle.speed(12)
        abc = screen.onscreenclick(turtle.goto)

        

        x_pos = int(turtle.xcor())
        y_pos = int(turtle.ycor())


        if x_pos < -150 and y_pos > 140 and x_pos != 0 and y_pos != 0:

            x_pos = 0
            y_pos = 0
            if positions[0] == a:
                positions[0] = figure
                if figure == "x":
                    figures.x_figure(processing.list_to_int_x(0), processing.list_to_int_y(0))
                else:
                    figures.o_figure(processing.list_to_int_x(0), processing.list_to_int_y(0))
                iterat+=1
            else:
                continue
            
        elif x_pos > -126 and y_pos < 390 and x_pos < 127 and y_pos > 140 and x_pos != 0 and y_pos != 0:

            if positions[1] == a:
                positions[1] = figure
                if figure == "x":
                    figures.x_figure(processing.list_to_int_x(1), processing.list_to_int_y(0))
                else:
                    figures.o_figure(processing.list_to_int_x(1), processing.list_to_int_y(0))
                iterat+=1
            else:
                continue

            x_pos = 0
            y_pos = 0

        elif x_pos > 139 and y_pos < 393 and x_pos < 392 and y_pos > 140 and x_pos != 0 and y_pos != 0:
            if positions[2] == a:
                positions[2] = figure
                
                if figure == "x":
                    figures.x_figure(processing.list_to_int_x(2), processing.list_to_int_y(0))
                else:
                    figures.o_figure(processing.list_to_int_x(2), processing.list_to_int_y(0))
                iterat+=1
            else:
                continue

            
            
            x_pos = 0
            y_pos = 0
        elif x_pos > -394 and y_pos < 126 and x_pos < -139 and y_pos > -128 and x_pos != 0 and y_pos != 0:
            if positions[3] == a:
                positions[3] = figure
                
                if figure == "x":
                    figures.x_figure(processing.list_to_int_x(0), processing.list_to_int_y(1))
                else:
                    figures.o_figure(processing.list_to_int_x(0), processing.list_to_int_y(1))
                iterat+=1
            else:
                continue
            
            
            
            x_pos = 0
            y_pos = 0
        elif x_pos > -129 and y_pos < 126 and x_pos < 127 and y_pos > -128 and x_pos != 0 and y_pos != 0:
            if positions[4] == a:
                positions[4] = figure
                if figure == "x":
                    figures.x_figure(processing.list_to_int_x(1), processing.list_to_int_y(1))
                else:
                    figures.o_figure(processing.list_to_int_x(1), processing.list_to_int_y(1))
                iterat+=1
            else:
                continue

            
            
            
            x_pos = 0
            y_pos = 0
        elif x_pos > 139 and y_pos < 125 and x_pos < 391 and y_pos > -128 and x_pos != 0 and y_pos != 0:
            if positions[5] == a:
                positions[5] = figure
                if figure == "x":
                    figures.x_figure(processing.list_to_int_x(2), processing.list_to_int_y(1))
                else:
                    figures.o_figure(processing.list_to_int_x(2), processing.list_to_int_y(1))
                iterat+=1
            else:
                continue

            
            
            
            x_pos = 0
            y_pos = 0

        elif x_pos > -394 and y_pos < -140 and x_pos < -139 and y_pos > -390 and x_pos != 0 and y_pos != 0:
            if positions[6] == a:
                positions[6] = figure
                if figure == "x":
                    figures.x_figure(processing.list_to_int_x(0), processing.list_to_int_y(2))
                else:
                    figures.o_figure(processing.list_to_int_x(0), processing.list_to_int_y(2))
                iterat+=1
            else:
                continue

            

            
            
            x_pos = 0
            y_pos = 0 
        elif x_pos > -128 and y_pos < -140 and x_pos < 127 and y_pos > -390 and x_pos != 0 and y_pos != 0:
            if positions[7] == a:
                positions[7] = figure
                if figure == "x":
                    figures.x_figure(processing.list_to_int_x(1), processing.list_to_int_y(2))
                else:
                    figures.o_figure(processing.list_to_int_x(1), processing.list_to_int_y(2))
                iterat+=1
            else:
                continue

            

            
            
            x_pos = 0
            y_pos = 0

        elif x_pos > 140 and y_pos < -140 and x_pos < 391 and y_pos > -390 and x_pos != 0 and y_pos != 0:
            if positions[8] == a:
                positions[8] = figure
                if figure == "x":
                    figures.x_figure(processing.list_to_int_x(2), processing.list_to_int_y(2))
                else:
                    figures.o_figure(processing.list_to_int_x(2), processing.list_to_int_y(2))
                iterat+=1
            else:
                continue

            
            
            x_pos = 0
            y_pos = 0

        turtle.goto(0, 0)
        if "x" in positions[0:1] and "x" in positions[1:2] and "x" in positions[2:3] or "x" in positions[3:4] and "x" in positions[4:5] and "x" in positions[5:6] or "x" in positions[6:7] and "x" in positions[7:8] and "x" in positions[8:9] or "x" in positions[0] and "x" in positions[4] and "x" in positions[8] or "x" in positions[2] and "x" in positions[4] and "x" in positions[6] or "x" in positions[0] and "x" in positions[3] and "x" in positions[6] or "x" in positions[1] and "x" in positions[4] and "x" in positions[7] or "x" in positions[2] and "x" in positions[5] and "x" in positions[8]:
        

            winner = 'X'
            checker = False
        elif "o" in positions[0:1] and "o" in positions[1:2] and "o" in positions[2:3] or "o" in positions[3:4] and "o" in positions[4:5] and "o" in positions[5:6] or "o" in positions[6:7] and "o" in positions[7:8] and "o" in positions[8:9] or "o" in positions[0] and "o" in positions[4] and "o" in positions[8] or "o" in positions[2] and "o" in positions[4] and "o" in positions[6] or "o" in positions[0] and "o" in positions[3] and "o" in positions[6] or "o" in positions[1] and "o" in positions[4] and "o" in positions[7] or "o" in positions[2] and "o" in positions[5] and "o" in positions[8]:
            

            winner = 'O'
            checker = False
        elif iterat == 9:
            

            checker = False
            winner = 'Tie'

    if checker == False:

        turtle.clearscreen()
        if winner == 'X':

            turtle.bgpic('img/x_win.png')
        elif winner == 'O':

            turtle.bgpic('img/o_win.png')
        elif winner == 'Tie':
            turtle.bgpic('img/Tie_win.png')

        turtle.penup()
        turtle.speed(10)
        turtle.hideturtle()
        while True:
            time.sleep(0.1)
            screen.onclick(turtle.goto)

            x_popo = int(turtle.xcor())
            y_popo = int(turtle.ycor())
            if x_popo > -358 and y_popo < -171 and x_popo < -206 and y_popo > -347:


                restarted()
            elif x_popo > 174 and y_popo < -171 and x_popo < 362 and y_popo > -355:
                quit()
            turtle.goto(0,0)
                      
restarted()