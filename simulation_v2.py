import random
import numpy as np
from matplotlib import pyplot as plt

number_of_time_steps = 500

blobs = np.array([50])
blobs_change = np.array([0])

total = 0
for i in range(number_of_time_steps-1):
    #variables
    spawn_rate = 0
    death_rate = 0.05
    replicate_rate = 0.1
    crowding_number = 0.001

    blob = blobs[-1]
    blob_change = 0
    #crowding
    crowding_effect = crowding_number*blob
    death_rate = death_rate+crowding_effect
    #death chance
    for i in range(blobs[-1]):
        death = random.random()
        if death <= death_rate:
            blob = blob-1
            blob_change = blob_change-1

    #replicate chance
    for i in range(blobs[-1]):
        replicate = random.random()
        if replicate <= replicate_rate:
            blob = blob+1
            blob_change = blob_change+1

    #spawn chance
    spawn = random.random()
    if spawn <= spawn_rate:
        blob = blob+1
        blob_change = blob_change+1

    blobs = np.append(blobs, [blob])
    blobs_change = np.append(blobs_change, [blob_change])
    total = total+blob


average = total/(number_of_time_steps-1)
print(average)

x = np.linspace(1, number_of_time_steps, number_of_time_steps)

fig, axs = plt.subplots(2)
fig.suptitle('Simulating Population')
axs[0].plot(x, blobs, color="#5a7b9a")
axs[1].plot(x, blobs_change)


plt.show()