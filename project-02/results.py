import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 


df=pd.read_csv('Iowa_Liquor_sales_sample_10pct.csv')

print df.head()
df_shape=df.shape 
print 'Question #1:  The dataset has the shape: ' 
print df_shape
print 'There are %s rows and %s columns' %(df_shape[0],df_shape[1])
print 'Here are the types of each column: '
print df.dtypes

print 'Question #2: '

print 'Here is the count for each column with how many missing elements it has:'

for col in df.columns:
   print col, df[col].isnull().sum()

print 'I think we should just leave these as null values, because to remove them, you would be losing other columns in that row which have meaningful data, and to select zero or the mean for these columns also wouldn\'t make sense, because the mean of a county number or a category number is meaningless.'

print 'To clean the data, I changed all of the columns with numeric values into floats if they were previously in strings.  Floats work for all columns, while ints would occasional lose data depending on the column - particularly dollar amounts where the cents can be important.  I also removed dollar signs and any other special characters that my show up.  For the date, I created 3 new float columns for the month, day, and year separately.'



def string_to_float(value):
	value=value.replace('$','')
	value=value.replace('/','')
	value=value.replace('-','')
	value=value.replace(',','')
	value_float=float(value)
	return value_float


def date_splitter_month(value):
	value=value.split('/')
	month=value[0]
	month_int=int(month)
	return month_int

def date_splitter_day(value):
	value=value.split('/')
	day=value[1]
	day_int=int(day)
	return day_int

def date_splitter_year(value):
	value=value.split('/')
	year=value[2]
	year_int=int(year)
	return year_int




df['State Bottle Cost float']=df['State Bottle Cost'].apply(string_to_float)
df['State Bottle Retail float']=df['State Bottle Retail'].apply(string_to_float)
df['Sale (Dollars) float']=df['Sale (Dollars)'].apply(string_to_float)
df['Month']=df['Date'].apply(date_splitter_month)
df['Day']=df['Date'].apply(date_splitter_day)
df['Year']=df['Date'].apply(date_splitter_year)
df['Zip Code float']=df['Zip Code'].apply(string_to_float)



print "Question #3: "


df_years_open = df.groupby('Store Number')['Year'].agg({'Mean': np.mean})


# print len(df_years_open[df_years_open==2016])
# print len(df_years_open)
# print len(df)
# print len(set(df['Store Number']))


# print df_years_open.head()

open_2016_only = list(df_years_open.loc[df_years_open['Mean']==2016].index)

#print open_2016_only
print "There are a total of %s unique store numbere in the data set.  Of which, %s had transactions only in 2016.  Since we are looking at sales from 2015 only, those rows will be excluded." %(len(df_years_open), len(open_2016_only))



def dummy_for_year(value):
	if value in open_2016_only:
		return 1
	else:
		return 0

df['dummy_2016']=df['Store Number'].apply(dummy_for_year)

# print df['dummy_2016']

df_2015_only = df[df['dummy_2016']==0]

print "Question #4: "

# print len(df)
# print len(df_2015_only)

# print df_2015_only.columns
# print df.head()
# print df.shape

print "What is the yearly liquor sales for each store in 2015?\n  As explained on the data.iowa.gov website, the Alcoholic Beverages Division is buying and selling at a retail price to the stores.  I will assume all of the liquor that was purchased from the state was sold, so the yearly liquor sales for each store is equal to the sum of \"Volume Sold (Liters)\" column for all rows of each store."

sales_by_store = pd.pivot_table(df_2015_only[df_2015_only['Year']==2015],index='Store Number',values='Volume Sold (Liters)',aggfunc=np.sum)
print sales_by_store.head()

print 'What is the profit for each store in 2015?\n Since we don\'t know how much each store is selling the bottles they purchase for, I will interpret this question to be \"What is the profit [to the Alcoholic Beverages Division] FROM each store?\"  To find that we can subtract the State Bottle Cost from the State Bottle Retail (the net profit) and multiply that by the Bottles Sold to find the profit for each transaction, and then we can sum up all of the rows from each store to find the total profit from each store to the Alcoholic Beverages Division.'



