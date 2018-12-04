# Author: Kexuan Zou
# Date: Dec 2, 2018

import numpy as np
import matplotlib.pyplot as plt
from model import Anchor, Localizer
from server import pair_bt, rssi_query_one, rssi_query_all
import time

rssi_0 = [439.43/1024, 439.43/1024, 439.43/1024, 1.33, 1.20]
rssi = [364.415/1024, 366.29/1024, 368.055/1024, 0.5, 0.5]
tx_x = [2.7, 0, 2.7, 5.5, 4]
tx_y = [0.8, 1.5, 3.6, 3.5, 3]
tx_sprite = 's'
rx_sprite = 'o'
tx_text = ['TX0', 'TX1', 'TX2', 'TX3', 'TX4']

anchors = []
for i in range(5):
    anchors.append(Anchor(id=i, coords=(tx_x[i], tx_y[i]), rssi_0 = rssi_0[i]))

for i, anchor in enumerate(anchors):
    anchor.update(rssi[i])

model = Localizer()
start_time = time.time()
pred = model.transform(anchors[:3])
print("--- %s seconds ---" % (time.time() - start_time))
print("Predicted coordinates for RX is", pred)

fig, ax = plt.subplots()
ax.scatter(tx_y, tx_x, s=50, c='r', marker=tx_sprite)
drawable, = ax.plot(0, 0, marker=rx_sprite, linestyle='None', markersize=12)
textbox = ax.text(0, -0.7, '', bbox=dict(boxstyle="round", ec=(1., 0.5, 0.5), fc=(1., 0.8, 0.8),))
ax.set_xlim(0, 6)
ax.set_ylim(0, 6)
drawable.set_data(pred[0], pred[1])
textbox.set_text(pred)
for i, txt in enumerate(tx_text):
    ax.annotate(txt, (tx_y[i], tx_x[i]))
plt.grid(True)
plt.title("Indoor positioning real-time result")
plt.show()
