import numpy as np
import matplotlib.pyplot as plt

points = np.array([[1, 2], [4, 4], [8, 1], [1, 2]])

def plot(points, title):
    plt.plot(points[:, 0], points[:, 1], 'ro-')
    plt.title(title)
    plt.axis('equal')
    plt.show()

def translate(points, tx, ty):  # translation
    return points + np.array([tx, ty])

def scale(points, sx, sy):  # scaling
    return points * np.array([sx, sy])

def rotate(points, angle_deg):  # rotation
    angle = np.radians(angle_deg)
    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle),  np.cos(angle)]
    ])
    return np.dot(points, rotation_matrix)

# Display original object
plot(points, "Original Object")

# Translation
tx = float(input("Enter translation in x: "))
ty = float(input("Enter translation in y: "))
plot(translate(points, tx, ty), "Translated Object")

# Scaling
sx = float(input("Enter scaling factor in x: "))
sy = float(input("Enter scaling factor in y: "))
plot(scale(points, sx, sy), "Scaled Object")

# Rotation
angle = float(input("Enter rotation angle: "))
plot(rotate(points, angle), "Rotated Object")
