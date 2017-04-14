import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn.linear_model import LogisticRegression
from sklearn.grid_search import GridSearchCV
from sklearn.feature_selection import RFE
from sklearn.svm.libsvm import predict_proba


file_name = 'school_data_training.csv'

df=pd.read_csv(file_name)

# for column in df.columns:
# 	print column
	# print type(column)

list_of_cols_with_nums=['ZIP Code','Safety Score','Family Involvement Score','Environment Score','Instruction Score','Leaders Score ','Teachers Score','Parent Engagement Score','Parent Environment Score','Average Student Attendance','Rate of Misconducts (per 100 students) ','Average Teacher Attendance','Individualized Education Program Compliance Rate ','Pk-2 Literacy %','Pk-2 Math %','Gr3-5 Grade Level Math %','Gr3-5 Grade Level Read % ','Gr3-5 Keep Pace Read %','Gr3-5 Keep Pace Math %','Gr6-8 Grade Level Math %','Gr6-8 Grade Level Read %','Gr6-8 Keep Pace Math%','Gr6-8 Keep Pace Read %','Gr-8 Explore Math %','Gr-8 Explore Read %','ISAT Exceeding Math %','ISAT Exceeding Reading % ','ISAT Value Add Math','ISAT Value Add Read','Students Taking  Algebra %','Students Passing  Algebra %','9th Grade EXPLORE (2009) ','9th Grade EXPLORE (2010) ','10th Grade PLAN (2009) ','10th Grade PLAN (2010) ','Net Change EXPLORE and PLAN','11th Grade Average ACT (2011) ','Net Change PLAN and ACT','College Eligibility %','Graduation Rate %','College Enrollment Rate %','College Enrollment (number of students) ','General Services Route ','Freshman on Track Rate %','Community Area Number','Ward','Police District']
list_of_yes_no_cols=['Healthy Schools Certified?']
dummy_cols=['Elementary, Middle, or High School','Safety Icon ','Family Involvement Icon','Environment Icon ','Instruction Icon ','Leaders Icon ','Teachers Icon ','Parent Engagement Icon ','Parent Environment Icon','ISAT Value Add Color Math','ISAT Value Add Color Read','Community Area Name']
cols_with_icons=[]





def create_dummy_vars(dataframe):
	for column in dummy_cols:
		#print column 
		new_df = pd.get_dummies(dataframe[column],prefix=column)
		#print new_df.columns
		dataframe=dataframe.join(new_df)
		# print dataframe.head()
	return dataframe

def no_spec_chars(value):
	value=value.replace('%','')
	return value

def str_to_float(dataframe):
	for column in list_of_cols_with_nums:
		dataframe[column]=dataframe[column].apply(lambda x: '0' if x=='NDA' else x)
		dataframe[column]=dataframe[column].apply(lambda x: '0' if pd.isnull(x)==True else x)
		
		try:
			dataframe[column]=dataframe[column].apply(lambda x: float(x))
		except:
			dataframe[column]=dataframe[column].apply(no_spec_chars)
			dataframe[column]=dataframe[column].apply(lambda x: float(x))

		dataframe[column]=dataframe[column].apply(lambda x: dataframe[column].mean() if x==0 else x)
	return dataframe

def yes_to_one(dataframe):
	for column in list_of_yes_no_cols:
		dataframe[column]=dataframe[column].apply(lambda x: 1 if x=='Yes' else 0)
	return dataframe




def df_transform(dataframe):
	dataframe=create_dummy_vars(dataframe)
	dataframe=str_to_float(dataframe)
	dataframe=yes_to_one(dataframe)
	return dataframe

df=df_transform(df)




