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
	return	results


output = q2_func(q2_dict) # Should be same as expected result 1
output = q2_func(q2_dict, q2_remainder) # Should be same as expected result 2