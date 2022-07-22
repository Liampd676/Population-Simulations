import random
import numpy as np
from matplotlib import pyplot as plt

number_of_time_steps = 150
starting_number = 5

blobs = np.array([starting_number])
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
    #death chance
    for i in range(blobs[-1]):
        death = random.random()
        if death <= death_rate+crowding_effect:
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

def expected_change(x):
    return spawn_rate+((replicate_rate-death_rate)-crowding_number*x)*x


expected_blobs = np.array([starting_number])
for i in range(number_of_time_steps-1):
    change = expected_change(expected_blobs[-1])
    next_number = expected_blobs[-1]+change
    expected_blobs = np.append(expected_blobs, [next_number])

average = total/(number_of_time_steps-1)
print(average)

timex = np.linspace(1, number_of_time_steps, number_of_time_steps)
numberx = np.linspace(0, 55, 200)

fig, axs = plt.subplots(2, 2)
axs[0, 0].plot(timex, blobs, color="#5a7b9a")
axs[0, 0].set_title('Total Number Of Blobs')
axs[0, 1].plot(numberx, expected_change(numberx), 'tab:orange')
axs[0, 1].set_title('Expected Change Over Number')
axs[0, 1].grid()
axs[1, 0].plot(timex, blobs_change, 'tab:green')
axs[1, 0].set_title('Change In Number Of Blobs')
axs[1, 1].plot(timex, expected_blobs, 'tab:red')
axs[1, 1].set_title('Expected Number Of Blobs')


plt.show()