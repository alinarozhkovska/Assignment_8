import pgzrun
from pgzero.actor import Actor

WIDTH = 600
HEIGHT = 400
TITLE = "Різдвяний арканоїд"

size_paddle = (WIDTH/3, HEIGHT/20)
count_of_lives = 3

class Paddle:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y

        self.width = width
        self.height = height

        self.color = color
    def get_rect(self):
        return Rect((self.x, self.y),(self.width, self.height))

class Ball:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y

        self.radius = radius

        self.x_direction = 3
        self.y_direction = -3

        self.color = color

    def move(self):
        if self.x + self.radius / 2 >= WIDTH:
            self.x_direction = -3

        if self.y - self.radius / 2 <= 0:
            self.y_direction = 3

        if self.x - self.radius / 2 <= 0:
            self.x_direction = 3

        if self.y + self.radius >= paddle.y and (self.x + self.radius / 2 >= paddle.x and self.x + self.radius / 2 <= paddle.x + paddle.width):
            self.y_direction = -3

        if len(hearts_list) != 0:
            self.x += self.x_direction
            self.y += self.y_direction
        else:
            self.x = -10
            self.y = -10


paddle = Paddle(WIDTH/2 - size_paddle[0]/2, HEIGHT - size_paddle[1] - 5, size_paddle[0], size_paddle[1], "black")
ball = Ball(paddle.x + paddle.width / 2, paddle.y - 15, 12, "red")
hearts_list = []
x_pos_heart = 15
if len(hearts_list) == 0:
    for i in range(count_of_lives):
        heart = Actor('heart')
        heart.pos = x_pos_heart, 15
        x_pos_heart += 25
        hearts_list.append(heart)
def draw():
    screen.fill((198,168,105))
    screen.draw.filled_rect(paddle.get_rect(), paddle.color)
    screen.draw.filled_circle((ball.x, ball.y), ball.radius, ball.color)
    for heart in hearts_list:
        heart.draw()
    if len(hearts_list) == 0:
        screen.draw.text("GAME OVER", (80, HEIGHT / 2 - 48), fontsize=96, color="red")
def update(dt):
    ball.move()
    if ball.y > HEIGHT:
        hearts_list.pop()
        ball.y = paddle.y - ball.radius
        ball.x = paddle.x + paddle.width / 2
def on_mouse_move(pos):#(567, 210)
    if pos[0] + paddle.width / 2 <= WIDTH and pos[0] - paddle.width / 2 >= 0 and len(hearts_list) != 0:

        paddle.x = pos[0] - paddle.width / 2


pgzrun.go()
