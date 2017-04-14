import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn.externals import joblib
from sklearn.tree import DecisionTreeRegressor, DecisionTreeClassifier,export_graphviz
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier

from imdbpie import Imdb
imdb = Imdb()
#imdb = Imdb(anonymize=True) # to proxy requests

df=pd.DataFrame(imdb.top_250())
list_of_award_nums=joblib.load('movie_award.pkl')

list_of_awards_no_null=[]
for item in list_of_award_nums:
	if len(item)!=3:
		new_list=[0,0,0]
		list_of_awards_no_null.append(new_list)
	else:
		list_of_awards_no_null.append(item)
# print list_of_awards_no_null
# print df.head()

# print df.describe()

# print df.columns
print df['can_rate'].value_counts()
print type(df['num_votes'][0])
print type(df['rating'][0])
print df['type'].value_counts()
print type(df['year'][0])


## All 250 "can_rate" are True
## All 250 "type" are Feature
## year in unicode
## no nulls in any column

for column in df.columns:
	print column, "total null: ",df[column].isnull().sum()


list_of_key_words=[]
def key_words(title):
	words=title.split(' ')
	for word in words:
		lc_word=word.lower()
		list_of_key_words.append(lc_word)
	return list_of_key_words



title_words=df['title'].apply(key_words)

title_words=pd.Series(title_words[0])
print len(title_words)
common_words = title_words.value_counts()

# print common_words[0:75]

# print common_words[67]
# print common_words[68]

## items  0 -67 include 2 or more instances.  The first 7 are removed becasue they are common english words
more_common_words=common_words[7:68].tolist()
print type(more_common_words)
# print common_words

# print more_common_words

def words_in_title(title):
	found_word=[]
	words=title.split(' ')
	for word in words:
		if word in more_common_words:   #### This is where I'm stuck
			found_word.append(word)
	return found_word


# Need to fix df['title_key_words']=df['title'].apply(words_in_title)
# print df['title_key_words'].head(50)



awards=pd.DataFrame(list_of_awards_no_null, columns=['oscar','win','nomination'])
print awards.head()



df['year_int']=df['year'].apply(lambda x: int(x))
df['title_length']=df['title'].apply(lambda x: len(x))
df=df.join(awards)




## Features to use in model: num_votes, title_length, year_int, awards(3), maybe keywords??

list_of_predictors=['num_votes','year_int','title_length','oscar','win','nomination']
X=df[list_of_predictors]
y_cont=df['rating']
y=df['rating'].apply(lambda x: 1 if x>=8.5 else 0)
print y[0:10]
print y[200:210]
print df.columns
print df['tconst'].head()



print len(list_of_award_nums)
length=[]
for item in list_of_award_nums:
	if len(item)!=3:
		length.append(item)

print len(length)
print df['oscar'].isnull().sum()

print df['win'].isnull().sum()
print df['nomination'].isnull().sum()


### Decision Tree Model Regression

X_train,X_test,y_train,y_test=train_test_split(X,y_cont,test_size=0.4)

dtr= DecisionTreeRegressor()
dtr.fit(X_train,y_train)

print "Decision Tree Regression: ", dtr.score(X_test,y_test)

rfr=RandomForestRegressor(n_estimators=100)

rfr.fit(X_train,y_train)
print "Random Forest Regression: ", rfr.score(X_test,y_test)



### Decision Tree Model Classification


X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.4)

dtc= DecisionTreeClassifier()
dtc.fit(X_train,y_train)

print "Decision Tree Classification: ", dtc.score(X_test,y_test)

rfc=RandomForestClassifier(n_estimators=100)

rfc.fit(X_train,y_train)
print "Random Forest Classification: ", rfc.score(X_test,y_test)


print df.head()
print df['rating'].describe()
z=df['title'].apply(lambda x: len(x))
print z.describe()


# from IPython.display import Image
# from sklearn.externals.six import StringIO
# import pydot

# dot_data=StringIO()
# export_graphviz(decision_tree=dtc,out_file=None)

# graph=pydot.graph_from_dot_data(dot_data)

# # Image(graph.create_png('decision_tree.png'))
# print X_test.head()
predictions=rfc.predict(X_test)
print type(predictions)

predictions = predictions.tolist()
y_test=y_test.tolist()



list_correct=[]
for i,item in enumerate(predictions):
	if item==y_test[i]:
		list_correct.append(1)
	else:
		list_correct.append(0)

print list_correct

fig=plt.figure()
ax=fig.add_subplot(1,1,1)
ax.set_title('Predicted Correctly by year of Release')
ax.scatter(X_test['year_int'].values,list_correct,color='red')

#ax.bar(X_test['year_int'].values,rfc.predict(X_test),color='green')

plt.savefig('predict vs. actual.png')

series_correct=pd.Series(list_correct)
print series_correct.describe()

fig2=plt.figure()
ax=fig2.add_subplot(1,1,1)
ax.hist(df['rating'])
ax.set_title('Histogram of movie Ratings')
plt.savefig('ratings of each movie.png')








