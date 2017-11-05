import turtle
import math
import fractions


class Spiro:
    def __init__(self, xc, yc, col, R, r, l):
        self.t = turtle.Turtle()
        self.t.shape('turtle')
        self.step = 5
        self.drawcompelete = False
        self.setparams(xc, yc, col, R, r, l)

        self.restart()

    def setparams(self, xc, yc, col, R, r, l):
        self.xc = xc
        self.yc = yc
        self.R = int(R)
        self.r = int(r)
        self.l = l
        self.col = col

        gcdVal = math.gcd(self.r, self.R)
        self.nRot = self.r // gcdVal
        self.k = r / float(R)
        self.t.color(*col)
        self.a = 0

    def restart(self):
        self.drawcompelete = False
        self.t.showturtle()
        self.t.up()

        R, k, l = self.R, self.k, self.l
        a = 0.0

        x = R * ((1 - k) * math.cos(a) + l * k * math.cos((1 - k) * a / k))
        y = R * ((1 - k) * math.sin(a) - l * k * math.sin((1 - k) * a / k))
        self.t.setpos(self.xc + x, self.yc + y)
        self.t.down()

    def draw(self):
        R, k, l = self.R, self.k, self.l

        for i in range(0, 360 * self.nRot + 1, self.step):
            a = math.radians(i)

            x = R * ((1 - k) * math.cos(a) + l * k * math.cos((1 - k) * a / k))
            y = R * ((1 - k) * math.sin(a) - l * k * math.sin((1 - k) * a / k))
            self.t.setpos(self.xc + x, self.yc + y)

        self.t.hideturtle()

    def update(self):

        if self.drawcompelete:
            return

        self.a += self.step
        R, k, l = self.R, self.k, self.l
        a = math.radians(self.a)
        x = R * ((1 - k) * math.cos(a) + l * k * math.cos((1 - k) * a / k))
        y = R * ((1 - k) * math.sin(a) - l * k * math.sin((1 - k) * a / k))
        lastx,lasty = self.t.pos()
        print('the angele is %f' % ((lasty - y - self.yc)/(lastx -x - self.xc)))
        dgree = math.degrees((lasty-y-self.yc)/(lastx-x-self.xc))
        self.t.setheading(dgree)
        self.t.setpos(self.xc + x, self.yc + y)

        if self.a >= 360 * self.nRot:
            self.drawcompelete = True
            self.t.hideturtle()

    def clear(self):
        self.t.clear()
