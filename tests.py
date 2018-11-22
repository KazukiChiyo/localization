import numpy as np
from base import Anchor, Localizer
import time

rssi_0 = [1.35, 1.44, 1.50, 1.33, 1.20]
rssi = [0.5, 0.5, 0.5, 0.5, 0.5]
tx_x = [1, 1.5, 8, 9, 4]
tx_y = [1, 6, 6, 3.5, 3]

anchors = []
for i in range(5):
    anchors.append(Anchor(id=i, coords=(tx_x[i], tx_y[i]), rssi_0 = rssi_0[i]))

for i, anchor in enumerate(anchors):
    anchor.update(rssi[i])

model = Localizer()
start_time = time.time()
pred = model.transform(anchors[:3])
print("--- %s seconds ---" % (time.time() - start_time))
print(pred)
