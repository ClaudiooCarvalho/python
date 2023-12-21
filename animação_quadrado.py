import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()

ax.set_xlim(0, 10)
ax.set_ylim(0, 10)


ax.set_xticks(range(11))
ax.set_yticks(range(11))
ax.grid(which='both', color='#fff', linestyle='--', linewidth=0.5)
ax.set_facecolor('#cf0c0c')

a = 5.0
b = 1.0
c = 0.0
d = 1.0

velocidade1 = 400.0

a1 = 1.0
b1 = 0.1
c1 = 1.0
d1 = 0.1

velocidade2 = 500.0

square1 = Rectangle((0, 0), 1, 1, color='#4685f2')
square2 = Rectangle((0, 0), 1, 1, color='#f2e146')
ax.add_patch(square1)
ax.add_patch(square2)

def init():
    return square1, square2


def update(frame):
    t = frame / (45 * 35)


    x = a * t * velocidade1 + b
    y = c * t * velocidade1 + d


    x1 = a1 * t * velocidade2 + b1
    y1 = c1 * t * velocidade2 + d1

    square1.set_xy((x, y))
    square2.set_xy((x1, y1))

    return square1, square2


ani = FuncAnimation(fig, update, frames=range(5 * 85), init_func=init, blit=True)


plt.show()


ani.save('animacao_reta_parametrizada_variacao_velocidade_2_quadrados.mp4', writer='ffmpeg')