df['profit_per_transaction']=(df['State Bottle Retail float']-df['State Bottle Cost float'])*df['Bottles Sold']
df_2015_only = df[df['dummy_2016']==0]

profit_by_store=pd.pivot_table(df_2015_only[df_2015_only['Year']==2015], index='Store Number', values='profit_per_transaction',aggfunc=np.sum)
print profit_by_store.head()




print 'Question #5: '



#print df[['Category', 'Category Name']].head(20)
category_sorted= pd.pivot_table(df,index=['Category','Category Name'],columns='Bottles Sold')
# print category_sorted
# print category_sorted[20:50]

# if (df['Category']<1020000):
# 	df['broad category']='whiskey'

def broad_category(value):
	if value <1020000:
		return 'whiskey'
	elif value < 1030000:
		return 'tequila'
	elif value <1040000:
		return 'vodka'
	elif value <1050000:
		return 'gin'
	elif value <1060000:
		return 'brandy'
	elif value <1070000:
		return 'rum'
	elif value <1080000:
		return 'cocktail'
	elif value <1090000:
		return 'shnapps'
	else:
		return 'other'

df['broad category']=df['Category'].apply(broad_category)
print "Here are the nine broader categories I created, with the number of different bevarages that went under each category."


print pd.pivot_table(df,index=['broad category'],values=['Category Name'],aggfunc=lambda x: len(x.unique()))

print 'Here is each broad category with the sum of bottles sold: '

sum_sales = df.groupby('broad category')['Bottles Sold'].sum()

print sum_sales
print 'The highest number of bottles sold is in the Vodka category with %s bottles sold.' %sum_sales.max()




print 'Broad category with the highest profits: '



sum_profits = df.groupby('broad category')['profit_per_transaction'].sum()
print sum_profits
print 'The highest profits is in the Whiskey category with %s dollars of profits.' %sum_profits.max()

print "Question #6: "

print df.groupby(['broad category','Category Name'])['State Bottle Retail float'].agg({'Average':np.mean,'Maximum':max, 'Minimum':min, 'Total':sum})


print "Question #7: "

print "Here is a list sorted by county and then by broad category, showing the total number of bottles sold for each category name."

##I need to figure out how to find the max sum of bottles sold for each category name
df_county_favorites = df.groupby(['County','broad category','Category Name'])['Bottles Sold'].sum()#.idxmax()
df_county_favorites_df=pd.DataFrame(df_county_favorites)
df_county_favorites_df.reset_index(inplace=True, col_fill='amounts')

df_county_favorites_2=pd.pivot_table(df,index=['County','broad category','Category Name'],values='Bottles Sold',aggfunc=np.sum)

print df_county_favorites_df.head(20)

df_favorites_by_cat=df_county_favorites_df.groupby(['County','broad category'])['Bottles Sold'].max()

df_favorites_by_cat=pd.DataFrame(df_favorites_by_cat)

print "Here are the amounts of bottles sold for the largest amount of bottles sold in each catergory.  I couldn't figure out how to print out the category name, so this is just the bottles sold column."
print df_favorites_by_cat.head(20)

# print df_county_favorites_df.loc[(df_county_favorites_df['Bottles Sold']==df_favorites_by_cat['Bottles Sold']),['County','broad category', 'Category Name']].head()

# for item in df_favorites_by_cat['Bottles Sold']:
# 	if (df_county_favorites['Bottles Sold']==item):
# 		print df_county_favorites['County','broad category','Category Name']


# favorites=[]
# for county in df_county_favorites_df['County']:
# 	for b_cat in df_county_favorites_df['broad category']:
# 		favorites.append(df_county_favorites_df[(df_county_favorites_df['County']==county) & (df_county_favorites_df['broad category']==b_cat)]['Bottles Sold'].max())

# print favorites 


# print df_county_favorites.index
# #print df_county_favorites.columns

# print df_county_favorites_2
# print type(df_county_favorites)
# print df_county_favorites_2.index
# print df_county_favorites_2.columns




##### Keep working here!!!
### make a pivot table of the pivot table
print df_county_favorites_2.idxmax('County')
print "Question #8: "

