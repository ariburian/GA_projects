import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 



filename='reddit_posts.csv'

df=pd.read_csv(filename)

# print df.columns
# print df.dtypes
# print df.shape
# print df.describe()


## I am going to be working only with these 9 rows.  Author, domain, selftext, and title are strings which should a strong affect on the clustering.  UTC, number of comments, retrieved on, and score are all numbers, and is_self is a boolean.


good_columns=[ u'author',
       u'created_utc',   u'domain',
        u'is_self',
       u'num_comments',  
       u'retrieved_on',  u'score',u'title']  

unused_columns=[u'selftext']

df=df[good_columns]
new_df=df[['created_utc','is_self','num_comments','retrieved_on','score']]


## None of my 9 columns are missing any data!!
# print df.isnull().sum()


from sklearn.feature_extraction.text import CountVectorizer

cv=CountVectorizer()
titles_vec=cv.fit_transform(df['title']).todense()


# print 'titles shape', titles_vec.shape
# print 'df shape', df.shape
titles_df=pd.DataFrame(titles_vec)

# text_vec=cv.fit_transform(df['selftext']).todense()

# text_df=pd.DataFrame(text_vec)


author_vec=cv.fit_transform(df['author']).todense()
author_df=pd.DataFrame(author_vec)
domain_vec=cv.fit_transform(df['domain']).todense()
domain_df=pd.DataFrame(domain_vec)

print 'titles type', type(titles_df)
print 'new_df type', type(new_df)
new_df=new_df.join(titles_df, rsuffix='title')
# df=df.join(text_df, rsuffix='text')
new_df=new_df.join(domain_df,rsuffix='domain')
new_df=new_df.join(author_df,rsuffix='author')

# from sklearn.feature_extraction.text import TfidfVectorizer

# tvec=TfidfVectorizer(stop_words='english')
# tvec.fit_transform(df['title']).todense()

# print 'tvec type', type(tvec)


# def get_words_from_text(value):
# 	cvec=CountVectorizer()
# 	cvec.fit(value)
# 	df_words=pd.DataFrame(cvec.transform(value).todense(),columns=cvec.get_feature_names())
# 	return df_words

# from sklearn.preprocessing import LabelEncoder

# def get_words_from_text(value):
# 	le=LabelEncoder()
# 	return le.fit_transform(value)

str_columns=['author','domain','selftext','title']


#df['selftext_word_count']=df['selftext'].apply(word_counter)
#df['selftext_cnt_vector']=df['selftext_word_count'].apply(get_words_from_text)

print "shape of df", new_df.shape

##PCA!!

from sklearn.decomposition import PCA

pca=PCA(n_components=10)
df_pca=pca.fit_transform(new_df)
# print pca.get_covariance()
print "explained variance ratio title", np.cumsum(pca.explained_variance_ratio_)


from sklearn.externals import joblib

joblib.dump(df_pca,'pca_all_columns.pkl')




