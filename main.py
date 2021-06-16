import turtle
import string
import random

apple_image = 'apple.gif'
background_image = 'background.gif'

font = ('Courier New', 40, 'bold')

wn = turtle.Screen()
wn.setup(width = 1.0, height = 1.0)
wn.bgpic("background.gif")
wn.addshape(apple_image)
wn.tracer(False)

class Apple:
    def init(self, position, letter):
        apple = turtle.Turtle()

        self.pos = position
        self.letter = letter
        self.apple = apple

        apple.shape(apple_image)
        apple.penup()
        apple.pencolor('white')

        wn.onkeypress(lambda: self.fall(), letter.lower())

        x, y = position
        apple.goto(((x-14), (y-37)))
        apple.write(letter, font = font)
        apple.goto(position)

        wn.update()

    def fall(self):
        wn.tracer(True)
        self.apple.clear()
        self.apple.goto((self.apple.xcor(), -125))
        self.apple.hideturtle()
        wn.tracer(False)

alphabet_string = list(string.ascii_lowercase)

for x in range(8):
    letter = random.choice(alphabet_string)
    alphabet_string.pop(alphabet_string.index(letter))
    x = random.randint(-100, 100)
    y = random.randint(0, 100)
    Apple((x,y), letter)

wn.listen()
wn.mainloop()
