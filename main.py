import pgzrun

WIDTH = 600
HEIGHT = 400
TITLE = "Різдвяний арканоїд"

size_paddle = (WIDTH/3, HEIGHT/20)

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

        self.x += self.x_direction
        self.y += self.y_direction


paddle = Paddle(WIDTH/2 - size_paddle[0]/2, HEIGHT - size_paddle[1] - 5, size_paddle[0], size_paddle[1], "black")
ball = Ball(paddle.x + paddle.width / 2, paddle.y - 15, 12, "red")

def draw():
    screen.fill((198,168,105))
    screen.draw.filled_rect(paddle.get_rect(), paddle.color)
    screen.draw.filled_circle((ball.x, ball.y), ball.radius, ball.color)

def update(dt):
    ball.move()

def on_mouse_move(pos):#(567, 210)
    if pos[0] + paddle.width / 2 <= WIDTH and pos[0] - paddle.width / 2 >= 0:

        paddle.x = pos[0] - paddle.width / 2


pgzrun.go()
