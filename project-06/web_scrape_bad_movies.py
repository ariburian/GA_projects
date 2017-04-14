import requests
from bs4 import BeautifulSoup
import time
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn.externals import joblib
import re

# from imdbpie import Imdb
# imdb = Imdb()

# df=pd.DataFrame(imdb.top_250())

# def get_url(value):
# 	url='http://www.imdb.com/title/' + value +'/'
# 	return url

# df['hyperlink']=df['tconst'].apply(get_url)
list_of_bad_titles=[]
def get_title_num(value):
	value=value.split('tt')
	one_title=value[1][0:7]
	return one_title




# list_of_lists=[]
# for i,name in enumerate(df['hyperlink']):
# 	list_of_awards=[]

name=requests.get('http://www.imdb.com/list/ls003856293/')


with open("hyperlink.html", "w") as f:
	f.write(name.content)

with open('hyperlink.html','r') as f:
	soup=BeautifulSoup(f,'lxml')


list1=soup.find_all('div',{'class':"image"})
# for item in list1:
# 	#print item.text
# 	list_of_bad_titles.append(item)

	# list_of_lists.append(list_of_awards)


print 'length of list 1',len(list1)

time.sleep(1)

for item in list1:
	#title_num=get_title_num(item)
	link=item.find('a')['href']
	print link



# title_only_list=[]
# for item in list_of_bad_titles:
# 	item_split=item.split(' ')
# 	title = item_split[1]
# 	for letter in title:
# 		letter_split=letter.split('\\\n')
# 		title_only=letter_split[1]
# 		title_only_list.append(title_only)



print list_of_bad_titles[0:3]


# print title_only_list[0]


# list_of_lists_nums=[]

# for awards in list_of_lists:
	
# 	#for item in list_of_awards:
# 	list_of_nums=[]
# 	item=str(awards)
# 	#item=item.split(' '|'\\')

# 	item=re.split(r'[ \\]',item)
# 	for word in item:
# 		try:
# 			number=int(word)
# 			if number !=0:
# 				list_of_nums.append(number)
# 				# print list_of_nums
# 		except:
# 			pass
# 	list_of_lists_nums.append(list_of_nums)
		


# print list_of_lists_nums


# # list_of_nums_no_zeros=[]
# # for item in list_of_nums:
# # 	if item==0:
# # 		pass
# # 	else:
# # 		list_of_nums_no_zeros.append(item)

# # print list_of_nums_no_zeros

# joblib.dump(list_of_lists_nums,'movie_award.pkl')



