import random
import numpy as np
from matplotlib import pyplot as plt

number_of_time_steps = 500
spawn_rate = 1
death_rate = 0.01
replicate_rate = 0.005

blobs = np.array([200])
blobs_change = np.array([0])

total = 0
for i in range(number_of_time_steps-1):
    blob = blobs[-1]
    blob_change = 0
    for i in range(blobs[-1]):
        death = random.random()
        if death <= death_rate:
            blob = blob-1
            blob_change = blob_change-1
    spawn = random.random()
    for i in range(blobs[-1]):
        replicate = random.random()
        if replicate <= replicate_rate:
            blob = blob+1
            blob_change = blob_change+1
    if spawn <= spawn_rate:
        blob = blob+1
        blob_change = blob_change=1
    blobs = np.append(blobs, [blob])
    blobs_change = np.append(blobs_change, [blob_change])
    total = total+blob



average = total/(number_of_time_steps-1)
print(average)

x = np.linspace(1, number_of_time_steps, number_of_time_steps)

plt.plot(x, blobs)
plt.show()