X=df[['Id','ZIP Code','Safety Score','Family Involvement Score','Environment Score','Instruction Score','Leaders Score ','Teachers Score','Parent Engagement Score','Parent Environment Score','Average Student Attendance','Rate of Misconducts (per 100 students) ','Average Teacher Attendance','Individualized Education Program Compliance Rate ','Healthy Schools Certified?',u'Elementary, Middle, or High School_ES',
       u'Elementary, Middle, or High School_HS',u'Safety Icon _Average', u'Safety Icon _NDA', u'Safety Icon _Strong',
       u'Safety Icon _Very Strong', u'Safety Icon _Very Weak',u'Family Involvement Icon_Average', u'Family Involvement Icon_NDA',
       u'Family Involvement Icon_Strong',u'Environment Icon _Average', u'Environment Icon _NDA',
       u'Environment Icon _Strong', u'Environment Icon _Very Strong',
       u'Environment Icon _Very Weak', u'Instruction Icon _Average', u'Instruction Icon _NDA',
       u'Instruction Icon _Strong', u'Instruction Icon _Very Strong',
       u'Instruction Icon _Very Weak', u'Leaders Icon _Average', u'Leaders Icon _NDA', u'Leaders Icon _Strong',
       u'Leaders Icon _Very Strong', u'Leaders Icon _Very Weak',
       u'Family Involvement Icon_Very Strong',
       u'Family Involvement Icon_Very Weak',u'Teachers Icon _Average', u'Teachers Icon _NDA',
       u'Teachers Icon _Strong', u'Teachers Icon _Very Strong',
       u'Teachers Icon _Very Weak', u'Parent Engagement Icon _Average', u'Parent Engagement Icon _NDA',
       u'Parent Engagement Icon _Strong',u'Parent Environment Icon_Average', u'Parent Environment Icon_NDA',
       u'Parent Environment Icon_Strong','Pk-2 Literacy %','Pk-2 Math %','Gr3-5 Grade Level Math %','Gr3-5 Grade Level Read % ','Gr3-5 Keep Pace Read %','Gr3-5 Keep Pace Math %','Gr6-8 Grade Level Math %','Gr6-8 Grade Level Read %','Gr6-8 Keep Pace Math%','Gr6-8 Keep Pace Read %','Gr-8 Explore Math %','Gr-8 Explore Read %','ISAT Exceeding Math %','ISAT Exceeding Reading % ','ISAT Value Add Math','ISAT Value Add Read','Students Taking  Algebra %','Students Passing  Algebra %','9th Grade EXPLORE (2009) ','9th Grade EXPLORE (2010) ','10th Grade PLAN (2009) ','10th Grade PLAN (2010) ','Net Change EXPLORE and PLAN','11th Grade Average ACT (2011) ','Net Change PLAN and ACT','College Eligibility %','Graduation Rate %','College Enrollment Rate %','College Enrollment (number of students) ','General Services Route ','Freshman on Track Rate %','Community Area Number','Ward','Police District',u'ISAT Value Add Color Math_Green', u'ISAT Value Add Color Math_NDA',
       u'ISAT Value Add Color Math_Red',u'ISAT Value Add Color Read_Green', u'ISAT Value Add Color Read_NDA',
       u'ISAT Value Add Color Read_Red',u'Community Area Name_ALBANY PARK', u'Community Area Name_ASHBURN',
       u'Community Area Name_AUBURN GRESHAM', u'Community Area Name_AUSTIN',
       u'Community Area Name_AVALON PARK',
       u'Community Area Name_BELMONT CRAGIN',
       u'Community Area Name_BRIDGEPORT', u'Community Area Name_BRIGHTON PARK',
       u'Community Area Name_CALUMET HEIGHTS',
       u'Community Area Name_CHICAGO LAWN', u'Community Area Name_CLEARING',
       u'Community Area Name_DOUGLAS', u'Community Area Name_DUNNING',
       u'Community Area Name_EAST GARFIELD PARK',
       u'Community Area Name_EAST SIDE', u'Community Area Name_EDGEWATER',
       u'Community Area Name_FOREST GLEN', u'Community Area Name_FULLER PARK',
       u'Community Area Name_GAGE PARK',
       u'Community Area Name_GRAND BOULEVARD',
       u'Community Area Name_GREATER GRAND CROSSING',
       u'Community Area Name_HEGEWISCH', u'Community Area Name_HERMOSA',
       u'Community Area Name_HUMBOLDT PARK', u'Community Area Name_HYDE PARK',
       u'Community Area Name_IRVING PARK', u'Community Area Name_KENWOOD',
       u'Community Area Name_LAKE VIEW', u'Community Area Name_LINCOLN SQUARE',
       u'Community Area Name_LOGAN SQUARE', 
       u'Community Area Name_LOWER WEST SIDE',
       u'Community Area Name_MCKINLEY PARK',
       u'Community Area Name_MORGAN PARK',
       u'Community Area Name_MOUNT GREENWOOD',
       u'Community Area Name_NEAR NORTH SIDE',
       u'Community Area Name_NEAR WEST SIDE', u'Community Area Name_NEW CITY',
       u'Community Area Name_NORTH CENTER',
       u'Community Area Name_NORTH LAWNDALE',
       u'Community Area Name_NORTH PARK', u'Community Area Name_NORWOOD PARK',
        u'Community Area Name_PORTAGE PARK',
       u'Community Area Name_PULLMAN', u'Community Area Name_RIVERDALE',
       u'Community Area Name_ROGERS PARK', u'Community Area Name_ROSELAND',
       u'Community Area Name_SOUTH CHICAGO',
       u'Community Area Name_SOUTH LAWNDALE',
       u'Community Area Name_SOUTH SHORE', u'Community Area Name_UPTOWN',
       u'Community Area Name_WASHINGTON HEIGHTS',
       u'Community Area Name_WASHINGTON PARK',
       u'Community Area Name_WEST ENGLEWOOD',
       u'Community Area Name_WEST GARFIELD PARK',
       u'Community Area Name_WEST LAWN', u'Community Area Name_WEST PULLMAN',
       u'Community Area Name_WEST RIDGE', u'Community Area Name_WEST TOWN']]##'Community Area Name_OHARE', 'Community Area Name_LOOP',
       
