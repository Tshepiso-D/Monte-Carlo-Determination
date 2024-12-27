import numpy as np
import matplotlib.pyplot as plt
import math as math
import numpy.random as random
print(" \nDetermine the value of the pi value using Monte Carlo Method!\n")
print("Circle Area/Square Area = Points in circle/Points in square\n")  # a formula for calculating the pi value
# I used 50 trials!
wrong_input=True

while wrong_input==True:     # Making sure to be ready for any input
    try:
        command=input("\nSelect number of trials or choose default number of trials\n default (select d) ")# select number of trials for calculating the value of pi
        if command.lower().strip()=='d':                         #modify input and check condition 
            no_of_trials=50                                      # default no of trials selected if condition met
        else:
            no_of_trials=int(command.strip())                            #no of trials is taken from user

        command=input("Select number of points on the square or choose default number of points\n default (select d) ")# select number of points for calculating the value of pi
        if command.lower().strip()=='d':                         #modify input and check condition 
            n=60000                                      # default no of points selected if condition met
        else:
            n=int(command.strip())
        wrong_input=False

    except:
        print("\nWrong input! Enter a number where a number is expected and enter d to select default settings\n")
        wrong_input=True
    

# Initial conditions 
#n=60000                                                  # the number of points we want on the square I used 60000
trial=0
pitrial=np.zeros(no_of_trials)                 # a list to make entries for pi values during each trial

while trial<=no_of_trials-1:                   # a while loop to calculate pi values during each loop
    B = random.uniform(-1,1,n)                 # make random n points between -1 and 1
    A = random.uniform(-1,1,n)                 # same as the line above, these are our coordinates!
    it=np.arange(0,n)                          # this is for my for loop will iterate with it
    t=0                                        # initial conditions
    s=0
    for i in it:
        if np.sqrt(B[i]**2+A[i]**2)<=1:       # condition to determine if point is in circle
            t+=1                              # add to the t variable if a point qualifies
        else:
            s+=1                              # if a point does not qualify add to the s variable just because i can

    r_c_s=t/(s+t)                             # calculate the ratio to points on circle to those on the square
    print("*************************************************************") # this prints some information the the terminal
    print("ratio of circle points to square points =        "+ str(r_c_s))
    print("Points in the circle =       "+str(t))
    print("Points in square =         "+str(s+t))
    print("Area of circle/Area of Square = pi/4 \n="+str(r_c_s))
    print("***************************************************************")
    print("Pi trial "+str(trial+1)+ " =      "+str(r_c_s*4))
    trial+=1                                   # increase the trial value so that we get a finite loop

    pitrial[trial-1] =r_c_s*4                   # make an entry to our pitrial list

#calculating the standard deviation and the standard deviation of the mean
N=len(pitrial)                                   # the number of pi values we have noted for the calculation of the mean
sum_pitrial=sum(pitrial)                         # sum our pi values
mean_pitrial=sum_pitrial/N                       # calculate mean

sq_of_ds=0                                       # calculate the sum of the squares of the difference between a pi value and the mean pi value
for i in range(N):
    sq_of_ds+=(pitrial[i]-mean_pitrial)**2       # add these ^ up

st_dev=np.sqrt(sq_of_ds/(N-1))                   # calculate standard deviation

st_dev_mean=st_dev/np.sqrt(N)                   # calculate standard deviation of the mean
print("*****************************************************************************************")# print to terminal rounded off to two decimal places
print("\nThe mean value of pi with the standard deviation of the mean is {}+-{}".format(round(mean_pitrial,3),round(st_dev_mean,3)))
print("*****************************************************************************************")

#print a figure of the square with the circle and the points for visuals
plt.figure(figsize=(10,10))
plt.plot(B,A,'.r')                          # plot a graph with the points
plt.title("The points on a square with a circle of radius 1") 
x=np.linspace(-1,1,6000) 
y=np.sqrt(1-x**2) 
u= -np.sqrt(1-x**2) 
plt.plot(x,y,"-g") 
plt.plot(x,u,"-g")                     
plt.draw
plt.savefig("file3")

def gaussian(datai,sigma,xbar):                                                # creates a function for our guassian
    t=1*math.e**(-(datai-xbar)**2/(2*(sigma**2)))/(sigma*np.sqrt(2*np.pi))
    return(t)

binwidth = 0.002                                                                  # bin width for the histogram
bins = np.arange(np.floor(min(pitrial)),np.floor(max(pitrial))+1,binwidth)            # bins are created using the np.arange results in a list with binwidth intervals
a=plt.figure(figsize=(10,10))           
n,bins,patches=plt.hist(pitrial,bins)
ni=len(n)
area_histt=0
for i in range(ni):
    area_histt+=n[i]*binwidth
model=np.linspace(3.12,3.155,no_of_trials)
plt.plot(pitrial,gaussian(pitrial,0.001,3.142)*area_histt,'*r',label="Original data points mapped to gaussian")    # plot a grap for the guassian with original data
plt.plot(model,gaussian(model,0.001,3.142)*area_histt,'-k',label="Gaussian Distribution for data")           # plot a graph for the guassian with the np.linspace function
plt.xlabel('pi')
plt.ylabel('Occurence')
plt.title("The Histogram for the data for pi with the guassian distribution of the data")
plt.xlim(3.11,3.18)
plt.legend()
plt.draw()
plt.savefig('file4')

plt.show()                                 # show what we plotted