# Problem 1
print '\nProblem 1\n'

import string

q1_dict = {'list':[1,2,3,4], 'tuple':('cat', 'dog'), 'integer':1, 
              'float':99.99, 1:'integer', 2:'integer_2', 'Uppercase_string':'ABCD',
              'CHARACTER':'C'}

## Fill in q1_func

def q1_func(dictionary):
  print "Here is the original dictionary: %s" %dictionary
  for item in dictionary.keys():
    lowercase_vowels='aeiou'
    item_string=str(item)
    if (item_string[0] in lowercase_vowels): 
      dictionary[item] ='vowel'
    elif (item_string[0] in string.ascii_lowercase): 
      dictionary[item] ='consonant'
    else:
      del dictionary[item]
  print "Here is the dictionary after running q1_func: %s" %(dictionary)
  return dictionary



q1_func(q1_dict) # Should be the same as expected result

# Problem 2
print '\nProblem 2\n'

q2_dict = {'A':[1,2,3,4,5], 'B':[12.1, 14.2, 20.3, 25.4], 'C':[10, 25.5, 50.9, 101]}
q2_remainder = [2,3,4,5]

## Fill in q2_func

def q2_func(dictionary, remainder=[]):
  if len(remainder)<1:
    remainder.append(2)
  print("Here is the starting dictionary: %s" %dictionary)
  print("Here is the remainder: %s" %remainder)
  results={}
  if len(remainder)==1:
    for key in dictionary.keys():
      temp=dictionary[key]
      dictionary[key]={}
      for item in temp:
        dictionary[key][item]=[]
        dictionary[key][item].append(item%remainder[0])
  else:
    for key in dictionary.keys():
      temp=dictionary[key]
      dictionary[key]={}
      for item in temp:
        dictionary[key][item]=[]
        #print 'the length of remainder is %s' %(len(remainder))
        for value in range(len(remainder)):
          dictionary[key][item].append(item%remainder[value])
  results=dictionary
  print results
  return  results


output = q2_func(q2_dict) # Should be same as expected result 1
output = q2_func(q2_dict, q2_remainder) # Should be same as expected result 2

# Problem 3
print '\nProblem 3\n'

q1_list1 = [1.5,3.5,5.5,7.5]
q2_list2 = [0,4,8,12]

## Fill in q3_func

def q3_func(list1, list2):
  multiplied=0
  iteration=1
  while multiplied<300:
    print 'Current List 1: %s' %list1
    print 'Current List 2: %s' %list2
    print'iteration: %s' %iteration
    for item in range(len(list1)):
      value1=list1[item]
      value2=list2[item]
      print 'Value 1: %s' %value1
      print 'Value 2: %s' %value2
      multiplied=value1 * value2
      print 'Multiplied Value: %s' %multiplied
      if(multiplied>=300):
        break
    for item in range(len(list1)):
      list1[item] *= 2
      list2[item] *= 2
    iteration +=1
  print 'Function Complete'


q3_func(q1_list1, q2_list2) # Should be same as expected result



# Problem 4
print '\nProblem 4\n'

# Fill in median_calculator and q4_func



def median_calculator(a_list):
  a_list.sort()
  if len(a_list)%2==1:
    median_list = a_list[len(a_list)/2]
  else:
    median_list = (a_list[len(a_list)/2-1]+a_list[len(a_list)/2])/float(2)
  return median_list





def q4_func(i, numbers):
  print "i is currently: %s" %i
  sum_numbers=sum(numbers)
  mean_numbers=sum_numbers/float(len(numbers))
  median_numbers=median_calculator(numbers)
  print 'The mean is: %s' %mean_numbers
  print 'The median is: %s' %median_numbers
  




for i in range(1, 15, 2):
    numbers = [x if not x % i == 0 else 0 for x in range(101)]
    q4_func(i, numbers) # should return same result as expected results
    



# Problem 5
print '\nProblem 5\n'

import numpy as np 

q5_predictions = [14.2,5.8,4.8,12.7,5.6,-1.2,5.3,11.9,4.8,8.1,1.5,8.5,14.9,6.1,
     6.8,12.6,15.5,24.3,15.6,16.8,22.3,22.6,26.2,19.0,24.3,26.3,
     25.3,31.6,27.3,33.0,32.6,30.7,29.6,34.7,32.7,43.1,40.1,35.4,49.6,38.6]

q5_true_values = [-15.5,-8.5,0.8,-3.9,4.9,12.7,10.0,16.5,5.7,13.1,10.3,12.4,-1.5,
     1.7,26.0,14.3,30.3,21.7,27.5,38.2,18.9,21.2,18.2,26.1,14.7,16.4,
     22.8,34.3,37.1,38.9,39.1,33.8,52.2,36.5,20.7,21.6,14.5,33.6,44.5,44.2]

#Fill in q5_func

def q5_func(true_values, predictions):
  errors=[]
  for item in range(len(true_values)):
    errors.append(predictions[item]-true_values[item])
    errors[item] = errors[item] ** 2
  mean_errors=sum(errors)/len(errors)
  rmse=np.sqrt(mean_errors)
  print 'RMSE: %s' %rmse
  return rmse

q5_func(q5_true_values, q5_predictions) # Should return same result as expected results




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


# Problem 10
print '\nProblem 10\n'

## Path forward is up to you!

math_int=map(int,math)
rate_int=map(int,rate)

fig=plt.figure()
ax=fig.add_subplot(1,1,1)
ax.set_title("Scatterplot of Testing Rate to Math Scores")
ax.set_xlabel("Precentage Rate of Eligible Students who took the SAT")
ax.set_ylabel("Average Score on Math Section of SAT")
ax.scatter(rate_int,math_int)
plt.savefig('q10.png')

print "There seems to be a negative-sloping linear relationship between the percent of students that took the SAT in a given state, and their avegare math scores.  This would imply that the higher the percent of students taking the test, the lower the average scores.  A possible reason for this negative correlation could be that when more students who may be less prepared to take the test are given the opportunity, those less-prepared students will score lower and bring down the state average.  One interesting data poing is Ohio, which has by far the lowest average scores, but yet has a low rate of students taking the test compared with other states."