y=df['probation']

##Logistic Regression

lr=LogisticRegression()

lr.fit(X,y)
print "lr score",lr.score(X,y)

##Grid Search

hyperparameters={'penalty':['l1','l2'],'C':[0.32,0.325,0.33]}
grid_search=GridSearchCV(lr,hyperparameters)#,verbose=10)
grid_search.fit(X,y)
lr_gs=LogisticRegression(penalty='l1',C=0.33)
lr_gs.fit(X,y)
print grid_search.best_estimator_
print "grid search score", lr_gs.score(X,y)
#print "predict proba lr", lr.predict_proba(X)


##RFE

rfe=RFE(lr,n_features_to_select=25)
rfe.fit(X,y)
#print rfe.support_
print "rfe score",rfe.score(X,y)

##Output

file_name='school_data_test.csv'
test=pd.read_csv(file_name)
test=df_transform(test)
X_test=test[['Id','ZIP Code','Safety Score','Family Involvement Score','Environment Score','Instruction Score','Leaders Score ','Teachers Score','Parent Engagement Score','Parent Environment Score','Average Student Attendance','Rate of Misconducts (per 100 students) ','Average Teacher Attendance','Individualized Education Program Compliance Rate ','Healthy Schools Certified?',u'Elementary, Middle, or High School_ES',
       u'Elementary, Middle, or High School_HS',u'Safety Icon _Average', u'Safety Icon _NDA', u'Safety Icon _Strong',
       u'Safety Icon _Very Strong', u'Safety Icon _Very Weak',u'Family Involvement Icon_Average', u'Family Involvement Icon_NDA',
       u'Family Involvement Icon_Strong',u'Environment Icon _Average', u'Environment Icon _NDA',
       u'Environment Icon _Strong', u'Environment Icon _Very Strong',
       u'Environment Icon _Very Weak', u'Instruction Icon _Average', u'Instruction Icon _NDA',
       u'Instruction Icon _Strong', u'Instruction Icon _Very Strong',
       u'Instruction Icon _Very Weak', u'Leaders Icon _Average', u'Leaders Icon _NDA', u'Leaders Icon _Strong',
       u'Leaders Icon _Very Strong', u'Leaders Icon _Very Weak',
       u'Family Involvement Icon_Very Strong',
       u'Family Involvement Icon_Very Weak',u'Teachers Icon _Average', u'Teachers Icon _NDA',
       u'Teachers Icon _Strong', u'Teachers Icon _Very Strong',
       u'Teachers Icon _Very Weak', u'Parent Engagement Icon _Average', u'Parent Engagement Icon _NDA',
       u'Parent Engagement Icon _Strong',u'Parent Environment Icon_Average', u'Parent Environment Icon_NDA',
       u'Parent Environment Icon_Strong','Pk-2 Literacy %','Pk-2 Math %','Gr3-5 Grade Level Math %','Gr3-5 Grade Level Read % ','Gr3-5 Keep Pace Read %','Gr3-5 Keep Pace Math %','Gr6-8 Grade Level Math %','Gr6-8 Grade Level Read %','Gr6-8 Keep Pace Math%','Gr6-8 Keep Pace Read %','Gr-8 Explore Math %','Gr-8 Explore Read %','ISAT Exceeding Math %','ISAT Exceeding Reading % ','ISAT Value Add Math','ISAT Value Add Read','Students Taking  Algebra %','Students Passing  Algebra %','9th Grade EXPLORE (2009) ','9th Grade EXPLORE (2010) ','10th Grade PLAN (2009) ','10th Grade PLAN (2010) ','Net Change EXPLORE and PLAN','11th Grade Average ACT (2011) ','Net Change PLAN and ACT','College Eligibility %','Graduation Rate %','College Enrollment Rate %','College Enrollment (number of students) ','General Services Route ','Freshman on Track Rate %','Community Area Number','Ward','Police District',u'ISAT Value Add Color Math_Green', u'ISAT Value Add Color Math_NDA',
       u'ISAT Value Add Color Math_Red',u'ISAT Value Add Color Read_Green', u'ISAT Value Add Color Read_NDA',
       u'ISAT Value Add Color Read_Red',u'Community Area Name_ALBANY PARK', u'Community Area Name_ASHBURN',
       u'Community Area Name_AUBURN GRESHAM', u'Community Area Name_AUSTIN',
       u'Community Area Name_AVALON PARK',
       u'Community Area Name_BELMONT CRAGIN',
       u'Community Area Name_BRIDGEPORT', u'Community Area Name_BRIGHTON PARK',
       u'Community Area Name_CALUMET HEIGHTS',
       u'Community Area Name_CHICAGO LAWN', u'Community Area Name_CLEARING',
       u'Community Area Name_DOUGLAS', u'Community Area Name_DUNNING',
       u'Community Area Name_EAST GARFIELD PARK',
       u'Community Area Name_EAST SIDE', u'Community Area Name_EDGEWATER',
       u'Community Area Name_FOREST GLEN', u'Community Area Name_FULLER PARK',
       u'Community Area Name_GAGE PARK',
       u'Community Area Name_GRAND BOULEVARD',
       u'Community Area Name_GREATER GRAND CROSSING',
       u'Community Area Name_HEGEWISCH', u'Community Area Name_HERMOSA',
       u'Community Area Name_HUMBOLDT PARK', u'Community Area Name_HYDE PARK',
       u'Community Area Name_IRVING PARK', u'Community Area Name_KENWOOD',
       u'Community Area Name_LAKE VIEW', u'Community Area Name_LINCOLN SQUARE',
       u'Community Area Name_LOGAN SQUARE', 
       u'Community Area Name_LOWER WEST SIDE',
       u'Community Area Name_MCKINLEY PARK',
       u'Community Area Name_MORGAN PARK',
       u'Community Area Name_MOUNT GREENWOOD',
       u'Community Area Name_NEAR NORTH SIDE',
       u'Community Area Name_NEAR WEST SIDE', u'Community Area Name_NEW CITY',
       u'Community Area Name_NORTH CENTER',
       u'Community Area Name_NORTH LAWNDALE',
       u'Community Area Name_NORTH PARK', u'Community Area Name_NORWOOD PARK',
       u'Community Area Name_PORTAGE PARK',
       u'Community Area Name_PULLMAN', u'Community Area Name_RIVERDALE',
       u'Community Area Name_ROGERS PARK', u'Community Area Name_ROSELAND',
       u'Community Area Name_SOUTH CHICAGO',
       u'Community Area Name_SOUTH LAWNDALE',
       u'Community Area Name_SOUTH SHORE', u'Community Area Name_UPTOWN',
       u'Community Area Name_WASHINGTON HEIGHTS',
       u'Community Area Name_WASHINGTON PARK',
       u'Community Area Name_WEST ENGLEWOOD',
       u'Community Area Name_WEST GARFIELD PARK',
       u'Community Area Name_WEST LAWN', u'Community Area Name_WEST PULLMAN',
       u'Community Area Name_WEST RIDGE', u'Community Area Name_WEST TOWN']]##'Community Area Name_OHARE', 'Community Area Name_LOOP',

def evaluation_transformation(dataset, predictions):
    dataset = dataset.join(pd.DataFrame(predictions, columns=['Prediction']))
    dataset[['Id', 'Prediction']].to_csv('submission.csv', index=False)



evaluation_transformation(X_test,lr_gs.predict(X_test))

