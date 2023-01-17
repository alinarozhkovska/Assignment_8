import pgzrun, random
import time
from pgzero.actor import Actor
from pgzero.rect import Rect

WIDTH = 560
HEIGHT = 400
TITLE = "Різдвяний арканоїд"

size_paddle = (WIDTH / 3, HEIGHT / 20)
count_of_lives = 3


class Paddle:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y

        self.width = width
        self.height = height

        self.color = color

    def get_rect(self):
        return Rect((self.x, self.y), (self.width, self.height))


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

        if self.y + self.radius >= paddle.y and (
                self.x + self.radius / 2 >= paddle.x and self.x + self.radius / 2 <= paddle.x + paddle.width):
            self.y_direction = -3

        if len(hearts_list) != 0 and len(obstacle_list) != 0:
            self.x += self.x_direction
            self.y += self.y_direction
        else:
            self.x = -10
            self.y = -10

    def touchElement(self):
        for obstacle in obstacle_list:

            if self.y - self.radius + 6 <= obstacle.y + obstacle.height\
                and self.x - self.radius + 6 <= obstacle.x + obstacle.width\
                and self.y + self.radius + 6 >= obstacle.y\
                and self.x + self.radius + 6 >= obstacle.x:

                if self.y_direction > 0:
                    self.y_direction = -3
                    self.y -= 3
                else:
                    self.y_direction = 3
                    self.y += 3

                if self.x - self.radius <= obstacle.x + obstacle.width\
                and self.x + self.radius >= obstacle.x - obstacle.width:

                    if self.x_direction > 0:
                        self.x_direction = -3
                        self.x -= 3
                    else:
                        self.x_direction = 3
                        self.x += 3

                if obstacle.health <= 1:
                    obstacle_list.remove(obstacle)

                elif obstacle.health == 2:
                    obstacle.health -= 1
                    obstacle.color = "blue"

                elif obstacle.health == 3:
                    obstacle.health -= 1
                    obstacle.color = "black"


class Obstacle:
    def __init__(self, x, y, width, height, color, health):
        self.x = x
        self.y = y

        self.health = health

        self.radius = 15

        self.width = width
        self.height = height

        self.color = color


paddle = Paddle(WIDTH / 2 - size_paddle[0] / 2, HEIGHT - size_paddle[1] - 5, size_paddle[0], size_paddle[1], "black")
ball = Ball(paddle.x + paddle.width / 2, paddle.y - 15, 12, "red")
hearts_list = []
x_pos_heart = 15
if len(hearts_list) == 0:
    for i in range(count_of_lives):
        heart = Actor('heart')
        heart.pos = x_pos_heart, 15
        x_pos_heart += 25
        hearts_list.append(heart)
obstacle_list = []
x_pos_obstacle = 15
y_pos_obstacle = 50
obstacle_hard = ["blue", "black", "orange"]
for i in range(18):
    obstacle_health = random.randint(1,3)
    obstacle = Obstacle(x_pos_obstacle, y_pos_obstacle, 50, 25, obstacle_hard[obstacle_health-1],  obstacle_health)
    x_pos_obstacle += 60
    if i == 8:
        y_pos_obstacle += 30
        x_pos_obstacle = 15
    obstacle_list.append(obstacle)
extra_lives = []

extra_size = Actor("big_bonus", (random.randint(50, 550), random.randint(-300, -50)))

timer = time.time()
def draw():
    screen.fill((198, 168, 105))
    screen.draw.filled_rect(paddle.get_rect(), paddle.color)
    screen.draw.filled_circle((ball.x, ball.y), ball.radius, ball.color)
    extra_size.draw()
    for heart in hearts_list:
        heart.draw()
    if len(hearts_list) == 0:
        screen.draw.text("GAME OVER", (80, HEIGHT / 2 - 48), fontsize=96, color="red")
    if len(obstacle_list) == 0:
        screen.draw.text("YOU WON!", (100, HEIGHT / 2 - 48), fontsize=96, color="red")

    for obstacle in obstacle_list:
        screen.draw.filled_rect(Rect((obstacle.x, obstacle.y), (obstacle.width, obstacle.height)), obstacle.color)
    for extra_live in extra_lives:
        extra_live.draw()


def update(dt):
    global timer
    ball.move()
    ball.touchElement()
    global count_of_lives, x_pos_heart
    if ball.y > HEIGHT:
        hearts_list.pop()
        ball.y = paddle.y - ball.radius
        ball.x = paddle.x + paddle.width / 2
    for obstacle in obstacle_list:
        if obstacle.y - ball.radius - 6 <= ball.y <= obstacle.y + ball.radius and obstacle.x - ball.radius - 6 <= ball.x <= obstacle.x + ball.radius:
            obstacle_list.remove(obstacle)
    if random.random() < 0.0005:
        y_pos_extra_live = 15
        x_pos_extra_live = random.randint(30, WIDTH - 30)
        extra_lives.append(Actor("heart", pos=(x_pos_extra_live, y_pos_extra_live)))

    for extra_live in extra_lives:
        extra_live.y += 2
        if extra_live.y == paddle.y and paddle.x < extra_live.x < paddle.x + paddle.width:
            x_pos_heart = len(hearts_list) * 25 + 15
            hearts_list.append(Actor("heart", pos=(x_pos_heart, 15)))
            extra_lives.remove(extra_live)

    if time.time() > timer + 15:
        extra_size.y += 2

    if extra_size.y >= HEIGHT:
        extra_size.y = random.randint(-400, -50)
        extra_size.x = random.randint(50, 550)

    if extra_size.y >= paddle.y and extra_size.x + extra_size.width / 2 >= paddle.x and extra_size.x - extra_size.width / 2 <= paddle.x + paddle.width:
        paddle.width *= 1.5

        timer = time.time()

        extra_size.y = random.randint(-400, -50)
        extra_size.x = random.randint(50, 550)

    if paddle.width > size_paddle[0] and time.time() > timer + 7:
        paddle.width = size_paddle[0]


def on_mouse_move(pos):
    if pos[0] + paddle.width / 2 <= WIDTH and pos[0] - paddle.width / 2 >= 0 and len(hearts_list) != 0 and len(
            obstacle_list) != 0:
        paddle.x = pos[0] - paddle.width / 2


pgzrun.go()
