
import matplotlib.pyplot as plt

def dda_line(x1, y1, x2, y2):
    x, y = x1, y1

    dx = x2 - x1
    dy = y2 - y1

    steps = int(max(abs(dx), abs(dy)))

    xinc = dx / steps
    yinc = dy / steps

    x_points = []
    y_points = []

    for i in range(steps + 1):
        x_points.append(round(x))
        y_points.append(round(y))

        x += xinc
        y += yinc

    plt.plot(x_points, y_points,'o-')
    plt.title("DDA Line Drawing Algorithm")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid(True)
    plt.show()
    


dda_line(3, 3, 12, 9)
