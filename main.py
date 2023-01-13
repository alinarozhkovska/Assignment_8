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

paddle = Paddle(WIDTH/2 - size_paddle[0]/2, HEIGHT - size_paddle[1] - 5, size_paddle[0], size_paddle[1], "black")


def draw():
    screen.fill((198,168,105))
    screen.draw.filled_rect(paddle.get_rect(), paddle.color)


def update(dt):
    pass

def on_mouse_move(pos):#(567, 210)
    if pos[0] + paddle.width / 2 <= WIDTH and pos[0] - paddle.width / 2 >= 0:

        paddle.x = pos[0] - paddle.width / 2


pgzrun.go()
