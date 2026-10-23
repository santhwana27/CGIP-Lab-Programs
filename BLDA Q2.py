
import matplotlib.pyplot as plt

def bresenham_line(x1, y1, x2, y2):
    points = []

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1

    x, y = x1, y1

    if dx > dy:
        p = 2 * dy - dx

        for i in range(dx + 1):
            points.append((x, y))

            if p >= 0:
                y += sy
                p -= 2 * dx

            x += sx
            p += 2 * dy

    else:
        p = 2 * dx - dy

        for i in range(dy + 1):
            points.append((x, y))

            if p >= 0:
                x += sx
                p -= 2 * dy

            y += sy
            p += 2 * dx

    return points

# Input
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

# Generate points
points = bresenham_line(x1, y1, x2, y2)

print("Bresenham Pixel Coordinates:")
print(points)

# Plot
x_points = [p[0] for p in points]
y_points = [p[1] for p in points]

plt.plot(x_points, y_points, 'o-')
plt.title("Bresenham's Line Drawing Algorithm")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()
