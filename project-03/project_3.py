

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#get_ipython().magic(u'matplotlib inline')
from sklearn.linear_model import LinearRegression, Ridge 
from sklearn import datasets, linear_model
from sklearn.cross_validation import train_test_split, cross_val_score



filename='airline.csv'
df=pd.read_csv(filename)
print df.head()


print df.columns



for column in df.columns:
    print column, type(df[column][0])



print df.describe()




lr=LinearRegression()

x=df['Distance'].values.reshape(-1,1)

y=df['ItinFare'].values.reshape(-1,1)


lr.fit(x,y)

print lr.predict(np.asarray([200.0,800.0,1500.0]).reshape(-1,1))

print lr.predict([800])


print "LR1 Distance Col Only Score: ",lr.score(x,y)


predict_distance=lr.predict(x)


plt.figure(figsize=(20,16))
plt.scatter(y,predict_distance)
plt.savefig('predict_distance.png')



print df.corr()
print type(df.corr())
print df.corr().describe()








lr2=LinearRegression()


X2=df[['Distance','Coupons']].values


lr2.fit(X2,y)


print "LR2 Distance and Coupons Score: ",lr2.score(X2,y)


predict_dist_coupon=lr2.predict(X2)


plt.figure(figsize=(20,16))
plt.scatter(y,predict_dist_coupon)
plt.savefig('predict_dist_coupon.png')


lr3=LinearRegression()
X3=df.loc[df['Origin']=='ORD',['Distance','Coupons']]
y=df.loc[df['Origin']=='ORD',['ItinFare']]
lr3.fit(X3,y)
print "LR3 Distance and Coupons, ORD only Score: ",lr3.score(X3,y)




# lr4=LinearRegression()

# X4=df[[ u'ItinID', u'FarePerMile', u'Coupons',
#        u'RoundTrip', u'OnLine', u'Passengers', 
#        u'BulkFare', u'Distance', u'DistanceGroup', u'MilesFlown']]
# #print X4.head()

# lr4.fit(X4,y)
# print "LR4 All numeric columns Score: ",lr4.score(X4,y)


# predict_all_ints=lr4.predict(X4)
# plt.scatter(y,predict_all_ints)
# plt.savefig('predict_all_ints.png')



lr6=LinearRegression()
X6=df[[ u'FarePerMile', u'Coupons',
       u'RoundTrip', u'OnLine', u'Passengers', 
       u'BulkFare', u'Distance', u'DistanceGroup', u'MilesFlown']]
y=df['ItinFare']
lr6.fit(X6,y)
print "LR6 All numeric less ItinID score: ",lr6.score(X6,y)



lr5=LinearRegression()
X5=df['FarePerMile'].values.reshape(-1,1)
lr5.fit(X5,y)
print "FarePerMile feeds in y to generate, so it can't be used as a prediction.  It's score is: ",  lr5.score(X5,y)


# Train_test_split



df['is_ord']=df['Origin'].apply(lambda x: 1 if x == 'ORD' else 0)
rp_carrier=pd.get_dummies(df['RPCarrier'])
#print rp_carrier.head()
df=df.join(rp_carrier,rsuffix='_dummy_var')
print df.head()


# In[40]:

X_clean=df[[u'Coupons',
       u'RoundTrip', u'OnLine', u'Passengers', 
       u'BulkFare', u'Distance', u'DistanceGroup', u'MilesFlown', u'is_ord',u'9E', u'AA', u'AS', u'B6', u'CP', u'DL',
       u'EV', u'F9', u'G7', u'MQ', u'NK', u'OO', u'S5', u'UA', u'VX', u'WN',
       u'YV', u'YX']]

X_train,X_test,y_train,y_test=train_test_split(X_clean,y,test_size=0.4)


lr_tts=LinearRegression()
model = lr_tts.fit(X_train, y_train)
print "Coefficients: ", model.coef_
print "intercept: ",model.intercept_
print "Score: ",model.score(X_train,y_train)
scores=cross_val_score(lr_tts,X_clean,y,cv=3)
print scores
predictions = lr_tts.predict(X_test)
plt.scatter(y_test,predictions)
print model.score(X_test,y_test)
plt.savefig('predictions_tts')


rr_tts=Ridge(alpha=5)
model_2=rr_tts.fit(X_train, y_train)
print "Coefficients: ", model_2.coef_
print "intercept: ",model_2.intercept_
print "Score: ",model_2.score(X_train,y_train)
predictions = rr_tts.predict(X_test)
plt.scatter(y_test,predictions)
print model_2.score(X_test,y_test)
plt.savefig('predictions_tts_ridge')


##Use lr_tts and test after it was trainded

test_score=model.score(X_test,y_test)
print "Score from test: ", test_score



