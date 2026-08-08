from boilerplate import format
import matplotlib.pyplot as plt
from testcases import get_cases

fig, ax = format()

cases = get_cases()

def draw_lines(case):
    for line in case:
        xs = [line[0][0], line[1][0]]
        ys = [line[0][1], line[1][1]]
        ax.plot(xs, ys)

def visualize(case):
    for line in case:
        xs, ys = [0, line[0][0], line[1][0]], [0, line[0][1],line[1][1]]
        ax.fill(xs, ys, alpha=0.3)

def visualize_two_sides(case):
    for line in case:
        xs = [0, line[0][0], line[1][0], 0, -line[0][0], -line[1][0]]
        ys = [0, line[0][1],line[1][1], 0, -line[0][1], -line[1][1]]
        ax.fill(xs, ys, alpha=0.3)

draw_lines(cases[0])
# visualize_two_sides(cases[1])
plt.show()