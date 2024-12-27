import numpy as np
import matplotlib.pyplot as plt
import math as math
import numpy.random as random

f = open("Activity1Data.txt",'r')    # open file

header = f.readline()                # read and ignore header

data = np.zeros(60)
i = 0
model=np.linspace(35,46,60)

def gaussian(datai,sigma,xbar):                                                # creates a function for our guassian
    t=1*math.e**(-(datai-xbar)**2/(2*(sigma**2)))/(sigma*np.sqrt(2*np.pi))
    return(t)
    
for line in f:                                                                  # loop over lines
        line = line.strip()
        columns = line.split()                                                  # manipulating the file
        data[i] =  float(columns[1])                                            # extract data
        i = i + 1

binwidth = 0.5                                                                  # bin width for the histogram
bins = np.arange(np.floor(min(data)),np.floor(max(data))+1,binwidth)            # bins are created using the np.arange results in a list with binwidth intervals
plt.figure(figsize=(10,10))           
n,bins,patches=plt.hist(data,bins)
ni=len(n)
area_hist=0
for i in range(ni):
    area_hist+=n[i]*binwidth
plt.plot(data,gaussian(data,1.905,40.083)*area_hist,'*r',label="Original data points mapped to gaussian")    # plot a grap for the guassian with original data
plt.plot(model,gaussian(model,1.905,40.083)*area_hist,'-k',label="Gaussian Distribution for data")           # plot a graph for the guassian with the np.linspace function
plt.xlabel('x')
plt.ylabel('Occurence')
plt.title("The Histogram for the data from Activity1 with the guassian distribution of the data")
plt.legend()
plt.draw()
plt.savefig('file1')

 #Creating a text file with data having standard deviation 2 and mean 40

midata = random.normal(40.0,2.0,60)                                             #creates data using randorm. normal
line=['Random numbers drawn from Gaussian with mu = 4 0. 0 and sigma = 2. 0']   # this is our heading
it=np.arange(0,60)                                                              # creates a list of numbers [0,60]
with open('ActivityData2.txt','w') as g:                                        # create a file in the folder and we can write to it
    g.write(line[0])                                                            # this is the line being written in the file
    for i in it:                                                                # Here I am writing the data number and the data in the file as two columns using 'it' indices to loop.
        g.write('\n')
        g.write(str(i+1)+'  '+str(midata[i]))

# Histograming this data
binwidth = 0.5                                                                  # bin width for the histogram
bins = np.arange(np.floor(min(midata)),np.floor(max(midata))+1,binwidth)            # bins are created using the np.arange results in a list with binwidth intervals                                                       # plot a graph for the guassian with the np.linspace function
plt.figure(figsize=(10,10))
t,patchess,binz=plt.hist(data,bins,color=(1,1,0))                                                #creates histograms
nii=len(t)
area_hist2=0
for i in range(nii):
    area_hist2+=t[i]*binwidth

plt.plot(model,gaussian(model,2,40)*area_hist2,'-m',label="Intended Guassian Distribution")                                      # plot a grap for the guassian with original data
plt.plot(model,gaussian(model,1.9,40.1)*area_hist2,'-k',label="Gaussian Distribution From the Data Statistics")                                
plt.xlabel('x')
plt.ylabel('Occurence')
plt.title("A Histogram of Generated Data and the Intended Guassian compared to the Guassian of the Data Set.")
plt.legend()
plt.draw()
plt.savefig('file2')
plt.show()                                                                      # this shows anything plotted