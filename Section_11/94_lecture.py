import tkinter


def parabola(par_x):
    return list(map(lambda x: x ** 2, par_x))


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
    # ratio = parCanvas.winfo_width() / 100
    ratio = 1
    ratio2 = 100 / par_canvas.winfo_height()
    print(ratio)
    for i in range(len(xes) - 1):
        par_canvas.create_line(xes[i] * ratio, ratio2 * parabola(xes[i] * ratio), xes[i + 1] * ratio,
                               ratio2 * parabola(xes[i + 1] * ratio), fill="black")


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
print(X)
Y = parabola(X)
print(Y)
plot(canvas, X, Y)

mainWindow.mainloop()
