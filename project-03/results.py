import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#get_ipython().magic(u'matplotlib inline')
from sklearn.linear_model import LinearRegression, Ridge 
from sklearn import datasets, linear_model
from sklearn.cross_validation import train_test_split, cross_val_score



filename='airline.csv'
df=pd.read_csv(filename)
# print df.head()

# print df.columns

# for column in df.columns:
#     print column, type(df[column][0])



# print df.describe()


print df.corr()
# print type(df.corr())
# print df.corr().describe()



df['is_ord']=df['Origin'].apply(lambda x: 1 if x == 'ORD' else 0)
rp_carrier=pd.get_dummies(df['RPCarrier'])
#print rp_carrier.head()
df=df.join(rp_carrier,rsuffix='_dummy_var')
# print df.head()


X_clean=df[[u'Coupons',
       u'RoundTrip', u'OnLine', u'Passengers', 
       u'BulkFare', u'Distance', u'DistanceGroup', u'MilesFlown', u'is_ord',u'9E', u'AA', u'AS', u'B6', u'CP', u'DL',
       u'EV', u'F9', u'G7', u'MQ', u'NK', u'OO', u'S5', u'UA', u'VX', u'WN',
       u'YV', u'YX']]
y=df[u'ItinFare']
X_train,X_test,y_train,y_test=train_test_split(X_clean,y,test_size=0.4)



lr_model_1=LinearRegression()
lr_model_1.fit(X_train, y_train)
print "Coefficients: ", lr_model_1.coef_
print "intercept: ",lr_model_1.intercept_
print "Score: ",lr_model_1.score(X_train,y_train)
scores=cross_val_score(lr_model_1,X_clean,y,cv=3)
print "CV Scores: ",scores
predictions = lr_model_1.predict(X_train)
fig=plt.figure()
ax=fig.add_subplot(1,1,1)

ax.scatter(y_train,predictions)
ax.set_title('Model 1 Linear Regression')
ax.set_xlabel('Actual y-values')
ax.set_ylabel('Predicted y-values')
plt.savefig('lr_model_1')













# Train_test_split




rr_model_2=Ridge(alpha=5)
rr_model_2.fit(X_train, y_train)
print "Coefficients: ", rr_model_2.coef_
print "intercept: ",rr_model_2.intercept_
print "Score: ",rr_model_2.score(X_train,y_train)
scores=cross_val_score(rr_model_2,X_clean,y,cv=3)
print "CV Scores: ",scores

predictions = rr_model_2.predict(X_train)

ax2=fig.add_subplot(1,1,1)
ax2.scatter(y_train,predictions)
ax2.set_title('Model 2 Ridge Regression')
ax2.set_xlabel('Actual y-values')
ax2.set_ylabel('Predicted y-values')
plt.savefig('rr_model_2')



##Use lr_tts and test after it was trainded

test_score=lr_model_1.score(X_test,y_test)
print "Model 1 Score from test: ", test_score


test_score_2=rr_model_2.score(X_test,y_test)
print 'Model 2 Score from test: "',rr_model_2.score(X_test,y_test)

