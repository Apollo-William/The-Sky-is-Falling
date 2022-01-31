import turtle
import random
from time import time, sleep

# Register shapes in mass
names = [
  'NinjaFL1', 'NinjaFL2', 'NinjaFR1', 'NinjaFR2', 'Apple', 'Bomb', 'FN Dojo'
]

# sprites
frameList = []
leftFrame = 'NinjaFL1.gif'
rightFrame = 'NinjaFR1.gif'

for name in names:
    file = name + ".gif"
    if name[0:5] == "Ninja":
      frameList.append(file)
    turtle.register_shape(file)

# Set up the screen
wn = turtle.Screen()
wn.title('Falling Skies')
wn.bgcolor('black')
wn.bgpic('FN Dojo.gif')
wn.setup(width=800, height=600)
wn.tracer(0)

# Mainloop speed
fps = 60

# Score
score = 0

# Health
lives = 3

# Player
player = turtle.Turtle()
player.speed(0)
player.shape('NinjaFR1.gif')
player.color('white')
player.penup()
player.goto(0, -250)
player.direction = 'stop'

# Good things
good_shape = []
good_things = []

for _ in range(20):
    good_thing = turtle.Turtle()
    good_thing.speed(0)
    good_thing.shape('Apple.gif')
    good_thing.color('green')
    good_thing.penup()
    good_thing.goto(-100, 250)
    good_thing.speed = random.randint(2, 5)

    good_things.append(good_thing)

# BOMBS
bad_things = []

for _ in range(20):
    bad_thing = turtle.Turtle()
    bad_thing.speed(0)
    bad_thing.shape('Bomb.gif')
    bad_thing.color('red')
    bad_thing.penup()
    player.xcor
    bad_thing.goto(100, 250)
    bad_thing.speed = random.randint(2, 5)

    bad_things.append(bad_thing)

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape('square')
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write('Score: 0  Lives: 3', align='center', font=('Courier', 24, 'normal'))


# Functions
def go_left():
    player.direction = 'left'
    player.shape(leftFrame)


def go_right():
    player.direction = 'right'
    player.shape(rightFrame)

# Keyboard bindings
wn.listen()

# Arrow keys
wn.onkeypress(go_left, 'Left')
wn.onkeypress(go_right, 'Right')

# WASD keys
wn.onkeypress(go_left, 'a')
wn.onkeypress(go_right, 'd')

# Main game loop
while True:

    # Limit actions done per second
    now = time()
    frameperiod = 1.0 / fps
    nextframe = now + frameperiod

    for frame in range(fps):

        while now < nextframe:
            sleep(nextframe - now)
            now = time()

        nextframe += frameperiod
        wn.update()

        if frame == 15 or 30 or 45 or 60:
          leftFrame = frameList[1]
          rightFrame = frameList[3]
        else:
          leftFrame = frameList[0]
          rightFrame = frameList[2]

        if player.direction == 'left':
            player.setx(player.xcor() - 3)

        if player.direction == 'right':
            player.setx(player.xcor() + 3)

        # Check for border collisions
        if player.xcor() < -390:
            player.setx(-390)

        elif player.xcor() > 390:
            player.setx(390)

        for good_thing in good_things:
            # Move the good things
            good_thing.sety(good_thing.ycor() - good_thing.speed)

            # Check if good things are off the screen
            if good_thing.ycor() < -300:
                good_thing.goto(random.randint(-300, 300),
                                random.randint(400, 800))

            # Check for collisions
            if player.distance(good_thing) < 40:
                # Score increases
                score += 10

                # Show the score
                pen.clear()
                pen.write('Score: {}  Lives: {}'.format(score, lives),
                          align='center',
                          font=('Courier', 24, 'normal'))

                # Move the good thing back to the top
                good_thing.goto(random.randint(-300, 300),
                                random.randint(400, 800))

        for bad_thing in bad_things:
            # Move the bad things
            bad_thing.sety(bad_thing.ycor() - bad_thing.speed)

            if bad_thing.ycor() < -300:
                bad_thing.goto(player.xcor(),
                               random.randint(400, 800))

            if player.distance(bad_thing) < 40:
                # Score increases
                score -= 10
                lives -= 1

                # Show the score
                pen.clear()
                pen.write('Score: {}  Lives: {}'.format(score, lives),
                          align='center',
                          font=('Courier', 24, 'normal'))

                # Move the bad things back to the top
                for bad_thing in bad_things:
                    bad_thing.goto(random.randint(-300, 300),
                                   random.randint(400, 800))

        # Check for game over
        if lives == 0:
            pen.clear()
            pen.write('Game Over! Score: {}'.format(score),
                      align='center',
                      font=('Courier', 24, 'normal'))
            wn.update()
            score = 0
            lives = 3
            pen.clear()
            pen.write('Score: {}  Lives: {}'.format(score, lives),
                      align='center',
                      font=('Courier', 24, 'normal'))

wn.mainloop()
