
import turtle
import Spiro
import random

class SpiroAnimator:

    def __init__(self,N):
        self.deltaT = 10
        self.width = turtle.window_width()
        self.height = turtle.window_height()

        self.spiros = []

        for i in range(N):
            rparams = self.genRandomParams()

            spiro = Spiro.Spiro(*rparams)
            self.spiros.append(spiro)
        self.update()



    def genRandomParams(self):

        width,height = self.width,self.height
        R = random.randint(50,min(width,height)//2)
        r = random.randint(10,9*R//10)
        l = random.uniform(0.1,0.9)

        xc = random.randint(-width//2+R,width//2-R)
        yc = random.randint(-height//2+R,height//2-R)

        col = (random.random(),random.random(),random.random())
        return (xc,yc,col,R,r,l)

    def restart(self):
        for spiro in self.spiros:
            spiro.clear()
            rparams = self.genRandomParams()
            spiro.setparams(*rparams)
            spiro.restart()


    def update(self):
        ncomplete = 0
        for spiro in self.spiros:
            spiro.update()
            if spiro.drawcompelete:
                ncomplete +=1

        if ncomplete == len(self.spiros):
            self.restart()

        turtle.ontimer(self.update,self.deltaT)



    def toggleTurtles(self):
        for spiro in self.spiros:
            if spiro.t.isvisible():
                spiro.t.hideturtle()
            else:
                spiro.t.showturtle()



