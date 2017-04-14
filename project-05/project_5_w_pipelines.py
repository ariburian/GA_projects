import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn.pipeline import make_pipeline, FeatureUnion, make_union
from sklearn.preprocessing import FunctionTransformer, LabelBinarizer

from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.model_selection import cross_val_score, GridSearchCV

filename='university_train.csv'

df=pd.read_csv(filename)




#list_of_dummies=['HIGHDEG','CCUGPROF']
list_of_dummies=['STABBR','ACCREDAGENCY','HIGHDEG','PREDDEG','CONTROL','LOCALE','CCUGPROF','CCSIZSET']


#list_of_numerics=['MD_FAMINC','AGE_ENTRY']
list_of_numerics=['ZIP','MAIN','NUMBRANCH','HBCU','PBI','MENONLY','WOMENONLY','DISTANCEONLY','UGDS','FEMALE','AGE_ENTRY','MARRIED','DEPENDENT','MD_FAMINC']


def get_dummy_column(dataframe):
	new_df=df[list_of_dummies]
	return new_df

def get_numeric_column(dataframe):
	new_df=df[list_of_numerics]
	return new_df

#def drop_last_dummy(dataframe):


def value_float(value):
	new_value=''		
	for char in str(value):
		if char.isdigit()==True:
			new_value +=char
		elif char =='.':
			new_value +=char
		else:
			pass
	return float(new_value)


def zipcode_func(value):
	first_three=[]
	for i in range(3):
		first_three.append(value[i])
	return first_three


def str_to_float(dataframe):
	for col in list_of_numerics:
		if col == 'ZIP':
			dataframe.loc[:,col]=dataframe[col].apply(lambda x: x[0:3])
		dataframe.loc[:,col]=dataframe[col].apply(value_float)
	return dataframe

def transform_dummies(dataframe):
	output = dataframe.copy()
	for col in list_of_dummies:
		output[col] = LabelBinarizer().fit_transform(output[col])
 	return output


pipeline_dummies=make_pipeline(FunctionTransformer(get_dummy_column,validate=False),FunctionTransformer(transform_dummies,validate=False))#,FunctionTransformer(drop_last_dummy))




pipeline_numerics=make_pipeline(FunctionTransformer(get_numeric_column,validate=False),FunctionTransformer(str_to_float,validate=False))




feature_union=make_union(pipeline_dummies,pipeline_numerics)
X = feature_union.fit_transform(df)
y= df['percent_on_student_loan']

# for col in df.columns:
# 	print col, type(col)



#Linear Regression

lin_reg=LinearRegression()#normalize=True)

print "cross val scores lin reg", cross_val_score(lin_reg,X,y)

lin_reg.fit(X,y)
print "lin reg score",lin_reg.score(X,y)


#Ridge Regression

ridge=Ridge(alpha=50)

print "cross val scores ridge", cross_val_score(ridge,X,y)
hyperparameters={'alpha':[0.7,1,1.5,2]}


# grid_search_r=GridSearchCV(ridge, hyperparameters, verbose=10)
# grid_search_r.fit(X,y)
# print "best estimator ridge",grid_search_r.best_estimator_
# print 'best score ridge',grid_search_r.best_score_


ridge.fit(X,y)
print "Ridge score", ridge.score(X,y)

#Lasso Regression

lasso=Lasso(alpha=50)

print "cross val scores lasso", cross_val_score(lasso,X,y)
hyperparameters={'alpha':[0.0,0.1,0.5,0.7]}


# grid_search=GridSearchCV(lasso, hyperparameters, verbose=10)
# grid_search.fit(X,y)

# print "best estimator",grid_search.best_estimator_
# print 'best score',grid_search.best_score_
lasso.fit(X,y)
print "Lasso score", lasso.score(X,y)

file_name='university_test.csv'
df_test=pd.read_csv(file_name)
X_test = feature_union.transform(df_test)
print 'x test shape', X_test.shape
print 'df test shape', df_test.shape


def evaluation_transformation(dataset, predictions):
    dataset=pd.DataFrame(dataset)
    #dataset=dataset.join(pd.DataFrame(df_test['id_number']))
    #print df_test['id_number'].shape
    #print dataset.shape
    dataset = dataset.join(pd.DataFrame(predictions, columns=['Prediction']))
    #print dataset
    dataset[['id_number', 'Prediction']].to_csv('reg_submission.csv', index=False)



evaluation_transformation(df_test,lasso.predict(X_test))


