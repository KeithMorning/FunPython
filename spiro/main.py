
import turtle
from PIL import Image
from datetime import datetime
import argparse
import SpiroAnimator
import Spiro

def saveDrawing():
    turtle.hideturtle()
    dateStr = datetime.now().strftime('%d%b%Y-%H%M%S')

    filename = 'spiro-'+ dateStr
    print('save drawing to %s.eps/png' % filename)
    canvas = turtle.getcanvas()
    canvas.postscript(file=filename + '.eps')
    img = Image.open(filename + '.eps')
    img.save(filename + '.png', 'png')
    turtle.showturtle()


def main():
    print('generating spirograph...')

    descStr = """

    This program draws spirographs using the Turtle module.

    """
    paraser = argparse.ArgumentParser(description=descStr)
    paraser.add_argument('--sparams',nargs=3,dest='sparams',required=False,help='the three arguments in sparams: R,r,l')
    args = paraser.parse_args()

    turtle.setup(width = 0.8)
    turtle.shape('turtle')

    turtle.title('Spirographs!')
    turtle.onkey(saveDrawing,'s')
    turtle.listen()

    turtle.hideturtle()
    if args.sparams:
        params = [float(x) for x in args.sparams]

        col = (0.0,0.0,0.0)
        spiro = Spiro(0,0,col,*params)

        spiro.draw()
    else:
        spiroAim = SpiroAnimator.SpiroAnimator(1)
        turtle.onkey(spiroAim.toggleTurtles,'t')
        turtle.onkey(spiroAim.restart,'space')

    turtle.mainloop()


if __name__ == '__main__':
    main()