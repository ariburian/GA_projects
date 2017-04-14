
 ##Problem 6
print '\nProblem 6\n'

import numpy as np 
import scipy.stats as sp 
import csv

path_to_csv = './assets/sat_scores.csv'

## Path forward is up to you!

state=[]
rate=[]
verbal=[]
math=[]

with open(path_to_csv, 'r') as f:
    reader = csv.reader(f)
    print reader
    for row in reader:
      state.append(row[0])
      rate.append(row[1])
      verbal.append(row[2])
      math.append(row[3])  

# Dropping those rows
state=state[1:len(state)-1]
rate=rate[1:len(rate)-1]
verbal=verbal[1:len(verbal)-1]
math=math[1:len(math)-1]

for item in range(0,len(state)):
  print "%s:  Verbal: %s, Math: %s, Rate: %s" %(state[item], verbal[item],math[item], rate[item])

print "All states are represented.  The length of the state list is 53, which includes 50 states, DC, a header row, and an \"ALL\" row."
print"The header row and ALL row were dropped, because they themselves are not states"


# Problem 7
print '\nProblem 7\n'

## Path forward is up to you!

######
# ## Problem 7

verbal=map(int,verbal)
math=map(int,math)
rate=map(int,rate)
min_verbal=min(verbal)
min_math=min(math)
min_rate=min(rate)
max_verbal=max(verbal)
max_math=max(math)
max_rate=max(rate)
mean_verbal=np.mean(verbal)
mean_math=np.mean(math)
mean_rate=np.mean(rate)
std_verbal=np.std (verbal)
std_math=np.std(math)
std_rate=np.std(rate)
median_verbal=np.median(verbal)
median_math=np.median(math)
median_rate=np.median(rate)
mode_verbal=sp.mode (verbal)
mode_math=sp.mode(math)
mode_rate=sp.mode(rate)

results=[[min_verbal,min_math,min_rate],[max_verbal,max_math,max_rate],[mean_verbal,mean_math,mean_rate],[std_verbal,std_math,std_rate],[median_verbal,median_math,median_rate],[mode_verbal[0],mode_math[0],mode_rate[0]]]
# all_data=[state,rate,verbal,math]
# stats_all_data={}
# for item in all_data:
#   stats_all_data['min']=min(all_data[item])
#   stats_all_data['max']=max(all_data[item])
#   stats_all_data['mean']=np.mean (all_data[item])
#   stats_all_data['standard deviation']=np.std(all_data[item])
#   stats_all_data['median']=np.median(all_data[item])
#   stats_all_data['mode']=sp.mode(all_data[item])
# print stats_all_data

stats=['minimum','maximum','mean','standard deviation','median','mode'] 
values=['verbal','math','rate']
for x in range (0,6):
  for y in range(0,3):
    print "The %s from %s is: %s" %(stats[x],values[y],results[x][y])

# Problem 8
print '\nProblem 8\n'

## Path forward is up to you!

import matplotlib.pyplot as plt

verbal_int=map(int,verbal)

fig=plt.figure()
ax=fig.add_subplot(1,1,1)
ax.set_title("Histogram of Verbal Scores")
ax.hist(verbal_int,bins=15)
plt.savefig('q8.png')

print "The data seems skewed to the right(positive), as we saw previously, that the mean is larger than the median. There is also a second peek around 560, which implies that its not only outliers pulling up the mean."


# Problem 9
print '\nProblem 9\n'

## Path forward is up to you!

math_int=map(int,math)

fig=plt.figure()
ax=fig.add_subplot(1,1,1)
ax.set_title("Histogram of Math Scores")
ax.hist(math_int,bins=15)
plt.savefig('q9.png')

print "The mean and median for math seem very similar to that of verbal, with a similar right (positive) skew.  For math, however, there is not second peak and the scores trail off gradually."






