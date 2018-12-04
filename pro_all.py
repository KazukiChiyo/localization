import numpy as np
from model import Anchor, Localizer
from server import pair_bt, rssi_query_one, rssi_query_all
import time

rssi_0 = [472.53/1024, 472.53/1024, 472.53/1024, 1.33, 1.20]
rssi = [356.55/1024, 367.955/1024, 362.03/1024, 0.5, 0.5]
tx_x = [2.7, 0, 2.7, 9, 4]
tx_y = [0.8, 1.5, 3.6, 3.5, 3]

# anchors = []
# for i in range(5):
#     anchors.append(Anchor(id=i, coords=(tx_x[i], tx_y[i]), rssi_0 = rssi_0[i]))
#
# for i, anchor in enumerate(anchors):
#     anchor.update(rssi[i])
#
# model = Localizer()
# start_time = time.time()
# pred = model.transform(anchors[:3])
# print("--- %s seconds ---" % (time.time() - start_time))
# print(pred)

f = pair_bt()
while True:
    print(rssi_query_all(f))
    # time.sleep(0.5)
