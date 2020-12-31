import time
import datetime
import warnings
from collections import deque
import serial
import numpy as np
import matplotlib.pyplot as plt
import keyboard
 
N = 200
data = deque([0] * N, maxlen=N) # deque con longitud máxima N
#Creamos la figura
plt.ion()
fig, ax = plt.subplots()
ll, = ax.plot(data)
 
# Abrimos la conexión con Arduino
arduino = serial.Serial('COM3', 9600)

#filenames generation

def killer():
    
    print("Exiting")

    #filenames generation

    timestamp = str(datetime.datetime.now().replace(microsecond=0).isoformat('.')).replace(":", "").replace("-", "").replace(".", "_")
    dataname = "data_" + timestamp + ".txt"
    figname = "fig_" + timestamp + ".png"
    
    # store the figure
    plt.savefig(figname)

    # store the data
    file=open(dataname,"w")
    for line in data:
        file.write(str(line)+"\n")
    file.close()

keyboard.add_hotkey('ctrl+shift+s', killer)
 
with arduino:
    while True:
        try:
            line = arduino.readline()

            #xx, yy = np.fromstring(line.decode('ascii', errors='replace'), sep=' ')
            string_n = line.decode()       # decode byte string into Unicode  
            string = string_n.rstrip()  # remove \n and \r
            flt = float(string)         # convert string to float

            data.append(flt)
            ll.set_ydata(data)
            ax.set_ylim(min(data) - 10, max(data) + 10)
            plt.pause(0.001)

        except ValueError:
            warnings.warn("Line {} didn't parse, skipping".format(line))

        except KeyboardInterrupt: #press control+c
            killer()

            break

            # print("Exiting")

            # #filenames generation

            # timestamp = str(datetime.datetime.now().replace(microsecond=0).isoformat('.')).replace(":", "").replace("-", "").replace(".", "_")
            # dataname = "data_" + timestamp + ".txt"
            # figname = "fig_" + timestamp + ".png"
            
            # # store the figure
            # plt.savefig(figname)

            # # store the data
            # file=open(dataname,"w")
            # for line in data:
            #     file.write(str(line)+"\n")
            # file.close()

            # break