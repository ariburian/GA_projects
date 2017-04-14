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
    



