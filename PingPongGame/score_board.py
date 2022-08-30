from turtle import Turtle


class ScoreBoard(Turtle):

    art = '''
      _____ _               _____                  
     |  __ (_)             |  __ \                 
     | |__) | _ __   __ _  | |__) |__  _ __   __ _ 
     |  ___/ | '_ \ / _` | |  ___/ _ \| '_ \ / _` |
     | |   | | | | | (_| | | |  | (_) | | | | (_| |
     |_|   |_|_| |_|\__, | |_|   \___/|_| |_|\__, |
                     __/ |                    __/ |
                    |___/                    |___/ 
    '''

    def __init__(self):
        super().__init__()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.penup()
        self.hideturtle()
        self.write_score()

    def write_score(self):
        self.goto(-40, 160)
        self.write(self.l_score, align="center", font=("Courier", 20, "normal"))
        self.goto(40, 160)
        self.write(self.r_score, align="center", font=("Courier", 20, "normal"))
        self.goto(0, 160)
        self.write(arg="-", align="center", font=("Courier", 20, "normal"))
        self.goto(-10, 200)
        self.write(arg=self.art, align="center", font=("Courier", 7, "normal"))

    def update_score(self, player):
        if player == 1:
            self.l_score += 1
        else:
            self.r_score += 1
        self.refresh_score()

    def refresh_score(self):
        self.clear()
        self.write_score()


