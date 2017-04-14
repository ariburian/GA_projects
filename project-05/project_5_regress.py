import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn.pipeline import make_pipeline, FeatureUnion, make_union
from sklearn.preprocessing import FunctionTransformer, LabelBinarizer

from sklearn.linear_model import LinearRegression

filename='university_train.csv'

df=pd.read_csv(filename)

list_of_dummies=['STABBR','ACCREDAGENCY','PREDDEG','HIGHDEG','CONTROL','LOCALE','CCUGPROF','CCSIZET']
list_of_numerics=['ZIP','MAIN','NUMBRANCH','HBCU','PBI','MENONLY','WOMENONLY','DISTANCEONLY','UGDS','AGE_ENTRY','FEMALE','MARRIED','DEPENDANT','MD_FAMINC']
# def get_dummy_column(dataframe):
# 	new_df=pd.DataFrame()
# 	for col in list_of_dummies:
# 		new_ser=dataframe[col]
# 		new_df=new_df.join(new_ser)
# 	return new_df


def create_dummy_vars(dataframe):
	for column in list_of_dummies: 
		new_df = pd.get_dummies(dataframe[column],prefix=column)
	return new_df

# def get_numeric_column(dataframe):
# 	new_df=pd.DataFrame()
# 	for col in list_of_numerics:
# 		new_ser=dataframe[col]
# 		new_df=new_df.join(new_ser)
# 	return new_df

#def drop_last_dummy(dataframe):


def value_float(value):
	for i, char in enumerate(len(value)):
		if value[i].isdigit()==False:
			value[i]=value[i].replace(char,'')
	return float(value)


# def str_to_float(dataframe):
# 	for col in list_of_numerics:
# 		dataframe[col]=dataframe[col].apply(value_float)
# 	return dataframe

X=pd.DataFrame()

for col in list_of_dummies:
	new_df=df[col].apply(create_dummy_vars)  
	X=X.join(new_df)

for col in list_of_numerics:
	new_df=df[col].apply(value_float)
	X=X.join(new_df)

print X.head()









# lin_reg=LinearRegression()

# lin_reg.fit(X,y)