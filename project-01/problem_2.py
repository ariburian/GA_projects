
# Problem 2
print '\nProblem 2\n'

q2_dict = {'A':[1,2,3,4,5], 'B':[12.1, 14.2, 20.3, 25.4], 'C':[10, 25.5, 50.9, 101]}
q2_remainder = [2,3,4,5]

def q2_func(a_dictionary,remainder=None):
  if (remainder==None):
    remainder=[2]
  print (a_dictionary)
  print(remainder)
  result={}
  if len(remainder)==1:
    for key in a_dictionary.keys():
      for item in range(len(a_dictionary[key])):
        find_remainder=a_dictionary[key][item]%remainder[0]
        data_point=a_dictionary[key][item]
        a_dictionary[key][item]=[]
        a_dictionary[key][item].append(data_point)
        a_dictionary[key][item].append(find_remainder)
    
  else:
    for key in a_dictionary.keys():
      for item in range(len(a_dictionary[key])):
        new_dict={}
        for i in remainder:
          new_dict[a_dictionary[key]]=a_dictionary[key][item]%i 
        a_dictionary[key]=new_dict


  results_dict=a_dictionary
  print results_dict
  return results_dict

q2_func(q2_dict)
q2_func(q2_dict,q2_remainder)









