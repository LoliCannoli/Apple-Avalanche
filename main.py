import turtle

apple_image = 'apple.gif'
background_image = 'background.gif'

font = ('Courier New', 40, 'bold')

wn = turtle.Screen()
wn.setup(width = 1.0, height = 1.0)
wn.bgpic("background.gif")
wn.addshape(apple_image)
wn.tracer(False)

current_letter = 'A'
class Apple:
    def __init__(self, position, letter):
        apple = turtle.Turtle()

        self.pos = position
        self.letter = letter
        self.apple = apple

        apple.shape(apple_image)
        apple.penup()
        apple.pencolor('white')

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

current_letter = Apple((0,100), 'A')
wn.onkeypress(lambda: current_letter.fall(), 'a')

wn.listen()

wn.mainloop()
