import numpy as np
from server import pair_bt, rssi_query_one
import matplotlib.pyplot as plt
from tqdm import tqdm
from scipy.stats import norm

n_samples = 200
id = 2

rssi = np.zeros(n_samples)
f = pair_bt()
for i in tqdm(range(n_samples)):
    rssi[i] = rssi_query_one(f, 3)

print("Average RSSI is", np.mean(rssi))
mu, std = norm.fit(rssi)
print("Fitted RSSI into Gaussian distribution N({}, {})".format(mu, std**2))
plt.hist(rssi, 20, normed=True)
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mu, std)
plt.plot(x, p, 'k', linewidth=2)
plt.xlabel('RSSI')
plt.ylabel('Counts')
plt.title('Distribution of RSSI for TX ' + str(id))
plt.show()
