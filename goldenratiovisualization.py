import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# ---------------- Figure ----------------
fig, ax = plt.subplots()
fig.patch.set_facecolor("black")
ax.set_facecolor("black")
ax.axis("off")
ax.set_aspect("equal")

# ---------------- Spiral ----------------
theta = np.linspace(0, 10 * np.pi, 1500)

a = 0.2
b = 0.2

r = a * np.exp(b * theta)

x = r * np.cos(theta)
y = r * np.sin(theta)

# rainbow colors
colors = plt.cm.hsv(np.linspace(0, 1, len(theta)))

# pre-create line segments 
lines = []

def update(i):
    if i >= len(theta) - 1:
        return lines

    # draw only one new segment per frame 
    line, = ax.plot(
        x[i:i+2],
        y[i:i+2],
        color=colors[i],
        linewidth=2
    )

    lines.append(line)

    return lines

ani = animation.FuncAnimation(
    fig,
    update,
    frames=len(theta),
    interval=20,
    blit=False,
    repeat=True
)

plt.show()