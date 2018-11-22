# Author: Kexuan Zou
# Date: Nov 10, 2018

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

tx_sprite = 's'
rx_sprite = 'o'
tx_x = [1, 1.5, 8, 9, 4]
tx_y = [1, 6, 6, 3.5, 3]
tx_text = ['TX0', 'TX1', 'TX2', 'TX3', 'TX4']

fig, ax = plt.subplots()
ax.scatter(tx_y, tx_x, s=50, c='r', marker=tx_sprite)
drawable, = ax.plot(0, 0, marker=rx_sprite, linestyle='None', markersize=12)
textbox = ax.text(0, -1, '', bbox=dict(boxstyle="round", ec=(1., 0.5, 0.5), fc=(1., 0.8, 0.8),))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

def update(data):
    drawable.set_data(data[0], data[1])
    textbox.set_text(data)
    return drawable, textbox,

def data_gen():
    while True:
        yield np.random.uniform(0, 10, 2)

ani = animation.FuncAnimation(fig, update, data_gen, interval=200)
for i, txt in enumerate(tx_text):
    ax.annotate(txt, (tx_y[i], tx_x[i]))

plt.grid(True)
plt.title("Indoor positioning real-time result")
plt.show()