print "Here is a list of all 99 counties in Iowa and their population sizes, sorted by population, obtained from http://www.iowa-demographics.com/counties_by_population.  Looking at the rows, there is a large jump in population size between county #10 (Dallas County with 80,000) to county #11(Warren County with 48,000).  Therefore, I will call the first 10 counties 'Large Counties', and the remaining counties 'Small Counties'."
df_county_pop=pd.read_csv('iowa_pop_by_county.csv')
print df_county_pop.head(20)

df_county_large = df[(df['County']=='Polk') | (df['County']=='Linn') | (df['County']=='Scott') | (df['County']=='Johnson') | (df['County']=='Black Hawk') | (df['County']=='Woodbury') | (df['County']=='Dubuque') | (df['County']=='Story') | (df['County']=='Pottawattamie') | (df['County']=='Dallas')]
#print df_county_large.head()


df_county_small = df[(df['County']!='Polk') & (df['County']!='Linn') & (df['County']!='Scott') & (df['County']!='Johnson') & (df['County']!='Black Hawk') & (df['County']!='Woodbury') & (df['County']!='Dubuque') & (df['County']!='Story') & (df['County']!='Pottawattamie') & (df['County']!='Dallas')]
#print df_county_small.head()

print "It seems, as would be expected, that large counties have more total stores than small counties.  Looking at the desciptions below, large counties have an average 68 stores with a median of 53 stores, while small counties have an average and a median of only 7 stores."
stores_in_large = df_county_large.groupby('County')['Store Number'].nunique()
print stores_in_large.describe()

stores_in_small = df_county_small.groupby('County')['Store Number'].nunique()
print stores_in_small.describe()


print "However, when you look at the average number of stores based on the average population size per county in each subset, you see that they have almost identically 4 stores for every 10,000 people."
df_county_pop['Population']=df_county_pop['Population'].apply(string_to_float)
# def add_pop(county):
# 	for county in df_county_pop['County']:
# 		if df[county]==df_county_pop[county]:
# 			return df_county_pop['Population']


# df['population']=df['County'].apply(add_pop)
#print df['population'][0:10]
a = df_county_pop['Population'][0:10].mean()
b = stores_in_large.mean()
c = b/a 
print "Number of stores per 10,000 people in a large county: ",c*10000 

d  = df_county_pop['Population'][10:].mean()
e  = stores_in_small.mean()
f  = e/d  

print "Number of stores per 10,000 people in a small county: ",f*10000 


bottles_large_c=df_county_large['Bottles Sold'].mean()
bottles_small_c= df_county_small['Bottles Sold'].mean()

print "Averaging all of the orders in the 2 subsets, we see that large counties ordered an average of %s bottles per order, while small counties order an average of %s bottles per order." %(bottles_large_c,bottles_small_c)

print "It appears there are only minor diffences in tastes between the large counties and small counties.  The first list below is the sorted sum total of all bottles sold in large counties, and the second list is the sorted sum total of all bottles sold in small counties.  The noticeable difference is that in large counties significantly more vodka is sold than whiskey, while in small counties there actually is slightly more whiskey sold than vodka.  A possible reason for this could be that in large counties there are more cities where people enjoy mixed drinks that contain vodka, while in small counties there are more rural inhabitants that would opt for a straight whiskey drink more often than they would a mixed vodka drink. All other catergories are in equal standing across the two lists."
print df_county_large.groupby('broad category')['Bottles Sold'].sum().sort_values(ascending=False)
print df_county_small.groupby('broad category')['Bottles Sold'].sum().sort_values(ascending=False)

print "Question #9: "
print "In county_graph.png I have 2 scatter plots of the number of stores in a county based on the the number of inhabitants of the county, with a separate graph for large counties and small counties.  There doesn't seem to be much correlation between the two variables.  With the large counties, there are only 10 data points, so nothing signficant can be observed.  With the small counties you do see that there is some positive correlation, that as the population goes up, you can expect to have more stores, as would be expected."
fig=plt.figure()
ax1=fig.add_subplot(1,2,1)
ax1.set_title('Number of Stores based\n on Pop. (Large Counties)')
# print df_county_pop[0:10].sort_values('County')
# print stores_in_large

ax1.scatter(df_county_pop['Population'][0:10],stores_in_large)

