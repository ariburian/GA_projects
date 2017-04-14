import numpy as np 
import scipy.stats as sp 


 ##Problem 6
print '\nProblem 6\n'

path_to_csv = './assets/sat_scores.csv'

## Path forward is up to you!
import csv


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
# 	stats_all_data['min']=min(all_data[item])
# 	stats_all_data['max']=max(all_data[item])
# 	stats_all_data['mean']=np.mean (all_data[item])
# 	stats_all_data['standard deviation']=np.std(all_data[item])
# 	stats_all_data['median']=np.median(all_data[item])
# 	stats_all_data['mode']=sp.mode(all_data[item])
# print stats_all_data

stats=['minimum','maximum','mean','standard deviation','median','mode']	
values=['verbal','math','rate']
for x in range (0,6):
	for y in range(0,3):
		print "The %s from %s is: %s" %(stats[x],values[y],results[x][y])

# print 'The min score for verbal is: %s' %min_verbal
# print 'The min score for verbal is: %s' %min_verbal
# print 'The min score for verbal is: %s' %min_verbal
# print 'The min score for verbal is: %s' %min_verbal




# Generate and print out the:

# - Minimum
# - Maximum 
# - Mean
# - Standard Deviation
# - Median
# - Mode 

# of the Verbal, Math, and Rate columns. You may use NumPy and SciPy for this instead of rolling out your own.
