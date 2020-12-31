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
data1 = deque([0] * N, maxlen=N)
data2 = deque([0] * N, maxlen=N)
#Creamos la figura
plt.ion()

fig, (ax1, ax2) = plt.subplots(2)
fig.suptitle('Reading vs. Time')
ax1.plot(data1)
ax2.plot(data2)
ll1, = ax1.plot(data1)
ll2, = ax2.plot(data2)
# Abrimos la conexión con Arduino
arduino = serial.Serial('COM4', 9600)

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

keyboard.add_hotkey('ctrl+shift+s', killer) # press control + shift + s to kill program
 
with arduino:
    while True:
        try:
            line = arduino.readline()

            #xx, yy = np.fromstring(line.decode('ascii', errors='replace'), sep=' ')
            string_n = line.decode()       # decode byte string into Unicode  
            string = string_n.rstrip()  # remove \n and \r
            n1 , n2 = string.split(";") 
            #flt = float(string)         # convert string to float
            flt1 = float(n1)         
            flt2 = float(n2)

            data.append(string)
            data1.append(flt1)          # add to the end of data list
            data2.append(flt2)

            ll1.set_ydata(data1)
            ll2.set_ydata(data2)
            #ax1.plot(data1),.set_ydata(data1)
            #ax2.plot(data2),.set_ydata(data2)
            ax1.set_ylim(min(data1) - 10, max(data1) + 10)
            ax2.set_ylim(min(data2) - 10, max(data2) + 10)
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