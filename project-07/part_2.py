import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

from sklearn.externals import joblib

x=joblib.load('pca_all_columns.pkl')
print type(x)

x_std=StandardScaler().fit_transform(x)

#print "explained variance ratio title", np.cumsum(x.explained_variance_ratio_)



fig=plt.figure()
for counter in range(1,10):
	km=KMeans(n_clusters=counter+1,n_jobs=-1)

	labels=km.fit_predict(x_std)

	centroids=km.cluster_centers_
	# score=silhouette_score(x_std,labels)

	ax=fig.add_subplot(3,3,counter)
	ax.set_title('%s Clusters' %(counter+1))
	# ax.set_xlabel('Sil. Score: %s' % score)
	plt.scatter(x_std[:,0],x_std[:,1],c=labels)
	for value in range (10):
		plt.scatter(centroids[0][value],centroids[1][value],color='red')

plt.savefig('kmeans.png')


plt.clf()


km=KMeans(n_clusters=2,n_jobs=-1)
labels=km.fit_predict(x_std)
centroids=km.cluster_centers_
fig2=plt.figure()
counter=1
for i in range (0,5):
	for y in range (0,5):
		ax=fig2.add_subplot(5,5,counter)
		#ax.set_title('plots feature %s by feature %s' %(i,y))
		plt.scatter(x_std[:,i],x_std[:,y],c=labels)
		for value in range (3):
			plt.scatter(centroids[0][value],centroids[1][value],color='red')
		counter +=1	
plt.savefig('best_view.png')


plt.clf()

fig3=plt.figure()
ax=fig3.add_subplot(1,1,1)
plt.scatter(x_std[:,0],x_std[:,1],c=labels)
plt.scatter(centroids[0][0],centroids[1][0],color='red')
plt.scatter(centroids[0][1],centroids[1][1],color='red')
plt.savefig('final_view.png')
plt.clf()

### TSNE!!!

# from sklearn.manifold import TSNE

# tsne=TSNE()

# tsne_kmeans=tsne.fit_transform(x_std)

# plt.scatter(tsne_kmeans[:,0],tsne_kmeans[:,1],c=labels)
# plt.savefig('tnse.png')
# plt.clf()


filename='reddit_posts.csv'

df=pd.read_csv(filename)



print type(labels)
print labels[0:5]

df_titles=df['title']



print df_titles.head()

list_1=[]
list_2=[]



for item in range(len(labels)):
	if labels[item]==0:
		list_1.append(df_titles[item])
	else:
		list_2.append(df_titles[item])


print len(list_1)
print len(list_2)

print 'list 1',list_1[0:5]
print 'list 2',list_2[0:5]

print 'labels',labels

pd.DataFrame(labels).to_csv('labels.csv')





			