ax2=fig.add_subplot(1,2,2)
ax2.set_title('Number of Stores based\n on Pop. (Small Counties)')
ax2.scatter(df_county_pop['Population'][10:],stores_in_small)

# ax3=fig.add_subplot(2,2,3)
# ax3.set_title('Number of Stores per every 10,000 people in a County (Large Counties)')
# print stores_in_large
# print df_county_large
# print df_county_small[0:10]
###df['stores per capita large_c']=((stores_in_large.sort_values()) /(df_county_large['Population'].sort_values())) 

#print df['stores per capita large_c'].head()
###ax3.scatter(df_county_pop['Population'][0:10],###)


# ax4=fig.add_subplot(2,2,4)
# ax4.set_title('Number of Stores per every 10,000 people in a County (Small Counties)')
# print f 
# #ax4.scatter(df_county_pop['Population'][10:],f*10000)

plt.savefig	('county_graph.png')


print "Question #10: "

file_path='Iowa_Unemployment_by_County.csv'

df_iowa_umemploy=pd.read_csv(file_path)
# print df_iowa_umemploy
print "I found data online with unemployment rates for each county in Iowa.  My hypothesis was that if a county has a higher unemployment rate, it would have a higher number of bottles sold per person.  I calculated  the number of bottles sold per person in each county and put that on the y-axis as the dependant variable, and the unemployment rate for each county on the x-axis as the independant variable.  After drawing a scatter plot, in unemployment_graph.png, I didn't see any real correlation.  Then I thought that if unemployed people aren't pushing up the average number of bottles sold per person, maybe college students are.  There are 3 counties in Iowa that have public universities:  Iowa State University in Story County, University of Iowa in Johnson County, and University of Northern Iowa in Black Hawk County.  I wanted to see if they have a high average bottle per person purchase rate.  I created a bar graph in college_counties.png, and saw that although all 3 counties aren't pushing up the state average, Johnson county was equal to the state average, and since it is the 4th largest county in Iowa, it can definitely be setting a trend for the rest of the state average.  Something to explore further is to look at counties with private univesities which could have even higher drinking rates, and also to look at individual cities in each county where the univesities are, which could have a higher bottle purchase rate than the rest of the county."
print df_iowa_umemploy.head(20)



df_bottles_sold = df.groupby('County')['Bottles Sold'].sum()
bottles_sold_df=pd.DataFrame(df_bottles_sold)
bottles_sold_df.reset_index(inplace=True)


df_county_pop_sorted=df_county_pop.sort_values(['County'])
#print df_county_pop_sorted.head(10)
df['bottles per capita']=bottles_sold_df['Bottles Sold'] / df_county_pop_sorted['Population']

#df_bottles_per_capita

# print df['bottles per capita'].head(20)

# print df_iowa_umemploy['December\n2016']
# print df['bottles per capita']

# print len(df_iowa_umemploy['December\n2016'])
# print len(df['bottles per capita'])
# print len(bottles_sold_df['Bottles Sold'])
# print len(df_county_pop_sorted['Population'])
# print df['bottles per capita'][80:120]

fig=plt.figure()
ax=fig.add_subplot(1,1,1)
ax.set_title('Bottles Sold Compared to Unemployment')
ax.set_xlabel('Unemployment Rates in Each County in Iowa')
ax.set_ylabel('Average of Bottles Sold in Each County in Iowa per Capita')
ax.set_ylim([0,4])
ax.scatter(df_iowa_umemploy['December\n2016'],df['bottles per capita'][0:99])

plt.savefig	('unemployment_graph.png')

story= df.loc[df['County']=='Story','bottles per capita'].mean()
johnson=df.loc[df['County']=='Johnson','bottles per capita'].mean()
black_hawk= df.loc[df['County']=='Black Hawk','bottles per capita'].mean()
all_state=df['bottles per capita'].mean()

fig=plt.figure()
ax=fig.add_subplot(1,1,1)
ax.set_title('Bottles Sold in College Counties')
ax.set_xlabel('Story, Johnson, Black Hawk, and All Counties')
ax.set_ylabel('Average of Bottles Sold in County per Capita')
ax.bar([1,2,3,4],[story,johnson,black_hawk,all_state])
plt.savefig('college_counties.png')






