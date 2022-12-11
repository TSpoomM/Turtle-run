import json
import turtle
import random
import time


class Player(turtle.Turtle):
    def __init__(self):
        super().__init__(visible=False)
        self.__user = ""
        self.__password = ""
        self.__score = 0

    @property
    def user(self):
        return self.__user

    @user.setter
    def user(self, new_user):
        self.__user = new_user

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, new_pass):
        self.__password = new_pass

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, new_score):
        self.__score = new_score

    def register(self):
        self.user = input("Enter your name: ")
        self.password = input("Enter Password: ")
        new_player = {
            self.user: {
                "password": self.password,
                "high score": self.score
            }
        }
        try:
            with open("players.json", "r") as data_file:
                data = json.load(data_file)
            data.update(new_player)
            with open("players.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        except FileNotFoundError:
            with open("players.json", "w") as data_file:
                json.dump(new_player, data_file, indent=4)
        print("Your account has been registered.")

    def login_game(self):
        self.user = input("Enter your name: ")
        self.password = input("Enter Password: ")
        with open("players.json", "r") as data_file:
            data = json.load(data_file)
        while True:
            try:
                if self.user in data:
                    if data[self.user]["password"] == self.password:
                        print("Login Successful.")
                        break
                    else:
                        print('Please enter a valid password.')
                        self.password = input("Enter Password: ")
                else:
                    print('username not found.')
                    self.user = input("Enter your name: ")
                    self.password = input("Enter Password: ")
            except KeyError:
                print('username not found.')
                self.user = input("Enter your name: ")
                self.password = input("Enter Password: ")

    # move left
    def move_left(self):
        if self.xcor() - 100 > -300:
            self.setx(self.xcor() - 100)

    # move right
    def move_right(self):
        if self.xcor() + 100 < 300:
            self.setx(self.xcor() + 100)


class Point(turtle.Turtle):
    def __init__(self, shape, pos):
        super().__init__(visible=False)
        self.shape(shape)
        self.speed(0)
        self.shape("circle")
        self.rgb = random.choice(['green', 'purple', 'blue'])
        self.color(self.rgb)
        self.shapesize(2)
        self.penup()
        self.setheading(270)
        self.setpos(random.choice(pos))
        self.showturtle()
        self.__move = 10
        self.__time = time.time()

    def move(self):
        self.forward(self.__move)
        if time.time() - self.__time > 1:
            self.__move += 5

    def collide(self, player):
        return abs(self.xcor() - player.xcor()) < 10 and abs(self.ycor() - player.ycor()) < 50


class Obstacles(turtle.Turtle):
    def __init__(self, shape, pos):
        super().__init__(visible=False)
        self.shape(shape)
        self.speed(0)
        self.shape("square")
        # t.color(randint(0, 255), randint(0, 255), randint(0, 255))
        self.rgb = random.choice(['red', 'yellow', 'orange'])
        # self.rgb = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.color(self.rgb)
        self.shapesize(2)
        self.penup()
        self.setheading(270)
        self.setpos(random.choice(pos))
        self.showturtle()
        self.__move02 = 15
        self.__time02 = time.time()

    def move02(self):
        self.forward(self.__move02)
        if time.time() - self.__time02 > 1:
            self.__move02 += 5

    def collide02(self, player):
        return abs(self.xcor() - player.xcor()) < 10 and abs(self.ycor() - player.ycor()) < 50


class Map:
    def __init__(self):
        self.__screen = turtle.Screen()
        turtle.TurtleScreen._RUNNING = True
        self.__screen.setup(800, 800)
        self.__screen.bgcolor("grey")
        self.__point = []
        self.__obstacles = []
        self.__life = 3

        # lane 1
        road = turtle.Turtle(visible=False)
        road.shape("square")
        road.penup()
        road.goto(0, 50)
        road.shapesize(stretch_len=5, stretch_wid=1000)
        road.color('black')
        road.speed(0)
        road.showturtle()

        # lane 2
        road2 = turtle.Turtle(visible=False)
        road2.shape("square")
        road2.penup()
        road2.goto(200, 250)
        road2.shapesize(stretch_len=5, stretch_wid=1000)
        road2.color('black')
        road2.speed(0)
        road2.showturtle()

        # lane 3
        road3 = turtle.Turtle(visible=False)
        road3.shape("square")
        road3.penup()
        road3.goto(-200, -250)
        road3.shapesize(stretch_len=5, stretch_wid=1000)
        road3.color('black')
        road3.speed(0)
        road3.showturtle()

        self.player = Player()

        font = ('style', 20, 'bold')
        t = turtle.Turtle(visible=False)
        t.color('white')
        t.fillcolor('white')
        t.begin_fill()
        t.penup()
        t.setpos(270, 300)
        t.write(f'score : ', font=font, align='left')
        t.setpos(270, 250)
        t.write(f'life : ', font=font, align='left')

        print("please register If you don't already have an account.")
        log_regis = input('(L)ogin or (R)egister: ')
        while True:
            if log_regis == 'L' or log_regis == 'l':
                self.player.login_game()
                print('-- How to play ? --')
                print('Press "Left", "Right" or "A", "D" yo Move.')
                break
            elif log_regis == 'R' or log_regis == 'r':
                self.player.register()
                print('-- How to play ? --')
                print('Press "Left", "Right" or "A", "D" yo Move.')
                break
            else:
                log_regis = input('(L)ogin or (R)egister: ')

        self.player.shape("turtle")
        self.player.shapesize(2)
        self.player.color('white')
        self.player.penup()
        self.player.left(90)
        self.player.backward(300)

    def create_point(self):
        self.__point.append(Point("square", [(0, 450), (200, 450), (-200, 450), (100, 450), (-100, 450)]))

    def create_obstacles(self):
        self.__obstacles.append(Obstacles("square", [(0, 450), (200, 450), (-200, 450), (100, 450), (-100, 450)]))

    def start(self):
        self.__screen.listen()
        self.__screen.onkeypress(self.player.move_left, "Left")
        self.__screen.onkeypress(self.player.move_right, "Right")
        self.__screen.onkeypress(self.player.move_left, "a")
        self.__screen.onkeypress(self.player.move_right, "d")
        self.player.showturtle()
        start01 = time.time()
        t2 = turtle.Turtle(visible=False)
        t2.speed(0)
        font = ('style', 20, 'bold')

        while True:
            if time.time() - start01 >= 1:
                creative = random.randint(0, 100)
                if creative <= 50:
                    self.create_point()
                elif creative <= 90:
                    self.create_obstacles()
                start01 = time.time()

            for obs in range(len(self.__point)):
                if isinstance(self.__point[obs], Point):
                    self.__point[obs].move()
                    if self.__point[obs].collide(self.player):
                        self.player.color(self.__point[obs].rgb)
                        self.__point[obs].hideturtle()
                        self.__point[obs] = None
                        self.player.score += 1
                        t2.clear()
                        t2.color('white')
                        t2.fillcolor('white')
                        t2.begin_fill()
                        t2.penup()
                        t2.setpos(370, 300)
                        t2.write(self.player.score, font=font, align='left')
                        t2.setpos(350, 250)
                        t2.write(self.__life, font=font, align='left')

            for obs in range(len(self.__obstacles)):
                if isinstance(self.__obstacles[obs], Obstacles):
                    self.__obstacles[obs].move02()
                    if self.__obstacles[obs].collide02(self.player):
                        self.player.color(self.__obstacles[obs].rgb)
                        self.__obstacles[obs].hideturtle()
                        self.__obstacles[obs] = None
                        self.__life -= 1
                        t2.clear()
                        t2.color('white')
                        t2.fillcolor('white')
                        t2.begin_fill()
                        t2.penup()
                        t2.setpos(370, 300)
                        t2.write(self.player.score, font=font, align='left')
                        t2.setpos(350, 250)
                        t2.write(self.__life, font=font, align='left')
                        if self.__life == 0:
                            print('Game over')
                            self.score()
                            lst = []
                            try:
                                with open("players.json", "r") as data_file:
                                    data = json.load(data_file)
                                    for i in data:
                                        lst.append(i)

                            except FileNotFoundError:
                                with open("players.json", "w") as data_file:
                                    json.dump(self.player.score, data_file, indent=4)

                            leaderboard = '|----------Leaderboard-----------|'
                            type_score = '|  Rank  |  name  |  High score  |'
                            print(f'{leaderboard:^30}')
                            print(f'{type_score}')
                            for i in range(len(lst)):
                                print(f'| {i+1:^6} | {lst[i]:^6} | {data[lst[i]]["high score"]:^12} |')

                            question = input('Do you want to play again ? [Y/N] : ').lower()
                            if question == 'y':
                                print("let's go!!!")
                                self.player.score = 0
                                self.__life = 3
                                t2.clear()
                                game.start()
                            elif question == 'n':
                                turtle.bye()
                            else:
                                print('invalid answer')

            self.__screen.update()

    def score(self):
        try:
            with open("players.json", "r") as data_file:
                data = json.load(data_file)
            if data[self.player.user]["high score"] < self.player.score:
                data[self.player.user]["high score"] = self.player.score
                with open("players.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)

        except FileNotFoundError:
            with open("players.json", "w") as data_file:
                json.dump(self.player.score, data_file, indent=4)


game = Map()
ready = input('Are you ready? [Y/N]: ').lower()
while True:
    if ready == 'y':
        print("Let's go!!!")
        game.start()
        break
    else:
        print("-----")
        ready = input('Are you ready? [Y/N]: ').lower()
