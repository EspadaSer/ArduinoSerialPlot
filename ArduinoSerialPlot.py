import serial
import time
import datetime
import matplotlib.pyplot as plt

# set up the serial line
ser = serial.Serial('COM3', 9600)
time.sleep(2)

# Read and record the data
data =[]                        # empty list to store the data
for i in range(50):
    b = ser.readline()          # read a byte string
    string_n = b.decode()       # decode byte string into Unicode  
    string = string_n.rstrip()  # remove \n and \r
    flt = float(string)         # convert string to float
    #print(flt)
    data.append(flt)            # add to the end of data list
    time.sleep(0.01)             # wait (sleep) 0.1 seconds

ser.close()

# show the data
#for line in data:
#    print(line)

#filenames generation
timestamp = str(datetime.datetime.now().replace(microsecond=0).isoformat('.')).replace(":", "").replace("-", "").replace(".", "_")
dataname = "data_" + timestamp + ".txt"
figname = "fig_" + timestamp + ".png"

# store the data
file=open(dataname,"w")
for line in data:
    file.write(str(line)+"\n")
file.close()

# if using a Jupyter notebook include
# %matplotlib inline

plt.plot(data)
plt.xlabel('Time (seconds)')
plt.ylabel('Reading')
plt.title('Reading vs. Time')
plt.savefig(figname)
plt.show()


