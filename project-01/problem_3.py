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