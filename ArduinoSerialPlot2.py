import serial
import time
import datetime
import matplotlib.pyplot as plt

# set up the serial line
ser = serial.Serial('COM4', 9600)
time.sleep(2)

# Read and record the data
data =[]                        # empty list to store the data
data1 = []
data2 = []
for i in range(50):
    b = ser.readline()          # read a byte string
    string_n = b.decode()       # decode byte string into Unicode  
    string = string_n.rstrip()  # remove \n and \r
    n1 , n2 = string.split(";") 
    #flt = float(string)         # convert string to float
    flt1 = float(n1)         
    flt2 = float(n2)
    #print(flt)
    data.append(string)
    data1.append(flt1)          # add to the end of data list
    data2.append(flt2)
    time.sleep(0.01)            # wait (sleep) 0.1 seconds

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

fig, (ax1, ax2) = plt.subplots(2)
fig.suptitle('Reading vs. Time')
ax1.plot(data1)
ax2.plot(data2)
plt.savefig(figname)
plt.show()

# plt.plot(data)
# plt.xlabel('Time (seconds)')
# plt.ylabel('Reading')
# plt.title('Reading vs. Time')
# plt.savefig(figname)
# plt.show()
