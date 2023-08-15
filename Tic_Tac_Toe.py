import time
import turtle

screen = turtle.Screen()

screen.title('Tic Tac Toe')
screen.setup(800, 800)

coordinates_x = []
coordinates_y = []
steps = []
a = []
positions = []
iteration = 0
figure = ''
x_pos = 0
y_pos = 0


def quit_turtle():
    turtle.bye()


def restarted():
    global coordinates_x, coordinates_y, steps, a, positions
    coordinates_x = [[-266], [0], [266]]
    coordinates_y = [[266], [0], [-266]]
    turtle.goto(0, 0)
    turtle.penup()
    positions = [[0], [0], [0], [0], [0], [0], [0], [0], [0]]
    steps = [[0], [1], [0], [1], [0], [1], [0], [1], [0], [1]]
    a = positions[0]
    game_process()


class Figures:
    global coordinates_x, coordinates_y

    def x_figure(coordinates_x_figure, coordinates_y_figure):
        x_figure = turtle.Turtle()
        x_figure.hideturtle()
        x_figure.pen(speed=10)
        x_figure.color('black')
        x_figure.shape('square')
        x_figure.penup()
        x_figure.goto(coordinates_x_figure, coordinates_y_figure)
        x_figure.shapesize(stretch_len=2, stretch_wid=12.25)
        x_figure.tilt(45)
        x_figure.showturtle()
        x_figure = x_figure.clone()
        x_figure.hideturtle()

        x_figure.tilt(-90)
        x_figure.penup()
        x_figure.showturtle()

    def o_figure(coordinates_x_figure, coordinates_y_figure):
        o_figure = turtle.Turtle()
        o_figure.speed(10)
        o_figure.hideturtle()
        o_figure.color('black')
        o_figure.penup()
        o_figure.goto(coordinates_x_figure, coordinates_y_figure)
        o_figure.pendown()
        o_figure.dot(250)
        o_figure.showturtle()


# noinspection PyUnresolvedReferences
class Processing:
    def list_to_int_x(self):
        cleaned_list = str(coordinates_x[self])
        cleaned_list = cleaned_list.replace('[', '')
        cleaned_list = cleaned_list.replace(']', '')
        return int(cleaned_list)

    def list_to_int_y(self):
        cleaned_list = str(coordinates_y[self])
        cleaned_list = cleaned_list.replace('[', '')
        cleaned_list = cleaned_list.replace(']', '')
        return int(cleaned_list)

    def check_winner(positions, player):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]  # Diagonals
        ]

        for combo in winning_combinations:
            if all(positions[i] == player for i in combo):
                return True
        return False

    def checking_click():
        global iteration, positions, a, figure, x_pos, y_pos
        button_positions = [[-400, -150, 390, 140, 0, 0, 0], [-126, 127, 390, 140, 1, 0, 1],
                            [139, 392, 390, 140, 2, 0, 2],
                            [-400, -150, 126, -128, 0, 1, 3], [-126, 127, 126, -128, 1, 1, 4],
                            [139, 392, 126, -128, 2, 1, 5],
                            [-400, -150, -140, -390, 0, 2, 6], [-126, 127, -140, -390, 1, 2, 7],
                            [139, 392, -140, -390, 2, 2, 8]]
        for i in range(len(button_positions)):
            border_x_first = button_positions[i][0]
            border_x_second = button_positions[i][1]
            border_y_first = button_positions[i][2]
            border_y_second = button_positions[i][3]
            for_figure_pos_x = button_positions[i][4]
            for_figure_pos_y = button_positions[i][5]
            for_positions = button_positions[i][6]

            if border_x_first < x_pos < border_x_second and border_y_first > y_pos > border_y_second and x_pos != 0 and y_pos != 0:
                print(for_figure_pos_x, for_figure_pos_y)
                if positions[for_positions] == a:
                    positions[for_positions] = figure
                    if figure == "x":
                        Figures.x_figure(Processing.list_to_int_x(for_figure_pos_x),
                                         Processing.list_to_int_y(for_figure_pos_y))
                    else:
                        Figures.o_figure(Processing.list_to_int_x(for_figure_pos_x),
                                         Processing.list_to_int_y(for_figure_pos_y))
                    iteration += 1
                x_pos = 0
                y_pos = 0


def game_process():
    global coordinates_x, coordinates_y, steps, a, positions, iteration, figure, x_pos, y_pos
    who_win = ''
    turtle.bgpic(r"img\TABLE.png")

    turtle.hideturtle()

    iteration = 0
    checker = True
    while checker:
        if steps[iteration] == a:
            figure = 'x'
        else:
            figure = 'o'

        turtle.penup()
        turtle.speed(12)
        screen.onscreenclick(turtle.goto)

        x_pos = int(turtle.xcor())
        y_pos = int(turtle.ycor())
        Processing.checking_click()

        turtle.goto(0, 0)
        if Processing.check_winner(positions, 'x'):
            who_win = 'X'
            checker = False

        elif Processing.check_winner(positions, 'o'):
            who_win = 'O'
            checker = False

        elif iteration == 9:
            checker = False
            who_win = 'Tie'
        else:
            who_win = 'Tie'

    if checker is False:
        turtle.clearscreen()
        if who_win == 'X':
            turtle.bgpic('img/x_win.png')
        elif who_win == 'O':
            turtle.bgpic('img/o_win.png')
        elif who_win == 'Tie':
            turtle.bgpic('img/Tie_win.png')

        turtle.penup()
        turtle.speed(10)
        turtle.hideturtle()

        while True:
            time.sleep(0.1)
            screen.onclick(turtle.goto)

            x_popo = int(turtle.xcor())
            y_popo = int(turtle.ycor())
            if -358 < x_popo < -206 and -171 > y_popo > -347:
                restarted()
            elif 174 < x_popo < 362 and -171 > y_popo > -355:
                quit_turtle()
            turtle.goto(0, 0)


restarted()
