import numpy as np
from server import pair_bt, rssi_query_one
import matplotlib.pyplot as plt
from tqdm import tqdm

n_samples = 200
id = 2

rssi = np.zeros(n_samples)
f = pair_bt()
for i in tqdm(range(n_samples)):
    rssi[i] = rssi_query_one(f, 3)

print("Average RSSI is", np.mean(rssi))
plt.hist(rssi, 20)
plt.xlabel('RSSI')
plt.ylabel('Counts')
plt.title('Distribution of RSSI for TX ' + str(id))
plt.show()
