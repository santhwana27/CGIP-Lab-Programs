
import matplotlib.pyplot as plt

def midpoint_circle(xc, yc, r):
    points = []
    x = 0
    y = r
    p = 1 - r

    while x <= y:
       
        points.extend([
            (xc + x, yc + y),
            (xc - x, yc + y),
            (xc + x, yc - y),
            (xc - x, yc - y),
            (xc + y, yc + x),
            (xc - y, yc + x),
            (xc + y, yc - x),
            (xc - y, yc - x)
        ])

        x += 1

        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * (x - y) + 1

    return points


xc = int(input("Enter center x: "))
yc = int(input("Enter center y: "))
r = int(input("Enter radius: "))


points = midpoint_circle(xc, yc, r)


print("Midpoint Circle Pixel Coordinates:")
print(points)


x_values = [p[0] for p in points]
y_values = [p[1] for p in points]

plt.figure(figsize=(7, 7))
plt.scatter(
    x_values,
    y_values,
    color="purple",
    s=100
)

plt.title("Midpoint Circle Drawing Algorithm")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.grid(True)
plt.axis("equal")
plt.show()
