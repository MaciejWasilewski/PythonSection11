import tkinter
import math


def parabola(par_x):
    return list(map(lambda x: (x ** 2) / 100, par_x))


def plot_circle(par_canvas, par_r, par_x, par_y, colour="red"):
    par_canvas.create_oval(par_x + par_r, par_y + par_r, par_x - par_r, par_y - par_r, outline=colour, width=2)


def circle(par_r, par_x, par_y, points=360):
    y = []
    x = []
    for angle in range(0, points):
        angle = angle * 360 / points
        print(angle)
        y.append(par_y + par_r * (math.sin(angle * (2 * math.pi) / 360)))
        x.append(par_x + par_r * (math.cos(angle * (2 * math.pi) / 360)))
    x.append(x[0])
    y.append(y[0])
    # y = list(map(lambda x: par_h + (math.sqrt(par_r ** 2 - ((x - par_g) ** 2))), list(range(par_g, par_g + par_r))))
    return x, y


def draw_axes(par_canvas):
    par_canvas.update()
    x_origin = par_canvas.winfo_width() / 2
    y_origin = par_canvas.winfo_height() / 2
    par_canvas.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    par_canvas.create_line(-x_origin, 0, x_origin, 0, fill="black")
    par_canvas.create_line(0, -y_origin, 0, y_origin, fill="black")


def draw_parabola(par_canvas):
    par_canvas.update()
    xes = range(-320, 320, 1)
    for i in range(len(xes) - 1):
        par_canvas.create_line(xes[i], *parabola(xes[i]), xes[i + 1],
                               parabola(xes[i + 1]), fill="black")


def plot(par_canvas, par_x, par_y):
    par_canvas.update()
    for i in range(len(par_x) - 1):
        par_canvas.create_line(par_x[i], -par_y[i], par_x[i + 1],
                               -par_y[i + 1], fill="black")


mainWindow = tkinter.Tk()
mainWindow.title("Parabola")
mainWindow.geometry("640x480")

canvas = tkinter.Canvas(mainWindow, width=640, height=480)
canvas.grid(row=0, column=0)

draw_axes(canvas)
X = list(range(-100, 100, 1))
X2 = list(range(-200, 200, 2))
plot(canvas, X, parabola(X))
print(X[0], X[-1])
print(len(X))
for i in range(3, 30, 1):
    x, y = circle(100, 200, 0, points=i)
    plot(canvas, x, y)
plot(canvas, X2, list(map(lambda x: x / 2, parabola(X2))))
plot_circle(canvas, 100, 100, 100, "blue")
mainWindow.mainloop()
