# Problem 5
import numpy as np 
print '\nProblem 5\n'

q5_predictions = [14.2,5.8,4.8,12.7,5.6,-1.2,5.3,11.9,4.8,8.1,1.5,8.5,14.9,6.1,
     6.8,12.6,15.5,24.3,15.6,16.8,22.3,22.6,26.2,19.0,24.3,26.3,
     25.3,31.6,27.3,33.0,32.6,30.7,29.6,34.7,32.7,43.1,40.1,35.4,49.6,38.6]

q5_true_values = [-15.5,-8.5,0.8,-3.9,4.9,12.7,10.0,16.5,5.7,13.1,10.3,12.4,-1.5,
     1.7,26.0,14.3,30.3,21.7,27.5,38.2,18.9,21.2,18.2,26.1,14.7,16.4,
     22.8,34.3,37.1,38.9,39.1,33.8,52.2,36.5,20.7,21.6,14.5,33.6,44.5,44.2]

#Fill in q5_func

def q5_func(true_values, predictions):
	errors=[]
	item=0
	print (len(predictions))
	print(len(true_values))
	for item in range()

	# while item<len(true_values):
	# 	#errors[item]=predictions[item]-true_values[item]

	# 	errors[item] = errors[item] ** 2
	# 	item += 1 
	# mean_errors=sum(errors)/len(errors)
	# rmse=np.sqrt(mean_errors)
	# print 'RMSE: %s' %rmse
	# return rmse

q5_func(q5_true_values, q5_predictions) # Should return same result as expected results
