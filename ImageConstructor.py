import numpy
import csv
import random

NUM_LEDS=500
MAX_HORIZONTAL=800
MAX_VERTICAL=500

with open('pixelLocations.csv', 'w', newline='') as csvfile:
    writer=csv.writer(csvfile, delimiter=',')
    for i in range(NUM_LEDS):
        x=random.randint(0,MAX_HORIZONTAL)
        y=random.randint(0,MAX_VERTICAL)
        writer.writerow([str(x),str(y)])